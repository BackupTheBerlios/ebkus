
"""Module für Gruppen."""

import string 

from ebkus.app import Request
from ebkus.app. ebapi import Gruppe, MitarbeiterGruppe, MitarbeiterGruppeList, Akte, Fall, FallGruppe, Bezugsperson, BezugspersonGruppe, ZustaendigkeitList, getNewGruppennummer, today, cc
from ebkus.app. ebapih import get_codes, mksel
from ebkus.html.templates import *


class menugruppe(Request.Request):
  """Hauptmenü der Gruppenkartei (Tabellen: Gruppe, MitarbeiterGruppe)."""
  
  permissions = Request.MENUGRUPPE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    # Headerblock, Menü u. Überschrift für das HTML-Template

    header = {'titel': 'Gruppenkartei',
              'ueberschrift':
              '<A name="top">Gruppenkartei %s</A>' % self.stelle['name']}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(ueberschrift_t % header)
    res.append(auswahlgrmenu_t)

    if self.mitarbeiter['benr__code'] == 'bearb':
      mitarbeitergruppenl = MitarbeiterGruppeList(where = 'mit_id = %s'
                                            % self.mitarbeiter['id'] )
      mitarbeitergruppenl.sort('mit_id__na', 'gruppe_id__name')
      for m in mitarbeitergruppenl:
        if m['gruppe_id__stz'] == self.stelle['id']:
          res.append(gruppenauswahl_t % m)

    elif self.mitarbeiter['benr__code'] == 'verw' or self.mitarbeiter['benr__code'] == 'admin':
      mitarbeitergruppenl = MitarbeiterGruppeList()
      mitarbeitergruppenl.sort('mit_id__na', 'gruppe_id__name')
      for m in mitarbeitergruppenl:
        if m['gruppe_id__stz'] == self.stelle['id']:
          res.append(gruppenauswahl_t % m)

    res.append(menugrsubmit_t)
    res.append(fuss_t)

    return string.join(res, '')


class gruppeneu(Request.Request):
  """Neue Gruppe eintragen (Tabellen: Gruppe, MitarbeiterGruppe)."""
  
  permissions = Request.GRUPPENEU_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    gruppentypen = get_codes('grtyp')
    teilnehmer = get_codes('teiln')
    gruppentypen.sort('name')
    teilnehmer.sort('name')

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Neue Gruppe', 'ueberschrift': 'Neue Gruppe'}

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'gruppeeinf'}
    gruppeid = Gruppe().getNewId()
    hiddenid ={'name': 'gruppeid', 'value': gruppeid}
    hiddenid2 ={'name': 'stz', 'value': self.stelle['id']}

    # Gruppenummer

    gruppennummer = getNewGruppennummer(self.stelle['code'])
    hiddengn ={'name': 'gn', 'value': gruppennummer }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemin_t )
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(gruppeneu_t % {'gn' : gruppennummer} )
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(formhiddennamevalues_t % hiddengn)
    res.append(formhiddennamevalues_t % hiddenid2)
    res.append(gruppeneu1_t % today())
    mksel(res, codeliste_t, teilnehmer)
    res.append(gruppeneu2_t)
    mksel(res, codeliste_t, gruppentypen)
    res.append(gruppeneu3_t)
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'ben', user)
    res.append(gruppeneu4_t)
    res.append(fuss_t)

    return string.join(res, '')


class updgruppe(Request.Request):
  """Gruppe ändern (Tabellen: Gruppe, MitarbeiterGruppe)."""
  
  permissions = Request.GRUPPENEU_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    if self.form.has_key('gruppeid'):
      gruppeid = self.form.get('gruppeid')
      gruppe = Gruppe(int(gruppeid))
    else:
      self.last_error_message = "Keine ID fuer die Gruppe erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
      
    mitarbeitergruppe =  gruppe['mitarbeiter']
    gruppentypen = get_codes('grtyp')
    teilnehmer = get_codes('teiln')
    gruppentypen.sort('name')
    teilnehmer.sort('name')

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Gruppe updaten',
              'ueberschrift':
              'Gruppe &quot;%(name)s, %(bgd)s.%(bgm)s.%(bgy)s-%(ed)s.%(em)s.%(ey)s&quot; &auml;ndern' % gruppe}

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'updgr'}
    hiddenid ={'name': 'gruppeid', 'value': gruppeid}
    hiddenid2 ={'name': 'stz', 'value': self.stelle['id']}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuegruppe_t % gruppe )
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(gruppeneu_t % gruppe )
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(formhiddennamevalues_t % hiddenid2)
    res.append(gruppeupd1_t % gruppe)
    mksel(res, codeliste_t, teilnehmer, 'id', gruppe['teiln'])
    res.append(gruppeneu2_t)
    mksel(res, codeliste_t, gruppentypen, 'id', gruppe['grtyp'])
    res.append(gruppeupd3_t )
    for m in mitarbeitergruppe:
      res.append(m['mit_id__na'] + '<BR>')
    res.append(gruppeupd4_t % gruppe)
    res.append(fuss_t)

    return string.join(res, '')


class gruppeteilnausw(Request.Request):
  """Teilnehmerauswahl (Tabellen: FallGruppe, BezugspersonGruppe)."""
  
  permissions = Request.GRUPPETEILN_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('gruppeid'):
      gruppeid = self.form.get('gruppeid')
      gruppe = Gruppe(gruppeid)
    else:
      self.last_error_message = "Keine ID fuer die Gruppe erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
      
    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Teilnehmerauswahl',
              'ueberschrift':
              "Teilnehmerauswahl aus der Klientenkartei f&uuml;r die Gruppe: %(name)s" % gruppe}

    # Fuer FORM-HIDDEN-VALUES

    hidden ={'file': 'gruppeteilneinf'}
    hiddenid ={'name': 'mitid', 'value': self.mitarbeiter['id']}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuegruppe_t % gruppe)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfdokgrneu_t % gruppe)
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)

    if self.mitarbeiter['benr__code'] == 'bearb':
      zustaendigkeiten = ZustaendigkeitList(where = 'ed = 0 and mit_id = %s'
                                            % self.mitarbeiter['id'] )
      zustaendigkeiten.sort('mit_id__na', 'fall_id__akte_id__na', 
                            'fall_id__akte_id__vn')
      res.append(teilnauswahl_t)

      for z in zustaendigkeiten:
        if z['fall_id__akte_id__stzak'] == self.stelle['id']:
          res.append(teilnauswahl1_t % z)
      res.append(teilnauswahl2_t)

      for z in zustaendigkeiten:
        if z['fall_id__akte_id__stzak'] == self.stelle['id']:
          akte = Akte(z['fall_id__akte_id'])
          fn = z['fall_id__fn']
          bezugspliste = akte['bezugspersonen']
          for b in bezugspliste:
            b['fn'] = fn
            res.append(teilnauswahl3_t % b)
            del b['fn']
      res.append(teilnauswahl4_t % today())

    elif self.mitarbeiter['benr__code'] == 'verw' or 'admin':
      zustaendigkeiten = ZustaendigkeitList(where = 'ed = 0' )
      zustaendigkeiten.sort('mit_id__na', 'fall_id__akte_id__na', 
                            'fall_id__akte_id__vn')
      res.append(teilnauswahl_t)

      for z in zustaendigkeiten:
        if z['fall_id__akte_id__stzak'] == self.stelle['id']:
          res.append(teilnauswahl1_t % z)
      res.append(teilnauswahl2_t)

      for z in zustaendigkeiten:
        if z['fall_id__akte_id__stzak'] == self.stelle['id']:
          akte = Akte(z['fall_id__akte_id'])
          fn = z['fall_id__fn']
          bezugspliste = akte['bezugspersonen']
          for b in bezugspliste:
            b['fn'] = fn
            res.append(teilnauswahl3_t % b)
            del b['fn']
      res.append(teilnauswahl4_t % today())

    res.append(formsubmitv_t %("Speichern", "Reset"))
    res.append(fuss_t)

    return string.join(res, '')


class gruppeteiln(Request.Request):
  """Gruppenteilnehmer eintragen (Tabellen: FallGruppe, BezugspersonGruppe)."""
  
  permissions = Request.GRUPPETEILN_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    if self.form.has_key('gruppeid'):
      gruppeid = self.form.get('gruppeid')
      gruppe = Gruppe(gruppeid)
    else:
      self.last_error_message = "Keine ID fuer Gruppe erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)

    bezugspersonen = gruppe['bezugspersonen']
    bezugspersonen.sort('bgy','bgm','bgd')
    faelle = gruppe['faelle']
    faelle.sort('fall_id__akte_id__na','bgy','bgm','bgd')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Gruppenteilnehmer',
              'ueberschrift':
              "%(name)s, %(bgd)s.%(bgm)s.%(bgy)s-%(ed)s.%(em)s.%(ey)s" % gruppe}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(ueberschrift_t % header)
    res.append(dokausgabe1_t % ('<A name="teiln">Teilnehmerliste</A><BR><BR>'))

    for f in faelle:
      fall = Fall(f['fall_id'])
      akte = Akte(fall['akte_id'])
      res.append(teiln1c_t % akte)
      res.append(teiln2c_t % f)

    for b in bezugspersonen:
      bezugsp = Bezugsperson(b['bezugsp_id'])
      res.append(teiln1d_t % bezugsp)
      res.append(teiln2d_t % b)

    res.append(teiln3_t)
    res.append(tabende_t)
    res.append(fussmin_t)

    return string.join(res, '')


class updteiln(Request.Request):
  """Teilnehmerdaten ändern (Tabellen: FallGruppe, BezugspersonGruppe)."""
  
  permissions = Request.GRUPPETEILN_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    if self.form.has_key('gruppeid'):
      gruppeid = self.form.get('gruppeid')
      gruppe = Gruppe(gruppeid)
    else:
      self.last_error_message = "Keine ID fuer die Gruppe erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)

    if self.form.has_key('bezugspid'):
      bezugspgrid = self.form.get('id')
      teiln = BezugspersonGruppe(int(bezugspgrid))
      bezugsp = Bezugsperson(teiln['bezugsp_id'])
    elif self.form.has_key('fallid'):
      fallgrid = self.form.get('id')
      teiln = FallGruppe(int(fallgrid))
      fall = Fall(teiln['fall_id'])
    else:
      self.last_error_message = "Keine ID fuer Fall oder Bezugsperson erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Datum des Teilnehmers ändern',
              'ueberschrift': "Datum des Gruppenteilnehmers &auml;ndern" }

    # Fuer FORM-HIDDEN-VALUES

    hidden ={'file': 'updgrteiln'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuegruppe_t % gruppe)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfdokgrneu_t % gruppe)
    res.append(formhiddenvalues_t % hidden)
    if self.form.has_key('fallid'):
      res.append(teilnupd_t % teiln)
      res.append(formhiddennamevalues_t % ({ 'name': 'fallgrid',
                                             'value' : teiln['id'] }))
    elif self.form.has_key('bezugspid'):
      res.append(formhiddennamevalues_t % ({ 'name': 'bezugspgrid',
                                             'value' : teiln['id'] }))
      res.append(teilnupdb_t % teiln)
    res.append(teilnupd1_t % teiln)
    res.append(formsubmitv_t %("Speichern", "Reset"))
    res.append(fuss_t)

    return string.join(res, '')


class rmteiln(Request.Request):
  """Teilnehmer löschen (Tabellen: FallGruppe, BezugspersonGruppe)."""
  
  permissions = Request.RMTEILN_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    if self.form.has_key('gruppeid'):
      gruppeid = self.form.get('gruppeid')
      gruppe = Gruppe(gruppeid)
    else:
      self.last_error_message = "Keine ID fuer Dokument erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)

    bezugspersonen = gruppe['bezugspersonen']
    faelle = gruppe['faelle']

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Gruppenteilnehmer löschen',
              'ueberschrift':
              "Teilnehmer der Gruppe &quot;%(name)s, %(bgd)s.%(bgm)s.%(bgy)s-%(ed)s.%(em)s.%(ey)s&quot;" % gruppe}

    # Fuer FORM-HIDDEN-VALUES

    hidden ={'file': 'removeteiln'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuegruppe_t % gruppe)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfdokgrneu_t % gruppe)
    res.append(formhiddenvalues_t % hidden)
    res.append(teilnauswahlb_t)
    for f in faelle:
      res.append(teilnauswahl1b_t % f)
    res.append(teilnauswahl2b_t)
    for b in bezugspersonen:
      res.append(teilnauswahl3b_t % b)
    res.append(teilnauswahl4b_t)
    res.append(formsubmitv_t %("L&ouml;schen", "Reset"))
    res.append(fuss_t)

    return string.join(res, '')

