from application.Controller import *
class inicioController(Controller):

    def __init__(self):
        Controller.__init__(self)
        self.modelo=self.loadModel('inicio')
        pass
    
    def index(self):
        reg = self.modelo.index()
        # noticias=self.modelo.simplenoticia()
        self.contenido = {
            'title': 'megaman 10',
            'script': self.javascript(),
            # 'banner':reg,
            # 'noticias':noticias,
            'facebook':'//www.facebook.com/plugins/likebox.php?href=http%3A%2F%2Fwww.facebook.com%2FDOMLOTERIA%3Ffref%3Dts&amp;width=1230&amp;height=285&amp;show_faces=true&amp;colorscheme=light&amp;stream=false&amp;show_border=false&amp;header=false" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:96%; height:285px;" allowTransparency="true" class="fright',
            'log':'<div id="l_error"></div><form action="./" method="get"><input type="text"id="lusuario"placeholder="Usuario :"name="usuario"title="usuario"><input type="text"id="lpass"name="pass"title="contrase&ntilde;a"placeholder="Contrase&ntilde;a :"><input type="submit" class="boton"value="Entrar"id="dale"title="entrar"><a href="registro"title="registrarse">Registrarse</a><a href="recuperar"title="recuperar contrase&ntilde;a">Recuperar Contrase&ntilde;a</a></form>'
                 }
        self.renderizar('index')

        pass
    def contacto(self):
        print('dale contacto')
        pass

