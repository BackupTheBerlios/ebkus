
"""Module für die Bezugspersonen."""

import string 

from ebkus.app import Request
from ebkus.app.ebapi import Akte, Fall, Bezugsperson, cc
from ebkus.app.ebapih import get_codes, mksel
from ebkus.html.templates import *


class persneu(Request.Request):
  """Neue Bezugsperson eintragen. (Tabelle: Bezugsperson)"""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('fallid'):
      fallid = self.form.get('fallid')
    else:
      self.last_error_message = "Keine ID für die Bezugsperson erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    fall = Fall(fallid)
    akte = Akte(fall['akte_id'])
    letzter_fall = akte['letzter_fall']
    bezugspersonen = akte['bezugspersonen']
    bezugspersonen.sort('verw__sort')
    verwandtschaftsarten = get_codes('klerv')
    familienarten = get_codes('fsfs')

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Neue Person eintragen',
              'ueberschrift': 'Neue Person eintragen'}

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'perseinf'}
    bpid = Bezugsperson().getNewId()
    hiddenid ={'name': 'bpid', 'value': bpid}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % letzter_fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % letzter_fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(persneuverw1_t)
    if self.form.has_key('klerv'):
      mksel(res, codeliste_t, verwandtschaftsarten, 'id',
            cc('klerv', self.form['klerv']))
    else:
      mksel(res, codeliste_t, verwandtschaftsarten)
    res.append(persneuna_t % akte )
    mksel(res, codeliste_t, familienarten)
    res.append(persneunot_t %
                    {'nobed': cc('notizbed', 't'), 
                    'vrt' : cc('vert', 'f') })
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    res.append(persneuakte_t % akte)
    for b in bezugspersonen:
        res.append(persneubpersonen_t % b)
    res.append(tabende_t)
    res.append(fuss_t)
    return string.join(res, '')

class updpers(Request.Request):
  """Bezugsperson ändern. (Tabelle: Bezugsperson)"""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('bpid'):
      id = self.form.get('bpid')
    else:
      self.last_error_message = "Keine ID für die Bezugsperson erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    bezugsperson = Bezugsperson(int(id))
    akte = bezugsperson['akte']
    letzter_fall = akte['letzter_fall']
    bezugspersonen = akte['bezugspersonen']
    bezugspersonen.sort('verw__sort')
    verwandtschaftsarten = get_codes('klerv')
    familienarten = get_codes('fsfs')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Bezugsperson &auml;ndern',
              'ueberschrift':
              "Bezugsperson '%(vn)s %(na)s' &auml;ndern" % bezugsperson} 

    # Fuer FORM-HIDDEN-VALUES

    hidden ={'file': 'updpers'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % letzter_fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % letzter_fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(updpersna_t % bezugsperson)
    mksel(res, codeliste_t, verwandtschaftsarten, 'id', bezugsperson['verw'])
    res.append(updpersfs_t)
    mksel(res, codeliste_t, familienarten, 'id', bezugsperson['fs'])
    if bezugsperson['nobed'] == cc('notizbed', 't'):
      check = 'checked'
    else:
      check = ''
    res.append(updpersnot_t % {'nobed': cc('notizbed', 't'), 
                               'check' : check,
                               'no': bezugsperson['no'],
                               'vrt': bezugsperson['vrt']})
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    res.append(persneuakte_t % akte)
    for b in bezugspersonen:
      res.append(persneubpersonen_t % b)
    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')


