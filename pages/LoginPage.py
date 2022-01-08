from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class LoginPage:
    __unTB=(By.ID,'username')
    __pwTB=(By.NAME,'pwd')
    __loginBTN=(By.XPATH,"//div[text()='Login ']")
    __errMsg=(By.XPATH,"//span[contains(text(),'invalid')]")

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,un):
        self.driver.find_element(*self.__unTB).send_keys(un)

    def setPassword(self, pw):
        self.driver.find_element(*self.__pwTB).send_keys(pw)

    def clickLogin(self):
        self.driver.find_element(*self.__loginBTN).click()

    def verify_err_msg_displayed(self,wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__errMsg))
            return True
        except:
            return False