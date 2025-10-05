from appium import webdriver
from appium.options.android import UiAutomator2Options

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

