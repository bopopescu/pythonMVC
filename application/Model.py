from application.database import *
#cursor con dicionario

class MySQLCursorDict(mysql.connector.cursor.MySQLCursor):

    def _row_to_python(self, rowdata, desc=None):
        row = super(MySQLCursorDict, self)._row_to_python(rowdata, desc)
        if row:
            return dict(zip(self.column_names, row))
        return None
#database
class Model(database):

    def __init__(self):
        database.__init__(self)
    def query(self,query):
        cursor = self.conexion.cursor(cursor_class=MySQLCursorDict)
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        cursor.execute(query)
        return cursor
        pass




