import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext
from tkcalendar import DateEntry
import pandas as pd
import csv
import os
from components.appointment_window import AppointmentWindow

class ServiceDashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_file = os.path.join(base_dir, 'gegevens', 'verhuurde_fietsen.csv')
        self.verhuurde_fietsen = pd.read_csv(self.data_file)
        
        label = ttk.Label(self, text="Service Dashboard")
        label.pack(pady=10)

        logout_button = ttk.Button(self, text="Log Out", command=self.controller.logout)
        logout_button.pack(anchor='ne', padx=10, pady=10)

        new_appointment_button = ttk.Button(self, text="Nieuwe Afspraak", command=self.open_new_appointment_window)
        new_appointment_button.pack(pady=5)

        self.filter_var = tk.StringVar()
        search_bar = ttk.Entry(self, textvariable=self.filter_var)
        search_bar.pack(pady=5)
        search_bar.bind("<KeyRelease>", self.update_filter)

        self.scrolled_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=100, height=20)
        self.scrolled_text.pack(pady=10)

        self.populate_afspraken()

    def open_new_appointment_window(self):
        AppointmentWindow(self, self.save_new_appointment)

    def edit_afspraak(self, afspraak):
        print(f"Editing afspraak: {afspraak['naam']} {afspraak['achternaam']}")
        AppointmentWindow(self, self.save_edited_appointment, afspraak)

    def save_new_appointment(self, appointment_data, _):
        fiets_id = appointment_data['fiets_id']
        verhuurdatum = appointment_data['verhuurdatum']
        terugbrengdatum = appointment_data['terugbrengdatum']
        totaaldagen = appointment_data['totaaldagen']
        naam = appointment_data['naam']
        achternaam = appointment_data['achternaam']

        # Controleer of het fiets ID geldig is
        if not fiets_id.isdigit() or int(fiets_id) < 1 or int(fiets_id) > 40:
            messagebox.showerror("Fout", "Ongeldig fiets ID. Voer een ID in tussen 1 en 40.")
            return

        # Controleer of de fiets beschikbaar is
        if int(fiets_id) in self.verhuurde_fietsen['fiets_id'].values:
            messagebox.showerror("Fout", "Deze fiets is al gereserveerd voor de opgegeven periode.")
            return

        # Bereken de kosten
        kosten = int(totaaldagen) * 8

        new_row = pd.DataFrame([[int(fiets_id), verhuurdatum, terugbrengdatum, int(totaaldagen), kosten, naam, achternaam]], columns=self.verhuurde_fietsen.columns)

        # Voeg de nieuwe afspraak toe aan de verhuurde fietsen
        self.verhuurde_fietsen = pd.concat([self.verhuurde_fietsen, new_row], ignore_index=True)

        # Schrijf het bijgewerkte DataFrame naar het CSV-bestand
        self.verhuurde_fietsen.to_csv(self.data_file, index=False)
        self.populate_afspraken()

    def save_edited_appointment(self, appointment_data, original_appointment):
        fiets_id = int(appointment_data['fiets_id'])
        verhuurdatum = appointment_data['verhuurdatum']
        terugbrengdatum = appointment_data['terugbrengdatum']
        totaaldagen = int(appointment_data['totaaldagen'])
        naam = appointment_data['naam']
        achternaam = appointment_data['achternaam']

        # Verwijder de originele afspraak
        self.verhuurde_fietsen = self.verhuurde_fietsen[self.verhuurde_fietsen.index != original_appointment.name]

        # Voeg de bewerkte afspraak toe
        new_row = pd.DataFrame([[fiets_id, verhuurdatum, terugbrengdatum, totaaldagen, totaaldagen * 8, naam, achternaam]], columns=self.verhuurde_fietsen.columns)
        self.verhuurde_fietsen = pd.concat([self.verhuurde_fietsen, new_row], ignore_index=True)

        # Schrijf het bijgewerkte DataFrame naar het CSV-bestand
        self.verhuurde_fietsen.to_csv(self.data_file, index=False)
        self.populate_afspraken()

    def update_filter(self, event):
        # Get the current filter text
        filter_text = self.filter_var.get().lower()
        
        # Filter data
        filtered_data = self.verhuurde_fietsen[self.verhuurde_fietsen.apply(lambda row: filter_text in row['naam'].lower() or filter_text in row['achternaam'].lower(), axis=1)]
        
        # Display filtered forms
        self.display_forms(filtered_data)

    def display_forms(self, data):
        self.scrolled_text.delete(1.0, tk.END)
        for index, row in data.iterrows():
            afspraak_text = f"Naam: {row['naam']} {row['achternaam']}, Fiets ID: {row['fiets_id']}, Verhuur: {row['verhuurdatum']}, Terug: {row['terugbrengdatum']}, Dagen: {row['totaaldagen']}, Kosten: €{row['kosten']}"
            button_frame = tk.Frame(self.scrolled_text)
            text_label = tk.Label(button_frame, text=afspraak_text)
            text_label.pack(side=tk.LEFT)
            edit_button = ttk.Button(button_frame, text="Edit", command=lambda r=row: self.edit_afspraak(r), cursor="hand2")
            delete_button = ttk.Button(button_frame, text="Delete", command=lambda r=row: self.delete_afspraak(r), cursor="hand2")
            edit_button.pack(side=tk.RIGHT, padx=5)
            delete_button.pack(side=tk.RIGHT, padx=5)
            button_frame.pack(fill=tk.X, pady=2)
            self.scrolled_text.window_create(tk.END, window=button_frame)
            self.scrolled_text.insert(tk.END, "")

    def populate_afspraken(self):
        self.display_forms(self.verhuurde_fietsen)

    def delete_afspraak(self, afspraak):
        # Bevestigingsdialoog
        confirm = messagebox.askyesno("Bevestiging", f"Weet je zeker dat je de afspraak voor {afspraak['naam']} {afspraak['achternaam']} wilt verwijderen?")
        if confirm:
            print(f"Verwijderen afspraak: {afspraak['naam']} {afspraak['achternaam']}")
            # Verwijder de afspraak uit het DataFrame
            self.verhuurde_fietsen = self.verhuurde_fietsen[self.verhuurde_fietsen.index != afspraak.name]
            # Schrijf het bijgewerkte DataFrame naar het CSV-bestand
            self.verhuurde_fietsen.to_csv(self.data_file, index=False)
            # Werk de afspraken in de GUI bij
            self.populate_afspraken()