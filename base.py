from appium.webdriver.common.appiumby import AppiumBy

class Driver:

    def __init__(self, driver):
        self.driver = driver

    def get_text(self, id):
        return self.driver.find_element(AppiumBy.ID, id).text

    def set_text(self, id, value):
        self.driver.find_element(AppiumBy.ID, id).send_keys(value)

    def clear_text(self, id):
        self.driver.find_element(AppiumBy.ID, id).clear()

    def click(self, id):
        self.driver.find_element(AppiumBy.ID, id).click()
