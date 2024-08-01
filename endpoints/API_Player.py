"""
API_Player class does the following:
a) serves as an interface between the test and API_Interface
b) contains several useful wrappers around commonly used combination of actions
c) maintains the test context/state
"""
from .API_Interface import API_Interface
from .Auth_API_Players.API_Player_Auth_Engine import API_Player_Auth_Engine
from .Auth_API_Players.API_Player_About_Engine import API_Player_About_Engine
from .Auth_API_Players.API_PLayer_Questions_Engine import API_Player_Questions_Engine
from utils.results import Results
import logging
import conf.utils_conf.base_url_conf as base_url_conf

class API_Player(Results):
    "The class that maintains the test context/state"

    def __init__(self, auth_url, aes_url, log_file_path=None, session_flag=False):
        "Constructor"
        super(API_Player, self).__init__(
            level=logging.DEBUG, log_file_path=log_file_path)
        self.api_obj = API_Interface(auth_url=base_url_conf.auth_api_base_url, aes_url=base_url_conf.aes_api_base_url, session_flag=session_flag)
        self.log_file_path = log_file_path

    def get_api_engine_object(self, engine_name):
        "Return the appropriate api object based on engine name"
        api_engine_obj = None
        api_engine_name = engine_name.lower()
        if api_engine_name in ["auth", "auth engine"]:
            api_engine_obj = API_Player_Auth_Engine(self.api_obj, log_file_path=self.log_file_path)
        elif api_engine_name in ["about", "about engine"]:
            api_engine_obj = API_Player_About_Engine(self.api_obj, log_file_path=self.log_file_path)
        elif api_engine_name in ["questions", "questions engine"]:
            api_engine_obj = API_Player_Questions_Engine(self.api_obj, log_file_path=self.log_file_path)
        
        return api_engine_obj
    