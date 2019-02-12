from application.Model import *
import mysql.connector
class inicioModel(Model):

    def __init__(self):
       Model.__init__(self)

       pass
    def index(self):
       cursor= self.query("SELECT * FROM baner")
       resultados = cursor.fetchall()
       cursor.close()
       return resultados
    pass

    def simplenoticia(self):
        cursor= self.query("SELECT titulo,foto,SUBSTRING(contenido,1,800) as contenido FROM noticias ORDER BY id DESC LIMIT 5")
        resul=cursor.fetchall()
        cursor.close()
        return resul
        pass

