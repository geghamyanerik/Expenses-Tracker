import sqlite3
import sys
sys.path.append("..")
from source import settings 
from abc import  ABC,abstractmethod

class Common(ABC):
    def __init__(self):
        self.con = sqlite3.connect(settings.DATABASE_PATH)
        self.cur = self.con.cursor()
    @abstractmethod    
    def init_db(self):
        pass
   
    def get_cursor(self):
        return self.cur
    def __del__(self):
        self.con.close()