import os
import sys
import jsonschema
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils.email_util as email_util
import conf.utils_conf.email_conf as email_conf
import conf.utils_conf.login_conf as login_conf
import conf.api_conf.auth_api_conf.auth_conf as auth_conf

# API Test for the auth engine
@pytest.mark.API
def test_refresh_token(test_api_obj):
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

        # Set email details
        imaphost = email_conf.imaphost
        email_username = email_conf.email_username2
        email_app_password = email_conf.app_password2
        subject = email_conf.verify_email_subject
        sender = email_conf.sender
            
        # Given I login at eas app
        auth_engine_obj = test_api_obj.get_api_engine_object(engine_name="auth engine")
        headers = auth_engine_obj.set_header_with_basic_auth()
        encypte_password = auth_engine_obj.encrypt(password,secret_key,iv)
        payload_token = auth_conf.token_payload(username,encypte_password)
        auth_engine_obj.auth_token(headers,payload_token)
        email_service_obj = email_util.Email_Util()
        code = email_service_obj.get_code(imaphost, email_username, email_app_password,subject,sender)
        result_flag = True if code else False
        test_api_obj.log_result(result_flag, 
                                positive='Login successfully', 
                                negative='Failed to login')

        # And I get authToken
        verify_token_payload = auth_conf.verify_token_payload(code,username)
        verifyToken = auth_engine_obj.verify_token(headers, verify_token_payload)
        authToken= verifyToken.get('content', {}).get('authToken', None)
        result_flag = True if authToken else False
        test_api_obj.log_result(result_flag, 
                                positive='Gets authToken successfully', 
                                negative='Failed to get authToken')

        # When I refresh token 
        refresh_token_payload = auth_conf.refresh_token_payload(authToken)
        refreshToken = auth_engine_obj.refresh_token(headers,refresh_token_payload)
        result_flag = True if refreshToken else False
        test_api_obj.log_result(result_flag, 
                                positive='Refresh Token successfully', 
                                negative='Failed to refresh token')
        
        #Then I validate refresh token schema
        try:
            validator = jsonschema.Draft7Validator(auth_conf.refresh_token_schema)
            result_flag = True if validator.is_valid(refreshToken) else False
        except jsonschema.exceptions.ValidationError as e:
            test_api_obj.write(f"Response schema validation error: {e}")

        test_api_obj.log_result(result_flag,
            positive='Refresh token schema validation is as expected',
            negative='Refresh token schema validation is not as expected.')
        
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
    test_refresh_token()