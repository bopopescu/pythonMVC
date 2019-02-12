from application.Model import *
import mysql.connector
class acercaModel(Model):

    def __init__(self):
       Model.__init__(self)
       pass
    def index(self):
       cursor= self.query("SELECT * FROM acerca")
       for cursor in cursor:
        acerca=cursor["acerca"]
        return acerca
        pass
    def personas(self):
     cursor= self.query("SELECT * FROM personal")
     resultados = cursor.fetchall()
     return resultados

    pass

