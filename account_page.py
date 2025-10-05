from base import Driver
from appium.webdriver.common.appiumby import AppiumBy

class AccountPage(Driver):
    package_name = "com.example.banking"

    def __init__(self, driver):
        super().__init__(driver)

        self.customer_name_textfield = f"{self.package_name}:id/displayCustomerNameTextView"
        self.accounts_listview = f"{self.package_name}:id/accountsListView"
        self.account_type_textfield = f"{self.package_name}:id/accountTypeTextView"
        self.account_view_button = f"{self.package_name}:id/viewAccountTransactionsButton"
        self.transfer_button = f"{self.package_name}:id/transferButton"


    def get_customer_name_welcome_message(self):
        return self.get_text(self.customer_name_textfield)


    def get_accounts_listview(self):
        return self.driver.find_element(AppiumBy.ID, self.accounts_listview)


    def transfer_button_click(self):
        self.click(self.transfer_button)
