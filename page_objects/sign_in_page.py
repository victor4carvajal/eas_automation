"""
This class models the sign in page
url: /sign-in
"""

from .Base_Page import Base_Page
import conf.ui_conf.locators.login_locators_conf as locators
import conf.ui_conf.locators.verify_user_access_locators_conf as verify_user_access_locators
from utils.Wrapit import Wrapit

class Sign_In_Page(Base_Page):
    "Page Object for the login page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = "sign-in"
        self.open(url)

    def reload(self):
        self.reload_page()
    
    def set_username(self,username):
        "set the username"
        self.smart_wait(locators.email_input,wait_seconds=15)
        self.set_text(locators.email_input,username)
        self.conditional_write(True,
                               positive=f'set the username to {username}',
                               negative='could not set the username')
    
    def set_password(self,password):
        "set the password"
        self.set_text(locators.password_input,password)
        self.conditional_write(True,
                               positive='set the password',
                               negative='could not set the password')
        
    def click_login(self):
        "submit login"
        result_flag = self.click_element(locators.login_button)
        self.conditional_write(result_flag,
                               positive='clicked the login button',
                               negative='could not click login button')
        return result_flag

    def verify_user_access_panel(self):
        "check the verify user access panel"
        result_flag = self.smart_wait(verify_user_access_locators.verify_user_access_panel,wait_seconds=15)
        self.conditional_write(result_flag,
                               positive='Verify user access panel present',
                               negative='could not find verify user access panel')
        return result_flag

    @Wrapit._screenshot
    def login(self,username,password):
        "login"
        self.start()
        self.reload()
        self.set_username(username)
        self.set_password(password)
        result_flag = self.click_login()
        result_flag &= self.verify_user_access_panel()
        self.conditional_write(result_flag,
                               positive='Send code for validation in to the app',
                               negative='could not send code')
        if result_flag:
            self.switch_page("verify-user-access")
        return result_flag