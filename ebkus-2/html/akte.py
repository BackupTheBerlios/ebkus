
"""Module für Akte und Fall."""

import string 

from ebkus.app import Request
from ebkus import config
from ebkus.app.ebapi import Akte, Fall, Zustaendigkeit, getNewFallnummer, today, cc
from ebkus.app.ebapih import get_codes, mksel
from templates import *


class akteneu(Request.Request):
  """Neue Fallakte anlegen (Tabellen: Akte, Fall, Zuständigkeit, Leistung)."""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    familienarten = get_codes('fsfs')
    leistungsarten = get_codes('fsle')
    
    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Neue Klienten-Akte',
              'ueberschrift': 'Neue Klientenakte anlegen'}

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'akteeinf'}
    akid = Akte().getNewId()
    hiddenid ={'name': 'akid', 'value': akid}
    hiddenid2={'name': 'stzbg', 'value': self.stelle['id']}
  
    # Fallnummer

    fallnummer = getNewFallnummer(self.stelle['code'])
    hiddenfn ={'name': 'fn', 'value': fallnummer }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemin_t )
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(akteneu_t ) 
    mksel(res, codeliste_t, familienarten)
    res.append(akteneuno_t)
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'ben', user)
    res.append(akteneufallbg_t % today())
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'ben', user)
    res.append(akteneuleist_t)
    mksel(res, codeliste_t, leistungsarten, 'code', '1')
    res.append(akteneuleistbg_t % today())
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(formhiddennamevalues_t % hiddenid2)
    res.append(formhiddennamevalues_t % hiddenfn)
    res.append(formsubmit_t)
    res.append(fuss_t)

    return string.join(res, '')


class waufnneu(Request.Request):
  """Wiederaufnahme einer vorhandener  Fallakte 
  (Tabellen: Akte, Fall, Zuständigkeit, Leistung)."""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.get('akid'):
      akid = self.form.get('akid')
    else:
      self.last_error_message = "Keine ID fuer die Akte erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)      
    akte = Akte(int(akid))
    letzter_fall = akte['letzter_fall']
    familienarten = get_codes('fsfs')
    leistungsarten = get_codes('fsle')

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Wiederaufnahme eintragen',
              'ueberschrift':
              "Wiederaufnahme des Klienten '%(vn)s %(na)s' eintragen" % akte} 

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'waufneinf'}
    fallid = Fall().getNewId()
    hiddenid ={'name': 'fallid', 'value': fallid}
    hiddenstatus ={'name': 'status', 'value': cc('stand', 'l')}
    hiddenid2={'name': 'stzbg', 'value': self.stelle['id']}

    # Fallnummer

    fallnummer = getNewFallnummer(self.stelle['code'])
    hiddenfn ={'name': 'fn', 'value': fallnummer }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % letzter_fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(waufnakte_t % akte)
    mksel(res, codeliste_t, familienarten, 'id', akte['fs'])
    res.append(waufnakteno_t % akte)
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'ben', user)
    res.append(akteneufallbg_t % today())
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'ben', user)
    res.append(akteneuleist_t)
    mksel(res, codeliste_t, leistungsarten)
    res.append(akteneuleistbg_t % today())
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(formhiddennamevalues_t % hiddenid2)
    res.append(formhiddennamevalues_t % hiddenfn)
    res.append(formhiddennamevalues_t % hiddenstatus)
    res.append(formsubmit_t)
    res.append(fuss_t)

    return string.join(res, '')


class updakte(Request.Request):
  """Akte ändern (Tabelle Akte)."""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('akid'):
      akid = self.form.get('akid')
      akte = Akte(int(akid))
    else:
      self.last_error_message = "Keine ID fuer die Akte erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    letzter_fall = akte['letzter_fall']
    bezugspersonen = akte['bezugspersonen']
    bezugspersonen.sort('verw__sort')
    familienarten = get_codes('fsfs')
    verwandtschaftsarten = get_codes('klerv')

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Klientendaten &auml;ndern',
              'ueberschrift':
              "Klientendaten '%(vn)s %(na)s' &auml;ndern" % akte} 

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'updakte'}
    hiddenid2={'name': 'stzbg', 'value': akte['stzbg']}
    hiddenid3={'name': 'stzak', 'value': akte['stzak']}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % letzter_fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % letzter_fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid2)
    res.append(formhiddennamevalues_t % hiddenid3)
    res.append(updaktena_t % akte)
    mksel(res, codeliste_t, familienarten, 'id', akte['fs'])
    res.append(updakteno_t % akte)
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    res.append(persneuakte_t % akte)
    for b in bezugspersonen:
      res.append(persneubpersonen_t % b)
    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')


class updfall(Request.Request):
  """Fall updaten (Tabelle: Fall)."""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('fallid'):
      fallid = self.form.get('fallid')
    else:
      self.last_error_message = "Keine ID fuer den Fall erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    fall = Fall(int(fallid))    
    akte = Akte(fall['akte_id'])
    zustaendigkeiten = fall['zustaendigkeiten']

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Beginndatum &auml;ndern',
              'ueberschrift':
              "Beginndatum f&uuml;r '%(vn)s %(na)s' &auml;ndern" % akte}

    # Fuer FORM-HIDDEN-VALUES

    hidden ={'file': 'updfall'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(updzda_t % fall)
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    if len(zustaendigkeiten) > 0:
      res.append(thzustaendigkeiten_t)
      for z in zustaendigkeiten:
        res.append(zustaendigkeiten_t % z)
    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')


class zda(Request.Request):
  """Fallakte abschliessen (Tabellen: Fall und Zuständigkeit)."""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('fallid'):
      fallid = self.form.get('fallid')
    else:
      self.last_error_message = "Keine ID fuer den Fall erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    fall = Fall(int(fallid))
    akte = Akte(fall['akte_id'])
    zustaendigkeiten = fall['zustaendigkeiten']
    zustaendigkeiten.sort('bgd', 'bgm', 'bgy')
    aktuell_zustaendig = fall['zustaendig']

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Abschlu&szlig;datum eintragen',
              'ueberschrift':
              "Abschlu&szlig;datum f&uuml;r '%(vn)s %(na)s' eintragen" % akte}

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'zdaeinf'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(thzda_t % fall)
    res.append(zdadatum_t % today())
    res.append(zustende_t % aktuell_zustaendig)
    res.append(formsubmit_t)
    res.append(liniekurz_t)
    if len(zustaendigkeiten) > 0:
      res.append(thzustaendigkeiten_t)
      for z in zustaendigkeiten:
        res.append(zustaendigkeiten_t % z)
    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')


class zdar(Request.Request):
  """Fallabschluss rückgängig machen und neue Zustaendigkeit eintragen
  (Tabellen: Fall und Zuständigkeit)."""
  
  permissions = Request.UPDATE_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('fallid'):
      fallid = self.form.get('fallid')
    else:
      self.last_error_message = "Keine ID fuer den Fall erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    fall = Fall(int(fallid))
    akte = Akte(fall['akte_id'])
    zustaendigkeiten = fall['zustaendigkeiten']
    zustaendigkeiten = fall['zustaendigkeiten']
    letzte_zustaendigkeit = zustaendigkeiten[-1]
    zustaendigkeiten.sort('bgd', 'bgm', 'bgy')

    # Headerblock, Menü u. Uberschrift für das HTML-Template

    header = {'titel': 'Abschlu&szuml;datum r&uuml;ckg&auml;gig machen',
              'ueberschrift':
              "Abschlussdatum f&uuml;r '%(vn)s %(na)s' r&uuml;ckg&auml;ngig machen" % akte}

    # Für FORM-HIDDEN-VALUES

    zustid = Zustaendigkeit().getNewId()
    hiddenid ={'name': 'zustid', 'value': zustid}
    hidden ={'file': 'zdareinf'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueneu_t % fall)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfneu_t % fall)
    res.append(formhiddenvalues_t % hidden)
    res.append(zdarzust1_t)
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'id', 
          letzte_zustaendigkeit['mit_id'])
    res.append(zdarzust2_t % today())
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(formsubmit_t)
    res.append(fuss_t)

    return string.join(res, '')


class rmakten(Request.Request):
  """Abfrageformular zum Löschen von Akten."""
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Akten und Gruppen löschen',
              'ueberschrift':
              "Akten und Gruppen löschen nach Ablauf der Aufbewahrungsfrist von %s Monaten" % config.LOESCHFRIST }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueadmin_t )
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "rmakten2")
    res.append(rmakten_t % config.LOESCHFRIST)
    res.append(formsubmitv_t % ("Löschen", "Reset"))
    res.append(fuss_t)

    return string.join(res, '')


class rmakten2(Request.Request):
  """Löscht die Akten, welche älter als die Löschfrist sind.
  Die Statistiktabellen bleiben erhalten. Die fall_id wird auf NULL gesetzt.
  """
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('frist'):
      frist = self.form.get('frist')
    else:
      self.last_error_message = "Keine Frist erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)      

    jahr = today().year
    monat = today().month
    heute = int(jahr)*12 + int(monat)
    loeschzeitm = int(heute)-int(frist)
    loeschjahr = int(loeschzeitm) / int(12)
    loeschmonat = int(loeschzeitm) - (int(loeschjahr) * int(12))

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Akten und Gruppen löschen',
              'ueberschrift':
              "Akten und Gruppen löschen nach Ablauf der Aufbewahrungsfrist von %s Monaten" % frist }

    # Fuer FORM-HIDDEN-VALUES

    hidden ={'file': 'removeakten'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menueadmin_t )
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "admin")
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % ({'value': frist, 'name': 'frist'}))
    res.append(formhiddennamevalues_t % ({'value': loeschjahr,
                                          'name': 'loeschjahr'}))
    res.append(formhiddennamevalues_t % ({'value': loeschmonat,
                                          'name': 'loeschmonat'}))
    res.append(rmakten2_t % (frist, loeschmonat, loeschjahr ))
    res.append(formsubmitv2_t % ("Ja! Löschen!"))
    res.append(fuss_t)

    return string.join(res, '')


