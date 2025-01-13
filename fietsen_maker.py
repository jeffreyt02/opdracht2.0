import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
import csv

class FietsenmakerDashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Fietsenmaker Dashboard")
        label.pack(pady=10)

        # Maak een frame voor de scrollable text
        frame = ttk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Maak de scrollable text widget
        self.scrolled_text = ScrolledText(frame, wrap=tk.WORD, width=100, height=20)
        self.scrolled_text.pack(fill=tk.BOTH, expand=True)

        # Laad de gegevens in
        self.load_data()

    def load_data(self):
        # Lees de CSV-bestand
        with open('C:\\Users\\SKIKK\\Desktop\\Haagse hoge\\kwartaal2\\opdracht2.0\\gegevens\\fiets_gegevens.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Voeg de gegevens toe aan de scrollable text
                self.scrolled_text.insert(tk.END, f"Naam: {row['naam']} {row['achternaam']}\n")
                self.scrolled_text.insert(tk.END, f"Verhuurdatum: {row['verhuurdatum']}\n")
                self.scrolled_text.insert(tk.END, f"Terugbrengdatum: {row['terugbrengdatum']}\n")
                self.scrolled_text.insert(tk.END, "-"*40 + "\n")