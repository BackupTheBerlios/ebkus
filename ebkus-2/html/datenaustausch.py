
"""Module für den Im- und Export aus der Datenbank."""

import string 
import time

from ebkus.app import Request
from ebkus.config import EXPORT_DIR, IMPORT_DIR, EBKUSROOT, EBKUSHOME
from ebkus.app.ebapi import Code, JugendhilfestatistikList, ExportprotokollList, ImportprotokollList, today, cc, getDBSite, EE
from ebkus.html.templates import *


class formabfrjghexport(Request.Request):
  """Auswahlformular für den Export der Jugendhilfestatistik."""
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    site = Code(cc('dbsite', '%s' % getDBSite()))
  
    # Headerblock, Menü u. Überschrift für das HTML-Template

    header = {'titel':
              'Bundesjugendhilfestatistik: Exportdatei erstellen',
              'ueberschrift':
              "Bundesjugendhilfestatistik: Exportdatei erstellen der %s" % site['name'] + " f&uuml;r das Statistische Landesamt"}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueadmin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "jghexportfeedback")
    res.append(thformabfr5_t % ('Erstelle Bundesjugendhilfestatistik',today().year) )
    res.append(formsubmitv_t % ("Okay","Reset") )
    res.append(formabfr5_2_t)
    res.append(fuss_t)

    return string.join(res, '')


class jghexportfeedback(Request.Request):
  """Aufruf zum Export der Jugendhilfestatistik und Feedback."""
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    import os

    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    if self.form.has_key('jahr'):
      jahr = self.form.get('jahr')
    else:
      self.last_error_message = "Kein Jahr erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)

    jghlist = JugendhilfestatistikList(where = 'ey = %s' % jahr)
    if len(jghlist) < 1:
      return '<HTML><BODY>Keine Bundesstatistik f&uuml;r %s </BODY></HTML>' % jahr
    try:
      os.system('python %s/app/jghexport.py %s ' % (EBKUSHOME, jahr) + '>%s/%s/jgh_log_%s.txt'
               % (EBKUSHOME, EXPORT_DIR, jahr) ) 
    except Exception, e:
      raise EE("Fehler beim Exportieren: %s") % str(e)

    site = Code(cc('dbsite', '%s' % getDBSite()))

    # Headerblock, Menü u. Überschrift für das HTML-Template

    header = {'titel':
              'Bundesjugendhilfestatistik: Exportdatei erstellen',
              'ueberschrift':
              "Bundesjugendhilfestatistik: Exportdatei der %s" % site['name'] + " f&uuml;r das Jahr %s " % jahr}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueadmin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    ausgabe = { 'ebkusroot' : EBKUSROOT,
                'exportdir' : EXPORT_DIR, 'jahr' : jahr }
    res.append(jghexportfeedback_t % ausgabe)
    res.append(downloadhinweis_t)
    res.append(fuss_t)

    return string.join(res, '')


class jghexportlist(Request.Request):
  """Listet die exportierten Jugendhilfestatistiken."""
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    import os
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    site = Code(cc('dbsite', '%s' % getDBSite()))
    dateiliste = os.listdir('%s/%s' % (EBKUSHOME, EXPORT_DIR) ) 
    dateiliste.sort()

    # Headerblock, Menü u. Überschrift für das HTML-Template

    header = {'titel':
              'Bundesjugendhilfestatistik: Exportliste',
              'ueberschrift':
              "Bundesjugendhilfestatistik: Liste der Exportdateien der %s" % site['name'] }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueadmin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(thjghexportliste_t)
    for f in dateiliste:
      if f[0:4] == 'jgh_':
        res.append(jghexportliste_t % (EBKUSROOT, EXPORT_DIR, f, f))
    res.append(tabende_t)
    res.append(downloadhinweis_t)
    res.append(fuss_t)

    return string.join(res, '')
    

class formabfrdbexport(Request.Request):
  """Auswahlformular für den Ex- bzw. Import von Daten."""
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    site = Code(cc('dbsite', '%s' % getDBSite() ) )    

    # Headerblock, Menü u. Überschrift für das HTML-Template

    header = {'titel':
              'Stellenabgleich: Ex- und Import von Daten',
              'ueberschrift':
              'Stellenabgleich: Ex- und Import von Daten in die Datenbank der '  + site['name']}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueadmin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "stellenabgleich")
    res.append(formexport_t)
    res.append(formsubmitv_t % ("Okay","Reset"))
    res.append(formexport2_t)
    res.append(exporthinweis_t % (EXPORT_DIR, EXPORT_DIR) )
    res.append(fuss_t)

    return string.join(res, '')


class stellenabgleich(Request.Request):
  """Aufruf der Datei für den Ex- bzw. Import von Daten."""
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    import os
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    site = Code(cc('dbsite', '%s' % getDBSite()))
    if self.form.has_key('dbexport'):
      arg = self.form.get('dbexport')
    else:
      self.last_error_message = "Kein Jahr erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)      

    if arg == 'i' or arg == 'e':
      try:
        os.system('python %s/app/dbexport.py -%s %s ' % (EBKUSHOME,
                                           arg, self.mitarbeiter['ben']))
      except Exception, e:
        raise EE("Fehler beim Exportieren: %s") % str(e)
    exportliste = ExportprotokollList(where = 'id > 0',
                                      order = 'dbsite,zeit desc')
    importliste = ImportprotokollList(where = 'id > 0',
                                      order = 'dbsite,zeit desc')

    # Headerblock, Menü u. Überschrift für das HTML-Template

    header = {'titel':
              'Stellenabgleich: Protokoll zum Ex- und Import von Daten',
              'ueberschrift':
              "Stellenabgleich: Protokoll zum Ex- und Import von Daten in die Datenbank der %s" % site['name'] }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueadmin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    if exportliste:
      res.append(thexport_t % 'Exportiert:')
      for e in exportliste:
        datum = time.strftime('%d.%m.%y / %H:%M:%S', time.localtime(e['zeit']))
        e['datum'] = datum
        res.append(export_t % e)
        del e['datum']
      res.append(tabende_t)

    if importliste:
      res.append(thexport_t % 'Importiert:')
      for i in importliste:
        datum = time.strftime('%d.%m.%y / %H:%M:%S', time.localtime(i['zeit']))
        i['datum'] = datum
        res.append(export_t % i)
        del i['datum']
      res.append(tabende_t)

    res.append(exporthinweis_t % (EXPORT_DIR, EXPORT_DIR ))
    res.append(fuss_t)

    return string.join(res, '')


