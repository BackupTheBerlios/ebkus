
"""Module für die Mitarbeiter-Daten."""

import string 

from ebkus.app import Request
from ebkus.config import MASTER_SITE
from ebkus.app.ebapi import Mitarbeiter, MitarbeiterList, Code, today
from ebkus.app.ebapih import get_codes, get_all_codes, mksel
from ebkus.html.templates import *


class mitausw(Request.Request):
  """Auswahlformular zum Ändern der Mitarbeiterdaten. """
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    bearbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stelle = self.stelle
    mitarbeiterliste = MitarbeiterList(where = '', order = 'na')  
    stellenzeichen = get_all_codes('stzei')
    benutzerarten = get_all_codes('benr')
    dienststatusl = get_all_codes('status')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel':
              'Mitarbeitereintrag zum &Auml;ndern ausw&auml;hlen',
              'ueberschrift':
              "Mitarbeitereintrag zum &Auml;ndern ausw&auml;hlen"}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemit_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(thmit_t)
    for m in mitarbeiterliste:
      res.append(mitlistehrefs_t % m)
    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')


class mitneu(Request.Request):
  """Mitarbeiterstammdatenformular."""
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    bearbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stelle = self.stelle
    mitarbeiterliste = MitarbeiterList(where = '', order = 'na')  
    stellenzeichen = get_all_codes('stzei')
    masterdb = Code(kat_code = 'dbsite', code = '%s' % MASTER_SITE)
    benutzerarten = get_all_codes('benr')
    dienststatusl = get_all_codes('status')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel':
              'Neuen Mitarbeiter eintragen', 'ueberschrift':
              "Neuen Mitarbeiter eintragen"}

    # Form-Hidden-Values

    hidden ={'file': 'miteinf'}
    mitid = Mitarbeiter().getNewId()
    hiddenid ={'name': 'mitid', 'value': mitid}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemit_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "admin")
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(thmit_t)
    res.append(mittext_t)
    res.append(mitsel1_t % "stat")
    mksel(res, codelistecode_t, dienststatusl, 'code', 'i')
    res.append(mitsel2_t)
    res.append(mitsel1_t % "benr")
    mksel(res, codelistecode_t, benutzerarten, 'code', 'bearb')
    res.append(mitsel2_t)
    res.append(mitsel1_t % "stz")
    mksel(res, codelistecode_t, stellenzeichen, 'code', stelle['code'])
    res.append(mitsel2_t)
    res.append(tabende_t)
    res.append(hinweis_t % masterdb['name'])
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    res.append(thmit_t)
    for m in mitarbeiterliste:
      res.append(mitliste_t % m)
    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')


class updmit(Request.Request):
  """Updateformular für die Stammdaten der Mitarbeiter. """
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    bearbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stelle = self.stelle
    stellenzeichen = get_codes('stzei')
    benutzerarten = get_codes('benr')
    dienststatusl = get_codes('status')
    mitarbeiterliste = MitarbeiterList(where = '', order = 'na')  
    if self.form.has_key('mitid'):
      mitid = self.form.get('mitid')
      mit = Mitarbeiter(int(mitid))
    else:
      self.last_error_message = "Keine ID fuer den Mitarbeiter erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Mitarbeitereintrag ändern',
              'ueberschrift':
              "Mitarbeitereintrag für <B> '%(vn)s %(na)s' </B> ändern" % mit}

    # Fuer FORM-HIDDEN-VALUES

    hidden ={'file': 'updmit'}
    hiddenid ={'name': 'mitid', 'value': mitid}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemit_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "admin")
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(thmit_t)
    res.append(mitupdtext_t % mit)
    res.append(mitsel1_t % "stat")
    mksel(res, codelistecode_t, dienststatusl, 'id', mit['stat'])
    res.append(mitsel2_t)
    res.append(mitsel1_t % "benr")
    mksel(res, codelistecode_t, benutzerarten, 'id', mit['benr'])
    res.append(mitsel2_t)
    res.append(mitsel1_t % "stz")
    mksel(res, codelistecode_t, stellenzeichen, 'id', mit['stz'])
    res.append(mitsel2_t)
    res.append(tabende_t)
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    res.append(thmit_t)
    for m in mitarbeiterliste:
      res.append(mitlistehrefs_t % m)
    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')



