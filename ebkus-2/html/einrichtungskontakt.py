
"""Module für die Einrichtungskontakte."""

import string 

from ebkus.app import Request
from ebkus.app.ebapi import Akte, Fall, Einrichtungskontakt, cc
from ebkus.app.ebapih import get_codes, mksel
from ebkus.html.templates import *


class einrneu(Request.Request):
  """Neuen Einrichtungskontakt eintragen. (Tabelle: Einrichtungskontakt.)"""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('fallid'):
      fallid = self.form.get('fallid')
    else:
      self.last_error_message = "Keine ID für den Fall erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    fall = Fall(int(fallid))
    akte = Akte(fall['akte_id'])
    letzter_fall = akte['letzter_fall']
    einrichtungen = akte['einrichtungen']
    einrichtungsarten = get_codes('klinsta')

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Neuen Einrichtungskontakt eintragen', 'ueberschrift': 'Neuen Einrichtungskontakt eintragen'}

    # Für FORMS-HIDDEN-VALUES

    hidden ={'file': 'einreinf'}
    einrid = Einrichtungskontakt().getNewId()
    hiddenid ={'name': 'einrid', 'value': einrid}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % letzter_fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % letzter_fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(theinrneu_t)
    mksel(res, codeliste_t, einrichtungsarten)
    res.append(einrneuna_t  % { 'nobed': cc('notizbed', 't'),                                 'status' : cc('einrstat', 'ja') }  )
    res.append(formsubmit_t )
    res.append(liniekurz_t)
    if einrichtungen == []:
      res.append(keineeinrneu_t)
    else:
      res.append(theinrneueinrichtungen_t)
      for e in einrichtungen:
        res.append(einrneueinrichtungen_t % e)
      res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')


class updeinr(Request.Request):
  """Einrichtungskontakt ändern. (Tabelle: Einrichtungskontakt.)"""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('einrid'):
      id = self.form.get('einrid')
    else:
      self.last_error_message = "Keine ID für die Einrichtung erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    einrichtung = Einrichtungskontakt(int(id))
    akte = Akte(einrichtung['akte_id'])
    letzter_fall = akte['letzter_fall']
    einrichtungen = akte['einrichtungen']
    einrichtungsarten = get_codes('klinsta')

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Einrichtungskontakt &auml;ndern',
              'ueberschrift':
              "Einrichtungskontakt '%(na)s' &auml;ndern" % einrichtung}

    # Für FORMS-HIDDEN-VALUES

    hidden ={'file': 'updeinr'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % letzter_fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % letzter_fall)
    res.append(theinrneu_t)
    mksel(res, codeliste_t, einrichtungsarten, 'id', einrichtung['insta'])
    if einrichtung['nobed'] == cc('notizbed', 't'):
      check = 'checked'
    else:
      check = ''
    res.append(updeinrna_t % einrichtung)
    res.append(checkbox_t % { 'name' : 'nobed', 
                              'id' : cc('notizbed', 't'), 'check' : check })
    res.append(updeinraktuell_t % einrichtung)
    res.append(formhiddenvalues_t % hidden)  
    res.append(formsubmit_t )
    res.append(liniekurz_t)
    if einrichtungen == []:
      res.append(keineeinrneu_t)
    else:
      res.append(theinrneueinrichtungen_t)
    for e in einrichtungen:
      res.append(einrneueinrichtungen_t % e)
    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')

