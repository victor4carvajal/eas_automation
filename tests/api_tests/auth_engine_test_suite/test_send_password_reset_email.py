"""
API Test
test auth engine
"""
import os
import sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils.email_util as email_util
import conf.utils_conf.email_conf as email_conf
import conf.utils_conf.login_conf as login_conf
import conf.api_conf.auth_conf as auth_conf

# API Test for the auth engine
@pytest.mark.API
def test_auth_engine(test_api_obj):
    "Run API tests"
    try:
        # Initialize variables
        expected_pass = 0
        actual_pass = -1

        # Set authentication details
        username = login_conf.USERNAME

        #Set email details
        imaphost = email_conf.imaphost
        email_app_password = email_conf.app_password
        subject = email_conf.send_password_reset_email_subject
        sender = email_conf.sender
            
        auth_engine_obj = test_api_obj.get_api_engine_object(engine_name="auth engine")
        
        #get token payload and headers
        headers = auth_engine_obj.get_headers()

        #Send password reset email
        passwordResetEmail = auth_engine_obj.send_password_reset_email(headers,username)
        result_flag = True if passwordResetEmail == False else True
        test_api_obj.log_result(result_flag, 
                                positive='Send password reset email successfully', 
                                negative='Failed to send password reset mail')
        
        print(passwordResetEmail)

        # Validate send password reset data
        result_flag = True if passwordResetEmail == auth_conf.send_password_reset_email_data else False
        test_api_obj.log_result(result_flag,
                                positive='Send password reset email data is as expected',
                                negative='Send password reset email data is not as expected.')
        
        # Initialize Email and get code
        email_service_obj = email_util.Email_Util()
        bodyEmail = email_service_obj.get_password_reset_email(imaphost, username, email_app_password,subject,sender)
        result_flag = True if bodyEmail == False else True
        test_api_obj.log_result(result_flag, 
                                positive='Get password reset email successfully', 
                                negative='Failed to get password reset email')
        
        # Write out test summary
        expected_pass = test_api_obj.total
        actual_pass = test_api_obj.passed
        test_api_obj.write_test_summary()

    except Exception as e:
        test_api_obj.write(f"Exception when trying to run test:{__file__}")
        test_api_obj.write(f"Python says:{str(e)}")

    # Assertion
    assert expected_pass == actual_pass, "Test failed: %s" % __file__

if __name__ == '__main__':
    test_auth_engine()