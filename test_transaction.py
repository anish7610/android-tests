from transaction_page import TransactionPage
from account_page import AccountPage
from datetime import datetime
import random
import pytest


@pytest.fixture
def transaction_page_setup(android_driver, login):
    account_page = AccountPage(android_driver)
    account_page.select_account("Checking")

    transaction_page = TransactionPage(android_driver)
    return transaction_page


def test_filter_transaction_by_keyword(transaction_page_setup):
    transaction_page = transaction_page_setup
    valid_keywords = ["Online Purchase", "Grocery Shopping", "Utility Bill Payment", "Withdrawal", "Salary Deposit", "Refund", "Bonus"]
    keyword = random.choice(valid_keywords)

    # Enter Keyword
    transaction_page.enter_keyword(keyword)
    transaction_page.filter_button_click()

    # Loop 5 times to get to the end of list
    for i in range(5):
        transaction_descriptions = transaction_page.get_transaction_desc()

        for transaction_desc in transaction_descriptions:
            assert transaction_desc.text == keyword
        
        # Scroll down and display the next two transactions
        transaction_page.driver.swipe(380, 1080, 380, 860)

    transaction_page.driver.press_keycode(4)


def test_filter_transaction_by_amount(transaction_page_setup):
    transaction_page = transaction_page_setup

    min_amount, max_amount = random.randint(20, 50), random.randint(75, 90)

    # Enter min and max amount
    transaction_page.enter_min_amount(min_amount)
    transaction_page.enter_max_amount(max_amount)
    transaction_page.filter_button_click()

    for i in range(5):
        transactions_amount = transaction_page.get_transaction_amount()

        for amount in transactions_amount:
            actual_amount = amount.text.split('$')[1]
            assert min_amount <= round(float(actual_amount), 2) <= max_amount

        transaction_page.driver.swipe(380, 1080, 380, 860)

    transaction_page.driver.press_keycode(4)


def test_filter_transaction_by_date(transaction_page_setup):
    transaction_page = transaction_page_setup

    # Set as per test date generated
    from_date = '2023/' + str(random.randint(10, 12)) + '/' + str(random.randint(1, 31))
    to_date = '2024/' + str(random.randint(1, 2)) + '/' + str(random.randint(1, 31))

    from_date, to_date = from_date, to_date
    expected_from_date = datetime.strptime(from_date, "%Y/%m/%d")
    expected_to_date = datetime.strptime(to_date, "%Y/%m/%d")

    # Enter from and to dates
    transaction_page.enter_from_date(from_date)
    transaction_page.enter_to_date(to_date)
    transaction_page.filter_button_click()

    for i in range(5):
        transactions_timestamp = transaction_page.get_transaction_timestamp()

        for timestamp in transactions_timestamp:
            print(from_date, timestamp.text, to_date)
            actual_timestamp = datetime.strptime(timestamp.text, "%d-%b-%Y")
            assert expected_from_date <= actual_timestamp < expected_to_date

        transaction_page.driver.swipe(380, 1080, 380, 860)
