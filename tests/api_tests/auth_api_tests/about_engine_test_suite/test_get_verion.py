import os
import sys
import jsonschema
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import conf.api_conf.auth_api_conf.about_conf as about_conf

@pytest.mark.API
def test_get_version(test_api_obj):
    "Run API tests"
    try:
        # Initialize variables
        expected_pass = 0
        actual_pass = -1
                    
        #Given I set up headers
        auth_engine_obj = test_api_obj.get_api_engine_object(engine_name="auth engine")
        about_engine_obj = test_api_obj.get_api_engine_object(engine_name="about engine")
        headers = auth_engine_obj.set_header_with_basic_auth()

        #When I get version 
        version = about_engine_obj.get_version(headers)
        result_flag = True if version else True
        test_api_obj.log_result(result_flag, 
                                positive='Gets version successfully', 
                                negative='Failed to get version')
    
        #Then I validate Token schema 
        try:
            validator = jsonschema.Draft7Validator(about_conf.version_schema)
            result_flag = True if validator.is_valid(version) else False
        except jsonschema.exceptions.ValidationError as e:
            test_api_obj.write(f"Response schema validation error: {e}")

        test_api_obj.log_result(result_flag,
            positive='Version schema validation is as expected',
            negative='Version schema validation is not as expected.')
        
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
    test_get_version()