# test_login.py
from login_page import LoginPage
from account_page import AccountPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants


def toast_message(android_driver):
    # Wait for the toast element to be present
    toast_locator = (By.XPATH, constants.TOAST_WIDGET)
    toast_element = WebDriverWait(android_driver, 10).until(EC.presence_of_element_located(toast_locator))
    return toast_element.text 


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
    assert welcome_message_text == constants.WELCOME_MESSAGE

    android_driver.press_keycode(4)


def test_invalid_user(android_driver):
    login_page = LoginPage(android_driver)

    # Perform login
    login_page.enter_username("bob")
    login_page.enter_password("sa-1")
    login_page.click_login_button()

    actual_toast_message = toast_message(android_driver)
    assert actual_toast_message == constants.USER_NOT_FOUND


def test_invalid_credentials(android_driver):
    login_page = LoginPage(android_driver)

    # Perform login
    login_page.enter_username("sa-1")
    login_page.enter_password("password")
    login_page.click_login_button()

    actual_toast_message = toast_message(android_driver)
    assert actual_toast_message == constants.INVALID_CREDENTIALS
