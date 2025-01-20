import tkinter as tk
from tkinter import ttk, messagebox
from servicedesk import ServiceDashboard
from eigenaar_dasboard import EigenaarDashboard
from fietsen_maker import FietsenmakerDashboard
from login import LoginScreen

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

    def logout(self):
        self.frames["LoginScreen"].reset_fields()
        self.show_frame("LoginScreen")

if __name__ == "__main__":
    app = App()
    app.geometry("820x650")  # Stel de grootte van het login venster in
    app.mainloop()