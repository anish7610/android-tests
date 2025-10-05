from appium.webdriver.common.appiumby import AppiumBy

class AccountPage:
    package_name = "com.example.banking"

    def __init__(self, driver):
        self.driver = driver
        self.customer_name_textfield = f"{self.package_name}:id/displayCustomerNameTextView"

    def get_customer_name_welcome_message(self):
        return self.driver.find_element(AppiumBy.ID, self.customer_name_textfield).text

