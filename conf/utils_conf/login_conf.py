import os

#login details
USERNAME = os.environ.get('AES_USERNAME')
PASSWORD = os.environ.get('AES_PASSWORD')
SECRET_KEY = os.environ.get('SECRET_KEY')
IV = os.environ.get('IV')