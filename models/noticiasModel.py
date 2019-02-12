from application.Model import *
import mysql.connector
import cgi
from math import ceil
class noticiasModel(Model):

    def __init__(self):
       Model.__init__(self)

       pass
    def index(self):
       cursor= self.query("SELECT * FROM acerca")
       for cursor in cursor:
        acerca=cursor["acerca"]
        return acerca
        pass
    def categorias(self):
     cursor= self.query("SELECT * FROM categoria")
     resultados = cursor.fetchall()
     return resultados

    pass

    def comentarios(self):
        cursor= self.query("SELECT id,SUBSTRING(comentario,1,150) as comentario,autor,foto,publicado,categoria,id_contenido FROM comentario ORDER BY id DESC LIMIT 5")
        resultados = cursor.fetchall()
        return resultados
        pass
    def musica(self):
        cursor=self.query("SELECT * FROM musica")
        resultados=cursor.fetchall()
        return resultados
        pass
    def simmusic(self):
        cursor=self.query("SELECT * FROM musica ORDER BY RAND()")
        resultados=cursor.fetchall()
        return resultados
        pass
    def noticias(self,lim,orden,pag):
        if lim==None:
         lim=5
        else:
         lim=lim
        if orden==None:
            orden='DESC'
        else:
            orden=orden
            pass
        paginacion=((int(pag) * int(lim))- int(lim))

        cursor=self.query("SELECT id,titulo,foto,contenido,user,categoria,visitas,publicado,comentarios   FROM noticias ORDER BY id %s LIMIT %s,%s"%(orden,paginacion,lim))

        #cursor=self.query("SELECT *  FROM noticias ORDER BY id %s LIMIT %s,%s"%(orden,paginacion,lim))

        resultados=cursor.fetchall()
        return resultados
        pass
    def contarcomentarios(self,com):
        cursor= self.query("SELECT COUNT(*) FROM comentario WHERE id_contenido='%s'"%com)
        resultado=cursor.fetchall()
        return resultado
        pass
    def contador(self,lim):
        if lim==None:
         lim=5
        else:
         lim=lim
        cursor= self.query("SELECT COUNT(*) as mun FROM noticias LIMIT %s"%(lim))
        result=cursor.fetchone()
        for i in result:
         result=result[i]
        result= int(ceil(ceil(result)/int(lim)))
        return result
        pass
    def simplenoticia(self,idn):
        cursor= self.query("SELECT * FROM noticias WHERE id='%s'"%idn)
        resul=cursor.fetchall()
        return resul
        pass
    def comxid(self,idn):
        cursor= self.query("SELECT * FROM comentario WHERE id_contenido='%s'"%idn)
        result=cursor.fetchall()
        return result
        pass
    def catnoticia(self,cat,lim,orden,pag):
        if lim==None:
         lim=5
        else:
         lim=lim
        if orden==None:
            orden='DESC'
        else:
            orden=orden
            pass
        paginacion=((int(pag) * int(lim))- int(lim))
        cursor= self.query("SELECT id,titulo,foto,contenido,user,categoria,visitas,publicado,comentarios FROM noticias WHERE categoria='%s' ORDER BY id %s LIMIT %s,%s"%(cat,orden,paginacion,lim))
        retu=cursor.fetchall()
        return retu
        pass

    def catcontador(self,lim,cat):
        if lim==None:
         lim=5
        else:
         lim=lim
        cursor= self.query("SELECT COUNT(*) as mun FROM noticias WHERE categoria='%s' LIMIT %s"%(cat,lim))
        result=cursor.fetchone()
        for i in result:
         result=result[i]
        result= int(ceil(ceil(result)/int(lim)))
        return result
        pass
