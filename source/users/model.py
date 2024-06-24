import sqlite3
import sys
sys.path.append("..")
from source import settings
from common.model import Common  


class UsersModel(Common):
    TABLE_NAME = "users"
    TABLE_BALACNE = "balanc"

    def __init__(self) -> None:
        super().__init__()
        self.init_db()
        self.createBalance()
    def createBalance(self):
        sql = f'''
        CREATE TABLE IF NOT EXISTS {self.TABLE_BALACNE}
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        balance TEXT
        )
        

'''
        self.cur.execute(sql)
        self.con.commit()
    
    def init_db(self):
        
        #self.con = sqlite3.connect(settings.DATABASE_PATH)
        #self.cur = self.con.cursor()
        sql = f'''
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME}
             (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT
            )
            '''
        self.cur.execute(sql)
        self.get_cursor().execute(sql)
        self.con.commit()
    def admin_exists(self):
        sql =f"SELECT * FROM {self.TABLE_NAME} "
        result = self.cur.execute(sql)

        if len(result.fetchall()):
            return True
        else:
            return False
    def create_admin(self,username:str,password:str):
        sql = f'''
    INSERT INTO {self.TABLE_NAME} (username,password) VALUES ('{username}','{password}')
'''
        self.cur.execute(sql)
        self.con.commit()
    def validate_admin(self,username:str,password:str):
        
        sql = f'''
        SELECT * FROM {self.TABLE_NAME}
        WHERE username = '{username}' AND password = '{password}'

        '''
        result = self.cur.execute(sql)
        if len(result.fetchall()):
            return True
        else:
            return False
    
    def __del__(self):
        print("Close")
        self.con.close

        
      
        