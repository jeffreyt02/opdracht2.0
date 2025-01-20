import tkinter as tk
from tkinter import ttk, messagebox

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Login")
        label.pack(pady=10)

        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(self, textvariable=self.username_var)
        self.username_entry.pack(pady=5)
        self.username_entry.insert(0, "type hier je log naam")
        self.username_entry.bind("<FocusIn>", self.clear_placeholder)
        self.username_entry.bind("<FocusOut>", self.add_placeholder)

        login_button = ttk.Button(self, text="Login", command=self.check_login)
        login_button.pack(pady=5)

    def clear_placeholder(self, event):
        if self.username_var.get() == "type hier je log naam":
            self.username_var.set("")

    def add_placeholder(self, event):
        if not self.username_var.get():
            self.username_var.set("type hier je log naam")

<<<<<<< Updated upstream
<<<<<<< Updated upstream
        # afhankelijk van welke rol je inlogt, krijg je een dashboard
        if rol:
            if rol == 'eigenaar':
                self.controller.show_frame("EigenaarDashboard")
            elif rol == 'fietsenmaker':
                self.controller.show_frame("FietsenmakerDashboard")
            elif rol == 'service':
                self.controller.show_frame("ServiceDashboard")
=======
=======
>>>>>>> Stashed changes
    def check_login(self):
        username = self.username_var.get()
        if username == "service1":
            self.controller.show_frame("ServiceDashboard")
        elif username == "eigenaar1":
            self.controller.show_frame("EigenaarDashboard")
        elif username == "fietsenmaker1":
            self.controller.show_frame("FietsenmakerDashboard")
<<<<<<< Updated upstream
>>>>>>> Stashed changes
        else:
            messagebox.showerror("Login Failed", "Geen geode gebruiksnaam probeer het nog eens")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Service Desk")
        self.geometry("1200x600")  # Pas de breedte en hoogte van de applicatie aan

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (LoginScreen, ServiceDashboard, EigenaarDashboard, FietsenmakerDashboard):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginScreen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "LoginScreen":
            frame.username_var.set("")
            frame.add_placeholder(None)

<<<<<<< Updated upstream
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
=======
>>>>>>> Stashed changes
=======
        else:
            messagebox.showerror("Login Failed", "Geen geode gebruiksnaam probeer het nog eens")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Service Desk")
        self.geometry("1200x600")  # Pas de breedte en hoogte van de applicatie aan

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (LoginScreen, ServiceDashboard, EigenaarDashboard, FietsenmakerDashboard):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginScreen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "LoginScreen":
            frame.username_var.set("")
            frame.add_placeholder(None)

>>>>>>> Stashed changes
