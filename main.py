import tkinter as tk
from tkinter import ttk, messagebox
from login import LoginScreen
import csv

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fietsenmakers App")
        self.geometry("500x400")

        # container frame waar alles wordt ingeladen
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")

        #  grid container een manier van plaatsing binnen tkinter
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames = {}

        #loop standaard tkinter: loopt over de te laden frames nu alleen login
        for F in (LoginScreen,):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Centreer de container
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Toon eerst het inlogscherm
        self.show_frame("LoginScreen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        print(f"Overgeschakeld naar frame: {page_name}")  # debug printen in terminal

if __name__ == "__main__":
    app = App()
    app.mainloop()