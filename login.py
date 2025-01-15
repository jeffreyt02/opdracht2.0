import tkinter as tk
from tkinter import ttk, messagebox

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.username_label = ttk.Label(self, text="Gebruikersnaam")
        self.username_label.pack(pady=5)
        
        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(self, textvariable=self.username_var)
        self.username_entry.pack(pady=5)
        self.username_entry.insert(0, "login naam")
        self.username_entry.bind("<FocusIn>", self.clear_placeholder)
        self.username_entry.bind("<FocusOut>", self.add_placeholder)

        self.password_label = ttk.Label(self, text="Wachtwoord")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def clear_placeholder(self, event):
        if self.username_var.get() == "login naam":
            self.username_var.set("")

    def add_placeholder(self, event):
        if not self.username_var.get():
            self.username_var.set("login naam")

    def login(self):
        username = self.username_var.get()
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
        users = {
            "service1": {"password": "password1", "role": "service"},
            "eigenaar1": {"password": "password2", "role": "eigenaar"},
            "fietsenmaker1": {"password": "password3", "role": "fietsenmaker"}
        }

        if username in users and users[username]["password"] == password:
            return users[username]["role"]
        return None