"""
API Test
test auth engine
"""
import os
import sys
import jsonschema
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils.email_util as email_util
import conf.utils_conf.email_conf as email_conf
import conf.utils_conf.login_conf as login_conf
import conf.api_conf.auth_conf as auth_conf
from page_objects.PageFactory import PageFactory

# API Test for the auth engine
@pytest.mark.API
def test_auth_engine(test_api_obj,test_obj):
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

        #Given I send password reset email
        passwordResetEmail = auth_engine_obj.send_password_reset_email(headers,username)
        result_flag = True if passwordResetEmail == False else True
        test_api_obj.log_result(result_flag, 
                                positive='Send password reset email successfully', 
                                negative='Failed to send password reset email')
        
        # When I validate send password reset data
        result_flag = True if passwordResetEmail == auth_conf.send_password_reset_email_data else False
        test_api_obj.log_result(result_flag,
                                positive='Send password reset email data is as expected',
                                negative='Send password reset email data is not as expected.')
        
        # Then I validate send reset password email schema
        try:
            validator = jsonschema.Draft7Validator(auth_conf.send_password_reset_email_schema)
            result_flag = True if validator.is_valid(passwordResetEmail) else False
        except jsonschema.exceptions.ValidationError as e:
            test_api_obj.write(f"Response schema validation error: {e}")

        test_api_obj.log_result(result_flag,
            positive='Send password reset email schema validation is as expected',
            negative='Send password reset email schema validation is not as expected.')
        
        # And I initialize Email and get reset token
        email_service_obj = email_util.Email_Util()
        encoded_url = email_service_obj.get_reset_token_url(imaphost, username, email_app_password,subject,sender)
        test_obj = PageFactory.get_page_object("forgot password page", base_url=test_obj.base_url)
        url = test_obj.get_reset_password_url(encoded_url)
        resetToken = email_service_obj.get_token_from_url(url)
        result_flag = True if resetToken else False
        test_api_obj.log_result(result_flag, 
                                positive='Get reset token successfully', 
                                negative='Failed to get reset token')
        
        #Given I verify token reset password 
        verify_token_reset_password_payload = auth_conf.verify_token_reset_password_payload(username,resetToken)
        verifyTokenResetPassword = auth_engine_obj.verify_token_reset_password(headers,verify_token_reset_password_payload)
        result_flag = True if verifyTokenResetPassword else False
        test_api_obj.log_result(result_flag,
                                positive='Verify token reset password successfully', 
                                negative='Failed to verify token reset password')
        
        # When I verify toke reset password data
        result_flag = True if verifyTokenResetPassword == auth_conf.verify_token_reset_password_data else False
        test_api_obj.log_result(result_flag,
                                positive='Verify token reset data is as expected',
                                negative='Verify token reset data is not as expected.')
        
        #Then I validate verify token reset password schema
        try:
            validator = jsonschema.Draft7Validator(auth_conf.verify_token_reset_password_schema)
            result_flag = True if validator.is_valid(verifyTokenResetPassword) else False
        except jsonschema.exceptions.ValidationError as e:
            test_api_obj.write(f"Response schema validation error: {e}")

        test_api_obj.log_result(result_flag,
            positive='Verify token reset password schema validation is as expected',
            negative='Verify token reset password schema validation is not as expected.')
        
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