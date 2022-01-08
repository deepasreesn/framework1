import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import ChromiumOptions
class BaseTest:
    xl_path="./data/input.xlsx"
    @pytest.fixture(autouse=True)
    def open_app(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",options=ChromiumOptions())
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://demo.actitime.com/login.do")
        self.wait=WebDriverWait(driver,10)
        self.driver=driver
        yield
        driver.quit()
