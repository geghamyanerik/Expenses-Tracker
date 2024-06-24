




class RegisterView:

    def get_user_info(self):
        print("Create Admin Acount")
        info = {}
        info["username"] = input("Username ")
        info["password"] = input("Password ")
        info["repeat_password"] = input("Repet Password ")
        if info["password"] != info["repeat_password"]:
            print("Password doesn't match.Try again! \n")
            return self.get_user_info()
        return info

class LoginView:
    def get_credentials(self):
        credentials = {}
        print("Enter Admin credentials to login ")
        credentials["username"] = input("Username ")
        credentials["password"] = input("Password ")
        #stugellllll

        
        return credentials
        