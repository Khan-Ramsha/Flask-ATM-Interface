from flask import Flask, render_template, redirect, request, url_for, session
from components.atm import ATM
from components.verify_user import Verify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        card_number = request.form['card_number']
        password = request.form['password']
        user = Verify(card_number, password)
        message, is_valid = user.verify()
        if is_valid:
            session['card_number'] = card_number
            return redirect(url_for('dashboard'))
        else:
            return render_template('index.html', error=message)
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'card_number' not in session:
        return redirect(url_for('home'))
    return render_template('dashboard.html')

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if 'card_number' not in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            card_number = session['card_number']
            password = request.form['password']
            atm = ATM(card_number, password)
            message = atm.deposit(amount)
            return render_template('message.html', message=message)
        except ValueError:
            return render_template('deposit.html', error="Invalid amount. Please enter a numeric value.")
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if 'card_number' not in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            card_number = session['card_number']
            password = request.form['password']
            atm = ATM(card_number, password)
            message = atm.withdraw(amount)
            return render_template('message.html', message=message)
        except ValueError:
            return render_template('withdraw.html', error="Invalid amount. Please enter a numeric value.")
    return render_template('withdraw.html')

@app.route('/balance', methods=['GET', 'POST'])
def balance():
    if 'card_number' not in session:
        return redirect(url_for('home'))
    card_number = session['card_number']
    password = request.form.get('password', '')
    atm = ATM(card_number, password)
    balance_message = atm.check_balance()
    return render_template('balance.html', balance=balance_message)

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if 'card_number' not in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        card_number = session['card_number']
        atm = ATM(card_number, old_password)
        message = atm.change_password(old_password, new_password)
        return render_template('message.html', message=message)
    return render_template('change_password.html')

@app.route('/logout')
def logout():
    session.pop('card_number', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
