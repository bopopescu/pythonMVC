import os
class Request:

    def __init__(self):
        if os.environ.get('REQUEST_URI'):
            url=os.environ.get('REQUEST_URI')
            url =url.split("/")
            if url[1]=='':
               self.controlador ='inicio'
            else:
               self.controlador = url[1].lower()

            if len(url)==2:
               self.metodo ='index'
            else:
                self.metodo = url[2].lower()

            if len(url)<4:
                self.argumentos = []
            else:
                self.argumentos = url[3].lower()

    pass
    def getcontrol(self):
        return self.controlador
        pass
    def getmetodo(self):
        return self.metodo
        pass
    def arg(self):
        return self.argumentos
        pass
pass

