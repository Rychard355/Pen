import mysql.connector

class db:
    def dbConnect(self):
        __host = "localhost"
        __database = "db_record"
        __user = "root"
        __password = ""

        self.__db = mysql.connector.connect(__host, __database, __user, __password)
        self.__dbCursor = self.__db.cursor()

        if self.__db.is_connect():
            print("erro") # erros deveram ser tratados pela futura classe "error"
    
    def register(self, surname, name, email, password):
        sql = "INSERT INTO users (`surname`, `name`, `email`, `password`) values (%s, %s, %s, %s)"
        val = (surname, name, email, password)

        self.__dbCursor.execute(sql, val)

    def get(self, column, table, value): # VERIFCAR O RETORNO DESTA FUNÇÃO
        sql = "SELECT %s FROM %s WHERE %s = %s"
        val = (column, table, column, value)

        return self.__dbCursor.execute(sql, val)
