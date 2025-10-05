from transfer_page import TransferPage
from account_page import AccountPage
from transaction_page import TransactionPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import constants

# Test Accounts. Set as per test data generated
CHECKING_ACCOUNT="4132263969"
SAVINGS_ACCOUNT="5750292325"
INVALID_ACCOUNT="123456789"


def toast_message(android_driver):
    # Wait for the toast element to be present
    toast_locator = (By.XPATH, constants.TOAST_WIDGET)
    toast_element = WebDriverWait(android_driver, 10).until(EC.presence_of_element_located(toast_locator))

    return toast_element.text 


def validate_transaction(transaction_page, expected_desc, expected_amount, expected_curr_bal):
    availble_balance = transaction_page.get_transaction_available_balance()
    desc = transaction_page.get_transaction_desc()[0].text
    amount = transaction_page.get_transaction_amount()[0].text
    current_balance = transaction_page.get_transaction_current_balance()[0].text

    print("Desc: ", desc)
    print("Amount: ", amount)
    print("Curr Bal: ", current_balance)
    print("Avail Bal: ", availble_balance)

    if 'Savings' in expected_desc:
        assert expected_desc in desc
    else:
        assert desc == expected_desc

    assert round(float(amount.split("$")[1]), 2) == round(float(expected_amount), 2)
    assert round(float(current_balance.split("$")[1]), 2) == round(float(expected_curr_bal), 2)
    assert round(float(availble_balance.split("$")[1]), 2) == round(float(expected_curr_bal), 2)

def test_transfer_successful(android_driver, login):
    """Successful Transfer from Savings to Checking."""

    account_from = "Savings"
    account_to_number = CHECKING_ACCOUNT
    transfer_amount = random.randint(20, 50)

    account_page = AccountPage(android_driver)
    transaction_page = TransactionPage(android_driver)

    accounts_balance = account_page.get_account_balance()
    expected_from_curr_bal = float(accounts_balance[1].text.split("$")[1]) - float(transfer_amount)
    expected_to_curr_bal = float(accounts_balance[0].text.split("$")[1]) + float(transfer_amount)

    # Initiate Transfer.
    account_page.transfer_button_click()
    transfer_page = TransferPage(android_driver)
    transfer_page.select_account(account_from)
    transfer_page.enter_to_account_number(account_to_number)
    transfer_page.enter_transfer_amount(transfer_amount)
    transfer_page.transfer_button_click()
    
    actual_toast_message = toast_message(android_driver)
    assert actual_toast_message == constants.TRANSFER_SUCCESSFUL

    # Navigate back to accounts page
    android_driver.press_keycode(4)

    # Select the transfer from account
    account_page.select_account(account_from)
    validate_transaction(transaction_page, f"Deposit to Acc. Checking-{account_to_number[-4:]}", transfer_amount, expected_from_curr_bal)

    # Navigate back to accounts page
    android_driver.press_keycode(4)

    # Select the transfer to account
    account_page.select_account(account_to_number[-4:])
    validate_transaction(transaction_page, "Deposit from Acc. Savings", transfer_amount, expected_to_curr_bal)

    android_driver.press_keycode(4)


def test_transfer_invalid_account(android_driver, login):
    """Invalid Transfer."""

    account_page = AccountPage(android_driver)
    account_page.transfer_button_click()

    # Default Transfer from_account is Checking
    transfer_page = TransferPage(android_driver)
    transfer_page.enter_to_account_number(INVALID_ACCOUNT)
    transfer_page.enter_transfer_amount(20)
    transfer_page.transfer_button_click()
    
    actual_toast_message = toast_message(android_driver)
    assert actual_toast_message == constants.ONE_OR_BOTH_ACCOUNT_NOT_FOUND


def test_transfer_insufficient_balance(android_driver, login):
    """Insufficient balance."""
    account_page = AccountPage(android_driver)
    account_page.transfer_button_click()

    # Default Transfer from_account is Checking
    transfer_page = TransferPage(android_driver)
    transfer_page.enter_to_account_number(SAVINGS_ACCOUNT)
    transfer_page.enter_transfer_amount(5000)
    transfer_page.transfer_button_click()
    
    actual_toast_message = toast_message(android_driver)
    assert actual_toast_message == constants.INSUFFICIENT_BALANCE


def test_transfer_to_self(android_driver, login):
    """Transfer to Self."""
    account_page = AccountPage(android_driver)
    account_page.transfer_button_click()

    # Default Transfer from_account is Checking
    transfer_page = TransferPage(android_driver)
    transfer_page.enter_to_account_number(CHECKING_ACCOUNT)
    transfer_page.enter_transfer_amount(20)
    transfer_page.transfer_button_click()

    actual_toast_message = toast_message(android_driver)
    assert actual_toast_message == constants.CANNOT_TRANSFER_TO_SELF

