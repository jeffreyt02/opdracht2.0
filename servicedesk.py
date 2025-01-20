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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_file = os.path.join(base_dir, 'gegevens', 'verhuurde_fietsen.csv')
        self.verhuurde_fietsen = pd.read_csv(self.data_file)
=======
=======
>>>>>>> Stashed changes

        # Dynamisch pad naar het CSV-bestand
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.csv_path = os.path.join(base_dir, 'gegevens', 'verhuurde_fietsen.csv')
        self.verhuurde_fietsen = pd.read_csv(self.csv_path)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        
        label = ttk.Label(self, text="Service Dashboard")
        label.pack(pady=10)

        logout_button = ttk.Button(self, text="Log Out", command=self.controller.logout)
        logout_button.pack(anchor='ne', padx=10, pady=10)

        new_appointment_button = ttk.Button(self, text="Nieuwe Afspraak", command=self.open_new_appointment_window)
        new_appointment_button.pack(pady=5)

        self.filter_var = tk.StringVar()
        search_bar = ttk.Entry(self, textvariable=self.filter_var)
        search_bar.pack(pady=5)
        search_bar.insert(0, "zoek hier een naam")
        search_bar.bind("<FocusIn>", self.clear_placeholder)
        search_bar.bind("<FocusOut>", self.add_placeholder)
        search_bar.bind("<KeyRelease>", self.update_filter)

        self.scrolled_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=100, height=20)
        self.scrolled_text.pack(pady=10)

        self.populate_afspraken()

    def open_new_appointment_window(self):
        AppointmentWindow(self, self.save_new_appointment)

<<<<<<< Updated upstream
<<<<<<< Updated upstream
    def edit_afspraak(self, afspraak):
        print(f"Editing afspraak: {afspraak['naam']} {afspraak['achternaam']}")
        AppointmentWindow(self, self.save_edited_appointment, afspraak)

    def save_new_appointment(self, appointment_data, _):
        fiets_id = appointment_data['fiets_id']
        verhuurdatum = appointment_data['verhuurdatum']
        terugbrengdatum = appointment_data['terugbrengdatum']
        totaaldagen = appointment_data['totaaldagen']
=======
    def open_edit_appointment_window(self, afspraak):
        AppointmentWindow(self, self.save_edited_appointment, afspraak)

    def save_new_appointment(self, appointment_data, _):
=======
    def open_edit_appointment_window(self, afspraak):
        AppointmentWindow(self, self.save_edited_appointment, afspraak)

    def save_new_appointment(self, appointment_data, _):
>>>>>>> Stashed changes
        verhuurdatum = appointment_data['verhuurdatum']
        terugbrengdatum = appointment_data['terugbrengdatum']
        totaaldagen = int(appointment_data['totaaldagen'])
        fiets_id = int(appointment_data['fiets_id'])
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        naam = appointment_data['naam']
        achternaam = appointment_data['achternaam']

        # Controleer of het fiets ID geldig is
        if not str(fiets_id).isdigit() or fiets_id < 1 or fiets_id > 40:
            messagebox.showerror("Fout", "Ongeldig fiets ID. Voer een ID in tussen 1 en 40.")
            return

        # Controleer of de fiets beschikbaar is voor de opgegeven periode
        for index, row in self.verhuurde_fietsen.iterrows():
            if fiets_id == row['fiets_id']:
                bestaande_verhuurdatum = pd.to_datetime(row['verhuurdatum'])
                bestaande_terugbrengdatum = pd.to_datetime(row['terugbrengdatum'])
                if (verhuurdatum <= bestaande_terugbrengdatum) and (terugbrengdatum >= bestaande_verhuurdatum):
                    messagebox.showerror("Fout", "Deze fiets is al gereserveerd voor de opgegeven periode.")
                    return

        # Bereken de kosten
        kosten = totaaldagen * 8

        new_row = pd.DataFrame([[int(fiets_id), verhuurdatum, terugbrengdatum, int(totaaldagen), kosten, naam, achternaam]], columns=self.verhuurde_fietsen.columns)

        # Voeg de nieuwe afspraak toe aan de verhuurde fietsen
<<<<<<< Updated upstream
<<<<<<< Updated upstream
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
=======
=======
>>>>>>> Stashed changes
        with open(self.csv_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(new_row)

        self.verhuurde_fietsen = pd.read_csv(self.csv_path)
        self.populate_afspraken()

    def save_edited_appointment(self, appointment_data, original_appointment):
        verhuurdatum = appointment_data['verhuurdatum']
        terugbrengdatum = appointment_data['terugbrengdatum']
        totaaldagen = int(appointment_data['totaaldagen'])
        fiets_id = int(appointment_data['fiets_id'])
        naam = appointment_data['naam']
        achternaam = appointment_data['achternaam']

        # Verwijder de oude afspraak
        self.verhuurde_fietsen = self.verhuurde_fietsen[self.verhuurde_fietsen.index != original_appointment.name]

        # Voeg de bijgewerkte afspraak toe
        updated_row = [fiets_id, verhuurdatum.strftime('%Y-%m-%d'), terugbrengdatum.strftime('%Y-%m-%d'), totaaldagen, totaaldagen * 8, naam, achternaam]
        self.verhuurde_fietsen.loc[len(self.verhuurde_fietsen)] = updated_row

        # Schrijf het bijgewerkte DataFrame naar het CSV-bestand
        self.verhuurde_fietsen.to_csv(self.csv_path, index=False)

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        self.populate_afspraken()

    def update_filter(self, event):
        # Get the current filter text
        filter_text = self.filter_var.get().lower()
        
        # Filter data
        filtered_data = self.verhuurde_fietsen[self.verhuurde_fietsen.apply(lambda row: filter_text in str(row['naam']).lower() or filter_text in str(row['achternaam']).lower(), axis=1)]
        
        # Display filtered forms
        self.display_forms(filtered_data)

    def display_forms(self, data):
        self.scrolled_text.delete(1.0, tk.END)
        for index, row in data.iterrows():
            afspraak_text = f"Naam: {row['naam']} {row['achternaam']}, Fiets ID: {row['fiets_id']}, Verhuur: {row['verhuurdatum']}, Terug: {row['terugbrengdatum']}, Dagen: {row['totaaldagen']}, Kosten: €{row['kosten']}"
            button_frame = tk.Frame(self.scrolled_text)
            text_label = tk.Label(button_frame, text=afspraak_text)
            text_label.pack(side=tk.LEFT)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
            edit_button = ttk.Button(button_frame, text="Edit", command=lambda r=row: self.edit_afspraak(r), cursor="hand2")
=======
            edit_button = ttk.Button(button_frame, text="Edit", command=lambda r=row: self.open_edit_appointment_window(r), cursor="hand2")
>>>>>>> Stashed changes
=======
            edit_button = ttk.Button(button_frame, text="Edit", command=lambda r=row: self.open_edit_appointment_window(r), cursor="hand2")
>>>>>>> Stashed changes
            delete_button = ttk.Button(button_frame, text="Delete", command=lambda r=row: self.delete_afspraak(r), cursor="hand2")
            edit_button.pack(side=tk.RIGHT, padx=5)
            delete_button.pack(side=tk.RIGHT, padx=5)
            button_frame.pack(fill=tk.X, pady=2)
            self.scrolled_text.window_create(tk.END, window=button_frame)
            self.scrolled_text.insert(tk.END, "")

    def populate_afspraken(self):
        self.display_forms(self.verhuurde_fietsen)

<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
=======



#voor de searchbar
    def clear_placeholder(self, event):
        if self.filter_var.get() == "zoek hier een naam":
            self.filter_var.set("")

    def add_placeholder(self, event):
        if not self.filter_var.get():
            self.filter_var.set("zoek hier een naam")

    # def edit_afspraak(self, afspraak):
    #     pass
>>>>>>> Stashed changes



#voor de searchbar
    def clear_placeholder(self, event):
        if self.filter_var.get() == "zoek hier een naam":
            self.filter_var.set("")

    def add_placeholder(self, event):
        if not self.filter_var.get():
            self.filter_var.set("zoek hier een naam")

    # def edit_afspraak(self, afspraak):
    #     pass

>>>>>>> Stashed changes
    def delete_afspraak(self, afspraak):
        # Bevestigingsdialoog
        confirm = messagebox.askyesno("Bevestiging", f"Weet je zeker dat je de afspraak voor {afspraak['naam']} {afspraak['achternaam']} wilt verwijderen?")
        if confirm:
<<<<<<< Updated upstream
<<<<<<< Updated upstream
            print(f"Verwijderen afspraak: {afspraak['naam']} {afspraak['achternaam']}")
            # Verwijder de afspraak uit het DataFrame
            self.verhuurde_fietsen = self.verhuurde_fietsen[self.verhuurde_fietsen.index != afspraak.name]
            # Schrijf het bijgewerkte DataFrame naar het CSV-bestand
            self.verhuurde_fietsen.to_csv(self.data_file, index=False)
=======
=======
>>>>>>> Stashed changes
            # Verwijder de afspraak uit het DataFrame
            self.verhuurde_fietsen = self.verhuurde_fietsen[self.verhuurde_fietsen.index != afspraak.name]
            # Schrijf het bijgewerkte DataFrame naar het CSV-bestand
            self.verhuurde_fietsen.to_csv(self.csv_path, index=False)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
            # Werk de afspraken in de GUI bij
            self.populate_afspraken()