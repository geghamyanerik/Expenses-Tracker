from .view import ManageExpensesView
from .model import ExpensesModel




class ManageExpensesController():
    
    def add_new_expense(self):
        expenses_view = ManageExpensesView()
        expenses_model = ExpensesModel()
        expesnses_info = expenses_view.get_expenses_info()

        
        expenses_model.create(
        
            category = expesnses_info["category"],
            amount = expesnses_info["amount"],
            date = expesnses_info["date"],
            list = expenses_model.recive()
            
         
        )
        

    
         
    def view_history(self):
        expenses_view = ManageExpensesView()
        expenses_model = ExpensesModel()
        all_expenses = expenses_model.list()
        expenses_view.display_expense_hostory(all_expenses)
    def reports(self):
        expenses_view = ManageExpensesView()
        expenses_model = ExpensesModel()
        all_reports = expenses_model.reports()
        expenses_view.see_record(all_reports)
    def show_balas(self):
        expenses_view = ManageExpensesView()
        expenses_model = ExpensesModel()
        list = expenses_model.recive()
        expenses_view.balance(list)

    def start(self):
        manage_exp_view = ManageExpensesView()
        selected_menu = manage_exp_view.menu_options()


        if selected_menu == 1:
            self.add_new_expense()
        elif selected_menu ==2:
            self.view_history()
        elif selected_menu ==3:
             self.show_balas()
            
        else:
            print("Invalid menu selcetd try again")
            return self.start()
        return self.start()
