from appium import webdriver
from appium.options.android import UiAutomator2Options

from login_page import LoginPage

import pytest


@pytest.fixture(scope="module")
def android_driver(request):
    capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    language='en',
    locale='US',
    appPackage = 'com.example.banking',
    appActivity = '.LoginActivity'
    )

    appium_server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    # Set an implicit wait with a timeout of 30 seconds
    driver.implicitly_wait(30)

    def driver_teardown():
        driver.quit()

    request.addfinalizer(driver_teardown)

    return driver


@pytest.fixture(scope="module")
def login(android_driver):
    login_page = LoginPage(android_driver)

    # Perform login
    login_page.enter_username("sa-1")
    login_page.enter_password("sa-1")
    login_page.click_login_button()
