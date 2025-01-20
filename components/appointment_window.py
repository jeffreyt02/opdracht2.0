import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from datetime import datetime
=======
import pandas as pd
>>>>>>> Stashed changes
=======
import pandas as pd
>>>>>>> Stashed changes

class AppointmentWindow(tk.Toplevel):
    def __init__(self, parent, save_callback, appointment=None):
        super().__init__(parent)
        self.title("Nieuwe Afspraak" if appointment is None else "Bewerk Afspraak")
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        self.geometry("400x400")
        self.save_callback = save_callback
        self.appointment = appointment

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self, text="Verhuurdatum").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.verhuurdatum_entry = DateEntry(self, date_pattern='yyyy-mm-dd', showweeknumbers=False)
        self.verhuurdatum_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        tk.Label(self, text="Terugbrengdatum").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.terugbrengdatum_entry = DateEntry(self, date_pattern='yyyy-mm-dd', showweeknumbers=False)
        self.terugbrengdatum_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        tk.Label(self, text="Totaal aantal dagen").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.totaaldagen_entry = tk.Entry(self)
        self.totaaldagen_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.totaaldagen_entry.config(state='readonly')

        tk.Label(self, text="Fiets ID").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.fiets_id_entry = tk.Entry(self)
        self.fiets_id_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        tk.Label(self, text="Naam").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.naam_entry = tk.Entry(self)
        self.naam_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        tk.Label(self, text="Achternaam").grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.achternaam_entry = tk.Entry(self)
        self.achternaam_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        tk.Button(self, text="Opslaan", command=self.save_appointment).grid(row=6, column=0, columnspan=2, pady=20)

        self.verhuurdatum_entry.bind("<<DateEntrySelected>>", self.calculate_days)
        self.terugbrengdatum_entry.bind("<<DateEntrySelected>>", self.calculate_days)

        if self.appointment is not None:
            self.load_appointment_data()
=======
=======
>>>>>>> Stashed changes
        self.geometry("400x400")  # Stel de grootte van het venster in
        self.save_callback = save_callback
        self.appointment = appointment

        tk.Label(self, text="Verhuurdatum").grid(row=0, column=0)
        self.verhuurdatum_entry = DateEntry(self, date_pattern='yyyy-mm-dd', showweeknumbers=False)
        self.verhuurdatum_entry.grid(row=0, column=1)

        tk.Label(self, text="Terugbrengdatum").grid(row=1, column=0)
        self.terugbrengdatum_entry = DateEntry(self, date_pattern='yyyy-mm-dd', showweeknumbers=False)
        self.terugbrengdatum_entry.grid(row=1, column=1)

        tk.Label(self, text="Totaaldagen").grid(row=2, column=0)
        self.totaaldagen_entry = tk.Entry(self)
        self.totaaldagen_entry.grid(row=2, column=1)
        self.totaaldagen_entry.config(state='readonly')  # Maak het veld alleen-lezen

        tk.Label(self, text="Fiets ID").grid(row=3, column=0)
        self.fiets_id_entry = tk.Entry(self)
        self.fiets_id_entry.grid(row=3, column=1)

        tk.Label(self, text="Naam").grid(row=4, column=0)
        self.naam_entry = tk.Entry(self)
        self.naam_entry.grid(row=4, column=1)

        tk.Label(self, text="Achternaam").grid(row=5, column=0)
        self.achternaam_entry = tk.Entry(self)
        self.achternaam_entry.grid(row=5, column=1)

        tk.Button(self, text="Opslaan", command=self.save_appointment).grid(row=6, column=0, columnspan=2)

        # Bind de date pickers om automatisch het aantal dagen te berekenen
        self.verhuurdatum_entry.bind("<<DateEntrySelected>>", self.calculate_days)
        self.terugbrengdatum_entry.bind("<<DateEntrySelected>>", self.calculate_days)

        if appointment is not None and not appointment.empty:
            self.load_appointment(appointment)

    def load_appointment(self, appointment):
        self.verhuurdatum_entry.set_date(pd.to_datetime(appointment['verhuurdatum']))
        self.terugbrengdatum_entry.set_date(pd.to_datetime(appointment['terugbrengdatum']))
        self.totaaldagen_entry.config(state='normal')
        self.totaaldagen_entry.insert(0, appointment['totaaldagen'])
        self.totaaldagen_entry.config(state='readonly')
        self.fiets_id_entry.insert(0, appointment['fiets_id'])
        self.naam_entry.insert(0, appointment['naam'])
        self.achternaam_entry.insert(0, appointment['achternaam'])
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

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

    def save_appointment(self):
        appointment_data = {
<<<<<<< Updated upstream
<<<<<<< Updated upstream
            "fiets_id": self.fiets_id_entry.get(),
            "verhuurdatum": self.verhuurdatum_entry.get_date().strftime('%Y-%m-%d'),
            "terugbrengdatum": self.terugbrengdatum_entry.get_date().strftime('%Y-%m-%d'),
            "totaaldagen": self.totaaldagen_entry.get(),
            "naam": self.naam_entry.get(),
            "achternaam": self.achternaam_entry.get()
        }
        self.save_callback(appointment_data, self.appointment)
        self.destroy()

    def load_appointment_data(self):
        self.verhuurdatum_entry.set_date(self.appointment['verhuurdatum'])
        self.terugbrengdatum_entry.set_date(self.appointment['terugbrengdatum'])
        self.totaaldagen_entry.config(state='normal')
        self.totaaldagen_entry.delete(0, tk.END)
        self.totaaldagen_entry.insert(0, self.appointment['totaaldagen'])
        self.totaaldagen_entry.config(state='readonly')
        self.fiets_id_entry.insert(0, self.appointment['fiets_id'])
        self.naam_entry.insert(0, self.appointment['naam'])
        self.achternaam_entry.insert(0, self.appointment['achternaam'])
=======
=======
>>>>>>> Stashed changes
            'verhuurdatum': self.verhuurdatum_entry.get_date(),
            'terugbrengdatum': self.terugbrengdatum_entry.get_date(),
            'totaaldagen': self.totaaldagen_entry.get(),
            'fiets_id': self.fiets_id_entry.get(),
            'naam': self.naam_entry.get(),
            'achternaam': self.achternaam_entry.get()
        }
        self.save_callback(appointment_data, self.appointment)
<<<<<<< Updated upstream
        self.destroy()
>>>>>>> Stashed changes
=======
        self.destroy()
>>>>>>> Stashed changes
