from application.Controller import *
class productosController(Controller):

    def __init__(self):
        Controller.__init__(self)
        pass
    
    def index(self):
        self.contenido = {
            'title': 'megaman 10',
            'script': self.javascript(),
            'log':'<div id="l_error"></div><form action="./" method="get"><input type="text"id="lusuario"placeholder="Usuario :"name="usuario"title="usuario"><input type="text"id="lpass"name="pass"title="contrase&ntilde;a"placeholder="Contrase&ntilde;a :"><input type="submit" class="boton"value="Entrar"id="dale"title="entrar"><a href="registro"title="registrarse">Registrarse</a><a href="recuperar"title="recuperar contrase&ntilde;a">Recuperar Contrase&ntilde;a</a></form>'
                 }
        self.renderizar('index')
        pass
    def contacto(self):
        print('dale contacto')
        pass

