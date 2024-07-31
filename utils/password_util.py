import random
import string

class Password_Util:

    def generate_password(self):
        upper_case = string.ascii_uppercase
        lower_case = string.ascii_lowercase
        digits = string.digits
        special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>/?"
    
        all_chars = upper_case + lower_case + digits + special_chars
    
        password = [
            random.choice(upper_case),
            random.choice(lower_case),
            random.choice(digits),
            random.choice(special_chars)
        ]
    
        while len(password) < 12:
            password.append(random.choice(all_chars))
    
        unique_chars = set(password)
        while len(unique_chars) < 5:
            password.append(random.choice(all_chars))
            unique_chars = set(password)
    
        random.shuffle(password)
    
        return ''.join(password)