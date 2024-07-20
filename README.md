# ATM Interface Using Python OOP  🏧💻

## Project Overview

This project is an ATM interface implemented using Python and Flask, utilizing Object-Oriented Programming (OOP) principles. The application allows users to perform various operations such as depositing money, withdrawing money, checking their balance, and changing their password.

## Features ✨

- **Deposit Money**:  💵 Deposit money to your account.
- **Withdraw Money**: 💸 Remove money from your account.
- **Check Balance**: 💰 View the current balance.
- **Change Password**:  🔒 Update the account password.

## Technologies Used 🛠️

- **Python**: For core application logic and OOP implementation.
- **Flask**: For creating the web interface.
- **Bootstrap**: For UI styling and responsiveness.

## Installation ⚙️

1. **Clone the Repository**:
    ```
    git clone https://github.com/Khan-Ramsha/Flask-ATM-Interface.git

    ```

2. **Navigate to the Project Directory**:
    ```
    cd Flask-ATM-Interface
    ```


3. **Install the Required Packages**:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask Application**:
    ```
    python app.py
    ```

2. **Open Your Web Browser** and navigate to `http://127.0.0.1:5000` to access the ATM interface.

3. **Log In** using the last 4 digits of your card number and a 4-digit password. You can then perform various operations such as depositing or withdrawing money, checking your balance, and changing your password.

## File Structure 🗂️

- `app.py`: Entry point of the application, handles routing and rendering of pages.
- `components/atm.py`: Contains the `ATM` class with methods for ATM operations.
- `components/verify_user.py`: Contains the `Verify` class for user verification.
- `templates/`: Contains HTML files for the web interface.
  - `index.html`: Login page.
  - `dashboard.html`: Main dashboard with operation links.
  - `deposit.html`: Deposit money page.
  - `withdraw.html`: Withdraw money page.
  - `balance.html`: Check balance page.
  - `change_password.html`: Change password page.
  - `message.html`: Displays the operation successfully completed.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or feature requests. 🙌

