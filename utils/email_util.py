"""
A simple IMAP util that will help us with account activation
* Connect to your imap host
* Login with username/password
* Fetch latest messages in inbox
* Get a recent registration message
* Filter based on sender and subject
* Return text of recent messages

[TO DO](not in any particular order)
1. Extend to POP3 servers
2. Add a try catch decorator
3. Enhance get_latest_email_uid to make all parameters optional
"""
#The import statements import: standard Python modules,conf
import base64
import json
import re
import os,sys,time,imaplib,email
from urllib.parse import urlparse, parse_qs, unquote
import requests
from bs4 import BeautifulSoup
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Email_Util:
    "Class to interact with IMAP servers"

    def connect(self,imap_host):
        "Connect with the host"
        self.mail = imaplib.IMAP4_SSL(imap_host)

        return self.mail


    def login(self,username,password):
        "Login to the email"
        result_flag = False
        try:
            time.sleep(5)
            self.mail.login(username,password)
        except Exception as e:
            print('\nException in Email_Util.login')
            print('PYTHON SAYS:')
            print(e)
            print('\n')
        else:
            result_flag = True

        return result_flag
    
    def search_email(self, subject, sender):
        try:
            self.mail.select('inbox')
            subject_criteria = f'SUBJECT "{subject}"'
            from_criteria = f'FROM "{sender}"'
            search_criteria = f'({subject_criteria} {from_criteria})'
            status, messages = self.mail.search(None, search_criteria)
            mail_ids = messages[0].decode().split()
            return mail_ids
        except Exception as e:
            print(f"Exception in Email_Util.search_email\nPYTHON SAYS:\n{str(e)}")
            return []
        
    def fetch_email_body(self, mail_id):
        try:
            status, msg_data = self.mail.fetch(mail_id, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get('Content-Disposition'))

                            if 'attachment' not in content_disposition:
                                if content_type == 'text/html':
                                    html_content = part.get_payload(decode=True).decode('utf-8', errors='replace')
                                    soup = BeautifulSoup(html_content, 'html.parser')
                                    body = soup.get_text()
                                    return body
                    else:
                        if msg.get_content_type() == 'text/html':
                            html_content = msg.get_payload(decode=True).decode('utf-8', errors='replace')
                            soup = BeautifulSoup(html_content, 'html.parser')
                            body = soup.get_text()
                            return body
        except Exception as e:
            print(f"Exception in Email_Util.fetch_email_body\nPYTHON SAYS:\n{str(e)}")
            return None

        return None
    
    def extract_verification_code(self, email_body):
        "Extract the verification code from the email body"
        match = re.search(r'Your user access verification code is:\s*(\d+)', email_body)
        if match:
            return match.group(1)
        else:
            print("Verification code not found.")
            return None
    
    def get_last_email_body(self, subject, sender):
        try:
            mail_ids = self.search_email(subject, sender)
            if not mail_ids:
                print("No emails found.")
                return None
            
            last_mail_id = mail_ids[-1]
            body = self.fetch_email_body(last_mail_id)            
            return body
        except Exception as e:
            print(f"Exception in Email_Util.get_last_email_body\nPYTHON SAYS:\n{str(e)}")
            return None

    def logout(self):
        "Logout"
        result_flag = False
        response = self.mail.logout()
        if response == 'BYE':
            result_flag = True

        return result_flag
    
    def get_code(self,imaphost,username,email_app_password,subject,sender):
        "gets code from email"
        self.connect(imaphost)
        self.login(username,email_app_password)
        body = self.get_last_email_body(subject,sender)
        code = self.extract_verification_code(body)
        self.logout()

        return code
    
    def fetch_link_reset_password_email(self, mail_id):
        
        try:
            status, msg_data = self.mail.fetch(mail_id, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get('Content-Disposition'))

                            if 'attachment' not in content_disposition:
                                if content_type == 'text/html':
                                    html_content = part.get_payload(decode=True).decode('utf-8', errors='replace')
                                    soup = BeautifulSoup(html_content, 'html.parser')
                                    body = soup.get_text()
                                    return body
                    else:
                        if msg.get_content_type() == 'text/html':
                            html_content = msg.get_payload(decode=True).decode('utf-8', errors='replace')
                            soup = BeautifulSoup(html_content, 'html.parser')
                            body = soup.get_text()
                            link = soup.find('a', string='Reset Your Password')
                            href = link.get('href')
                            return href
        except Exception as e:
            print(f"Exception in Email_Util.fetch_email_body\nPYTHON SAYS:\n{str(e)}")
            return None

        return None
    
    def get_last_reset_password_email_body(self, subject, sender):

        try:
            mail_ids = self.search_email(subject, sender)
            if not mail_ids:
                print("No emails found.")
                return None
            
            last_mail_id = mail_ids[-1]
            body = self.fetch_link_reset_password_email(last_mail_id)            
            return body
        except Exception as e:
            print(f"Exception in Email_Util.get_last_email_body\nPYTHON SAYS:\n{str(e)}")
            return None
        
    def get_link_reset_password(self,encoded_url):

        response = requests.get(encoded_url)
        final_url = response.url
        parsed_url = urlparse(final_url)
        query_params = parse_qs(parsed_url.query)
        token = query_params.get('token', [None])[0]
        
        return token
    
    def get_reset_token_url(self,imaphost,username,email_app_password,subject,sender):

        self.connect(imaphost)
        self.login(username,email_app_password)
        encoded_url = self.get_last_reset_password_email_body(subject,sender)
        self.logout()

        return encoded_url
        
    def decode_base64_token(self, encoded_token):
        padding = len(encoded_token) % 4
        if padding != 0:
            encoded_token += '=' * (4 - padding)
        try:
            decoded_bytes = base64.urlsafe_b64decode(encoded_token)
            decoded_str = decoded_bytes.decode('utf-8')
            try:
                decoded_json = json.loads(decoded_str)
                return decoded_json 

            except json.JSONDecodeError:
                return decoded_str 
        except Exception as e:
            raise ValueError(f"Error decoding the token: {str(e)}")
        
    def get_token_from_url(self, url):
        parsed_url = urlparse(url)
        query = parsed_url.query
        token = None
        for param in query.split('&'):
            key, value = param.split('=')
            if key == 'token':
                token = unquote(value)
                break
        if token:
            decoded_str = self.decode_base64_token(token)
            decoded_token = decoded_str.get("token")
            return decoded_token
        else:
            raise ValueError("No token found in the URL.")
        
    def get_user_first_name_from_url(self, url):
        parsed_url = urlparse(url)
        query = parsed_url.query
        token = None
        for param in query.split('&'):
            key, value = param.split('=')
            if key == 'token':
                token = unquote(value)
                break
        if token:
            decoded_str = self.decode_base64_token(token)
            decoded_user_first_name = decoded_str.get("userFirstName")
            return decoded_user_first_name
        else:
            raise ValueError("No userFirstName found in the URL.")
        
    def get_user_last_name_from_url(self, url):
        parsed_url = urlparse(url)
        query = parsed_url.query
        token = None
        for param in query.split('&'):
            key, value = param.split('=')
            if key == 'token':
                token = unquote(value)
                break
        if token:
            decoded_str = self.decode_base64_token(token)
            decoded_user_last_name = decoded_str.get("userLastname")
            return decoded_user_last_name
        else:
            raise ValueError("No userLastname found in the URL.")
