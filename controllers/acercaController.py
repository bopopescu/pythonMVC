from application.Controller import *
class acercaController(Controller):

    def __init__(self):
        Controller.__init__(self)
        self.acerca=self.loadModel('acerca')
        pass
    
    def index(self):
        self.contenido = {
            # 'acerca':self.acerca.index(),
            'script':self.javascript()
                 }
        self.renderizar('index')
        pass
    def contacto(self):
        print('dale contacto')
        pass

