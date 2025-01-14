import unittest
from main import App

class TestLoginFunctionaliteit(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.login_screen = self.app.frames["LoginScreen"]


