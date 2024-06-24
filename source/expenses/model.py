import sqlite3
import sys
from source import settings

sys.path.append("..")
from common.model import Common



class ExpensesModel(Common):

    TABLE_NAME = "expenses"

    def __init__(self) -> None:
        super().__init__()
        self.init_db()

    def init_db(self):

        
        sql = f'''
    CREATE TABLE IF NOT EXISTS {self.TABLE_NAME}
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        amount REAL,
        date TEXT
       
    )

'''
        self.cur.execute(sql)
        self.con.commit()
    def create(self,category:str,amount:float,date:str,list):
       
        resul = tuple((int(x[0])) for x in list)

        y = resul[0]
        print(type(y))
        if y < amount:
            print("Չկա բավար գումար")
        else:
             sql = f'''
    INSERT INTO {self.TABLE_NAME} (category , amount, date) VALUES ('{category}','{amount}','{date}')
    '''
             self.cur.execute(sql)
             self.con.commit()
             y = y- amount
             sq = f'''
    UPDATE   balanc SET balance = {y} 

    ''' 
             self.cur.execute(sq)
             self.con.commit()


       
        
    def list(self):
        sql = f'''
    SELECT * FROM {self.TABLE_NAME}
    '''
        result = self.cur.execute(sql)
        return result.fetchall()
    def recive(self):
        sql = f'''
    SELECT balance  FROM balanc WHERE  id = 1

    '''
        result = self.cur.execute(sql)
        return result.fetchall()
    def reports(self):
        sql = f'''
    SELECT category,SUM(amount) AS total_amount, COUNT(id) AS total_records FROM {self.TABLE_NAME} GROUP BY category
'''
        result = self.cur.execute(sql)
        result = result.fetchall()
        return result
    def __del__(self):
        
        self.con.close
   



