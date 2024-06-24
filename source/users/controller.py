from .model import UsersModel
from .view import RegisterView,LoginView




class LoginController:

    def start(self):
       user_model = UsersModel()
       value = int(input("1.Գրանցվել   2.Մուտք գործել "))
       if value == 2:
           login_view = LoginView()
           credentials = login_view.get_credentials()
           validate = user_model.validate_admin(credentials["username"],credentials["password"])
           if not validate:
               print("Invalid credentials. try again \n")
               return self.start( )
       elif value == 1:
           register_view =RegisterView()
           user_info = register_view.get_user_info()
           user_model.create_admin(user_info["username"],user_info["password"])
           
       else:
           print("Սխալ")
           return self.start()