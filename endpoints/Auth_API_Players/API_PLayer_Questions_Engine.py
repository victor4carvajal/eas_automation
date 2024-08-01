"""
Question specific API Player
"""
from utils.results import Results
import logging

class API_Player_Questions_Engine(Results):
    "class for questions api player"

    def __init__(self, api_obj, log_file_path=None, session_flag=False):
        super(API_Player_Questions_Engine, self).__init__(
            level=logging.DEBUG, log_file_path=log_file_path)
        self.api_obj = api_obj

    def get_questions(self,headers):

        response = self.api_obj.get_questions(headers=headers)
        if response.get('error',None):
            raise ValueError(f'error when trying to get questions. {response.get("error",None)}')
        questions = response.get('json_response',False)
        result_flag = True if questions is not {} else False
        self.conditional_write(result_flag,
                                positive="Questions data is available",
                                negative="Questions data is not found.")
        
        return questions