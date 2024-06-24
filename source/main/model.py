import sys
sys.path.append("..")

from source import settings
import os





class MainMenuModel:

    def init_db(self):
        if not os.path.exists(settings.DATABASE_PATH):
            db_file = open(settings.DATABASE_PATH,"w")
            db_file.close()

