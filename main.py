import json  
import bcrypt  
import sys  
import os  
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
from login_ui import login  # Importing your UI design  
import subprocess
class Login(QtWidgets.QMainWindow):  
    def __init__(self):  
        super().__init__()  
        self.ui = login()  # Create an instance of the UI class  
        self.ui.setupUi(self)  # Setup the UI  
        # self.ui.createaccbutton.clicked.connect(self.create_account)  # Connect button to create account  
        self.ui.loginbutton.clicked.connect(self.login)  # Connect button to login  
        self.ui.exitbutton.clicked.connect(self.close)  # Connect exit button to close the application  
        self.ui.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
    # def create_account(self):  
    #     email = self.ui.emailfield.text()  
    #     password = self.ui.passwordfield.text()  

    #     if email and password:  
    #         hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())  
    #         user_data = {email: {'password': hashed_password.decode('utf-8')}}  

    #         # Check if users.json exists or handle file writing  
    #         try:
    #             if os.path.exists('users.json'):  
    #                 with open('users.json', 'r+') as f:  
    #                     users = json.load(f)  
    #                     if email in users:  
    #                         self.ui.errorfield.setText("Account already exists!")  
    #                         return  
    #                     users.update(user_data)  
    #                     f.seek(0)  
    #                     json.dump(users, f, indent=4)  
    #                     f.truncate()  # Ensure the file is truncated after updates  
    #             else:  
    #                 with open('users.json', 'w') as f:  
    #                     json.dump(user_data, f, indent=4)  

    #             self.ui.errorfield.setText("Account created successfully!")  
    #             self.ui.emailfield.clear()  # Clear email field
    #             self.ui.passwordfield.clear()  # Clear password field
    #         except Exception as e:
    #             self.ui.errorfield.setText(f"Error saving account: {e}")  

    #     else:  
    #         self.ui.errorfield.setText("Please enter both email and password.")  

    def login(self):  
            email = self.ui.emailfield.text()  
            password = self.ui.passwordfield.text()  

            if email and password:  
                if os.path.exists('users.json'):  
                    with open('users.json') as f:  
                        users = json.load(f)  
                    if email in users and bcrypt.checkpw(password.encode('utf-8'), users[email]['password'].encode('utf-8')):  
                        self.ui.errorfield.setText("Login successful!")  
                        self.close()
                        self.run_executable()  # Call the function to run the executable  
                    else:  
                        self.ui.errorfield.setText("Invalid credentials!")  
                # else:  
                #     self.ui.errorfield.setText("No accounts found. Please create one.")  
            else:  
                self.ui.errorfield.setText("Please enter both email and password.")  

    def run_executable(self):  
        # Replace 'path_to_your_executable.exe' with the actual path to your .exe file
        subprocess.Popen(['admin.exe'])  # Launch the executable
    # Main Application  

def main():  
    app = QtWidgets.QApplication(sys.argv)  
    window = Login()  # Use the Login class  
    window.show()  
    sys.exit(app.exec_())  

if __name__ == "__main__":  
    main()
