
"""Module für den Code und die Kategorieen."""

import string 

from ebkus.app import Request
from ebkus.config import MASTER_SITE
from ebkus.app.ebapi import Kategorie, KategorieList, TabelleList, FeldList, Code, today
from ebkus.app.ebapih import get_codes, get_all_codes, mksel, mk_ausgabe_codeliste
from ebkus.html.templates import *


class codelist(Request.Request):
  """Tabellarische Liste der Kategorien und Codes. """
  
  permissions = Request.CODE_PERM

  def processForm(self, REQUEST, RESPONSE):
    user = self.user

    katliste = KategorieList(where = "code <> '%s' " % "verwtyp", 
                             order = 'name')

    # Headerblock, Menue u. Überschrift fuer das HTML-Template

    header = {'titel': 'Kategorielisten',
              'ueberschrift':
              '<A name="top"> Alle Kategorie- und Merkmalslisten im &Uuml;berblick</A>'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuecode_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(thkatliste_t)

    for k in katliste:
      k1 = k.copy()
      if k1['dok'] == None:
        k2 = {'dok' : ''}
        k1.dict_update(k2)
      res.append(katliste_t % k1)
      del k2
      feldliste = FeldList(where = 'kat_id = %s' %k['id'])
      for f in feldliste:
        res.append(tabliste_t %f)
      res.append(katlistende_t)
    res.append(tabende_t)

    for k in katliste:
      res.append(thkat_t % k)
      res.append(thcodeliste_t)
      cliste = get_all_codes(k['code'])
      mk_ausgabe_codeliste(res, codelisten_t, cliste)
      res.append(tabende_t)
      res.append(hreftop_t % "codelist#top")

    res.append(fuss_t)

    return string.join(res, '')


class codetab(Request.Request):
  """1 Code-Tabelle."""
  
  permissions = Request.CODE_PERM

  def processForm(self, REQUEST, RESPONSE):
    user = self.user
    stelle = self.stelle
    if self.form.has_key('tabelle'):
      tabelle = self.form.get('tabelle')
    else:
      self.last_error_message = "Keine ID fuer die Tabelle erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)

    tliste = TabelleList(where = "klasse = '%s'" % tabelle)

    if len(tliste) == 1:
      tab = tliste[0]
      felder = tab['felder']
      felder.sort('kat_id__name')

    # Headerblock, Menü u. Überschrift fuer das HTML-Template

    header = {'titel':
              "Kategorieliste der '%s'" % tabelle,
              'ueberschrift':
              '<A name="top"> Kategorie- und Merkmalslisten zu: '+ "'%s'" % tabelle +' </A>'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuecode_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)

    x = []
    for f in felder:
      if f['kat_id'] and f['kat_id'] not in x:
        a = felder.find('kat_id', f['kat_id'])
        if len(a) >= 1:
          x.append(f['kat_id'])
          k = Kategorie(f['kat_id'])
          res.append(thkat_t % k)
          res.append(thcodeliste_t)
          cliste = get_all_codes(k['code'])
          mk_ausgabe_codeliste(res, codelisten_t, cliste) 
          res.append(tabende_t)
          res.append(hreftop_t % "codetab?tabelle=%s#top" % tabelle)

    res.append(fuss_t)

    return string.join(res, '')


class codeneu(Request.Request):
  """Eingabeformular fuer neuen Code."""
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    user = self.user
    stelle = self.stelle
    if self.form.has_key('katid'):
      katid = self.form.get('katid')
    else: 
      self.last_error_message = "Keine ID fuer das Item erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    kat = Kategorie(int(katid))
    codeliste = get_all_codes(kat['code'])
    masterdb = Code(kat_code = 'dbsite', code = '%s' % MASTER_SITE)
    
    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel':
              'Neues Merkmal eintragen',
              'ueberschrift': "Neues Merkmal der Kategorie '%(name)s' eintragen" % (kat)}

    # Form-Hidden-Values
    
    hidden ={'file': 'codeeinf'}
    codeid = Code().getNewId()
    hiddenlist = [{'name': 'codeid', 'value': codeid},
                {'name': 'katid', 'value': kat['id']},
                {'name': 'katcode', 'value': kat['code']}]

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuecode_t )
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "admin")
    res.append(formhiddenvalues_t % hidden)
    for h in hiddenlist:
      res.append(formhiddennamevalues_t % h)
    last = len(codeliste)
    res.append(thcodeneu_t % kat)
    res.append(codeneu1_t )
    i = 1
    while i < len(codeliste) + 2:
      if i == len(codeliste) + 1:
        sel = "selected"
      else:
        sel = ''
      res.append(codeneu2_t % (i, sel, i))
      i = i + 1
    res.append(codeneu3_t)
    res.append(tabende_t)
    res.append(codeneu4_t)
    res.append(codehilfe_t % (masterdb['name']))
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    res.append(thkat1_t % kat)
    res.append(thcodeliste1_t)
    mk_ausgabe_codeliste(res, codelisten1_t, codeliste)
    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')


class updcode(Request.Request):
  """Updateformular fuer den Code."""
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    user = self.user
    stelle = self.stelle
    if self.form.has_key('codeid'):
      codeid = self.form.get('codeid')
    else:
      self.last_error_message = "Keine ID fuer das Item erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)      
    code = Code(codeid)
    kat = Kategorie(code['kat_id'])
    codeliste = get_all_codes(code['kat_code'])
    masterdb = Code(kat_code = 'dbsite', code = '%s' % MASTER_SITE)

    # Headerblock, Menü u. Überschrift fuer das HTML-Template

    header = {'titel': 'Merkmal &auml;ndern',
              'ueberschrift':
              "Merkmal '%(name)s' der Kategorie '%(kat_id__name)s' &auml;ndern" % (code)}

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'updcode'}
    hiddenlist = [{'name': 'codeid', 'value': codeid},
                {'name': 'katid', 'value': kat['id']},
                {'name': 'katcode', 'value': kat['code']}]

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuecode_t )
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "admin")
    res.append(formhiddenvalues_t % hidden)
    for h in hiddenlist:
      res.append(formhiddennamevalues_t % h)
    res.append(thupdcode_t % kat)
    res.append(updcode1_t % code)
    mksel(res, updcode2_t, codeliste, 'sort', code['sort'])
    mk_ausgabe_codeliste(res, updcode3_t, code)
    if code['off'] == 1:
      check = 'checked'
    else:
      check = ''
    res.append(updcode4_t % {'check' : check} )
    mk_ausgabe_codeliste(res, updcode5_t, code)
    res.append(tabende_t)
    mk_ausgabe_codeliste(res, updcode6_t, code)
    res.append(updcodehilfe_t % masterdb['name'])
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    res.append(thupdkat1_t % kat)
    res.append(thupdcodeliste_t)
    mk_ausgabe_codeliste(res, updcodeliste_t, codeliste)
    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')




