# test_login.py
from login_page import LoginPage
from account_page import AccountPage


def test_valid_login(android_driver):

    # Open Login Page
    login_page = LoginPage(android_driver)

    # Perform login
    login_page.enter_username("sa-1")
    login_page.enter_password("sa-1")
    login_page.click_login_button()

    # Validate Account Page
    account_page = AccountPage(android_driver)
    welcome_message_text = account_page.get_customer_name_welcome_message()
    assert "Hello, John" == welcome_message_text

    android_driver.press_keycode(4)

def test_invalid_user(android_driver):

    login_page = LoginPage(android_driver)

    # Perform login
    login_page.enter_username("bob")
    login_page.enter_password("sa-1")
    login_page.click_login_button()

    login_error_msg = login_page.get_login_error_msg()

    assert login_error_msg == "User not found"



def test_invalid_credentials(android_driver):

    login_page = LoginPage(android_driver)

    # Perform login
    login_page.enter_username("sa-1")
    login_page.enter_password("password")
    login_page.click_login_button()

    login_error_msg = login_page.get_login_error_msg()

    assert login_error_msg == "Invalid Credentials"
