# Achtung: zu publizierende Funktionen haben nicht immer
# einen __doc__ string. Ich habe cgi_module_publisher.py (Zeile 803
# entsprechend modifiziert.

from ebkus.db import sql
from ebkus.db import dbapp

class EBKuS:
  """Eine Instanz dieser Klasse bildet den Ausgangspunkt für Bobos
  Suche nach dem zu publizierendem Objekt.
  http://localhost/efb/ebs/klkarte?akid=22
  Gefunden wird entweder
  - eine Methode dieser Klasse
  - ein Funktionsobjekt über __getitem__
  """
  def __init__(self):
    self.functions = getFunctionsToBePublished()
    self.classes = getClassesToBePublished()
    sql.opendb()

  def __getitem__(self, name):
    try:
      klass = getattr(self.classes, name)
      object = klass()
      object.ebkus = self
      return object.process
    except:
      pass
    return getattr(self.functions, name)

  def dispatch(self, name, REQUEST, RESPONSE):
    function = self[name]
    return function(REQUEST, RESPONSE)

  # Beispiele

##   def xakteneu(self, REQUEST, RESPONSE):
##     "publish"
##     import Cakteneu
##     obj = Cakteneu.akteneu()
##     return obj.process(REQUEST, RESPONSE)

##   def xmenu(self, REQUEST, RESPONSE):
##     "publish"
##     import menu
##     return menu.menu(REQUEST, RESPONSE)

##   def test(self, REQUEST, RESPONSE):
##     "publish"
##     return "the test result" + str(REQUEST.form)

  def index_html(self, REQUEST, RESPONSE):
    return "Die Default Seite"

def makeObject(dict):
  class p: pass
  object = p()
  object.__dict__.update(dict)
  return object  
    
def getClassesToBePublished():
  """publish"""
  from ebkus.html.menu import menu
  from ebkus.html.klientenkarte import klkarte
  from ebkus.html.gruppenkarte import gruppenkarte
  from ebkus.html.akte import akteneu, waufnneu, updakte, updfall, zda, zdar, rmakten, rmakten2 
  from ebkus.html.anmeldung import anmneu, updanm
  from ebkus.html.bezugsperson import persneu, updpers
  from ebkus.html.einrichtungskontakt import einrneu, updeinr
  from ebkus.html.leistung import leistneu, updleist
  from ebkus.html.zustaendigkeit import zustneu, updzust
  from ebkus.html.fachstatistik import fsneu, updfs, updfsausw
  from ebkus.html.jghstatistik import jghneu, updjgh, updjghausw
  from ebkus.html.aktenvorblatt import vorblatt
  from ebkus.html.dokumentenkarte import dokkarte
  from ebkus.html.dokument import vermneu, updverm, updvermausw, upload, updgrverm, rmdok
  from ebkus.html.viewdokument import dokview, dokview2, print_pdf, printgr_pdf, suchetxt
  from ebkus.html.gruppe import menugruppe, gruppeneu, updgruppe, gruppeteilnausw, gruppeteiln, updteiln, rmteiln
  from ebkus.html.abfragen import fsabfr, fsergebnis, jghabfr, jghergebnis, formabfr2, formabfr3, abfr1, abfr2, abfr3, formabfr4, abfr4, formabfr5, abfr5, formabfr6, formabfr6a, formabfr6b, abfr6a, abfr6b
  from ebkus.html.datenaustausch import formabfrjghexport, jghexportfeedback, jghexportlist, formabfrdbexport, stellenabgleich
  from ebkus.html.mitarbeiter import mitausw, mitneu, updmit
  from ebkus.html.code import codelist, codetab, codeneu, updcode
  from ebkus.html.administration import admin, feedback
  
  return makeObject(locals())


def getFunctionsToBePublished():
  """Alle Funktionen, die hier im lokalen Namesraum sichtbar sind,
  werden von Bobo publiziert.
  Die Funktion sollte etwas zurückliefern, mit dem Bobo etwas anfangen
  kann:
  - einen String (HTML oder Text)
  - ein Objekt mit einer asHTML() Methode
  - ansonstent wird das Ergebnis der repr() Funktion genommen
  
  """
  #  Alle bisherigen Funktionen sind jetzt Klassen von
  #  getClassesToBePublished(). 

  #  Beispiel:
  #  from menu import menu

  return makeObject(locals())





