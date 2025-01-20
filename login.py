import tkinter as tk
from tkinter import ttk, messagebox
import csv

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.username_label = ttk.Label(self, text="Gebruikersnaam")
        self.username_label.pack(pady=5)
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(pady=5)

        self.password_label = ttk.Label(self, text="Wachtwoord")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        rol = self.authenticate(username, password)

        # afhankelijk van welke rol je inlogt, krijg je een dashboard
        if rol:
            if rol == 'eigenaar':
                self.controller.show_frame("EigenaarDashboard")
            elif rol == 'fietsenmaker':
                self.controller.show_frame("FietsenmakerDashboard")
            elif rol == 'service':
                self.controller.show_frame("ServiceDashboard")
        else:
            messagebox.showerror("Error", "Ongeldige gebruikersnaam of wachtwoord")

    def authenticate(self, username, password):
        # Gebruik het volledige pad naar het bestand
        file_path = 'C:/Users/SKIKK/Desktop/Haagse hoge/kwartaal2/opdracht2.0/gegevens/users.csv'
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username and row['password'] == password:
                    return row['role']
        return None

    def reset_fields(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)