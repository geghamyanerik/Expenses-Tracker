from typing import Dict
from datetime import date
from tabulate import tabulate



class ManageExpensesView:


    EXPENSE_CATEGORIES = [
        "Entertaiment",
        "Grocery",
        "Transportation",
        "Other"
    ]
    def menu_options(self):
        print("Կառավարել Ծախսերը")
        print("1.Ավելացնել Նոր Ծախսեր:")
        print("2. Տեսնել Ծախսերը")
        print("3. Տեսնել Հաշիվը")
        selected_menu = int(input("Ընտրել (1 , 2 կամ 3) "))
        return selected_menu
    def display_expense_hostory(self,record):
        print(tabulate(record,headers = ["ID","Category","Amount$","Data"]))
    def see_record(self,reports):
        print(tabulate(reports,headers = ["Category","TotalAmount","Qty"]))
    def balance(self,list):
          
           
            print(tabulate(list,headers = ["$"]))

    def get_expenses_info(self):
        data = {}
        print("Add new Expense record")
        print("Select expanse category")
        
        
        

        
        for idx , value in enumerate(self.EXPENSE_CATEGORIES):
            print(f"\t{str(idx)}. {value}")
        
      
        
        category = int(input("Select Category from the list: "))
        data["category"] = self.EXPENSE_CATEGORIES[category]
        data["amount"] = float(input("Amount $: "))
        
        
        
        
        
        data["date"] = str(date.today())  
        
        
        
        return data
    