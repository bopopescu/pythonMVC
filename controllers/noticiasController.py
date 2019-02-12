from application.Controller import *
class noticiasController(Controller):

    def __init__(self):
        Controller.__init__(self)
        self.noticias=self.loadModel('noticias')
        pass
    
    def index(self):
        pag= self.form.getvalue("pag")
        limite=self.form.getvalue("limite")
        orden=self.form.getvalue("orden")
        if pag:
            pag=int(pag)
        else:
            pag=1
        pass
        if pag==1:
            selected='class="selecion"'
        else:
            selected=''
        pass
        categorias=self.noticias.categorias()
        comentarios=self.noticias.comentarios()
        musica=self.noticias.musica()
        simmu=self.noticias.simmusic()
        noticias=self.noticias.noticias(limite,orden,pag)
        contador=self.noticias.contador(limite)

        if pag==contador:
            selected2='class="selecion"'
        else:
            selected2=''
        if orden=='ASC':
            ok='selected';ok1='';
        else:
            ok1='selected';ok='';
        if limite=='5':
            si='selected';si2='';si3='';si4='';si5='';si6='';
        elif limite=='10':
            si='';si2='selected';si3='';si4='';si5='';si6='';
        elif limite=='15':
            si='';si2='';si3='selected';si4='';si5='';si6='';
        elif limite=='20':
            si='';si2='';si3='';si4='selected';si5='';si6='';
        elif limite=='25':
            si='';si2='';si3='';si4='';si5='selected';si6='';
        elif limite=='30':
            si='';si2='';si3='';si4='';si5='';si6='selected';
        else:
            si='selected';si2='';si3='';si4='';si5='';si6='';
        self.contenido = {
            'script':self.javascript(),
            'log':'<div id="l_error"></div><form action="./" method="get"><input type="text"id="lusuario"placeholder="Usuario :"name="usuario"title="usuario"><input type="text"id="lpass"name="pass"title="contrase&ntilde;a"placeholder="Contrase&ntilde;a :"><input type="submit" class="boton"value="Entrar"id="dale"title="entrar"><a href="registro"title="registrarse">Registrarse</a><a href="recuperar"title="recuperar contrase&ntilde;a">Recuperar Contrase&ntilde;a</a></form>',
            'categorias':categorias,
            'comentarios':comentarios,
            'musica':musica,
            'musin':simmu,
            'noticias':noticias,
            'pag':pag,
            'selected':selected,
            'selected2':selected2,
            'sig':pag+1,
            'ant':pag-1,
            'total':contador,
            'ok':ok,
            'ok1':ok1,
            'orden':orden,
            'limite':limite,
            'si':si,
            'si2':si2,
            'si3':si3,
            'si4':si4,
            'si5':si5,
            'si6':si6
                 }
        self.renderizar('index')
        pass
    def cuerpo(self):
        pag= self.form.getvalue("pag")
        if pag:
            pag=int(pag)
        else:
            pag=1
        pass
        limite=self.form.getvalue("limite")
        orden=self.form.getvalue("orden")
        contador=self.noticias.contador(limite)
        if limite=='5':
            si='selected';si2='';si3='';si4='';si5='';si6='';
        elif limite=='10':
            si='';si2='selected';si3='';si4='';si5='';si6='';
        elif limite=='15':
            si='';si2='';si3='selected';si4='';si5='';si6='';
        elif limite=='20':
            si='';si2='';si3='';si4='selected';si5='';si6='';
        elif limite=='25':
            si='';si2='';si3='';si4='';si5='selected';si6='';
        elif limite=='30':
            si='';si2='';si3='';si4='';si5='';si6='selected';
        else:
            si='selected';si2='';si3='';si4='';si5='';si6='';
        if pag==1:
            selected='class="selecion"'
        else:
            selected=''
        if pag==contador:
            selected2='class="selecion"'
        else:
            selected2=''
        noticias=self.noticias.noticias(limite,orden,pag)
        if orden=='ASC':
            ok='selected';ok1='';
        else:
            ok1='selected';ok='';
        self.contenido={
            'noticias':noticias,
            'pag':pag,
            'selected':selected,
            'selected2':selected2,
            'sig':pag+1,
            'ant':pag-1,
            'total':contador,
            'ok':ok,
            'ok1':ok1,
            'orden':orden,
            'limite':limite,
            'si':si,
            'si2':si2,
            'si3':si3,
            'si4':si4,
            'si5':si5,
            'si6':si6
        }
        self.renderizar('cuerpo','ok')
        pass
    #fin cuerpo*************************************************************
    def simple(self):

        id= int(self.form.getvalue("id"))
        pag= self.form.getvalue("pag")
        if pag:
            pag=int(pag)
        else:
            pag=1
        pass
        if pag==1:
            selected='class="selecion"'
        else:
            selected=''
        categorias=self.noticias.categorias()
        comentarios=self.noticias.comentarios()
        musica=self.noticias.musica()
        simmu=self.noticias.simmusic()
        noticias=self.noticias.simplenoticia(id)

        comxid=self.noticias.comxid(id)
        self.contenido={
            'script':self.javascript(),
            'log':'<div id="l_error"></div><form action="./" method="get"><input type="text"id="lusuario"placeholder="Usuario :"name="usuario"title="usuario"><input type="text"id="lpass"name="pass"title="contrase&ntilde;a"placeholder="Contrase&ntilde;a :"><input type="submit" class="boton"value="Entrar"id="dale"title="entrar"><a href="registro"title="registrarse">Registrarse</a><a href="recuperar"title="recuperar contrase&ntilde;a">Recuperar Contrase&ntilde;a</a></form>',
            'categorias':categorias,
            'comentarios':comentarios,
            'musica':musica,
            'musin':simmu,
            'noticias':noticias,
            'pag':pag,
            'selected':selected,
            'sig':pag+1,
            'ant':pag-1,
            'comxid':comxid
        }
        self.renderizar('simple')
        pass
    def categorias(self):
        limite=self.form.getvalue("limite")
        orden=self.form.getvalue("orden")
        cat= self.form.getvalue("cat")
        pag= self.form.getvalue("pag")
        total=self.noticias.catcontador(limite,cat)
        if pag:
            pag=int(pag)
        else:
            pag=1
        pass
        if pag==1:
            selected='class="selecion"'
        else:
            selected=''
        if pag==total:
            selected2='class="selecion"'
        else:
            selected2=''
        if orden=='ASC':
            ok='selected';ok1='';
        else:
            ok1='selected';ok='';
        if limite=='5':
            si='selected';si2='';si3='';si4='';si5='';si6='';
        elif limite=='10':
            si='';si2='selected';si3='';si4='';si5='';si6='';
        elif limite=='15':
            si='';si2='';si3='selected';si4='';si5='';si6='';
        elif limite=='20':
            si='';si2='';si3='';si4='selected';si5='';si6='';
        elif limite=='25':
            si='';si2='';si3='';si4='';si5='selected';si6='';
        elif limite=='30':
            si='';si2='';si3='';si4='';si5='';si6='selected';
        else:
            si='selected';si2='';si3='';si4='';si5='';si6='';
        categorias=self.noticias.categorias()
        comentarios=self.noticias.comentarios()
        musica=self.noticias.musica()
        simmu=self.noticias.simmusic()
        noticias=self.noticias.catnoticia(cat,limite,orden,pag)
        #comxid=self.noticias.comxid(id)
        self.contenido={
            'script':self.javascript(),
            'log':'<div id="l_error"></div><form action="./" method="get"><input type="text"id="lusuario"placeholder="Usuario :"name="usuario"title="usuario"><input type="text"id="lpass"name="pass"title="contrase&ntilde;a"placeholder="Contrase&ntilde;a :"><input type="submit" class="boton"value="Entrar"id="dale"title="entrar"><a href="registro"title="registrarse">Registrarse</a><a href="recuperar"title="recuperar contrase&ntilde;a">Recuperar Contrase&ntilde;a</a></form>',
            'categorias':categorias,
            'comentarios':comentarios,
            'musica':musica,
            'musin':simmu,
            'noticias':noticias,
            'pag':pag,
            'selected':selected,
            'selected2':selected2,
            'sig':pag+1,
            'ant':pag-1,
            'cate':cat,
            'total':total,
            'ok':ok,
            'ok1':ok1,
            'orden':orden,
            'limite':limite,
            'si':si,
            'si2':si2,
            'si3':si3,
            'si4':si4,
            'si5':si5,
            'si6':si6
        }
        self.renderizar('categorias')
        pass
    #******************************
    def ccuerpo(self):
        pag= self.form.getvalue("pag")
        limite=self.form.getvalue("limite")
        orden=self.form.getvalue("orden")
        cat=self.form.getvalue("cat")
        total=self.noticias.catcontador(limite,cat)
        if pag:
            pag=int(pag)
        else:
            pag=1
        pass
        if pag==1:
            selected='class="selecion"'
        else:
            selected=''
        if pag==total:
            selected2='class="selecion"'
        else:
            selected2=''
        if orden=='ASC':
            ok='selected';ok1='';
        else:
            ok1='selected';ok='';
        if limite=='5':
            si='selected';si2='';si3='';si4='';si5='';si6='';
        elif limite=='10':
            si='';si2='selected';si3='';si4='';si5='';si6='';
        elif limite=='15':
            si='';si2='';si3='selected';si4='';si5='';si6='';
        elif limite=='20':
            si='';si2='';si3='';si4='selected';si5='';si6='';
        elif limite=='25':
            si='';si2='';si3='';si4='';si5='selected';si6='';
        elif limite=='30':
            si='';si2='';si3='';si4='';si5='';si6='selected';
        else:
            si='selected';si2='';si3='';si4='';si5='';si6='';
        noticias=self.noticias.catnoticia(cat,limite,orden,pag)
        self.contenido={
            'noticias':noticias,
            'pag':pag,
            'selected':selected,
            'sig':pag+1,
            'ant':pag-1,
            'cate':cat,
            'total':total,
            'ok':ok,
            'ok1':ok1,
            'orden':orden,
            'limite':limite,
            'selected':selected,
            'selected2':selected2,
            'si':si,
            'si2':si2,
            'si3':si3,
            'si4':si4,
            'si5':si5,
            'si6':si6
        }
        self.renderizar('ccuerpo','ok')
        pass

