"""
This class models the dashboard page
url: /dashboard
"""

from .Base_Page import Base_Page
import conf.ui_conf.locators.verify_user_access_conf as locators
from utils.Wrapit import Wrapit

class Dashboard_Page(Base_Page):
    "Page Object for the verify user access page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = "dashboard"
        self.open(url)
    
    def set_code(self,code):
        "set the code"
        self.set_text(locators.code_input,code)
        self.conditional_write(True,
                               positive=f'set the code to {code}',
                               negative='could not set the code')
    
    def set_password(self,password):
        "set the password"
        self.set_text(locators.password_input,password)
        self.conditional_write(True,
                               positive='set the password',
                               negative='could not set the password')
        
    def click_submit(self):
        "submit login"
        result_flag = self.click_element(locators.submit_button)
        self.conditional_write(result_flag,
                               positive='clicked the submit button',
                               negative='could not click submit button')
        return result_flag

    def verify_profile_image(self):
        "check the profile image is present"
        result_flag = self.smart_wait(locators.profile_image,wait_seconds=15)
        self.conditional_write(result_flag,
                               positive='profile image present',
                               negative='could not find profile image')
        return result_flag

    @Wrapit._screenshot
    def enter_code(self,code):
        "enter validation code"
        self.set_code(code)
        result_flag = self.click_submit()
        #result_flag &= self.verify_profile_image()
        self.conditional_write(result_flag,
                               positive='logged into the app',
                               negative='could not login')
        if result_flag:
            self.switch_page("verify user access page")
        return result_flag
    