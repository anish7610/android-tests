from base import Driver
from appium.webdriver.common.appiumby import AppiumBy


class AccountPage(Driver):
    package_name = "com.example.banking"

    def __init__(self, driver):
        super().__init__(driver)

        self.customer_name_textfield = f"{self.package_name}:id/displayCustomerNameTextView"
        self.accounts_listview = f"{self.package_name}:id/accountsListView"
        self.account_type_textfield = f"{self.package_name}:id/accountTypeTextView"
        self.account_balance_textfield = f"{self.package_name}:id/accountBalanceTextView"
        self.account_view_button = f"{self.package_name}:id/viewAccountTransactionsButton"
        self.transfer_button = f"{self.package_name}:id/transferButton"


    def get_customer_name_welcome_message(self):
        return self.get_text(self.customer_name_textfield)


    @property
    def accounts(self):
        return self.driver.find_element(AppiumBy.ID, self.accounts_listview)


    def get_account_balance(self):
        return self.accounts.find_elements(AppiumBy.ID, self.account_balance_textfield)


    def transfer_button_click(self):
        self.click(self.transfer_button)


    def select_account(self, value):
        account_types = self.accounts.find_elements(AppiumBy.ID, self.account_type_textfield)

        account_view_buttons = self.accounts.find_elements(AppiumBy.ID, self.account_view_button)

        for idx, acc_type in enumerate(account_types):
            if value in acc_type.text:
                account_view_buttons[idx].click()
                break
