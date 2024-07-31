import os

#login details

#Secret keys 
SECRET_KEY = os.environ.get('SECRET_KEY')
IV = os.environ.get('IV')

# User details for password recovery
USERNAME1 = os.environ.get('AES_USERNAME1')
SECURITY_QUESTION = os.environ.get("SECURITY_QUESTION")
ANSWER = os.environ.get("ANSWER")

# User details with a predefined password
USERNAME2 = os.environ.get('AES_USERNAME2')
PASSWORD = os.environ.get('AES_PASSWORD')