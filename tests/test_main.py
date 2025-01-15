import unittest
from unittest.mock import patch
from main import App
from servicedesk import ServiceDashboard
from components.appointment_window import AppointmentWindow

class TestLoginFunctionaliteit(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.login_screen = self.app.frames["LoginScreen"]
        self.service_dashboard = self.app.frames["ServiceDashboard"]

    def test_login_service(self):
        self.login_screen.username_var.set("service1")
        self.login_screen.password_entry.insert(0, "password1")
        self.login_screen.login()
        self.assertEqual(self.app.frames["ServiceDashboard"].tkraise(), None)

    def test_login_eigenaar(self):
        self.login_screen.username_var.set("eigenaar1")
        self.login_screen.password_entry.insert(0, "password2")
        self.login_screen.login()
        self.assertEqual(self.app.frames["EigenaarDashboard"].tkraise(), None)

    def test_login_fietsenmaker(self):
        self.login_screen.username_var.set("fietsenmaker1")
        self.login_screen.password_entry.insert(0, "password3")
        self.login_screen.login()
        self.assertEqual(self.app.frames["FietsenmakerDashboard"].tkraise(), None)

    def test_login_invalid(self):
        self.login_screen.username_var.set("invalid")
        self.login_screen.password_entry.insert(0, "invalid")
        self.login_screen.login()
        self.assertEqual(self.app.frames["LoginScreen"].tkraise(), None)

    @patch('components.appointment_window.AppointmentWindow.__init__', return_value=None)
    def test_new_appointment_popup(self, mock_appointment_window):
        self.service_dashboard.open_new_appointment_window()
        self.assertTrue(mock_appointment_window.called)

    @patch('components.appointment_window.AppointmentWindow.__init__', return_value=None)
    def test_edit_appointment_popup(self, mock_appointment_window):
      
        if not self.service_dashboard.verhuurde_fietsen.empty:
            afspraak = self.service_dashboard.verhuurde_fietsen.iloc[0]
            self.service_dashboard.open_edit_appointment_window(afspraak)
            self.assertTrue(mock_appointment_window.called)

if __name__ == "__main__":
    unittest.main()