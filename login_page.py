from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    package_name = "com.example.banking"

    def __init__(self, driver):
        self.driver = driver
        self.username_textfield = f"{self.package_name}:id/editUsernameText"
        self.password_textfield = f"{self.package_name}:id/editPasswordText"
        self.login_button = f"{self.package_name}:id/loginButton"
        self.login_error_msg = f"{self.package_name}:id/loginErrorMessageTextView"


    def enter_username(self, username):
        self.driver.find_element(AppiumBy.ID, self.username_textfield).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(AppiumBy.ID, self.password_textfield).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(AppiumBy.ID, self.login_button).click()

    def get_login_error_msg(self):
        return self.driver.find_element(AppiumBy.ID, self.login_error_msg).text
