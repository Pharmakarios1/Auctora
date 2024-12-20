import random
import re
import string


def is_valid_email(email: str) -> bool:
    """
    Checks if the provided string is a valid email address.
    
    Parameters:
        email (str): The string to check.
        
    Returns:
        bool: True if the string is a valid email, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))


def otp_generator() -> str:
    """
    Generates a 6-digit numeric OTP.
    """
    return ''.join(random.choices(string.digits, k=6))
