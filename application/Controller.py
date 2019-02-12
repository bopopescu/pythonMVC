from application.View import *
import importlib
import cgi
import cgitb
cgitb.enable()

class Controller(View):

    def __init__(self):
        View.__init__(self)
        self.form = cgi.FieldStorage()
        pass
    def loadModel(self,model):

        modelo = model+'Model';
        rutaModelo = 'models/'+modelo+'.py';
        cojemodelo = 'models.'+modelo
        if os.access(rutaModelo, os.R_OK):
            controlador = importlib.import_module(cojemodelo,modelo)
            control = getattr(controlador, modelo)
            modelos = control()
            return modelos
            #getattr(modelos,self.getmetodo())()

        else:
            print('Error de modelo');
            pass
    def javascript(self):
        value='<script type="text/javascript" language="javascript" src="/dom/'+self.getcontrol()+'/'+self.getmetodo()+'.js"></script>';
        return value

        pass