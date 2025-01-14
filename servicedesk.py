import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext
from tkcalendar import DateEntry
import pandas as pd
import csv

class ServiceDashboard(tk.Frame):
    # definiëren en packen van de widgets
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.verhuurde_fietsen = pd.read_csv('C:/Users/SKIKK/Desktop/Haagse hoge/kwartaal2/opdracht2.0/gegevens/verhuurde_fietsen.csv')
        
        label = ttk.Label(self, text="Service Dashboard")
        label.pack(pady=10)

        logout_button = ttk.Button(self, text="Log Out", command=self.logout)
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

    # alle functies
    def logout(self):
        self.controller.show_frame("LoginScreen")

    def new_afspraak(self):
        pass

    def open_new_appointment_window(self):
        self.new_appointment_window = tk.Toplevel(self)
        self.new_appointment_window.title("Nieuwe Afspraak")

        tk.Label(self.new_appointment_window, text="Verhuurdatum").grid(row=0, column=0)
        self.verhuurdatum_entry = DateEntry(self.new_appointment_window, date_pattern='yyyy-mm-dd')
        self.verhuurdatum_entry.grid(row=0, column=1)

        tk.Label(self.new_appointment_window, text="Terugbrengdatum").grid(row=1, column=0)
        self.terugbrengdatum_entry = DateEntry(self.new_appointment_window, date_pattern='yyyy-mm-dd')
        self.terugbrengdatum_entry.grid(row=1, column=1)

        tk.Label(self.new_appointment_window, text="Totaaldagen").grid(row=2, column=0)
        self.totaaldagen_entry = tk.Entry(self.new_appointment_window)
        self.totaaldagen_entry.grid(row=2, column=1)
        self.totaaldagen_entry.config(state='readonly')  # Maak het veld alleen-lezen

        tk.Label(self.new_appointment_window, text="Fiets ID").grid(row=3, column=0)
        self.fiets_id_entry = tk.Entry(self.new_appointment_window)
        self.fiets_id_entry.grid(row=3, column=1)

        tk.Label(self.new_appointment_window, text="Naam").grid(row=4, column=0)
        self.naam_entry = tk.Entry(self.new_appointment_window)
        self.naam_entry.grid(row=4, column=1)

        tk.Label(self.new_appointment_window, text="Achternaam").grid(row=5, column=0)
        self.achternaam_entry = tk.Entry(self.new_appointment_window)
        self.achternaam_entry.grid(row=5, column=1)

        tk.Button(self.new_appointment_window, text="Opslaan", command=self.save_new_appointment).grid(row=6, column=0, columnspan=2)

        # Bind de date pickers om automatisch het aantal dagen te berekenen
        self.verhuurdatum_entry.bind("<<DateEntrySelected>>", self.calculate_days)
        self.terugbrengdatum_entry.bind("<<DateEntrySelected>>", self.calculate_days)

    def calculate_days(self, event):
        try:
            verhuurdatum = self.verhuurdatum_entry.get_date()
            terugbrengdatum = self.terugbrengdatum_entry.get_date()
            totaaldagen = (terugbrengdatum - verhuurdatum).days
            self.totaaldagen_entry.config(state='normal')
            self.totaaldagen_entry.delete(0, tk.END)
            self.totaaldagen_entry.insert(0, str(totaaldagen))
            self.totaaldagen_entry.config(state='readonly')
        except Exception as e:
            messagebox.showerror("Fout", f"Er is een fout opgetreden bij het berekenen van de dagen: {e}")

    def save_new_appointment(self):
        verhuurdatum = self.verhuurdatum_entry.get_date()
        terugbrengdatum = self.terugbrengdatum_entry.get_date()
        totaaldagen = self.totaaldagen_entry.get()
        fiets_id = self.fiets_id_entry.get()
        naam = self.naam_entry.get()
        achternaam = self.achternaam_entry.get()

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

        new_row = [fiets_id, verhuurdatum.strftime('%Y-%m-%d'), terugbrengdatum.strftime('%Y-%m-%d'), totaaldagen, kosten, naam, achternaam]

        # Voeg de nieuwe afspraak toe aan de verhuurde fietsen
        with open('C:/Users/SKIKK/Desktop/Haagse hoge/kwartaal2/opdracht2.0/gegevens/verhuurde_fietsen.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(new_row)

        self.new_appointment_window.destroy()
        self.verhuurde_fietsen = pd.read_csv('C:/Users/SKIKK/Desktop/Haagse hoge/kwartaal2/opdracht2.0/gegevens/verhuurde_fietsen.csv')
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
            edit_button = ttk.Button(button_frame, text="Edit", command=lambda r=row: self.edit_afspraak(r))
            delete_button = ttk.Button(button_frame, text="Delete", command=lambda r=row: self.delete_afspraak(r))
            edit_button.pack(side=tk.RIGHT, padx=5)
            delete_button.pack(side=tk.RIGHT, padx=5)
            button_frame.pack(fill=tk.X, pady=2)
            self.scrolled_text.window_create(tk.END, window=button_frame)
            self.scrolled_text.insert(tk.END, "")

    def populate_afspraken(self):
        self.display_forms(self.verhuurde_fietsen)

    def edit_afspraak(self, afspraak):
        pass

    def delete_afspraak(self, afspraak):
        pass