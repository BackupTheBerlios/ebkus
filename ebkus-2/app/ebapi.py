#!/usr/local/bin/python
"""Anwendungsschnittstelle für die EB Klientenverwaltung.

Die eigentlichen Objektklassen liegen im automatisch generierten Modul
ebapigen.py und werden hier nur importiert. Weiter manuelle
Ergänzungen, Subklassendefinitionen, Methodendefinitionen, etc. können
in diesem Modul abgelegt werden.

"""

import sys
import string

from ebkus.app.ebapigen import *
from ebkus.db import dbapp
from ebkus import config



####################
# utility Funktionen
####################


def getDBSite():
  return config.SITE

def cc(kat_code, code):
  """Liefert die code id für eine kat_code/code Kombination.
  Bsp:  cc('stzei', 'B') liefert die Zahl 230"""
  try: id = Code(kat_code = kat_code, code =  code)['id']
  except: 
    raise dbapp.DBAppError("Code '%s' für Kategorie '%s' existiert nicht" % (code, kat_code))
  return id
def cn(kat_code, name):
  """Liefert die code id für eine kat_code/codename Kombination.
  Bsp:  cn('stzei', 'EFB-Wienerstr.') liefert die Zahl 230"""
  try: id = Code(kat_code = kat_code, name =  name)['id']
  except: 
    raise dbapp.DBAppError("Code '%s' für Kategorie '%s' existiert nicht" % (name, kat_code))
  return id


class Date:
  def __init__(self, year = None, month = None, day = None):
    """No error checking. Use the check method."""
    if year is month is day is None: # assume today
      import time
      year, month, day = time.localtime(time.time())[:3]
    if month is None: month = 1
    if day is None: day = 1
    self.year, self.month, self.day = year, month, day

  def totuple(self):
    return self.year, self.month, self.day

  def __getitem__(self, key):
    if key == 'day': return self.day
    elif key == 'month': return self.month
    elif key == 'year': return self.year
    else:
      raise KeyError, key

  def check(self):
    """Liefert true, falls Datum (0,0,0) ist, oder ein korrektes Datum."""
    y = self.year
    m = self.month
    d = self.day
    if y == m == d == 0:
      return 1
    yok = 1980 < y < 2030
    mok = 0 < m < 13
    ml = (31,29,31,30,31,30,31,31,30,31,30,31)
    if mok:
      dok = d > 0 and d <= ml[m-1]
    return yok and mok and dok
    
  def __cmp__(self, other):
    """Works only if dates have been checked true. If a date is all zero,
    it compares greater than any other date."""
    if isinstance(other, Date):
      if self.year == 0:
	return other.year != 0
      if other.year == 0:
	return -1
      if self.year == other.year:
	if self.month == other.month:
	  if self.day == other.day: return 0
	  else: return cmp(self.day, other.day)
	else:  return cmp(self.month, other.month)
      else:  return cmp(self.year, other.year)
    else: 
      return cmp(self, other)
	    
	
  def __str__(self):
    return "%02d.%02d.%04d" % (self.day, self.month, self.year)
  __repr__ = __str__

today = Date

#print today()


#########################################################
# getDate, setDate
#
# Achtung!
# Beruht auf der Konvention, daß Datum immer mit Feldnamen
# angegeben ist, die wie folgt aufgebaut sind:
#   <key>y   (bgy)
#   <key>m   (bgm)
#   <key>d   (bgd)
##########################################################

def getDate(self, key):
  y,m,d = key + 'y', key + 'm', key + 'd'
  return Date(self[y], self[m], self[d])

def setDate(self, key, date):
  y,m,d = key + 'y', key + 'm', key + 'd'
  self[y], self[m], self[d] = date.totuple()

dbapp.DBObjekt.getDate = getDate
dbapp.DBObjekt.setDate = setDate


def getQuartal(monat):
  """Gibt das Quartal für einen bestimmten Monat aus."""
  if int(monat) > 0 and int(monat) < 13:
    q = ((int(monat) - 1) / 3) + 1
    return int(q)
  else:
    raise EE("Keine Monatszahl zwischen 1 und 12")


def getNewId(self):
  """Standardmethode, um neue Werte für Schlüsselfelder zu erzeugen. 
  
  Verwendet die Tabelle tabid (Klasse TabellenID), um eine neue id zu
  generieren abhängig von der Datenbankinstallation, die durch
  die Datenbanksite definiert ist. Die Datenbankinstallation ist in
  der Datei 'config.py' unter dem Namen 'SITE' definiert und kann mit der
  Funktion getDBSite() ermittelt werden.

  Mit der Zeile 
  
       DBObjekt.getNewId = getNewId 
  
  wird diese Funktion als Methode der Klasse DBObjekt installiert und
  damit auf alle Unterklassen von DBObjekt, die in 'ebapigen'
  definiert werden, vererbt.

  Da die 'new' Methode von DBObjekt getNewId verwendet, kann z.B. eine
  neuer Mitarbeiter wie folgt erzeugt werden:

         m = Mitarbeiter()
         m.new()
         m['vn'] = 'Tom'
         m['na'] = 'Friedrich'
         m.insert()

  """

  if not self.primarykey:
    raise dbapp.DBAppError("Cannot getNewId without primarykey")

  tid = TabellenID(table_name = self.table, dbsite = cc('dbsite',  getDBSite()))
  maxist = tid['maxist']
  max = tid['maxid']
  min = tid['minid']
  if maxist:
    newid = maxist + 1
  else:
    newid = 1
  if newid > max:
    raise dbapp.DBAppError("No more ids availabe for table '%s'" % self.table)
  tid.update({'maxist' : newid})
  return newid

dbapp.DBObjekt.getNewId = getNewId


def getNewFallnummer(stz_code):
  """Neue Fallnummer erzeugen."""
  jahresfallliste = FallList(where = 'bgy = %(year)d' % today() + 
			     " and fn like '%%%s%%'" % stz_code) 

  return str(len(jahresfallliste) + 1) + '-' + str(today().year) + stz_code

def getNewGruppennummer(stz_code):
  """Neue Gruppennummer erzeugen."""
  jahresgruppenl = GruppeList(where = 'bgy = %(year)d' % today() + 
			     " and gn like '%%%s%%'" % stz_code) 

  return str(len(jahresgruppenl) + 1) + '-' + str(today().year) + stz_code


##############################
# Berechnete Felder für Akte
##############################

def _wiederaufnehmbar(self, key):
  letzter_fall = self['letzter_fall']
  if letzter_fall and letzter_fall['zday'] != 0:
    zdazeit_in_monaten = letzter_fall['zday']*12 + letzter_fall['zdam']
    heute_in_monaten =   today().year*12 + today().month
    wiederaufnehmbar =  (heute_in_monaten - zdazeit_in_monaten) > 0
  else: wiederaufnehmbar = 0
  #self.data['wiederaufnehmbar'] = wiederaufnehmbar # data cache
  self._cache_field('wiederaufnehmbar', wiederaufnehmbar)
  return wiederaufnehmbar

def _letzter_fall(self, key):
  faelle = self['faelle']
  if faelle:
    faelle.sort('bgy', 'bgm', 'bgd')
    letzter_fall = faelle[-1]
  else:
    letzter_fall = None
  #self.data['letzter_fall'] = letzter_fall # data cache
  self._cache_field('letzter_fall', letzter_fall)
  return letzter_fall


def _aktueller_fall(self, key):
  letzter_fall = self['letzter_fall']
  aktueller_fall = None
  if letzter_fall:
    if letzter_fall['zday'] == 0:
      aktueller_fall = letzter_fall
  #self.data['aktueller_fall'] = aktueller_fall # data cache
  self._cache_field('aktueller_fall', aktueller_fall)
  return aktueller_fall

def _aktuell_akte(self, key):
  res = not self['aktueller_fall'] is None
  #self.data['aktuell'] = res # data cache
  self._cache_field('aktuell', res)
  return res


Akte.attributemethods['wiederaufnehmbar'] = _wiederaufnehmbar
Akte.attributemethods['letzter_fall'] = _letzter_fall
Akte.attributemethods['aktueller_fall'] = _aktueller_fall
Akte.attributemethods['aktuell'] = _aktuell_akte


############################
# Berechnete Felder für Fall
############################

def _aktuell_fall(self, key):
  return self['zday'] == 0

def _zustaendig_fall(self, key):
  found = 0
  for z in self['zustaendigkeiten']:
    if z['ed'] == 0:
      found = 1
      break
  if found: res =  z
  else: res =  None
  self._cache_field('zustaendig', res)
  return res

def _zuletzt_zustaendig_fall(self, key):
  zs = self['zustaendigkeiten']
  zs.sort('bgy', 'bgm', 'bgd')
  res = zs[0]
  self._cache_field('zuletzt_zustaendig', res)
  return res

Fall.attributemethods['aktuell'] = _aktuell_fall
Fall.attributemethods['zustaendig'] = _zustaendig_fall
Fall.attributemethods['zuletzt_zustaendig'] = _zuletzt_zustaendig_fall


############################
# Pfaddefinitionen
############################


Akte.pathdefinitions = {
  'akte': 'self'
}
Anmeldung.pathdefinitions = {
  'akte': 'fall_id__akte'
}

Leistung.pathdefinitions = {
  'akte': 'fall_id__akte'
}
Zustaendigkeit.pathdefinitions = {
  'akte': 'fall_id__akte'
}
Fachstatistik.pathdefinitions = {
  'akte': 'fall_id__akte'
}
Jugendhilfestatistik.pathdefinitions = {
  'akte': 'fall_id__akte'
}

Dokument.pathdefinitions = {
  'akte': 'fall_id__akte'
}

Gruppe.pathdefinitions = {
  'gruppe': 'self'
}

MitarbeiterGruppe.pathdefinitions = {
  'gruppe': 'gruppe_id__gruppe'
}

Gruppendokument.pathdefinitions = {
  "gruppe": "gruppe_id__gruppe"
}

FallGruppe.pathdefinitions = {
  'gruppe': 'gruppe_id__gruppe', 'akte': 'fall_id__akte'
}

BezugspersonGruppe.pathdefinitions = {
  'gruppe': 'gruppe_id__gruppe', 'akte': 'bezugsp_id__akte'
}

def akte_undo_cached_fields(self):
  """Zieht alle gecachten Feldwerte zurück, aus allen Objekten, 
  die mit einer Akte zusammenhängen. Nach jedem insert oder update
  aufzurufen, damit keine falschen gecachten Werte auftreten."""

  for f in self['faelle']:
    for l in f['leistungen']: l.undo_cached_fields()
    for z in f['zustaendigkeiten']: z.undo_cached_fields()
    for a in f['anmeldung']: a.undo_cached_fields()
    for fs in f['fachstatistiken']: fs.undo_cached_fields()
    for jgh in f['jgh_statistiken']: jgh.undo_cached_fields()
    for d in f['dokumente']: d.undo_cached_fields()
    for g in f['gruppen']: g.undo_cached_fields()
    f.undo_cached_fields()
  for b in self['bezugspersonen']:
    for gr in b['gruppen']: gr.undo_cached_fields()
    b.undo_cached_fields()
  for e in self['einrichtungen']: e.undo_cached_fields()
  self.undo_cached_fields()

Akte.akte_undo_cached_fields = akte_undo_cached_fields

def gruppe_undo_cached_fields(self):
  """Zieht alle gecachten Feldwerte zurück, aus allen Objekten, 
  die mit einer Gruppe zusammenhängen. Nach jedem insert oder update
  aufzurufen, damit keine falschen gecachten Werte auftreten."""

  for m in self['mitarbeiter']: m.undo_cached_fields()
  for b in self['bezugspersonen']: b.undo_cached_fields()
  for f in self['faelle']: f.undo_cached_fields()
  for d in self['gruppendokumente']: d.undo_cached_fields()
  self.undo_cached_fields()

Gruppe.gruppe_undo_cached_fields = gruppe_undo_cached_fields

## Allgemein Stringüberrüfung
## Datumsüberprüfung
## Codeüberprüfung
## Foreignkeyüberprüfung


#############################################################################
##
## Allgemeines für die folgenen Prüffunktionen (check_*)
## =====================================================

## 1. und 2. Argument ist eine dictionary und ein key, wodurch der
## zu prüfende Wert definiert ist (in unserem Beispiel die form).

## Der Wert kann immer (muß aber nicht) ein String sein, der je nach
## Prüffunktion umgewandelt wird. Falls die Umwandlung mißlingt, wird
## eine Exception geworfen.

## Falls ein Fehler auftritt, wird eine EBUpdateError Exception geworfen mit 
## dem errorstring als Argument.

## Falls das default Argument belegt ist (d.h. nicht None ist), wird es
## zurückgegeben falls 
## - die dictionary keinen Eintrag unter key hat
## - ein Eintrag existiert, dieser aber None oder '' ist

## Die default Werte werden *nicht* weiter überprüft.

## Falls kein default Wert angegeben ist (default = None), führt das Fehlen
## eines gültigen Wertes zu einem Fehler.
##
## Gültige Werte:
##  check_str_not_empty: ein nicht-leerer String
##  check_int_not_empty: ein Integer, kann auch 0 sein
##  check_fk: eine id, für die ein Objekt der entsprechenden Klasse existiert
##  check_code: ein code, für das ein Code Objekt der entsprechenden Kategorie 
##              existiert
##  check_date: ein gültiges Datum zwischen 1980 und today()
##              falls maybezero true ist, ist auch (0,0,0) zulässig
##              falls maybefuture true ist, kann das Datum in der Zukunft liegen
##                (bis 2030)
##              falls nodayallowed true ist, kann der Tag weggelassen werden (d=None)
##                Er wird dann auf 1 gesetzt.
##
#############################################################################

# Hilfsfunktion, damit das default Argument auch ein Objekt sein kann,
# aus dem der Wert geholt wird
def k_or_val(key, default):
  try: val = default[key]
  except: val = default
  return val

# Garantiert einen nicht-leeren String
def check_str_not_empty(dict, key, errorstring, default = None):
  val = dict.get(key)
  if val is None or val == '':
    if not default is None: return k_or_val(key, default)  
  if not val or type(val) != type(''): raise EE(errorstring)
  return val

def check_int_not_empty(dict, key, errorstring, default = None):
  val = dict.get(key)
  if val is None or val == '':
    if not default is None: return k_or_val(key, default)
  if type(val) == type(1): return val
  try: val = int(val)
  except:  raise EE(errorstring)
  return val


def check_fk(dict, key, klass, errorstring, default = None):
  fk = dict.get(key)
  if fk is None or fk == '':
    if not default is None: return k_or_val(key, default)
  try: fk = int(fk)
  except: raise EE(errorstring)
  try:
    #print 'FK', type(fk), fk
    obj = klass(fk)
  except Exception, e: 
    raise EE("%s: %s" % (errorstring, e))
  return fk
            
  

def check_date(dict, key, errorstring, default = None,
               maybezero = None, maybefuture = None, nodayallowed = None):
  
  if type(key) == type(()):
    d, m, y = key[0], key[1], key[2] 
  else:
    d, m, y = key + 'd', key + 'm', key + 'y'
  d, m, y = dict.get(d), dict.get(m), dict.get(y)
  if d is m is y is None or d == m == y == '':
    if not default is None: 
      if isinstance(default, Date): return default
      if isinstance(default, DBObjekt): return default.getDate(key)
      if type(default) == type(()): return apply(Date, default)
  if nodayallowed and d is None or d == '':
    d = '1'
  try:
    d,m,y = int(d), int(m), int(y)
  except:
    raise EE(errorstring)
  datum = Date(y,m,d)
  if (not datum.check()  or 
      (not maybefuture and datum.year != 0 and today() < datum) or
      (not maybezero and datum.year == 0)):
    raise EE("%s: %s" % (errorstring, str(datum)))
  return datum

def check_code(dict, key, kat_code, errorstring, default = None):
  code = dict.get(key)
  # print key, kat_code, code
  if code is None or code == '':
    if not default is None: 
      if type(default) == type(''): return cc(kat_code, default)
      else: return k_or_val(key, default)
  try: code = int(code)
  except: raise EE(errorstring)
  try:
    codeobj = Code(code)
    assert codeobj['kat_code'] == kat_code
    # print 'Code:' ,code
  except Exception, e: 
    raise EE("%s: %s" % (errorstring, e))
  return code


def get_string_fields(object, form, formnames, default = None, objectnames = None):
  if not objectnames:
    objectnames = formnames
  pairs = map(None, formnames, objectnames)
  for fname, objname in pairs:
    val = form.get(fname)
    if val is None:
      if not default is None: 
        val = k_or_val(objname, default)
    elif type(val) != type(''): raise TypeError(fname)
    object[objname] = val


# Falls der Wert eines Feldes in der form None oder '' ist und kein Default-
# wert angegeben ist,  wird der Wert auf None gesetzt.
# Ansonsten wird überprüft, ob es sich um ein Integer handelt,
# sonst Fehler.

def get_int_fields(object, form, formnames, default = None, objectnames = None):
  if not objectnames:
    objectnames = formnames
  pairs = map(None, formnames, objectnames)
  for fname, objname in pairs:
    val = form.get(fname)
    if val is None or val == '':
      if not default is None: 
        val = k_or_val(objname, default)
      else: val = None
    else: 
      try: val = int(val)
      except: raise TypeError(fname)
    object[objname] = val


# Gibt das existierende Objekt zurück.
# Hier gibt es keine defaults, da das Objekt existieren muß.
def check_exists(dict, key, klass, errorstring):
  """Raise an error if an instance of klass with id id doesn't exists."""
  try:
    id = int(dict[key])
    obj = klass(id)
  except:
    raise EE(errorstring)
  return obj

#######################
# Weiter Prüffunktionen
#######################

def check_unique(value, klass, field, errorstring):
  """Raise an error if value already exists for field for any instance of klass."""
  try:
    obj = klass(field, val)
    raise EE(errorstring % obj)
  except: pass
  return value

def check_not_exists(id, klass, errorstring):
  """Raise an error if an instance of klass with id id already exists."""
  try:
    obj = klass(id)
  except: pass
  else:
    raise EE(errorstring % obj)


########################
# Exceptions
########################

class EBUpdateError(Exception):
  pass

EE = EBUpdateError

# Es könnte auch Warnungen geben, die aber nicht einen Eintrag 
# verhindern, z.B.zu alte Datumsangaben (mehr als zwei Jahre zurück)

class EBUpdateWarning(Exception):
  pass


def mk_daten_dirs(n=None):
  """Erstellt die Datenverzeichnispfade bei der Installation fuer die Akten
     und das Exportverzeichnis."""

  import os
  akten_path = '%s/%s/%s' % (config.EBKUSHOME, config.DATEN_DIR, 'akten')
  gruppen_path = '%s/%s/%s' % (config.EBKUSHOME, config.DATEN_DIR, 'gruppen')
  try:
    os.mkdir('%s/%s' % (config.EBKUSHOME, config.DATEN_DIR), 0700) 
  except: pass
  try:
    os.mkdir('%s' % (akten_path), 0700)
  except: pass
  try:
    os.mkdir('%s' % (gruppen_path),0700)
  except: pass
  try:
    os.mkdir('%s/%s' % (config.EBKUSHOME, config.EXPORT_DIR) )
  except: pass
  
  if n is None or n == '':
    n = config.AK_DIRS_MAX
  m = int(n) 
  akdirs = range(m)
  for a in akdirs:
    try:
      os.mkdir('%s/%s' % (akten_path, str(a)) ,0700)
    except Exception, e:
      raise ('Keine Aktenverzeichnisse angelegt: %s' %(e))
  print 'Aktenverzeichnisse angelegt'

  return ''

def get_akte_path(akid):
  """Ermittelt den Pfad für die Dokumente 1 Akte anhand der Aktenid."""

  n = config.AK_DIRS_MAX # max. je n Akten in n Verzeichnissen
  akdirs = int(akid)/int(n)
  try:
    akte_path = '%s/%s/%s' % (config.EBKUSHOME,
                             config.DATEN_DIR, 'akten') + str('/%d/%d') % (akdirs,akid)
  except Exception, e:
    raise ('Kein Aktenverzeichnis. %s' %(e))
  return akte_path


def mk_akte_dir(akid):
  """Erstellt 1 Verzeichnis fuer 1 Akte anhand der Aktenid;
     gibt Pfad der Akte zurueck."""

  import os
  n = config.AK_DIRS_MAX # max. je n Akten in n Verzeichnissen
  if int(akid) < int(n):     
    akdir = 0                    
  else:
    akdir = int(akid)/int(n)   
  akte_path = '%s/%s/%s' % (config.EBKUSHOME, config.DATEN_DIR, 'akten') + str('/%d/%d') % (akdir,akid)
  try:
    os.mkdir('%s' % akte_path,0700) 
  except: pass
  return akte_path

def mk_gruppe_dir(gruppeid):
  """Erstellt 1 Verzeichnis fuer 1 Gruppe anhand der Gruppenid;
     gibt Pfad der Gruppe zurueck. """

  import os

  gruppe_path = '%s/%s/%s' % (config.EBKUSHOME,
                              config.DATEN_DIR, 'gruppen') + str('/%d') % (gruppeid)
  try:
    os.mkdir('%s' % gruppe_path,0700) 
  except: pass
  return gruppe_path

def get_gruppe_path(gruppeid):
  """Ermittelt den Pfad für die Dokumente 1 Gruppe anhand der Gruppenid. """

  try:
    gruppe_path = '%s/%s/%s' % (config.EBKUSHOME,
                             config.DATEN_DIR, 'gruppen') + str('/%d') % (gruppeid)
  except Exception, e:
    raise ('Kein Gruppenverzeichnis. %s' %(e))
  return gruppe_path


def get_rm_datum(frist=None):
  """Ermittelt anhand der Loeschfrist (Aufbewahrungsfrist) das Loeschdatum. """
  
  if frist is None or frist == '':
    frist = config.LOESCHFRIST
  jahr = today().year
  monat = today().month
  heute = int(jahr)*12 + int(monat)
  loeschzeitm = int(heute)-int(frist)
  loeschjahr = int(loeschzeitm) / int(12)
  loeschmonat = int(loeschzeitm) - (int(loeschjahr) * int(12))
  loeschdatum = {'loeschjahr' : loeschjahr, 'loeschmonat' : loeschmonat}
  return loeschdatum


def convert_pstoascii():
  """Konvertiert die PDF-Dokumente in schlechtes Ascii. Unixspezifisch,
     verwendet Systemaufruf fuer das Programm: pstoascii. """
    
  import os
  import ebkus.db.sql
  sql.opendb()

  dokl = DokumentList(where = 'mtyp = %s'
                      % cc('mimetyp', 'pdf'), order = 'fall_id,id')
  grdokl = GruppendokumentList(where = 'mtyp = %s'
                               % cc('mimetyp', 'pdf'), order = 'gruppe_id,id')

  for d in grdokl:
    gruppe_path = get_gruppe_path(d['gruppe_id'])
    dateil = os.listdir('%s' % gruppe_path)
    if '%s.txt' % d['id'] not in dateil and '%s.pdf' % d['id'] in dateil:
      os.system('ps2ascii %s/%s.pdf %s/%s.txt'
                % (gruppe_path,d['id'],gruppe_path,d['id']))

  for d in dokl:
    fall = Fall(d['fall_id'])
    akte_path = get_akte_path(fall['akte_id'])
    dateil = os.listdir('%s' % akte_path)
    if '%s.txt' % d['id'] not in dateil and '%s.pdf' % d['id'] in dateil:
      os.system('ps2ascii %s/%s.pdf %s/%s.txt'
                % (akte_path,d['id'],akte_path,d['id']))

  sql.closedb()



