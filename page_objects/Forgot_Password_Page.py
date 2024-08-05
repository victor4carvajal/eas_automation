"""
This class models the login page
url: /login
"""

import time
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit

class Forgot_Password_Page(Base_Page):
    "Page Object for the forgot password page"

    def get_reset_password_url(self,url):
        self.open_reset_password(url)
        time.sleep(5)
        url = self.get_current_url()
        self.reload_page()

        return url