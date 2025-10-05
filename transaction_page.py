from base import Driver
from appium.webdriver.common.appiumby import AppiumBy


class TransactionPage(Driver):
    package_name = "com.example.banking"

    def __init__(self, driver):
        super().__init__(driver)
        self.keyword_textfield = f"{self.package_name}:id/keywordsEditText"
        self.min_amount_textfield = f"{self.package_name}:id/minAmountEditText"
        self.max_amount_textfield = f"{self.package_name}:id/maxAmountEditText"
        self.from_date_textfield = f"{self.package_name}:id/fromDateEditText"
        self.to_date_textfield = f"{self.package_name}:id/toDateEditText"
        self.filter_button = f"{self.package_name}:id/filterButton"
        self.transactions_listview = f"{self.package_name}:id/accountTransactionsRecyclerView"
        self.transaction_desc_textview = f"{self.package_name}:id/transactionDescriptionTextView"
        self.transaction_amount_textview = f"{self.package_name}:id/transactionAmountTextView"
        self.transaction_timestamp_textview = f"{self.package_name}:id/transactionTimestampTextView"


    def enter_keyword(self, keyword):
        self.set_text(self.keyword_textfield, keyword)


    def enter_min_amount(self, min_amount):
        self.clear_text(self.min_amount_textfield)
        self.set_text(self.min_amount_textfield, min_amount)


    def enter_max_amount(self, max_amount):
        self.clear_text(self.max_amount_textfield)
        self.set_text(self.max_amount_textfield, max_amount)


    def enter_from_date(self, from_date):
        self.clear_text(self.from_date_textfield)
        self.set_text(self.from_date_textfield, from_date)


    def enter_to_date(self, to_date):
        self.clear_text(self.to_date_textfield)
        self.set_text(self.to_date_textfield, to_date)


    def filter_button_click(self):
        self.click(self.filter_button)


    def get_transactions_listview(self):
        return self.driver.find_element(AppiumBy.ID, self.transactions_listview)
