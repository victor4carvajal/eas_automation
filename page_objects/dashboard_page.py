"""
This class models the dashboard page
url: /dashboard
"""

from .Base_Page import Base_Page
import conf.ui_conf.locators.dashboard_locators_conf as locators
from utils.Wrapit import Wrapit

class Dashboard_Page(Base_Page):
    "Page Object for the dashboard page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = "dashboard"
        self.open(url)

    def logout(self):
        self.click_element(locators.user_button)
        self.click_element(locators.sign_out_button)
    