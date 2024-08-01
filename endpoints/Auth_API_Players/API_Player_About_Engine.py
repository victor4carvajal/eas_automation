"""
About specific API Player
"""
from utils.results import Results
import logging

class API_Player_About_Engine(Results):
    "class for About api player"

    def __init__(self, api_obj, log_file_path=None, session_flag=False):
        super(API_Player_About_Engine, self).__init__(
            level=logging.DEBUG, log_file_path=log_file_path)
        self.api_obj = api_obj

    def get_version(self,headers):

        response = self.api_obj.get_version(headers=headers)
        if response.get('error',None):
            raise ValueError(f'error when trying to get version. {response.get("error",None)}')
        version = response.get('json_response',False)
        result_flag = True if version is not {} else False
        self.conditional_write(result_flag,
                                positive="Version data is available",
                                negative="Version data is not found.")
        
        return version