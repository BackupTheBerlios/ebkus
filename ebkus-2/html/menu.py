
"""Menü von EBKuS - Startseite."""

import string 

from ebkus.app import Request
from ebkus.config import EBKUSROOT
from ebkus.app.ebapi import today, ZustaendigkeitList
from ebkus.html.templates import *


class menu(Request.Request):
  """Menü der Klientenverwaltung."""
  
  permissions = Request.MENU_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stelle = self.stelle
    mitarbeiter = self.mitarbeiter
    
    # Headerblock, Menü u. Überschrift für das HTML-Template

    header = {'titel': 'Klientenkartei',
              'ueberschrift': '<A name="top">Klientenkartei %s</A>'
              % stelle['name']}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(ueberschrift_t % header)
    res.append(auswahlmenu_t)

    if mitarbeiter['benr__code'] == 'bearb':
      zustaendigkeiten = ZustaendigkeitList(where = 'ed = 0 and mit_id = %s'
                                            % mitarbeiter['id'] )
      zustaendigkeiten.sort('mit_id__na', 'fall_id__akte_id__na',
                            'fall_id__akte_id__vn')
      for z in zustaendigkeiten:
        if z['fall_id__akte_id__stzak'] == stelle['id']:
          res.append(klientauswahl_t % z)

    elif mitarbeiter['benr__code'] == 'verw':
      zustaendigkeiten = ZustaendigkeitList(where = 'ed = 0', order = 'id')
      zustaendigkeiten.sort('mit_id__na', 'fall_id__akte_id__na', 
                            'fall_id__akte_id__vn')
      for z in zustaendigkeiten:
        if z['fall_id__akte_id__stzak'] == stelle['id']:
          res.append(klientauswahl_t % z)

    # Admin soll keine Klientennamen erhalten, er braucht nur das Admin-Menu.
##     elif mitarbeiter['benr__code'] == 'admin':
##       zustaendigkeiten = ZustaendigkeitList(where = 'ed = 0', order = 'id')
##       zustaendigkeiten.sort('mit_id__na', 'fall_id__akte_id__na', 
##                             'fall_id__akte_id__vn')
##       for z in zustaendigkeiten:
##         if z['fall_id__akte_id__stzak'] == stelle['id']:
##           res.append(klientauswahl_t % z)

    res.append(menusubmit_t )
    res.append(abfragen_t % today() ) 
    res.append(administration_t)
    res.append(dokumentation_t % (EBKUSROOT, EBKUSROOT) )
    res.append(menufuss_t)

    return string.join(res, '')







