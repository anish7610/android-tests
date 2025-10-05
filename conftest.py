from appium import webdriver
from appium.options.android import UiAutomator2Options

from login_page import LoginPage

import pytest



@pytest.fixture(scope="module")
def driver(request):
    capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    language='en',
    locale='US',
    app='bank.apk'
    )

    appium_server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    # Set an implicit wait with a timeout of 30 seconds
    driver.implicitly_wait(30)

    def driver_teardown():
        driver.quit()

    request.addfinalizer(driver_teardown)

    return driver

@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)

    # Perform login
    login_page.enter_username("sa-1")
    login_page.enter_password("sa-1")
    login_page.click_login_button()
