import time
import pytest
from generic.BaseTest import BaseTest
from generic.Excel import Execl
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class Test_ValidLogin(BaseTest):

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        un = Execl.getData(self.xl_path, "ValidLogin", 2, 1);
        pw = Execl.getData(self.xl_path, "ValidLogin", 2, 2);
        login_page = LoginPage(self.driver)
        login_page.setUserName(un)
        login_page.setPassword(pw)
        login_page.clickLogin()
        res = HomePage(self.driver).verify_home_page_displayed(self.wait)
        print(res)
