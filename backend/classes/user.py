from contextlib import nullcontext
import db

class user:
    def __init__(self):
        self.__db = db.DB()

    def register(self, surname, name, email, password): # registra um novo usuário
        if self.__db.get('email', 'users', email) or self.__db.get('surname', 'users', surname): #----VEFIQUE MELHOR O RETORNO DA FUNÇÃO GET
            return False

        self.__db.register(surname, name, email, password)
        return True
    
    def login(self, surname, password):
        if self.__db.get('surname', 'users', surname) or self.__db.get('password', 'users', password):
            return False
        return True
