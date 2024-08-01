import os
import sys
import jsonschema
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import conf.api_conf.auth_api_conf.questions_conf as questions_conf

@pytest.mark.API
def test_get_security_questions(test_api_obj):
    "Run API tests"
    try:
        # Initialize variables
        expected_pass = 0
        actual_pass = -1
                    
        #Given I set up headers
        auth_engine_obj = test_api_obj.get_api_engine_object(engine_name="auth engine")
        questions_engine_obj = test_api_obj.get_api_engine_object(engine_name="questions engine")
        headers = auth_engine_obj.set_header_with_basic_auth()

        #When I get security questions 
        questions = questions_engine_obj.get_questions(headers)
        result_flag = True if questions else True
        test_api_obj.log_result(result_flag, 
                                positive='Get security questions successfully', 
                                negative='Failed to get security questions')
        
        #And I validate Token data
        result_flag = True if questions == questions_conf.questions_data else False
        test_api_obj.log_result(result_flag,
                                positive='Questions data is as expected',
                                negative='Questions data is not as expected.')
    
        #Then I validate Token schema 
        try:
            validator = jsonschema.Draft7Validator(questions_conf.questions_schema)
            result_flag = True if validator.is_valid(questions) else False
        except jsonschema.exceptions.ValidationError as e:
            test_api_obj.write(f"Response schema validation error: {e}")

        test_api_obj.log_result(result_flag,
            positive='Questions schema validation is as expected',
            negative='Questions schema validation is not as expected.')
        
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
    test_get_security_questions()