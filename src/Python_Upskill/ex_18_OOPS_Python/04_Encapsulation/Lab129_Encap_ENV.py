from dotenv import load_dotenv
import os

class VWOLoginPage:
    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        load_dotenv()
        print("username from env: ",os.getenv("VWO_USERNAME"))
        print("password from env: ",os.getenv("VWO_PASSWORD"))
        if self.email == os.getenv("VWO_USERNAME") and self.password == os.getenv("VWO_PASSWORD"):
            print("Allowed, Login success")
        else:
            print("Login Failed")

email = input("enter the email:")
password = input("enter the password:")

login_obj_ref = VWOLoginPage(email,password)
login_obj_ref.login_confirm()

print(os.name)
