from base import Driver
from appium.webdriver.common.appiumby import AppiumBy

class AccountPage(Driver):
    package_name = "com.example.banking"

    def __init__(self, driver):
        super().__init__(driver)

        self.customer_name_textfield = f"{self.package_name}:id/displayCustomerNameTextView"
        self.accounts_listview = f"{self.package_name}:id/accountsListView"
        self.account_type_textfield = f"{self.package_name}:id/accountTypeTextView"

    def get_customer_name_welcome_message(self):
        return super().get_text(self.customer_name_textfield)

    def get_accounts_listview(self):
        return self.driver.find_element(AppiumBy.ID, self.accounts_listview)
