
"""Module für die Anmeldung."""

import string 

from ebkus.app import Request
from ebkus.app.ebapi import Akte, Fall, Anmeldung, cc
from ebkus.app.ebapih import get_codes, mksel
from templates import *


class anmneu(Request.Request):
  """Neue Anmeldung eintragen. (Tabelle: Anmeldung)"""
  
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
    bezugspersonen = akte['bezugspersonen']
    bezugspersonen.sort('verw__sort')
    zugangsarten = get_codes('fszm')

    # Datum des Fallbeginns und Nachname der 1 Bezugspers. zur Übernahme
    # im Formular anbieten.

    anmeldung = Anmeldung()
    anmeldung['ad'] = fall['bgd']
    anmeldung['am'] = fall['bgm']
    anmeldung['ay'] = fall['bgy']
    if bezugspersonen:
      b1 = bezugspersonen[0]
      anmeldung['von'] = b1['na']
      anmeldung['mtl'] = b1['tl1']
    else:
      anmeldung['von'] = ''
      anmeldung['mtl'] = ''

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Neue Anmeldeinformation eintragen',
              'ueberschrift':
              "Neue Anmeldeinformation zu '%(vn)s %(na)s' eintragen" % akte }

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'anmeinf'}
    anmid = Anmeldung().getNewId()
    hiddenid ={'name': 'anmid', 'value': anmid}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(anmneuvon_t % anmeldung)
    mksel(res, codeliste_t, zugangsarten)
    res.append(anmneuempfehlung_t )
    res.append(formsubmit_t)
    res.append(fuss_t)

    return string.join(res, '')


class updanm(Request.Request):
  """Anmeldung ändern. (Tabelle: Anmeldung)"""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('anmid'):
      id = self.form.get('anmid')
    else:
      self.last_error_message = "Keine ID für die Anmeldung erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    anmeldung = Anmeldung(int(id))
    fall = Fall(anmeldung['fall_id'])
    akte = Akte(fall['akte_id'])
    zugangsarten = get_codes('fszm')

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Anmeldeinformation &auml;ndern',
              'ueberschrift':
              "Anmeldeinformation zu '%(vn)s %(na)s' &auml;ndern" % akte}

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'updanm'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(anmneuvon_t % anmeldung)
    mksel(res, codeliste_t, zugangsarten, 'id', anmeldung['zm'])
    res.append(updanmempfehlung_t % anmeldung)
    res.append(formsubmit_t)
    res.append(fuss_t)

    return string.join(res, '')




