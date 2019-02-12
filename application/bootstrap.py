from application.request import *
import importlib
class Bootstrap(Request):
    def __init__(self):
        Request.__init__(self)
    def run(self):
        metodos = self.getmetodo()
        controller = self.getcontrol()+'Controller';
        metodo = self.getmetodo();
        args = self.arg();
        rutaControlador = 'controllers/'+controller+'.py';
        vista = 'controllers.'+controller
        if os.access(rutaControlador, os.R_OK):
            controlador = importlib.import_module(vista,controller)
            control = getattr(controlador, controller)
            control = control()
            getattr(control, metodos)()

        else:
            print('no se encontro la vista')

pass
b=Bootstrap()
b.run()
