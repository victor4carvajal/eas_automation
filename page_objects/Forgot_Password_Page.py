"""
This class models the login page
url: /login
"""

from .Base_Page import Base_Page
from utils.Wrapit import Wrapit

class Forgot_Password_Page(Base_Page):
    "Page Object for the login page"

    def get_reset_password_url(self,url):
        "Use this method to go to specific URL -- if needed"
        self.open_reset_password(url)
        url = self.get_current_url()

        return url