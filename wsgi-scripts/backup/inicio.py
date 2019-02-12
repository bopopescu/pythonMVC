#!C:\Python27\python.exe -u
#!/usr/bin/env python
import cgitb
cgitb.enable()
import cgi
import urlparse
import os, string
query = os.environ.get('QUERY_STRING')
parsed = os.environ.get('REQUEST_URI')
parsed = parsed.split("/")
cabeza ='maqueta/cabeza.tpl'
pagina = 'views/'+parsed[1]+'/index.tpl'
pie='maqueta/pie.tpl'
print "Content-Type: text/html;charset=utf-8"
head =open(cabeza).read()
body=open(pagina).read()
foot=open(pie).read()
print
print head
print body
print foot