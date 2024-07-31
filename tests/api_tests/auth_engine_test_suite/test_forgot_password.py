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
import utils.password_util as pass_util
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
        username = login_conf.USERNAME1
        secret_key = login_conf.SECRET_KEY
        iv = login_conf.IV
        answer = login_conf.ANSWER
        security_Question = login_conf.SECURITY_QUESTION

        #Set email details
        imaphost = email_conf.imaphost
        email_username = email_conf.email_username1
        email_app_password = email_conf.app_password1
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
        encoded_url = email_service_obj.get_reset_token_url(imaphost, email_username, email_app_password,subject,sender)
        test_obj = PageFactory.get_page_object("forgot password page", base_url=test_obj.base_url)
        url = test_obj.get_reset_password_url(encoded_url)
        token = email_service_obj.get_token_from_url(url)
        result_flag = True if token else False
        test_api_obj.log_result(result_flag, 
                                positive='Get reset token successfully', 
                                negative='Failed to get reset token')
        
        #Given I verify token reset password 
        verify_token_reset_password_payload = auth_conf.verify_token_reset_password_payload(username,token)
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
        
        # Given I want generete a new passoword 
        pass_service_obj = pass_util.Password_Util()
        newPass = pass_service_obj.generate_password()
        result_flag = True if newPass else False
        test_api_obj.log_result(result_flag,
                                positive='Generate new password successfully', 
                                negative='Failed to generate new password')
        
        # And I set password reset payload
        encypte_new_password = auth_engine_obj.encrypt(newPass,secret_key,iv)
        encypte_answer = auth_engine_obj.encrypt(answer,secret_key,iv)
        userFirstName = email_service_obj.get_user_first_name_from_url(url)
        userLastName = email_service_obj.get_user_last_name_from_url(url)
        password_reset_payload = auth_conf.password_reset_payload(encypte_answer,username,encypte_new_password,security_Question,token,userFirstName,userLastName)

        # When I reset the password
        passwordReset = auth_engine_obj.password_reset(headers,password_reset_payload)
        result_flag = True if (passwordReset == 200) else False
        test_api_obj.log_result(result_flag,
                                positive='Password reset successfully', 
                                negative='Failed to reset the password')
        
        #Then I validate password reset schema
        try:
            validator = jsonschema.Draft7Validator(auth_conf.password_reset_schema)
            result_flag = True if validator.is_valid(passwordReset) else False
        except jsonschema.exceptions.ValidationError as e:
            test_api_obj.write(f"Response schema validation error: {e}")

        test_api_obj.log_result(result_flag,
                                positive='Password reset schema validation is as expected',
                                negative='Password reset schema validation is not as expected.')
        
        # And I login with the newPassword
        payload_token = auth_conf.token_payload(username,encypte_new_password)
        login = auth_engine_obj.auth_token(headers,payload_token)
        result_flag = True if login == False else True
        test_api_obj.log_result(result_flag, 
                                positive='Login successfully', 
                                negative='Failed to login')
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