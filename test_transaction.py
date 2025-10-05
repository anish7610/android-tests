from transaction_page import TransactionPage
from account_page import AccountPage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime

import pytest


@pytest.fixture
def transaction_page_setup(android_driver, login):

    account_page = AccountPage(android_driver)
    accounts_listview = account_page.get_accounts_listview()
    account_view_transaciton_buttons = accounts_listview.find_elements(AppiumBy.ID, account_page.account_view_button)

    # Select the first account - Checking
    account = account_view_transaciton_buttons[0].click()

    transaction_page = TransactionPage(android_driver)

    return transaction_page


def test_filter_transaction_by_keyword(transaction_page_setup):
    transaction_page = transaction_page_setup

    # Enter Keyword
    transaction_page.enter_keyword("Bonus")
    transaction_page.filter_button_click()

    transactions_listview = transaction_page.get_transactions_listview()

    actions = ActionChains(transaction_page.driver)


    # Loop 5 times to get to the end of list
    for i in range(5):
        transaction_descriptions = transactions_listview.find_elements(AppiumBy.ID, transaction_page.transaction_desc_textview)
       
        for transaction_desc in transaction_descriptions:
            assert transaction_desc.text == "Bonus" 
        
        # Scroll down and display the next two transactions
        transaction_page.driver.swipe(380, 1080, 380, 860)

    transaction_page.driver.press_keycode(4)


def test_filter_transaction_by_amount(transaction_page_setup):
    transaction_page = transaction_page_setup

    min_amount, max_amount = 45.0, 70

    # Enter min and max amount
    transaction_page.enter_min_amount(min_amount)
    transaction_page.enter_max_amount(max_amount)
    transaction_page.filter_button_click()

    transactions_listview = transaction_page.get_transactions_listview()

    actions = ActionChains(transaction_page.driver)

    for i in range(5):
        transactions_amount = transactions_listview.find_elements(AppiumBy.ID, transaction_page.transaction_amount_textview)

        for amount in transactions_amount:
            actual_amount = amount.text.split('$')[1]
            assert min_amount <= round(float(actual_amount), 2) <= max_amount

        transaction_page.driver.swipe(380, 1080, 380, 860)

    transaction_page.driver.press_keycode(4)


def test_filter_transaction_by_date(transaction_page_setup):
    transaction_page = transaction_page_setup

    from_date, to_date = '2019/2/20', '2020/11/7'

    expected_from_date = datetime.strptime(from_date, "%Y/%m/%d")
    expected_to_date = datetime.strptime(to_date, "%Y/%m/%d")

    # Enter from and to dates
    transaction_page.enter_from_date(from_date)
    transaction_page.enter_to_date(to_date)
    transaction_page.filter_button_click()

    transactions_listview = transaction_page.get_transactions_listview()

    actions = ActionChains(transaction_page.driver)

    for i in range(5):
        transactions_timestamp = transactions_listview.find_elements(AppiumBy.ID, transaction_page.transaction_timestamp_textview)

        for timestamp in transactions_timestamp:
            actual_timestamp = datetime.strptime(timestamp.text, "%d-%b-%Y")
            assert expected_from_date <= actual_timestamp <= expected_to_date

        transaction_page.driver.swipe(380, 1080, 380, 860)
