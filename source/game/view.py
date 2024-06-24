import random
from main.controller import MainMenuView



class GameView:
  
    def addBalance(self,list):
        result = tuple((int(x[0])) for x in list)
        number = result[0]

        
        while True:
           number1 = random.randint(1,9999)
           operator = random.choice(r"+-*")
           number2 = random.randint(1,999)

           result = input("Ինչ կստացվի " +str( number1 ) + operator + str( number2)+ " = ")
           x = (eval( str(number1 ) + operator + str(number2)))
           if int(result) ==  eval( str(number1) + operator + str(number2)):
               print("Ճիշտ է դուք վաստակեցիք 20$ ")
               number += 20
               answer = input("1.Շարունակել 2.Դուրս գալ ")
               if answer == "1":
                   continue
               elif answer ==2:
                   return number
                   
                   break
           else:
                    print("Սխալ ճիշտ պատասխանը "+ str(x) +" է")
                    answer = input("1.Շարունակել 2.Դուրս գալ ")
                    if answer == "1":
                        continue
                    elif answer =="2":
                        mm_view = MainMenuView()
                        selected_menu = mm_view.display_menu()
                        return number

                        break

                     
           return number
               
           
       
        