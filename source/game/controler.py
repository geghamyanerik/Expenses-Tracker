from .view import GameView
from .model import Balance



class Game:
  
    def start(self):
         balance_model = Balance()
         
         balance_model.start_balas()
         list = balance_model.recive()
         balance_view = GameView()
         mek =balance_view.addBalance(list)
       
        
      
         balance_model.uptade(mek)
       
        
        