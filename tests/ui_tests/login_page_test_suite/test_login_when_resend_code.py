"""
This test file will resend validation code
"""
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
import conf.utils_conf.email_conf as email_conf
import utils.email_util as email_util
import conf.utils_conf.login_conf as login_conf

import pytest

@pytest.mark.GUI
def test_login_when_resend_code(test_obj):
    'resend validation code successful'

    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #Set email details
        imaphost = email_conf.imaphost
        email_username = email_conf.email_username2
        email_app_password = email_conf.app_password2
        subject = email_conf.verify_email_subject
        sender = email_conf.sender

        # Given I login at EAS to send code
        test_obj = PageFactory.get_page_object("Sign-in page", base_url=test_obj.base_url)
        result_flag = test_obj.login(login_conf.USERNAME2,login_conf.PASSWORD)
        test_obj.log_result(result_flag,
                            positive='successfully send validation code',
                            negative='failed to send validation code')
        
        # And I click on resend code
        test_obj = PageFactory.get_page_object("verify-user-access page", base_url=test_obj.base_url)
        result_flag = False if test_obj.resend_code() else True
        test_obj.log_result(result_flag,
                            positive='successfully resend validation code',
                            negative='failed to resend validation code')
        
        # When I login at my email to the  get code
        email_service_obj = email_util.Email_Util()
        code = email_service_obj.get_code(imaphost, email_username, email_app_password,subject,sender)
        result_flag = True if code else False
        test_obj.log_result(result_flag, 
                            positive='Get code successfully', 
                            negative='Failed to get code')
        
        # Then I enter the code to login successful 
        result_flag = test_obj.enter_code(code)
        test_obj.log_result(result_flag,
                            positive='successfully logged into the EAS application',
                            negative='failed to login to the EAS application')
        
        # And I Logout
        test_obj = PageFactory.get_page_object("dashboard page",base_url=test_obj.base_url)
        result_flag = False if test_obj.logout() else True
        test_obj.log_result(result_flag,
                            positive='successfully to logout to the EAS application',
                            negative='failed to logout to the EAS application')

        #Print out the result
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__