from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def display(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        return element.is_displayed()

    def contains(self, locator_type, locator_value, a):
        element = self.get_element(locator_type, locator_value)
        return element.text.__contains__(a)

    def endswith(self, locator_type, locator_value, a):
        element = self.get_element(locator_type, locator_value)
        return element.text.endswith(a)

    def text_equal(self, locator_type, locator_value, a):
        element = self.get_element(locator_type, locator_value)
        return element.text.__eq__(a)

    def Action_chain(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def click_on_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()

    def type_into_element(self, locator_type, locator_value, text):
        element = self.get_element(locator_type, locator_value)
        element.send_keys(text)

    def get_element(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def get_elements(self, locator_type, locator_value):
        elements = None
        if locator_type.endswith("_id"):
            elements = self.driver.find_elements(By.ID, locator_value)
        elif locator_type.endswith("_xpath"):
            elements = self.driver.find_elements(By.XPATH, locator_value)
        elif locator_type.endswith("_name"):
            elements = self.driver.find_elements(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            elements = self.driver.find_elements(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            elements = self.driver.find_elements(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_css"):
            elements = self.driver.find_elements(By.CSS_SELECTOR, locator_value)
        return elements
