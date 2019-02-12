from application.Model import *
import mysql.connector
class serviciosModel(Model):

    def __init__(self):
       Model.__init__(self)
       pass
    def index(self):
       cursor= self.query("SELECT * FROM servicios")
       for cursor in cursor:
        servicio=cursor["servicio"]
        return servicio

    pass

