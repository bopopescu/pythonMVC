#!C:\Python27\python.exe -u
#!/usr/bin/env python
import cgitb
cgitb.enable()
import cgi
print "Content-Type: text/html;charset=utf-8"
print
form = cgi.FieldStorage()
i = str(form.getvalue('a'))
print i