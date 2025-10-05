from base import Driver

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TransferPage(Driver):
    package_name = "com.example.banking"

    def __init__(self, driver):
        super().__init__(driver)

        self.from_account_spinner = f"{self.package_name}:id/fromAccountSpinner"
        self.to_account_number = f"{self.package_name}:id/toAccountEditText"
        self.transfer_amount = f"{self.package_name}:id/amountEditText"

        self.transfer_button = f"{self.package_name}:id/transferButton"


    def enter_to_account_number(self, to_account_number):
        self.clear_text(self.to_account_number)
        self.set_text(self.to_account_number, to_account_number)


    def enter_transfer_amount(self, amount):
        self.clear_text(self.transfer_amount)
        self.set_text(self.transfer_amount, amount)


    def transfer_button_click(self):
        self.click(self.transfer_button)


    def select_account(self, account_type):
        spinner_element = self.driver.find_element(AppiumBy.ID, self.from_account_spinner)
        ActionChains(self.driver).click(spinner_element).perform()

        account_to_select = self.driver.find_element(By.ANDROID_UIAUTOMATOR, f"new UiSelector().textContains(\"{account_type}\")")
        account_to_select.click()
