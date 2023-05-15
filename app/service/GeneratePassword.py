import random
import string
import uuid
import time


class PasswordGenerator:
    def __init__(self):
        pass

    def generate_password(self, length, use_words=True, use_numbers=True, use_symbols=True):

        chars = ""
        if use_words:
            chars += string.ascii_letters
        if use_numbers:
            chars += string.digits
        if use_symbols:
            chars += "{!#$%&(*+@^-)"

        password = "".join(random.choice(chars) for _ in range(length))
        return password
    
    def generate_password_data(self, request_password):
        password = self.generate_password(request_password['length'], request_password['use_words'], request_password['use_numbers'], request_password['use_symbols'])

        valid_until = time.time() + request_password['valid_days'] * 24 * 3600

        password_data = {
            'email': request_password['email'],
            'password': password,
            "max_views": request_password['max_views'],
            "num_views ": request_password['num_views'],
            "valid_until": valid_until,
            "valid_days": False,
        }

        return password_data
    
    def can_view(self, num_views, max_views, valid_until):
        return num_views < max_views and time.time() < valid_until
  