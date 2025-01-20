import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext
import pandas as pd

class FietsenmakerDashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Fietsenmaker Dashboard")
        label.pack(pady=10)

        logout_button = ttk.Button(self, text="Log Out", command=self.controller.logout)
        logout_button.pack(anchor='ne', padx=10, pady=10)

        self.scrolled_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=100, height=20)
        self.scrolled_text.pack(pady=10)

        self.populate_fietsen()

    def populate_fietsen(self):
        # Lees de gegevens uit het CSV-bestand
        verhuurde_fietsen = pd.read_csv('C:/Users/SKIKK/Desktop/Haagse hoge/kwartaal2/opdracht2.0/gegevens/verhuurde_fietsen.csv')

        # Voeg de gegevens toe aan de ScrolledText widget
        for index, row in verhuurde_fietsen.iterrows():
            fiets_info = f"Fiets ID: {row['fiets_id']}, Naam: {row['naam']} {row['achternaam']}, Verhuurdatum: {row['verhuurdatum']}, Terugbrengdatum: {row['terugbrengdatum']}, Totaaldagen: {row['totaaldagen']}, Kosten: €{row['kosten']}"
            self.scrolled_text.insert(tk.END, fiets_info + "\n")
            self.scrolled_text.insert(tk.END, "-"*40 + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fietsenmaker Dashboard")
    FietsenmakerDashboard(root, None).pack(fill="both", expand=True)
    root.mainloop()