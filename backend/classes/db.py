import mysql.connector

class db:
    def dbConnect(self):
        __host = "localhost"
        __database = "db_record"
        __user = "root"
        __password = ""

        self.__db = mysql.connector.connect(__host, __database, __user, __password)

        if (self.__db.is_connect()):
            print("erro") # erros deveram ser tratados pela futura classe "error"
    
    def get(self, table, where): # tem como intuito pegar alguma informação do banco de dados
        pass
