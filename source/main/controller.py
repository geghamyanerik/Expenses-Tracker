'''This moude; will caontain controllers for Main Menu app'''
from .model import MainMenuModel
from .view import MainMenuView
from users.controller import LoginController
from expenses.controller import ManageExpensesController
from game.controler import Game

class MainMenuControler:

    def start(self):
       

       mm_model = MainMenuModel()
       mm_model.init_db()

       login_controller = LoginController
       login_controller.start(self)


       mm_view = MainMenuView()
       selected_menu = mm_view.display_menu()

       if selected_menu ==1:
           manage_controller = ManageExpensesController()
           manage_controller.start()

       elif selected_menu == 2:
           manage_controller = ManageExpensesController()
           manage_controller.reports()
           mm_view = MainMenuView()
           selected_menu = mm_view.display_menu()
       elif selected_menu == 3:
            game_controler = Game()
            game_controler.start()
           
       else:
           print("Սխալ")
           return self.start()