from transfer_page import TransferPage
from account_page import AccountPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def toast_message(android_driver):
    # Wait for the toast element to be present
    toast_locator = (By.XPATH, '//android.widget.Toast')
    toast_element = WebDriverWait(android_driver, 10).until(EC.presence_of_element_located(toast_locator))

    return toast_element.text 


def test_transfer_successful(android_driver, login):

    account_page = AccountPage(android_driver)
    account_page.transfer_button_click()

    transfer_page = TransferPage(android_driver)
    transfer_page.enter_to_account_number("2099019500")
    transfer_page.enter_transfer_amount(20)
    transfer_page.transfer_button_click()
    
    actual_toast_message = toast_message(android_driver)

    assert actual_toast_message == '"Transfer successful"'


def test_transfer_invalid_account(android_driver, login):

    account_page = AccountPage(android_driver)
    account_page.transfer_button_click()

    transfer_page = TransferPage(android_driver)
    transfer_page.enter_to_account_number("123456789")
    transfer_page.enter_transfer_amount(20)
    transfer_page.transfer_button_click()
    
    actual_toast_message = toast_message(android_driver)

    assert actual_toast_message == '"One or both accounts not found"'


def test_transfer_insufficient_balance(android_driver, login):

    account_page = AccountPage(android_driver)
    account_page.transfer_button_click()

    transfer_page = TransferPage(android_driver)
    transfer_page.enter_to_account_number("2099019500")
    transfer_page.enter_transfer_amount(5000)
    transfer_page.transfer_button_click()
    
    actual_toast_message = toast_message(android_driver)

    assert actual_toast_message == '"Insufficient funds for transfer"'
