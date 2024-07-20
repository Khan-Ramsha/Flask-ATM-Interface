from flask import session

class ATM:
    def __init__(self, card_number, password):
        self.card_number = card_number
        self.password = password
        if 'accounts' not in session:
            session['accounts'] = {}
        if card_number not in session['accounts']:
            session['accounts'][card_number] = {'password': password, 'balance': 0}
        self.account = session['accounts'][card_number]

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.account['balance'] += amount
        session['accounts'][self.card_number] = self.account
        session.modified = True
        return f"Deposited: ${amount:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.account['balance']:
            return "Insufficient balance."
        self.account['balance'] -= amount
        session['accounts'][self.card_number] = self.account
        session.modified = True
        return f"Withdrew: ${amount:.2f}"

    def check_balance(self):
        return f"Current balance: ${self.account['balance']:.2f}"

    def change_password(self, old_password, new_password):
        if old_password != self.account['password']:
            return "Incorrect password."
        if len(new_password) != 4 or not new_password.isdigit():
            return "Password must be a 4-digit number."
        self.account['password'] = new_password
        session['accounts'][self.card_number] = self.account
        session.modified = True
        return "Password changed successfully."
