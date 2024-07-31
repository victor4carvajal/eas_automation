import os
#Details needed for the Gmail
#Fill out the email details over here
imaphost ="imap.gmail.com"  #Add imap hostname of your email client
verify_email_subject = "Please verify your sign in"
send_password_reset_email_subject = "Please reset your password"
sender = "info@gmstek.com"

# User details for password recovery
email_username1 = os.environ.get('EMAIL_USERNAME1')
email_username2 = os.environ.get('EMAIL_USERNAME2')

# User details with a predefined password
app_password1 = os.environ.get('APP_PASSWORD1')
app_password2 = os.environ.get('APP_PASSWORD2')

#Details for sending pytest report
smtp_ssl_host = 'smtp.gmail.com'  # Add smtp ssl host of your email client
smtp_ssl_port = 465  # Add smtp ssl port number of your email client
sender1 = 'abc@xyz.com' #Add senders email address here
targets = ['asd@xyz.com','qwe@xyz.com'] # Add recipients email address in a list




