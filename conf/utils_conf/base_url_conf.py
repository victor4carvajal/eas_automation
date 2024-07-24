"""
Conf file for base_url
"""
import os

base_url = os.environ.get('AES_ENV')
auth_api_base_url = os.environ.get('AUTH_API_URL')
aes_api_base_url = os.environ.get('AES_API_URL')

