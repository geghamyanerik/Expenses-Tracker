"""
    This modue is the starting point of the app
"""
from main.controller import MainMenuControler

def start():
    maincontroler = MainMenuControler()
    maincontroler.start()


start()