#!C:\Python27\python.exe -u
#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()# para reportar errores
print('Content-Type: text/html;charset=utf-8\n')
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import application.request
import application.bootstrap
import application.View
import application.Controller

