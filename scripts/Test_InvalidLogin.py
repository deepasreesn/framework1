import pytest

from generic.BaseTest import BaseTest
from pages.LoginPage import LoginPage
from generic.Excel import Execl

class Test_InvalidLogin(BaseTest):

    @pytest.mark.run(order=2)
    def test_invalid_login(self):
       un=Execl.getData(self.xl_path,"InvalidLogin",2,1);
       pw=Execl.getData(self.xl_path,"ValidLogin",2,2);
       login_page=LoginPage(self.driver)
       login_page.setUserName(un)
       login_page.setPassword(pw)
       login_page.clickLogin()
       result=login_page.verify_err_msg_displayed(self.wait)
       assert result