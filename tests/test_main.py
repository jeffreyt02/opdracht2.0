import unittest
import os
import pandas as pd
import logging
from main import App  # Zorg ervoor dat je de juiste module importeert waar de App-klasse is gedefinieerd
from eigenaar_dasboard import EigenaarDashboard  # Importeer de EigenaarDashboard-module
from components.appointment_window import AppointmentWindow  # Importeer de AppointmentWindow-module

# Configureer logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


#hoeronder alle inlog tests en een set  up
class TestLoginFunctionaliteit(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.geometry("800x600")  # Stel de grootte van het venster in
        self.login_screen = self.app.frames["LoginScreen"]

    def test_login_service(self):
        logging.info("Attempting login with username: service1 and password: password")
        self.login_screen.username_entry.insert(0, "service1")
        self.login_screen.password_entry.insert(0, "password")
        self.login_screen.login()
        self.assertEqual(self.app.frames["ServiceDashboard"].tkraise(), None)
        logging.info("Login successful, role: service")

    def test_login_eigenaar(self):
        logging.info("Attempting login with username: eigenaar1 and password: password")
        self.login_screen.username_entry.insert(0, "eigenaar1")
        self.login_screen.password_entry.insert(0, "password")
        self.login_screen.login()
        self.assertEqual(self.app.frames["EigenaarDashboard"].tkraise(), None)
        logging.info("Login successful, role: eigenaar")

    def test_login_fietsenmaker(self):
        logging.info("Attempting login with username: fietsenmaker1 and password: password")
        self.login_screen.username_entry.insert(0, "fietsenmaker1")
        self.login_screen.password_entry.insert(0, "password")
        self.login_screen.login()
        self.assertEqual(self.app.frames["FietsenmakerDashboard"].tkraise(), None)
        logging.info("Login successful, role: fietsenmaker")

    def test_login_invalid(self):
        logging.info("Attempting login with username: invalid and password: invalid")
        self.login_screen.username_entry.insert(0, "invalid")
        self.login_screen.password_entry.insert(0, "invalid")
        self.login_screen.login()
        self.assertEqual(self.app.frames["LoginScreen"].tkraise(), None)
        logging.info("Login failed")


        #dasboard test met testdata: kijkt of er een grafiek in de testeigenaadasboard met de test gegevens
class TestEigenaarDashboard(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.geometry("800x600")  # Stel de grootte van het venster in
        self.eigenaar_dashboard = self.app.frames["EigenaarDashboard"]

    def test_load_data(self):
        logging.info("Loading data into EigenaarDashboard")
        # Maak een tijdelijk CSV-bestand
        temp_csv = 'temp_verhuurde_fietsen.csv'
        data = {
            'fiets_id': [1, 2],
            'verhuurdatum': ['2023-01-01', '2023-02-01'],
            'terugbrengdatum': ['2023-01-05', '2023-02-05'],
            'totaaldagen': [4, 4],
            'kosten': [32, 32],
            'naam': ['Jan', 'Piet'],
            'achternaam': ['Jansen', 'Pietersen']
        }
        pd.DataFrame(data).to_csv(temp_csv, index=False)

        # Stel het tijdelijke CSV-bestand in als data_file
        self.eigenaar_dashboard.data_file = temp_csv

        # Roep de plot_graph-methode aan om de gegevens in te laden
        self.eigenaar_dashboard.plot_graph()

        # Controleer of de gegevens correct zijn ingeladen
        df = pd.read_csv(temp_csv)
        self.assertEqual(len(df), 2)
        self.assertIn('Jan', df['naam'].values)
        self.assertIn('Piet', df['naam'].values)

        # Verwijder het tijdelijke CSV-bestand
        os.remove(temp_csv)
        logging.info("Data loaded successfully into EigenaarDashboard")
if __name__ == "__main__":
    unittest.main()