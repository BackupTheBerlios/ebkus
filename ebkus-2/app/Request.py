
"""Allgemeine Klasse für den Request."""

from ebkus.app import ebapi


# Benutzerrechte für inhaltliche Teile (Dateien) des Programms.
# Neue Einträge in der Kategorie 'Benutzerrechte' müssen hier 
# aufenommen werden, damit sie wirksam sind.
# (STAT ist die Abkürzung für Statistik, ABFR für Abfragen)
# VERM für Vermerk, RM für REMOVE.


ADMIN_PERM = 'admin',
UPDATE_PERM = 'verw','bearb',
CODE_PERM = 'admin','verw','bearb',
ABFR_PERM = 'verw','bearb',
STATABFR_PERM = 'verw','bearb',
STAT_PERM = 'verw','bearb',
KLKARTE_PERM = 'verw','bearb',
MENU_PERM = 'admin','verw','bearb',
VERM_PERM = 'bearb',            # vermerk_permission
NOTIZ_PERM = 'bearb',
DOK_PERM = 'bearb',
DOKVIEW_PERM = 'bearb',
RMDOK_PERM = 'bearb',
RMAKTEN_PERM = 'admin',
GRUPPENKARTE_PERM = 'bearb',
MENUGRUPPE_PERM = 'bearb',
GRUPPETEILN_PERM = 'bearb',
GRUPPENEU_PERM = 'bearb',
RMTEILN_PERM = 'bearb',


class Request:

  def process(self, REQUEST, RESPONSE):
    try:
      self.REQUEST = REQUEST
      self.RESPONSE = RESPONSE
      self.form = self.REQUEST.form
      self.checkAuth()
      return self.processForm(REQUEST, RESPONSE)
    except Exception, e:
      self.last_error_message = str(e)
      return self.EBKuSError(REQUEST, RESPONSE)

  def checkAuth(self):
    """Prüft Benutzername und Benutzerberechtigung.
    Setzt self.user, self.mitarbeiter, self.stelle"""
    
    try:
      self.user = self.REQUEST.environ['REMOTE_USER']
    except:
      raise ebapi.EE("Keine Benutzerkennung")

    ml = ebapi.MitarbeiterList(where = "ben = '%s'"  % self.user +
                                  " and stat = %d"  % ebapi.cc('status', 'i'),
                                  order = 'na')
    if len(ml) != 1:
      raise ebapi.EE("Kein gültiger Benutzername: %s" % self.user)
    self.mitarbeiter = ml[0]
    code_perm = ebapi.Code(self.mitarbeiter['benr'])
    if code_perm['code'] not in self.permissions:
      raise ebapi.EE("Keine Berechtigung zum Erhalt der angefordeten Daten")
    self.stelle = ebapi.Code(self.mitarbeiter['stz'])

  def EBKuSError(self, REQUEST, RESPONSE):
    "Im Falle eines Fehlers eine schöne HTML-Fehlermeldung ausgeben."
    return '<HTML><BODY>' + self.last_error_message + '</BODY></HTML>'


  def getMitarbeiterliste(self):
    stz_id = self.stelle['id']
    ml = ebapi.MitarbeiterList(
      where = 'stat = %s and benr = %s and stz = %s' 
      % (ebapi.cc('status', 'i'), ebapi.cc('benr', 'bearb'), stz_id),
      order = 'na')
    return ml

