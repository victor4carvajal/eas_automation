"""
A composed interface for all the API objects
Use the API_Player to talk to this class
"""
import requests
from .Base_API import Base_API
from .Auth_Engine_Endpoints import Auth_Endpoint_Endpoints

class API_Interface(
	Base_API,
	Auth_Endpoint_Endpoints):
	
	"A composed interface for the API objects"

	def __init__(self, url, session_flag=False):
		"Constructor"
		# make base_url available to all API endpoints
		self.request_obj = requests
		if session_flag:
			self.create_session()
		self.api_base_url = url

	def create_session(self):
		"Create a session object"
		self.request_obj = requests.Session()

		return self.request_obj
