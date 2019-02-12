__author__ = 'Alexander brache'
import mysql.connector
from mysql.connector import errorcode
class database:
    def __init__(self):

     self.conexion = mysql.connector.connect(user='root',database='simple',host='127.0.0.1',charset='utf8',use_unicode=True,get_warnings=True,raise_on_warnings=True)

    pass
pass