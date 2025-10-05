from appium.webdriver.common.appiumby import AppiumBy


class Driver:

    def __init__(self, driver):
        self.driver = driver


    def get_text(self, element_id):
        return self.driver.find_element(AppiumBy.ID, element_id).text


    def set_text(self, element_id, value):
        self.driver.find_element(AppiumBy.ID, element_id).send_keys(value)


    def clear_text(self, element_id):
        self.driver.find_element(AppiumBy.ID, element_id).clear()


    def click(self, element_id):
        self.driver.find_element(AppiumBy.ID, element_id).click()
