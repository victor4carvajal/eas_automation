"""
PageFactory uses the factory design pattern.
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
"""

from page_objects.zero_page import Zero_Page
from page_objects.sign_in_page import Sign_In_Page
from page_objects.verify_user_access_page import Verify_User_Access_Page
from page_objects.dashboard_page import Dashboard_Page
from page_objects.Forgot_Password_Page import Forgot_Password_Page
import conf.utils_conf.base_url_conf


class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url=conf.utils_conf.base_url_conf.base_url):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name in ["zero","zero page","agent zero"]:
            test_obj = Zero_Page(base_url=base_url)
        elif page_name in ["sign-in", "sign-in page"]:
            test_obj = Sign_In_Page(base_url=base_url)
        elif page_name in ["verify-user-access", "verify-user-access page"]:
            test_obj = Verify_User_Access_Page(base_url=base_url)
        elif page_name in ["dashboard", "dashboard page"]:
            test_obj = Dashboard_Page(base_url=base_url)
        elif page_name in ["forgot password page"]:
            test_obj = Forgot_Password_Page(base_url=base_url)

        return test_obj

    get_page_object = staticmethod(get_page_object)