"""Generic database adapter for MySQL. Implements only the minimum
of functionality needed in sql.py"""


from ebkus.config import DATABASE_TYPE, DATABASE_NAME, DATABASE_HOST

if DATABASE_TYPE == 'MySQL':

  import MySQL

  def connect(host = None, user = '' , passw = '', dbname = ''):
    db = MySQL.connect(host, user, passw)
    if dbname:
      db.selectdb(dbname)
    return DBAdapter(db)

  class DBAdapter:

    def __init__(self, dbhandle):
      self.dbhandle = dbhandle

    def selectdb(self, dbname):
      self.dbhandle.selectdb(dbname)

    def query(self, query):
      return self.dbhandle.do(query)

    def listtables(self):
      tables = self.dbhandle.listtables()
      tables = map(lambda x: x[0], tables)
      return tables

    def listfields(self, table):
      return self.dbhandle.listfields(table)

    def close(self):
      self.dbhandle.close()
      self.dbhandle = None


elif DATABASE_TYPE == 'mSQL':

  import mSQL

  def connect(host = None, user = '', passw = '', dbname = ''):
    db = mSQL.connect()
    if dbname:
      db.selectdb(dbname)
    return DBAdapter(db)

  class DBAdapter:

    def __init__(self, dbhandle):
      self.dbhandle = dbhandle

    def selectdb(self, dbname):
      self.dbhandle.selectdb(dbname)

    def query(self, query):
      return self.dbhandle.query(query)

    def listtables(self):
      tables = self.dbhandle.listtables()
      return tables

    def listfields(self, table):
      return self.dbhandle.listfields(table)

    def close(self):
      self.dbhandle.close()
      self.dbhandle = None


elif DATABASE_TYPE == 'MySQLdb':

  import MySQLdb

  ebkustype_conv = { MySQLdb.FIELD_TYPE.TINY: int,
              MySQLdb.FIELD_TYPE.SHORT: int,
              MySQLdb.FIELD_TYPE.LONG: int,
              MySQLdb.FIELD_TYPE.FLOAT: float,
              MySQLdb.FIELD_TYPE.DOUBLE: float,
              MySQLdb.FIELD_TYPE.LONGLONG: long,
              MySQLdb.FIELD_TYPE.INT24: int,
              MySQLdb.FIELD_TYPE.YEAR: int }

  MySQLdb.type_conv = ebkustype_conv
  
  def connect(dbhost = None, user = '', passwd = '', db = ''):
    db = MySQLdb.connect(host = DATABASE_HOST, db = DATABASE_NAME)
    return DBAdapter(db)

  class DBAdapter:
    
    def __init__(self, dbhandle):
      self.dbhandle = dbhandle

    def selectdb(self, db = ''):
      self.dbhandle.connect(db = DATABASE_NAME)

    def query(self, query):
      cursor = self.dbhandle.cursor()
      if query[:6] == 'SELECT':
        cursor.execute(query)
        return cursor.fetchall()
      else: return cursor.execute(query)
    
    def listtables(self):
      cursor = self.dbhandle.cursor()
      cursor.execute('SHOW tables')
      tables = map(lambda x: x[0], cursor.fetchall())
      return tables

    def listfields(self, table):
      cursor = self.dbhandle.cursor()
      cursor.execute('SHOW fields from %s' % table)
      return cursor.fetchall()
    
    def close(self):
      self.dbhandle.close()
      self.dbhandle = None




