class TestLoginFunctionaliteit(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.login_screen = self.app.frames["LoginScreen"]

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

if __name__ == "__main__":
    unittest.main()
