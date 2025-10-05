# test_login.py
from login_page import LoginPage
from account_page import AccountPage


def test_valid_login(driver):

    # Open Login Page
    login_page = LoginPage(driver)

    # Perform login
    login_page.enter_username("sa-1")
    login_page.enter_password("sa-1")
    login_page.click_login_button()

    # Validate Account Page
    account_page = AccountPage(driver)
    welcome_message_text = account_page.get_customer_name_welcome_message()
    assert "Hello, John" == welcome_message_text

    driver.press_keycode(4)

def test_invalid_user(driver):

    login_page = LoginPage(driver)

    # Perform login
    login_page.enter_username("bob")
    login_page.enter_password("sa-1")
    login_page.click_login_button()

    login_error_msg = login_page.get_login_error_msg()

    assert login_error_msg == "User not found"



def test_invalid_credentials(driver):

    login_page = LoginPage(driver)

    # Perform login
    login_page.enter_username("sa-1")
    login_page.enter_password("password")
    login_page.click_login_button()

    login_error_msg = login_page.get_login_error_msg()

    assert login_error_msg == "Invalid Credentials"
