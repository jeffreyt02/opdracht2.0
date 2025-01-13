import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import pandas as pd

class ServiceDashboard(tk.Frame):
    # definiëren en packen van de widgets
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Service Dashboard")
        label.pack(pady=10)

        logout_button = ttk.Button(self, text="Log Out", command=self.logout)
        logout_button.pack(anchor='ne', padx=10, pady=10)

        search_bar = ttk.Entry(self)
        search_bar.pack(pady=5)
        search_bar.bind("<KeyRelease>", self.search_afspraken)

        self.scrolled_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=100, height=20)
        self.scrolled_text.pack(pady=10)

        self.populate_afspraken()

    # alle functies
    def logout(self):
        pass

    def new_afspraak(self):
        pass

    def search_afspraken(self, event):
        pass

    def populate_afspraken(self):
        # inladen van gegevens: dit moet nog dynamisch.... voor dat je het upload
        df = pd.read_csv('C:\\Users\\SKIKK\\Desktop\\Haagse hoge\\kwartaal2\\opdracht2.0\\gegevens\\fiets_gegevens.csv')
        self.scrolled_text.delete(1.0, tk.END)
        for index, row in df.iterrows():
            # Zorg ervoor dat de kolom 'totaaldagen' numerieke waarden bevat
            if pd.isna(row['totaaldagen']):
                row['totaaldagen'] = 0
            afspraak_text = f"{row['naam']} {row['achternaam']}, Verhuur: {row['verhuurdatum']}, Terug: {row['terugbrengdatum']}, Dagen: {row['totaaldagen']}"
            button_frame = tk.Frame(self.scrolled_text)
            text_label = tk.Label(button_frame, text=afspraak_text)
            text_label.pack(side=tk.LEFT)
            spacer = tk.Label(button_frame, text="")
            spacer.pack(side=tk.LEFT, expand=True, fill=tk.X)
            edit_button = ttk.Button(button_frame, text="Edit", command=lambda r=row: self.edit_afspraak(r))
            delete_button = ttk.Button(button_frame, text="Delete", command=lambda r=row: self.delete_afspraak(r))
            edit_button.pack(side=tk.RIGHT, padx=5)
            delete_button.pack(side=tk.RIGHT, padx=5)
            button_frame.pack(fill=tk.X, pady=2)
            self.scrolled_text.window_create(tk.END, window=button_frame)
            self.scrolled_text.insert(tk.END, "-"*40 + "\n"
)

    def edit_afspraak(self, afspraak):
        pass

    def delete_afspraak(self, afspraak):
        pass