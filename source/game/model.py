import sqlite3
import sys
sys.path.append("..")
from source import settings



class Balance:
    TABLE_NAME = "balanc"

    def __init__(self):
        self.init_db()
    
    def init_db(self):
        self.con = sqlite3.connect(settings.DATABASE_PATH)
        self.cur = self.con.cursor()
        
    def start_balas(self):
        sql = f'''
        INSERT INTO {self.TABLE_NAME} (balance) VALUES ('0')
    '''
        self.cur.execute(sql)
        self.con.commit()
    
    def recive(self):
        sql = f'''
    SELECT balance  FROM {self.TABLE_NAME} WHERE  id = 1

    '''
        result = self.cur.execute(sql)
        return result.fetchall()
    def uptade(self,balance):
          sql = f'''
    UPDATE   {self.TABLE_NAME} SET balance = {balance} 

    ''' 
          self.cur.execute(sql)
          self.con.commit()
    def _del__(self):
        self.con.close()

    def prin(self,mek):
        print(mek)
        
    def __del__(self):
        
        self.con.close()