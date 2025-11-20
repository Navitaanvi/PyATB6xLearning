class VWOLoginPage:
    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "navita@gmail.com" and self.password == "pass123":
            print("Allowed to Login")
        else:
            print("Login Failed")

email = input("Enter the vwo Login email: ")
password = input("Enter the vwo password: ")

vwo_obj_ref = VWOLoginPage(email,password)
vwo_obj_ref.login_confirm()
