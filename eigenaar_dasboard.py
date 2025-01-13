import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class EigenaarDashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Eigenaar Dashboard")
        label.pack(pady=10)

        show_chart_button = ttk.Button(self, text="Toon Verhuur Grafiek", command=self.show_chart)
        show_chart_button.pack(pady=10)

    def show_chart(self):
        # Lees de CSV-bestand
        df = pd.read_csv('C:\\Users\\SKIKK\\Desktop\\Haagse hoge\\kwartaal2\\opdracht2.0\\gegevens\\fiets_gegevens.csv')

        # Converteer de verhuurdatum naar datetime
        df['verhuurdatum'] = pd.to_datetime(df['verhuurdatum'])

        # Groepeer op maand en tel het aantal verhuurde fietsen
        df['maand'] = df['verhuurdatum'].dt.to_period('M')
        verhuur_per_maand = df.groupby('maand').size()

        # Maak de grafiek
        fig, ax = plt.subplots()
        verhuur_per_maand.plot(kind='bar', ax=ax)
        ax.set_title('Aantal verhuurde fietsen per maand')
        ax.set_xlabel('Maand')
        ax.set_ylabel('Aantal verhuurde fietsen')
        ax.set_xticklabels(verhuur_per_maand.index, rotation=0)  # Plaats de datums horizontaal

        # Voeg de grafiek toe aan het tkinter venster
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

