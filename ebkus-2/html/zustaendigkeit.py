
"""Module für die Zuständigkeiten."""

import string 

from ebkus.app import Request
from ebkus.app.ebapi import Akte, Fall, Zustaendigkeit, today
from ebkus.app.ebapih import mksel
from ebkus.html.templates import *


class zustneu(Request.Request):
  """Neue Zuständigkeit eintragen. (Tabelle: Zuständigkeit.)"""
  
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
    zustaendigkeiten = fall['zustaendigkeiten']
    zustaendigkeiten.sort('bgy', 'bgm', 'bgd')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Neue Zust&auml;ndigkeit eintragen',
              'ueberschrift':
              "Neue Zust&auml;ndigkeit f&uuml;r '%(vn)s %(na)s' eintragen" % akte}

    # Fuer FORM-HIDDEN-VALUES

    hidden ={'file': 'zusteinf'}
    zustid = Zustaendigkeit().getNewId()
    hiddenid ={'name': 'zustid', 'value': zustid}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(thzustneu_t )
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'na', user)
    res.append(zustneudatum_t % today())
    res.append(zustende_t % fall['zustaendig'])
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    if len(zustaendigkeiten) > 0:
      res.append(thzustaendigkeiten_t)
      for z in zustaendigkeiten:
        res.append(zustaendigkeiten_t % z)
      res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')


class updzust(Request.Request):
  """Neue Zuständigkeit eintragen. (Tabelle: Zuständigkeit.)"""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('zustid'):
      id  = self.form.get('zustid')
    else:
      self.last_error_message = "Keine ID für die Zuständigkeit erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    zustaendigkeit = Zustaendigkeit(int(id))
    fall = Fall(zustaendigkeit['fall_id'])
    akte = Akte(fall['akte_id'])
    zustaendigkeiten = fall['zustaendigkeiten']
    zustaendigkeiten.sort('bgd', 'bgm', 'bgy')

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Eintrag zur Zust&auml;ndigkeit korrigieren',
              'ueberschrift':
              "Eintrag zur Zust&auml;ndigkeit f&uuml;r '%(vn)s %(na)s' korrigieren" % akte}

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'updzust'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(thupdzust_t )
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'id', 
            zustaendigkeit['mit_id'])
    res.append(updzustdatum_t % zustaendigkeit)
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    if len(zustaendigkeiten) > 0:
      res.append(thzustaendigkeiten_t)
      for z in zustaendigkeiten:
        res.append(zustaendigkeiten_t % z)
    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')



