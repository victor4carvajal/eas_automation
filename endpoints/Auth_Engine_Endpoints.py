"""
Endpoints of Auth
"""
class Auth_Endpoint_Endpoints:
    "class for auth endpoints"

    def auth_url(self,suffix=''):
        "append api endpoint to the base url"
        return self.auth_api_base_url+'api/v1/auth'+suffix

    def auth_token(self,headers,payload):
        "gets access token"
        url = self.auth_url(f"/token")
        response = self.post(url,headers=headers,json=payload)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }
    
    def verify_token(self,headers,payload):
        "verifies access token"
        url = self.auth_url(f"/verifyToken")
        response = self.post(url,headers=headers,json=payload)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }
    
    def resend_validation_code(self,headers,userName):
        "resend validation code"
        url = self.auth_url(f"/resendValidationCode/{userName}")
        response = self.post(url,headers=headers)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }
    
    def send_password_reset_email(self,headers,userName):
        "Send password reset to email"
        url = self.auth_url(f"/SendPasswordResetEmail/{userName}")
        response = self.post(url,headers=headers)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }
    
    # Not in use 
    def vendor(self,payload,headers):
        "vendor"
        url = self.auth_url(f"/vendor")
        response = self.post(url,headers=headers,json=payload)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }
    
    #Not in use
    def request_reset_password(self,payload,headers,email):
        "Requests reset password"
        url = self.auth_url(f"/RequestResetPassword/{email}")
        response = self.post(url,headers=headers,json=payload)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }
    
    def refresh_token(self,payload,headers):
        "Gets refresh token"
        url = self.auth_url(f"/refreshToken")
        response = self.post(url,headers=headers,json=payload)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }
    
    def check_password(self,payload,headers):
        "Checks the password"
        url = self.auth_url(f"/checkPassword")
        response = self.post(url,headers=headers,json=payload)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }
    
    def verify_token_reset_password(self,payload,headers):
        "Verifies token reset password"
        url = self.auth_url(f"/VerifyTokenResetPassword")
        response = self.post(url,headers=headers,json=payload)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }
    
    def password_reset(self,payload,headers):
        "Resets the password"
        url = self.auth_url(f"/PasswordReset")
        response = self.post(url,headers=headers,json=payload)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }
    
    def update_password(self,payload,headers):
        "Updates the password"
        url = self.auth_url(f"/UpdatePassword")
        response = self.put(url,headers=headers,json=payload)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }
    
    def check_password_eas(self,payload,headers):
        "checks the password eas"
        url = self.auth_url(f"/CheckPasswordEAS")
        response = self.post(url,headers=headers,json=payload)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }
    
    def update_security_question_with_pass(self,payload,headers):
        "Updates security question with Pass"
        url = self.auth_url(f"/UpdateSecurityQuestionWithPass")
        response = self.put(url,headers=headers,json=payload)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }