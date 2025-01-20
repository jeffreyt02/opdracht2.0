import unittest
from main import App  # Zorg ervoor dat je de juiste module importeert waar de App-klasse is gedefinieerd
from components.appointment_window import AppointmentWindow  # Importeer de AppointmentWindow-module

class TestLoginFunctionaliteit(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.geometry("800x600")  # Stel de grootte van het venster in
        self.login_screen = self.app.frames["LoginScreen"]

    def test_login_service(self):
        self.login_screen.username_entry.insert(0, "service1")
        self.login_screen.password_entry.insert(0, "password")
        self.login_screen.login()
        self.assertEqual(self.app.frames["ServiceDashboard"].tkraise(), None)

    def test_login_eigenaar(self):
        self.login_screen.username_entry.insert(0, "eigenaar1")
        self.login_screen.password_entry.insert(0, "password")
        self.login_screen.login()
        self.assertEqual(self.app.frames["EigenaarDashboard"].tkraise(), None)

    def test_login_fietsenmaker(self):
        self.login_screen.username_entry.insert(0, "fietsenmaker1")
        self.login_screen.password_entry.insert(0, "password")
        self.login_screen.login()
        self.assertEqual(self.app.frames["FietsenmakerDashboard"].tkraise(), None)

    def test_login_invalid(self):
        self.login_screen.username_entry.insert(0, "invalid")
        self.login_screen.password_entry.insert(0, "invalid")
        self.login_screen.login()
        self.assertEqual(self.app.frames["LoginScreen"].tkraise(), None)

    
if __name__ == "__main__":
    unittest.main()