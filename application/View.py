from application.request import *
from libreria.microtemplates.base import Template as plantillas

class View(Request):

    def __init__(self):
        Request.__init__(self)
        pass
    
    def renderizar(self,vista, item =''):
        ruta = 'views/'+self.getcontrol()+'/'
        cabeza= 'maqueta/cabeza.tpl'
        rutaView = 'views/'+self.getcontrol()+'/'+vista+'.tpl'
        pie= 'maqueta/pie.tpl'
        def read_html(engine):
            html_file_path = os.path.join(ruta, "%s.tpl" % engine)
            with open(html_file_path) as html_file:
                html = html_file.read()
            return html
        tplread = read_html(vista)

        cuerpo=plantillas(tplread).render(**self.contenido)
        if os.access(rutaView, os.R_OK):
          if item =='':
           print(open(cabeza).read())
          pass
          print(cuerpo)
          #print(open(rutaView).read())
          if item =='':
            print(open(pie).read())
        else:
            print('Error de vista')