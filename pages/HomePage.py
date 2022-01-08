from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class HomePage:
    __welcome_msg = (By.XPATH, "//td[text()='Enter Time-Track']")

    def __init__(self, driver):
        self.driver = driver

    def verify_home_page_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__welcome_msg))
            return True
        except:
            return False