#!/usr/local/bin/python

"""
  Parsen der Code-, Kategorien-, Mitarbeiter-,TabellenId-Liste.
  
  Kategorien eintragen
    aus der vollständigen Liste
  Codes eintragen
    aus der vollständigen Liste
  Administrator und Mitarbeiter eintragen
    aus der Liste
  (die Daten stehen in migrdata)
  
Tabelle feld mit den Kategoriecodes/ids aktualisieren
  die Daten stehen in schemagen (Table/Field Instanzen)

Tabelle tabid initialisieren

"""
import string
from ebkus.app.ebapi import *
from migrdata_kreuzberg import *
# from migrdata_minimum import *
# from migrdata import *
from ebkus.db import sql
from ebkus.db import dbapp
from ebkus.gen import schemagen
from ebkus.gen import schemadata
from ebkus import config
from time import time

#class MigrError(Exception):
#  pass


class IdGen:
  def __init__(self):
    self.A = 1
    self.B = 3000001
    
  def get(self, dbsite):
    if dbsite == 'A': return self.getA()
    if dbsite == 'B': return self.getB()
    raise 'FALSCHE DBSITE'
  
  def getA(self):
    res = self.A
    self.A = self.A + 1
    return res

  def getB(self):
    res = self.B
    self.B = self.B + 1
    return res


def parse_code_list(str):
  import string
  import re
  codes = []
  lines  = string.split(str, '\n')
  for lstr in lines:
    lstr = string.strip(lstr)
    if not lstr:
      continue
    l = re.split('[\s]*;[\s]*', lstr)
    if len(l) < 3:
      print lstr
      raise 'Error in codelist'
    codes.append(l)
  return codes

## print parse_code_list(code_list_str)
## print

def parse_kategorie_list(str):
  import string
  import re
  kategories = []
  lines  = string.split(str, '\n')
  for lstr in lines:
    lstr = string.strip(lstr)
    if not lstr:
      continue
    l = re.split('[\s]*;[\s]*', lstr)
    if len(l) < 2:
      print lstr
      raise 'Error in kategorielist %s' % lstr
    kategories.append(l[:2])
  return kategories


## print parse_kategorie_list(kategorie_list_str)
## print

def parse_mitarbeiter_list(str):
  import string
  import re
  mitarbeiter = []
  lines  = string.split(str, '\n')
  for lstr in lines:
    lstr = string.strip(lstr)
    if not lstr:
      continue
    l = re.split('[\s]*;[\s]*', lstr)
    if len(l) < 6:
      print lstr
      raise 'Error in codelist'
    mitarbeiter.append(l)
  return mitarbeiter

def parse_tab_id(str):
  import string
  import re
  codes = []
  lines  = string.split(str, '\n')
  for lstr in lines:
    lstr = string.strip(lstr)
    if not lstr:
      continue
    l = re.split('[\s]*,[\s]*', lstr)
    if len(l) < 5:
      print lstr
      raise 'Error in codelist'
    codes.append(l)
  return codes

def insert_kategorien():
  kl = KategorieList(where = '')
  print kl
  if kl:
    print 'Kategorien schon definiert, werden gelöscht'
    kl.deleteall()
  print 'Kategorien einfügen'
  klistdata = parse_kategorie_list(kategorie_list_str)
  idgen = IdGen()
  aenderungszeit = int(time())
  for kd in klistdata:
    k = Kategorie()
    k.new(idgen.getA())
    k['code'] = kd[0]
    k['name'] = kd[1]
    k['zeit'] = aenderungszeit
    k.insert()

def insert_kategorie_codes():
  cl = CodeList(where = '')
  if cl:
    print 'Codes schon definiert, werden gelöscht'
    cl.deleteall()
  print 'Codes einfügen'
  clistdata = parse_code_list(code_list_str)
  bereichslist = string.split(bereichs_kategorien_str)
  idgen = IdGen()
  katcode = None
  aenderungszeit = int(time())
  for cd in clistdata:
    if katcode != cd[2]:
      # Neue Kategorie
      katl = KategorieList(where = "code = '%s'" % cd[2])
      if len(katl) != 1:
        raise 'Keine eindeutige Kategorie für code: %s' % cd
      kat = katl[0]
      katcode = cd[2]
      sort = 1
      print "Code für '%s' einfügen" % kat['name']
    c = Code()
    c.new(idgen.getA())
    c['code'] = cd[0]
    c['name'] = cd[1]
    c['kat_id'] = kat['id']
    c['kat_code'] = kat['code']
    c['sort'] = sort
    c['off'] = 0
    c['zeit'] = aenderungszeit
    assert c['kat_code'] == katcode == kat['code'] == cd[2]
    sort = sort + 1
    if katcode in bereichslist and len(cd) > 3:
      if cd[3]:
        c['mini'] = int(cd[3])
        print 'Mini: %(kat_code)s %(name)s %(mini)s' % c
      if cd[4]:
        c['maxi'] = int(cd[4])
        print 'Maxi: %(kat_code)s %(name)s %(maxi)s' % c
    c.insert()
    
def update_feld():
  print 'Feld tabelle ergänzen'
  tables = schemagen.get_schema_info(schemadata.schemainfo)
  verwtlist = CodeList(where = "kat_code = 'verwtyp'")
  katlist = KategorieList(where = '')
  dbtlist = TabelleList(where = '')
  for t in tables:
    dbt = dbtlist.findu("tabelle", t.tablename)
    assert dbt['tabelle'] == t.tablename
    print "Tabelle '%s'" % t.tablename
    dbfields = FeldList(where = "tab_id = %s" % dbt['id'])
    for f in t.fields:
      dbf = dbfields.findu('feld', f.fieldname)
      assert dbf['feld'] == f.fieldname
      verwtyp = verwtlist.findu('code', f.verwtyp)
      dbfupd = Feld()
      dbfupd['verwtyp'] = verwtyp['id']
      print "  Feld '%s' (%s %s)" % (f.fieldname, f.verwtyp, f.ref)
      if f.verwtyp in 'kb':
        kat = katlist.findu('code', f.kat_code)
        dbfupd['kat_id'] = kat['id']
        dbfupd['kat_code'] = kat['code']
      if f.verwtyp in 'fk':    # kodierte Felder sind Fremdschlüssel nach code
        dbfupd['ftab_id'] = dbtlist.findu('tabelle', f.ftable)['id']
        if f.verwtyp in 'f':    # Name für inverse Beziehung
          dbfupd['inverse'] = f.inverse
      dbf.update(dbfupd)

def insert_mitarbeiter():
  mitl = MitarbeiterList(where = '')
  if mitl:
    print 'Mitarbeiter schon eingetragen, werden gelöscht'
    mitl.deleteall()
  print 'Mitarbeiter einfügen'
  mlistdata = parse_mitarbeiter_list(mitarbeiter_list_str)
  idgen = IdGen()
  aenderungszeit = int(time())
  for ml in mlistdata:
    m = Mitarbeiter()
    m.new(idgen.getA())
    m['vn'] = ml[0]
    m['na'] = ml[1]
    m['ben'] = ml[2]
    m['stat'] = cc('status', '%s' % ml[3])
    m['benr'] = cc('benr', '%s' % ml[4])
    m['stz'] = cc('stzei', '%s' % ml[5])
    m['zeit'] = aenderungszeit
    m.insert()

def init_tabid():
  kl = TabellenIDList(where = '')
  print "================================================================="
  print 'Tabelle tabid (Klasse TabellenID) einrichten'
  if kl:
    print '*** Einträge schon vorhanden, werden gelöscht'
    kl.deleteall()
  print "================================================================="

  tl = TabelleList(where = '', order = 'id')
  site = Code(cc('dbsite', config.SITE))
  for n in tl:
    feldl = FeldList(where = 'tab_id = %d and verwtyp = %d'
                      % (n['id'], cc('verwtyp', 's')))
    if feldl:
      t = TabellenID()
      t['table_id'] = n['id']
      t['table_name'] = n['tabelle']
      t['dbsite'] = site['id']
      t['minid'] = site['mini']
      t['maxid'] = site['maxi']
      obj = eval(n['klasse'])()
      idfield = obj.primarykey
      idmax =  obj._max(idfield, where = "%s < %s" % (idfield, t['maxid']))
      if not idmax:
        idmax = 1
      t['maxist'] = max((int(t['minid']) -1), idmax)
      print '%18s: realmax %3s (dbsite/min/max/ist: %2s %6s %6s %s)' \
            % ( t['table_name'], idmax, t['dbsite'], t['minid'], t['maxid'], t['maxist'])
      t.insert()

def migrate():
  insert_kategorien()
  insert_kategorie_codes()
  insert_mitarbeiter()
  update_feld()
  init_tabid()
  print
  print 'Codelisten einlesen beendet!'


if __name__ == '__main__':
  dbapp.cache_off()
  opendb()
  migrate()
  closedb()
  mk_daten_dirs(config.AK_DIRS_MAX)
  
print




