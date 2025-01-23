import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

class EigenaarDashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Eigenaar Dashboard")
        label.pack(pady=10)

        logout_button = ttk.Button(self, text="Log Out", command=self.controller.logout)
        logout_button.pack(anchor='ne', padx=10, pady=10)

        self.plot_graph()

    def plot_graph(self):
            # Dynamisch pad naar het CSV-bestand
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_dir, 'gegevens', 'verhuurde_fietsen.csv')

        
        # Lees de gegevens uit het CSV-bestand
        verhuurde_fietsen = pd.read_csv(csv_path)

        # Converteer de verhuurdatum naar datetime
        verhuurde_fietsen['verhuurdatum'] = pd.to_datetime(verhuurde_fietsen['verhuurdatum'])

        # Groepeer de gegevens per maand en tel het aantal verhuurde fietsen en de totale omzet
        verhuurde_fietsen['maand'] = verhuurde_fietsen['verhuurdatum'].dt.to_period('M')
        verhuur_per_maand = verhuurde_fietsen.groupby('maand').size()
        omzet_per_maand = verhuurde_fietsen.groupby('maand')['kosten'].sum()

        # Maak de grafiek
        fig, ax1 = plt.subplots()

        # Plot het aantal verhuurde fietsen
        ax1.bar(verhuur_per_maand.index.astype(str), verhuur_per_maand, color='b', alpha=0.6, label='Aantal verhuurde fietsen')
        ax1.set_xlabel('Maand')
        ax1.set_ylabel('Aantal verhuurde fietsen', color='b')
        ax1.tick_params(axis='y', labelcolor='b')

        # Maak een tweede y-as voor de omzet
        ax2 = ax1.twinx()
        ax2.plot(omzet_per_maand.index.astype(str), omzet_per_maand, color='r', marker='o', label='Totale omzet')
        ax2.set_ylabel('Totale omzet (€)', color='r')
        ax2.tick_params(axis='y', labelcolor='r')

        # Voeg een titel en legenda toe
        fig.suptitle('Aantal verhuurde fietsen en totale omzet per maand')
        fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

        # Voeg de grafiek toe aan het tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)

