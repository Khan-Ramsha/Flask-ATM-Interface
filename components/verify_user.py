import re

class Verify:
    def __init__(self, card_number, password):
        self.card_number = card_number
        self.password = password

    def verify(self):
        if not re.match(r'^\d{4}$', self.card_number):
            return "Card number must be a 4-digit number.", False
        if not re.match(r'^\d{4}$', self.password):
            return "Password must be a 4-digit number.", False
        return None, True
