import mysql.connector

class DB:
    def __init__(self):
        self.__db = mysql.connector.connect(
            host = "localhost",
            database = "db_record",
            user = "root", 
            password = ""
            )
            
        if not self.__db.is_connection():
            print("erro")