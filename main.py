import tkinter as tk
from tkinter import ttk, messagebox
from servicedesk import ServiceDashboard
from eigenaar_dasboard import EigenaarDashboard  # Correcte bestandsnaam
from fietsen_maker import FietsenmakerDashboard

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Login")
        label.pack(pady=10)

        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(pady=5)
        self.username_entry.insert(0, "Username")

        login_button = ttk.Button(self, text="Login", command=self.check_login)
        login_button.pack(pady=5)

    def check_login(self):
        username = self.username_entry.get()
        if username == "service1":
            self.controller.show_frame("ServiceDashboard")
        elif username == "eigenaar1":
            self.controller.show_frame("EigenaarDashboard")
        elif username == "fietsenmaker1":
            self.controller.show_frame("FietsenmakerDashboard")
        else:
            messagebox.showerror("Login Failed", "Invalid username")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Service Desk")
        self.geometry("800x600")  # Pas de breedte en hoogte van de applicatie aan

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

if __name__ == "__main__":
    app = App()
    app.mainloop()