"""
This class models the verify user access page
url: /verify-user-access
"""

from .Base_Page import Base_Page
import conf.ui_conf.locators.verify_user_access_locators_conf as locators
import conf.ui_conf.locators.dashboard_locators_conf as dashboard_locators
from utils.Wrapit import Wrapit

class Verify_User_Access_Page(Base_Page):
    "Page Object for the verify user access page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = "verify-user-access"
        self.open(url)
    
    def set_code(self,code):
        "set the code"
        self.set_text(locators.code_input,code)
        self.conditional_write(True,
                               positive=f'set the code to {code}',
                               negative='could not set the code')
        
    def click_submit(self):
        "submit login"
        result_flag = self.click_element(locators.submit_button)
        self.conditional_write(result_flag,
                               positive='clicked the submit button',
                               negative='could not click submit button')
        return result_flag

    def verify_user_name(self):
        "check the user name"
        result_flag = self.smart_wait(dashboard_locators.user_button,wait_seconds=15)
        self.conditional_write(result_flag,
                               positive='User name is present',
                               negative='could not find user name')
        return result_flag

    @Wrapit._screenshot
    def enter_code(self,code):
        "enter validation code"
        self.start()
        self.set_code(code)
        result_flag = self.click_submit()
        result_flag &= self.verify_user_name()
        self.conditional_write(result_flag,
                               positive='logged into the app',
                               negative='could not login')
        if result_flag:
            self.switch_page("dashboard")
        return result_flag
    
    def resend_code(self):
        "Resend validation code"
        self.start()
        self.click_element(locators.resend_code_button)
        result_flag = self.click_element(locators.resend_code_button)
        self.conditional_write(result_flag,
                               positive='clicked the resend code button',
                               negative='could not click resend code button')
    