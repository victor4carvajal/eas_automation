"""
API Test
test auth engine
"""
import os
import sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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
        password = login_conf.PASSWORD
        secret_key = login_conf.SECRET_KEY
        iv = login_conf.IV
        
        auth_engine_obj = test_api_obj.get_api_engine_object(engine_name="auth engine")
        
        #get payload and headers
        headers = auth_engine_obj.get_headers()
        encypte_password = auth_engine_obj.encrypt(password,secret_key,iv)
        payload_token = auth_conf.token_payload(username,encypte_password)

        #Send auth token 
        token = auth_engine_obj.auth_token(headers,payload_token)
        print(token)
        test_api_obj.log_result(token, 
                                positive='Send Token successfully', 
                                negative='Failed to send token')

        # Write out test summary
        expected_pass = test_api_obj.total
        actual_pass = test_api_obj.passed
        test_api_obj.write_test_summary()

    except Exception as e:
        print(e)
        test_api_obj.write(f"Exception when trying to run test:{__file__}")
        test_api_obj.write(f"Python says:{str(e)}")

    # Assertion
    assert expected_pass == actual_pass, "Test failed: %s" % __file__

if __name__ == '__main__':
    test_auth_engine()