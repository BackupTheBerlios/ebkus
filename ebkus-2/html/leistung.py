
"""Module für die Leistung."""

import string 

from ebkus.app import Request
from ebkus.app.ebapi import Akte, Fall, Leistung, cc, today
from ebkus.app.ebapih import get_codes, mksel
from ebkus.html.templates import *


class leistneu(Request.Request):
  """Neue Leistung eintragen. (Tabelle: Leistung.)"""
  
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
    leistungen = fall['leistungen']
    leistungen.sort('bgy', 'bgm', 'bgd')
    leistungsarten = get_codes('fsle')

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Neue Leistung eintragen',
              'ueberschrift':
              "Neue Leistung f&uuml;r '%(vn)s %(na)s' eintragen" % akte}

    # Für FORM-HIDDEN-VALUES

    hidden = {'file': 'leisteinf'}
    leistid = Leistung().getNewId()
    hiddenid ={'name': 'leistid', 'value': leistid}
    hiddenid2 ={'name': 'stz', 'value': self.stelle['id']}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(formhiddennamevalues_t % hiddenid2)
    res.append(thleistneu_t)
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'ben', user)
    res.append(leistneu_t)
    mksel(res, codeliste_t, leistungsarten)
    res.append(leistneubg_t % today())
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    if leistungen == []:
      res.append(keineleistungneu_t)
    else:
      res.append(thleistungsliste_t)
      for l in leistungen:
        res.append(leistungsliste_t % l)
      res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')


class updleist(Request.Request):
  """Leistung ändern. (Tabelle: Leistung.)"""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('leistid'):
      id = self.form.get('leistid')
    else:
      self.last_error_message = "Keine ID für die Leistung erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    leistung = Leistung(int(id))
    fall = Fall(leistung['fall_id'])
    akte = Akte(fall['akte_id'])
    leistungen = fall['leistungen']
    leistungen.sort('bgy', 'bgm', 'bgd')
    leistungsarten = get_codes('fsle')

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Leistung &auml;ndern',
              'ueberschrift':
              "Leistung f&uuml;r '%(vn)s %(na)s' &auml;ndern" % akte}

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'updleist'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(thleistneu_t)
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'id', leistung['mit_id'])
    res.append(leistneu_t)
    mksel(res, codeliste_t, leistungsarten,  'id', leistung['le'])
    res.append(leistdatum_t % leistung)
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    if leistungen == []:
      res.append(keineleistungneu_t)
    else:
      res.append(thleistungsliste_t)
      for l in leistungen:
        res.append(leistungsliste_t % l)
      res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')
