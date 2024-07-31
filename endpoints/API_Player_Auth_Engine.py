"""
Auth specific API Player
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
from utils.results import Results
import logging

class API_Player_Auth_Engine(Results):
    "class for auth api player"

    def __init__(self, api_obj, log_file_path=None, session_flag=False):
        super(API_Player_Auth_Engine, self).__init__(
            level=logging.DEBUG, log_file_path=log_file_path)
        self.api_obj = api_obj

    def encrypt(self,password,secret_key,iv):

        key_bytes = secret_key.encode('utf-8')
        iv_bytes = iv.encode('utf-8')
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        padded_password = pad(password.encode('utf-8'), AES.block_size)
        encrypted_bytes = cipher.encrypt(padded_password)
        encrypted_base64_password = base64.b64encode(encrypted_bytes).decode('utf-8')
    
        return encrypted_base64_password

    def get_headers(self):
        """
        Create header details with specific values.
        """
        headers = {
            'Content-Type': 'application/json'
        }
        return headers

    def auth_token(self,headers,payload):

        response = self.api_obj.auth_token(headers=headers,payload=payload)
        if response.get('error',None):
            raise ValueError(f'error when trying to get token details. {response.get("error",None)}')
        token = response.get('json_response',False)
        result_flag = True if token is not {} else False
        self.conditional_write(result_flag,
                                positive="Token data is available",
                                negative="Token data is not found.")
        return token
        
    def verify_token(self,headers,payload):

        response = self.api_obj.verify_token(headers=headers,payload=payload)
        if response.get('error',None):
            raise ValueError(f'error when trying to get token details. {response.get("error",None)}')
        verifyToken = response.get('json_response',False)
        result_flag = True if verifyToken is not {} else False
        self.conditional_write(result_flag,
                                positive="Verify token data is available",
                                negative="Verify token data is not found.")
        return verifyToken
    
    def resend_validation_code(self,headers,userName):

        response = self.api_obj.resend_validation_code(headers=headers,userName=userName)
        if response.get('error',None):
            raise ValueError(f'error when trying to resend validation code. {response.get("error",None)}')
        resendValidationCode = response.get('json_response',False)
        result_flag = True if resendValidationCode is not {} else False
        self.conditional_write(result_flag,
                                positive="Resend Validation code data is available",
                                negative="Resend Validation code data is not found.")
        return resendValidationCode
    
    def send_password_reset_email(self,headers,userName):

        response = self.api_obj.send_password_reset_email(headers=headers,userName=userName)
        if response.get('error',None):
            raise ValueError(f'error when trying to send password reset email. {response.get("error",None)}')
        sendPasswordResetEmail = response.get('json_response',False)
        result_flag = True if sendPasswordResetEmail is not {} else False
        self.conditional_write(result_flag,
                                positive="Send password reset email data is available",
                                negative="Send password reset email data is not found.")
        return sendPasswordResetEmail
    
    def verify_token_reset_password(self,headers,payload):
        
        response = self.api_obj.verify_token_reset_password(headers=headers,payload=payload)
        if response.get('error',None):
            raise ValueError(f'error when trying to verify token reset password. {response.get("error",None)}')
        verifyTokenResetPassword = response.get('json_response',False)
        result_flag = True if verifyTokenResetPassword is not {} else False
        self.conditional_write(result_flag,
                                positive="Verify token reset password data is available",
                                negative="Verify token reset password data is not found.")
        return verifyTokenResetPassword