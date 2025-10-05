from base import Driver

class LoginPage(Driver):
    package_name = "com.example.banking"

    def __init__(self, driver):
        super().__init__(driver)

        self.username_textfield = f"{self.package_name}:id/editUsernameText"
        self.password_textfield = f"{self.package_name}:id/editPasswordText"
        self.login_button = f"{self.package_name}:id/loginButton"
        self.login_error_msg = f"{self.package_name}:id/loginErrorMessageTextView"


    def enter_username(self, username):
        self.set_text(self.username_textfield, username)


    def enter_password(self, password):
        self.set_text(self.password_textfield, password)


    def click_login_button(self):
        self.click(self.login_button)


    def get_login_error_msg(self):
        return self.get_text(self.login_error_msg)
