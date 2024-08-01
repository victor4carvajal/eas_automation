import os
import sys
import jsonschema
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils.email_util as email_util
import conf.utils_conf.email_conf as email_conf
import conf.utils_conf.login_conf as login_conf
import conf.api_conf.auth_conf as auth_conf

# API Test for the auth engine
@pytest.mark.API
def test_resend_validation_code(test_api_obj):
    "Run API tests"
    try:
        # Initialize variables
        expected_pass = 0
        actual_pass = -1

        # Set authentication details
        username = login_conf.USERNAME2
        password = login_conf.PASSWORD
        secret_key = login_conf.SECRET_KEY
        iv = login_conf.IV

        #Set email details
        imaphost = email_conf.imaphost
        email_username = email_conf.email_username2
        email_app_password = email_conf.app_password2
        subject = email_conf.verify_email_subject
        sender = email_conf.sender
            
        auth_engine_obj = test_api_obj.get_api_engine_object(engine_name="auth engine")
        
        #Given I want to get token payload and headers
        headers = auth_engine_obj.get_headers()
        encypte_password = auth_engine_obj.encrypt(password,secret_key,iv)
        payload_token = auth_conf.token_payload(username,encypte_password)

        #When I send validation code 
        token = auth_engine_obj.auth_token(headers,payload_token)
        result_flag = True if token == False else True
        test_api_obj.log_result(result_flag, 
                                positive='Send code successfully', 
                                negative='Failed to send code')

        #Then I resend validation code 
        resendCode = auth_engine_obj.resend_validation_code(headers,username)
        result_flag = True if resendCode == False else True
        test_api_obj.log_result(result_flag, 
                                positive='Resend validation code successfully', 
                                negative='Failed to resend validation code')

        #When I validate Token data
        result_flag = True if resendCode == auth_conf.resend_validation_code_data else False
        test_api_obj.log_result(result_flag,
                                positive='Resend validation code data is as expected',
                                negative='Resend Validation code is not as expected.')
        
        #And I validate Token schema 
        try:
            validator = jsonschema.Draft7Validator(auth_conf.resend_validation_code_schema)
            result_flag = True if validator.is_valid(resendCode) else False
        except jsonschema.exceptions.ValidationError as e:
            test_api_obj.write(f"Response schema validation error: {e}")

        test_api_obj.log_result(result_flag,
            positive='Resend validation code schema validation is as expected',
            negative='Resend Validation code schema validation is not as expected.')
        
        #Then I login at email to get code
        email_service_obj = email_util.Email_Util()
        code = email_service_obj.get_code(imaphost, email_username, email_app_password,subject,sender)
        result_flag = True if code == False else True
        test_api_obj.log_result(result_flag, 
                                positive='Get code successfully', 
                                negative='Failed to get code')
        
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
    test_resend_validation_code()