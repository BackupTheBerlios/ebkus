
"""Module für die Abfragen."""

import string 

from ebkus import config
from ebkus.db.sql import SQL
from ebkus.db.dbapp import Container 
from ebkus.app import Request
from ebkus.app.ebapi import Fachstatistik, FachstatistikList, Jugendhilfestatistik, JugendhilfestatistikList, TabelleList, ZustaendigkeitList, AkteList, FallList, GruppeList, Code, Feld, Mitarbeiter, today, cc, check_int_not_empty, check_str_not_empty, EBUpdateError, getQuartal, get_rm_datum
from ebkus.app.ebapih import get_codes, mksel, get_all_codes, xcountitem, xcountnlist, xcountbereich, fstat_ausgabe

from ebkus.html.templates import *


class fsabfr(Request.Request):
  """Formular für die Fachstatistikabfrage."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stellen = get_all_codes('stzei')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Fachstatistikabfrage',
              'ueberschrift': "Fachstatistikabfrage"}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuefs_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(fsabfrjahr_t % ({'file': "fsergebnis",
                                'year': '%(year)s' % today()}))
    res.append(fsabfrstelle_t)
    mksel(res, codeliste_t, stellen, 'id', self.stelle['id'])
    res.append(fsabfrtabende_t)
    res.append(formsubmitv_t %("Okay", "Reset"))
    res.append(fuss_t)

    return string.join(res, '')


class fsergebnis(Request.Request):
  """Ergebnis der Fachstatistikabfrage (Tabellen: Fachstatistik,
  FachstatistikLeistung, FachstatistikElternproblem,
  FachstatistikKindproblem)."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    try:
      year = check_int_not_empty(self.form, 'year', "Fehler beim Jahr",)
      op = check_str_not_empty(self.form, 'op', "Fehler beim Operator",)
    except EBUpdateError, e:
      return  '<HTML><BODY>' + str(e) + '</BODY></HTML>'

    if self.form.has_key('stz'):
      stz = self.form.get('stz')
    else:
      self.last_error_message = "Keine Men&uuml;auswahl erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)

    if type(stz) is type(''):
      stz = [stz]
    query_stelle = ''
    stellen_anzeige = ''
    for s in stz:
      stelle = Code(s) 
      query_stelle = query_stelle + ' or stz =' + ' %s ' % s
      stellen_anzeige = stellen_anzeige + ' %(name)s. ' % stelle

    fsl = FachstatistikList (where =  "jahr %s %s and ( %s )"
                             % (op, year, query_stelle[4:]) )

    query_anzeige = "Jahr %s %s und Stelle(n): %s" % (op, year, stellen_anzeige)

    if len(fsl) > 0:
      pass
    else:
      return  '<HTML><BODY>' + "Sorry. Keine Datensätze gefunden" + '</BODY></HTML>'

    gesamt = len(fsl)

    tabellen = TabelleList(where = "klasse = 'Fachstatistik'")
    if len(tabellen) == 1:
      fstat = tabellen[0]
      felder = fstat['felder']

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Fachstatistikergebnisse',
              'ueberschrift':
              "Fachstatistikergebnisse vom %(day)d.%(month)d.%(year)d:<BR>Stelle(n): " % today() +  " %s " %  stellen_anzeige }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuefs_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(gesamtzahl_t % (gesamt, gesamt, query_anzeige))
    ausgabe = fstat_ausgabe(res, felder, fsl, mitarbeiterliste)
    res.append(fuss_t)

    return string.join(res, '')


class jghabfr(Request.Request):
  """Formular für die Bundesjugendhilfestatistikabfrage."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stellen = get_all_codes('stzei')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Jugendhilfestatistikabfrage',
              'ueberschrift': "Jugendhilfestatistikabfrage"}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuefs_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(fsabfrjahr_t % ({'file' : 'jghergebnis',
                                'year' :  '%(year)s' % today()}))
    res.append(fsabfrstelle_t)
    mksel(res, codeliste_t, stellen, 'id', self.stelle['id'])
    res.append(fsabfrtabende_t)
    res.append(formsubmitv_t %("Okay", "Reset"))
    res.append(fuss_t)

    return string.join(res, '')


class jghergebnis(Request.Request):
  """Ergebnis der Bundesjugendhilfestatistikabfrage.
  (Tabelle: Jugendhilfestatistik)."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    try:
      year = check_int_not_empty(self.form, 'year', "Fehler beim Jahr",)
      op = check_str_not_empty(self.form, 'op', "Fehler beim Operator",)
    except EBUpdateError, e:
      return '<HTML><BODY>' + str(e) + '</BODY></HTML>'

    if self.form.has_key('stz'):
      stz = self.form.get('stz')
    else:
      return '<HTML><BODY> Keine Stelle markiert </BODY></HTML>'

    if type(stz) is type(''):
      stz = [stz]
    query_stelle = ' '
    stellen_anzeige = ' '
    for s in stz:
      stelle = Code(s) 
      query_stelle = query_stelle + ' or stz =' + ' %s ' % s
      stellen_anzeige = stellen_anzeige + ' %(name)s. ' % stelle

    jghl = JugendhilfestatistikList (where = 'ey  %s %s and ( %s )'
                                     % (op, year, query_stelle[4:]) )

    query_anzeige = 'Jahr %s %s und Stelle(n): %s' % (op, year,
                                                      stellen_anzeige)

    if len(jghl) > 0:
      pass
    else:
      return  '<HTML><BODY>' + "Sorry. Keine Datensätze gefunden" + '</BODY></HTML>'

    gesamt = len(jghl)

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Jugendhilfestatistikauswertung %(year)s' % today(),
              'ueberschrift':
              "Jugendhilfestatistikauswertung vom %(day)d.%(month)d.%(year)d.<BR>Stelle(n): " % today() +  " %s " %  stellen_anzeige }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuefs_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(gesamtzahl_t % (gesamt, gesamt, query_anzeige))
    res.append(thkategoriejgh_t % "Beendigungsgrund")
    for i in xcountitem('bgr', jghl, 'bgr'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Geschlecht")
    for i in xcountitem('gs', jghl, 'gs'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Altersgruppe")
    for i in xcountitem('ag', jghl, 'ag'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Junger Mensch lebt")
    for i in xcountitem('fs', jghl, 'fs'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Staatsangehörigkeit")
    for i in xcountitem('hke', jghl, 'hke'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Geschwisterzahl")
    for i in xcountbereich('gsa', jghl, 'gsa'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Geschwisterzahl unbekannt")
    for i in xcountitem('gsu', jghl, 'gsu'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "1. Kontaktaufnahme durch")
    for i in xcountitem('zm', jghl, 'zm'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Beratungsanlaß")
    for i in xcountitem('ba0', jghl, 'ba0'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    for i in xcountitem('ba1', jghl, 'ba1'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    for i in xcountitem('ba2', jghl, 'ba2'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    for i in xcountitem('ba3', jghl, 'ba3'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    for i in xcountitem('ba4', jghl, 'ba4'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    for i in xcountitem('ba5', jghl, 'ba5'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    for i in xcountitem('ba6', jghl, 'ba6'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    for i in xcountitem('ba7', jghl, 'ba7'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    for i in xcountitem('ba8', jghl, 'ba8'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    for i in xcountitem('ba9', jghl, 'ba9'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Beratungsschwerpunkt")
    for i in xcountitem('schw', jghl, 'schw'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Beratung setzt ein bei dem jungen Menschen")
    for i in xcountitem('fbe0', jghl, 'fbe0'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Beratung setzt ein bei den Eltern")
    for i in xcountitem('fbe1', jghl, 'fbe1'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Beratung setzt ein in der Familie")
    for i in xcountitem('fbe2', jghl, 'fbe2'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Beratung setzt ein im sozialen Umfeld")
    for i in xcountitem('fbe3', jghl, 'fbe3'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(thkategoriejgh_t % "Mitarbeiter")
    for i in xcountnlist(mitarbeiterliste, jghl, 'mit_id'):
      res.append(item_t % (i[0],  i[1], i[2]) )
    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')


class formabfr2(Request.Request):
  """Suchformular (Tabellen: Fall, Akte, Zuständigkeit)."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stellen = get_all_codes('stzei')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Suche alle Beratungen ab Fallnummer',
              'ueberschrift': "Suche alle Beratungen ab Fallnummer" }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "abfr2")
    res.append(stz_t)
    mksel(res, codeliste_t, stellen, 'id', self.stelle['id'])
    res.append(suchefallnummer_t)
    res.append(formsubmitv_t %("Okay", "Reset"))
    res.append(fuss_t)

    return string.join(res, '')


class abfr1(Request.Request):
  """Ergebnis der Abfrage aller Klienten
  (Tabellen: Fall, Akte, Zuständigkeit)."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    mitarbeiter = self.mitarbeiter
    stelle = self.stelle
    
    try:
      o = check_str_not_empty(self.form, 'o', "Kein Operator")
      ed = check_int_not_empty(self.form, 'ed', "Kein Datum", 0)
    except EBUpdateError, e:
      return  '<HTML><BODY>' + str(e) + '</BODY></HTML>'

    if o == 'laufend':
      ber = 'Laufende'
      op = '='
    elif o == 'alle':
      ber = 'Alle'
      op = '>='
    elif o == 'zda':
      ber = 'Abgeschlossene'
      op = '>'

    # Headerblock, Menue u. Überschrift fuer das HTML-Template

    header = {'titel': '%s Beratungen' %ber,
              'ueberschrift': "%s Beratungen an der %s bis zum %s"
              % (ber, stelle['name'], today())}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(thabfr1_t)
    if mitarbeiter['benr__code'] == 'bearb':
      zustaendigkeiten = ZustaendigkeitList(where = 'ed %s %s and mit_id = %s'
                                            % (op, ed, mitarbeiter['id'] ))
      zustaendigkeiten.sort('mit_id__na', 'fall_id__akte_id__na', 
                            'fall_id__akte_id__vn')
      for z in zustaendigkeiten:
        if z['fall_id__akte_id__stzak'] == stelle['id']:
          res.append(abfr1_t % z)

    elif mitarbeiter['benr__code'] == 'verw':
      zustaendigkeiten = ZustaendigkeitList(where = 'ed %s %s' %(op, ed)
                                            , order = 'id')
      zustaendigkeiten.sort('fall_id__id')
      for z in zustaendigkeiten:
        if z['fall_id__akte_id__stzak'] == stelle['id']:
          res.append(abfr1_t % z)

    elif mitarbeiter['benr__code'] == 'admin':
      zustaendigkeiten = ZustaendigkeitList(where = 'ed %s %s' %(op, ed)
                                            , order = 'id')
      zustaendigkeiten.sort('fall_id__id')
      for z in zustaendigkeiten:
        if z['fall_id__akte_id__stzak'] == stelle['id']:
          res.append(abfr1_t % z)

    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')



class abfr2(Request.Request):
  """Ergebnis der Suche in der Klienten- oder Gruppenkartei."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    mitarbeiter = self.mitarbeiter
    stelle = self.stelle

    try:
      fn = check_str_not_empty(self.form, 'expr', "Keine Fallnummer")
      stzid = check_int_not_empty(self.form, 'stz', "Kein Stellenzeichen")
    except EBUpdateError, e:
      return  '<HTML><BODY>' + str(e) + '</BODY></HTML>'

    op = '>='
    ed = 0
    if op == '=':
      ber = 'Laufende'
    elif op == '>=':
      ber = 'Alle'
    elif op == '>':
      ber = 'Abgeschlossene'

    stelle = Code(id=stzid)
    faelle = FallList(where = "fn = '%s' " % fn )
    if len(faelle) == 1:
      fall = faelle[0]
    else:
      return '<HTML><BODY>' + "Keinen oder mehrere Fälle zur Fallnummer gefunden" + '</BODY></HTML>'

    # Headerblock, Menue u. Überschrift fuer das HTML-Template

    header = {'titel': '%s Beratungen' %ber,
              'ueberschrift':
              "%s Beratungen ab Fallnummer: '%s' an der %s bis zum %s" % 
              (ber, fn, stelle['name'], today())}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(thabfr1_t)

    if mitarbeiter['benr__code'] == 'bearb':
      zustaendigkeiten = ZustaendigkeitList(where = 'ed %s %s and mit_id = %s and fall_id >= %s'
                 % (op, ed, mitarbeiter['id'], fall['id'] ))
      zustaendigkeiten.sort('mit_id__na', 'fall_id__akte_id__na', 
                            'fall_id__akte_id__vn')
      for z in zustaendigkeiten:
        if z['fall_id__akte_id__stzak'] == stelle['id']:
          res.append(abfr1_t % z)

    elif mitarbeiter['benr__code'] == 'verw':
      zustaendigkeiten = ZustaendigkeitList(where = 'ed %s %s and fall_id >= %s'
                                        % (op, ed, fall['id']) , order = 'id')
      zustaendigkeiten.sort('fall_id__id')
      for z in zustaendigkeiten:
        if z['fall_id__akte_id__stzak'] == stelle['id']:
          res.append(abfr1_t % z)

    elif mitarbeiter['benr__code'] == 'admin':
      zustaendigkeiten = ZustaendigkeitList(where = 'ed %s %s and fall_id >= %s'
                                           % (op, ed, fall['id']), order = 'id')
      zustaendigkeiten.sort('fall_id__id')
      for z in zustaendigkeiten:
        if z['fall_id__akte_id__stzak'] == stelle['id']:
          res.append(abfr1_t % z)

    res.append(tabende_t)
    res.append(fuss_t)

    return string.join(res, '')


class formabfr3(Request.Request):
  """Suchformular (Tabellen: Fall, Akte, Gruppe, Zuständigkeit)."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stellen = get_all_codes('stzei')
    stelle = self.stelle
    
    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Suche in der Kartei',
              'ueberschrift':
              "Suche in der Kartei nach Vorname oder Nachname oder Fallnummer oder Gruppe" }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "abfr3")
    res.append(stz_t)
    res.append(codelisteos_t % stelle)

    #  Bei Austausch von Akten zwischen den Stellen:
    #  mksel(res, codeliste_t, stellen, 'id', stelle['id'])

    res.append(suchwort_t)
    res.append(formsubmitv_t %("Okay", "Reset"))
    res.append(liniekurz_t)
    res.append(suchhilfe_t % stelle)
    res.append(fuss_t)

    return string.join(res, '')


class abfr3(Request.Request):
  """Ergebnis der Suche in der Klienten- oder Gruppenkartei."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    mitarbeiter = self.mitarbeiter
    stelle = self.stelle

    try:
      expr = check_str_not_empty(self.form, 'expr', "Kein Suchausdruck")
      stzid = check_int_not_empty(self.form, 'stz', "Kein Stellenzeichen")
      table = check_str_not_empty(self.form, 'table', "Keine Suchklasse")
    except EBUpdateError, e:
      return  '<HTML><BODY>' + str(e) + '</BODY></HTML>'

    stzid = stelle['id']

    expr1 = "%" + expr + "%"
    if table == "akte":
      akten = AkteList(where = "stzak = %s and (vn %s '%s' or na %s '%s')"
                       % (stzid, config.CLIKE, expr1, config.CLIKE, expr1),
                       order = 'na,vn')

    elif table == "fall":
      faelle = FallList(where = "fn %s '%s'" % (config.CLIKE, expr1),
                        order = 'fn' )

    elif table == "bezugsperson":
      bezugspersonen = BezugspersonList(where = "vn %s '%s' or na %s '%s'"
                                        % (config.CLIKE, expr1, config.CLIKE,
                                           expr1),
                                        order = 'na,vn')

    elif table == 'gruppe':
      gruppen = GruppeList(where = "stz = '%s' and name %s '%s' or thema %s '%s'"
                        % (stzid, config.CLIKE, expr1, config.CLIKE, expr1))

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Resultat der Karteiabfrage',
              'ueberschrift': "Resultat der Karteiabfrage nach '%s'" % expr}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    if table == "akte" and mitarbeiter['benr__code'] == 'bearb':
      res.append(thabfr1_t)
      for a in akten:
        letzter_fall = a['letzter_fall']
        zustaendigkeit = letzter_fall['zuletzt_zustaendig']
        if zustaendigkeit['mit_id'] == mitarbeiter['id']:
          res.append(abfr1_t % zustaendigkeit)
      res.append(tabende_t)

    elif table == "akte" and (mitarbeiter['benr__code'] == 'verw' or mitarbeiter['benr__code'] == 'admin'):
      res.append(thabfr1_t)
      for a in akten:
        letzter_fall = a['letzter_fall']
        zustaendigkeit = letzter_fall['zuletzt_zustaendig']
        if zustaendigkeit['fall_id__akte_id__stzak'] == stzid:
          res.append(abfr1_t % zustaendigkeit)
      res.append(tabende_t)

    elif table == "bezugsperson" and mitarbeiter['benr__code'] == 'bearb':
      res.append(thabfr1_t)
      for b in bezugspersonen:
        if b['akte_id__stzak'] == stzid:
          letzter_fall = b['akte_id__letzter_fall']
          zustaendigkeit = letzter_fall['zuletzt_zustaendig']
          if zustaendigkeit['mit_id'] == mitarbeiter['id']:
            res.append(abfr3a_t % zustaendigkeit)
            res.append(abfr3b_t % b)
            res.append(abfr3c_t % zustaendigkeit)
      res.append(tabende_t)

    elif table == "bezugsperson" and (mitarbeiter['benr__code'] == 'verw' or mitarbeiter['benr__code'] == 'admin'):
      res.append(thabfr1_t)
      for b in bezugspersonen:
        if b['akte_id__stzak'] == stzid:
          letzter_fall = b['akte_id__letzter_fall']
          zustaendigkeit = letzter_fall['zuletzt_zustaendig']
          if zustaendigkeit['fall_id__akte_id__stzak'] == stzid:
            res.append(abfr3a_t % zustaendigkeit)
            res.append(abfr3b_t % b)
            res.append(abfr3c_t % zustaendigkeit)
      res.append(tabende_t)

    elif table == "fall" and mitarbeiter['benr__code'] == 'bearb':
      res.append(thabfr1_t)
      for f in faelle:
        if f['akte_id__stzak'] == stzid:
          zustaendigkeit = f['zuletzt_zustaendig']
          if zustaendigkeit['mit_id'] == mitarbeiter['id']:
            res.append(abfr1_t % zustaendigkeit)
      res.append(tabende_t)

    elif table == "fall" and (mitarbeiter['benr__code'] == 'verw' or mitarbeiter['benr__code'] == 'admin'):
      res.append(thabfr1_t)
      for f in faelle:
        if f['akte_id__stzak'] == stzid:
          zustaendigkeit = f['zuletzt_zustaendig']
          if zustaendigkeit['fall_id__akte_id__stzak'] == stzid:
            res.append(abfr1_t % zustaendigkeit)
      res.append(tabende_t)

    elif table == "gruppe" and mitarbeiter['benr__code'] == 'bearb':
      res.append(thabfrgr_t)
      for g in gruppen:
        mitgruppen = mitarbeiter['gruppen']
        for m in mitgruppen:
          if m['gruppe_id'] == g['id']:
            res.append(abfrgr_t % g)
      res.append(tabende_t)

    elif table == "gruppe" and (mitarbeiter['benr__code'] == 'verw' or mitarbeiter['benr__code'] == 'admin'):
      res.append(thabfrgr_t)
      for g in gruppen:
        if g['stz'] == stzid:
          res.append(abfrgr_t % g)
      res.append(tabende_t)

    res.append(fuss_t)

    return string.join(res, '')


class formabfr4(Request.Request):
  """Suchformular für die Anzahl der Neumeldungen und zdA's pro Jahr."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stelle = self.stelle
    
    # Headerblock, Menü u. Überschrift für das HTML-Template

    header = {'titel': 'Neumeldezahl',
              'ueberschrift':
              "Neumelde- u. Abschlusszahl (z.d.A.) an der %s"
              % stelle['name'] + " im Jahr X pro Monat und Quartal " }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "abfr4")
    res.append(thformabfr5_t % ('Neumelde- und Abschlusszahl',today().year) )
    res.append(formsubmitv_t %("Okay","Reset"))
    res.append(formabfr5_2_t)
    res.append(fuss_t)

    return string.join(res, '')


class abfr4(Request.Request):
  """Anzahl der Neumeldungen u. Abschlüsse pro Jahr und Quartal."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stelle = self.stelle

    try:
      jahr = check_int_not_empty(self.form, "jahr", "Keine Jahreszahl eingeben")
    except EBUpdateError, e:
      return  '<HTML><BODY>' + str(e) + '</BODY></HTML>'

    loeschfrist = get_rm_datum()
    lauf_jahr = '%(year)d' % today()
    if jahr > loeschfrist['loeschjahr'] and jahr <= int(lauf_jahr) :
      pass
    else:
      self.last_error_message = "Die Jahreszahl ist kleiner als das eingestellte Löschdatum (Jahr) oder grösser als das laufende Jahr"
      return self.EBKuSError(REQUEST, RESPONSE)

    neumeldungen = FallList(where = 'bgy = %s' % jahr
                            + ' and akte_id__stzak = %d' % stelle['id'],
                            order = 'bgm' ) 
    zdaliste = JugendhilfestatistikList(where = 'ey = %s' % jahr
                            + ' and stz = %d' % stelle['id'],
                            order = 'em' ) 

    neul = []
    zdal = []
    for n in neumeldungen:
      neul.append(n['bgm'])
    for z in zdaliste:
      zdal.append(z['em'])

    # Headerblock, Menü u. Überschrift für das HTML-Template

    header = {'titel': 'Neumeldezahl',
              'ueberschrift':
              "Neumelde- (anhand der Fallliste) u. Abschlusszahl (anhand der Bundesstatistik) an der %s" % stelle['name']
              + " im Jahr %s pro Monat" % jahr }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(thabfr4_t)

    # Quartalszahlen pro Jahr 

    quartal1_neu = 0
    quartal1_zda = 0
    quartal2_neu = 0
    quartal2_zda = 0
    quartal3_neu = 0
    quartal3_zda = 0
    quartal4_neu = 0
    quartal4_zda = 0
    i = 1
    while i < 13:
      neumeldezahl = neul.count(i)
      zdazahl = zdal.count(i)
      if i < 4:
        quartal1_neu = quartal1_neu + neumeldezahl
        quartal1_zda = quartal1_zda + zdazahl
      if i > 3 and i < 7:
        quartal2_neu = quartal2_neu + neumeldezahl
        quartal2_zda = quartal2_zda + zdazahl
      if i > 6 and i < 10:
        quartal3_neu = quartal3_neu + neumeldezahl
        quartal3_zda = quartal3_zda + zdazahl
      if i > 9 and i < 13:
        quartal4_neu = quartal4_neu + neumeldezahl
        quartal4_zda = quartal4_zda + zdazahl
      res.append(abfr4_t % (i, neumeldezahl, zdazahl) )
      i = i + 1

    res.append(abfr4ges_t % (quartal1_neu, quartal1_zda,quartal2_neu,
                             quartal2_zda,quartal3_neu, quartal3_zda,
                             quartal4_neu, quartal4_zda, len(neul), len(zdal)) )
    res.append(fuss_t)

    return string.join(res, '')


class formabfr5(Request.Request):
  """Suchformular: Klientenzahl pro Mitarbeiter u. Jahr."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    # Headerblock, Menü u. Überschrift für das HTML-Template

    header = {'titel': 'Klientenzahl pro Mitarbeiter',
              'ueberschrift':
              "Klientenzahl pro Mitarbeiter der %s" % self.stelle['name']
              + " f&uuml;r das Jahr .... "}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "abfr5")
    res.append(thformabfr5_t % ('Klientenzahl pro Mitarbeiter', today().year) )
    res.append(formsubmitv_t % ("Okay","Reset") )
    res.append(formabfr5_2_t)
    res.append(fuss_t)

    return string.join(res, '')


class abfr5(Request.Request):
  """Klientenzahl pro Mitarbeiter u. Jahr."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stelle = self.stelle
    try:
      jahr = check_int_not_empty(self.form, "jahr", "Keine Jahreszahl eingeben")
    except EBUpdateError, e:
      return  '<HTML><BODY>' + str(e) + '</BODY></HTML>'
    loeschfrist = get_rm_datum()
    lauf_jahr = '%(year)d' % today()
    if jahr > loeschfrist['loeschjahr'] or jahr <= int(lauf_jahr):
      pass
    else:
      self.last_error_message = "Die Jahreszahl ist kleiner als das eingestellte Löschdatum (Jahr) oder grösser als das laufende Jahr"
      return self.EBKuSError(REQUEST, RESPONSE)

    # Headerblock, Menü u. Überschrift für das HTML-Template

    header = {'titel': 'Klientenzahl pro Mitarbeiter',
              'ueberschrift':
              "Klientenzahl pro Mitarbeiter der %s" % stelle['name']
              + " f&uuml;r %s anhand der Zuständigkeitsliste" % jahr}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(thabfr5_t % jahr)

    a = 0
    b = 0
    c = 0
    for m in mitarbeiterliste:
      neuel = ZustaendigkeitList(where = 'bgy = %s' % jahr
                                 + ' and mit_id = %d ' %m['id'])
      laufendl = ZustaendigkeitList(where = 'ey = 0 and bgy <= %s' % jahr
                                   + ' and bgy > 1980 and mit_id = %d ' %m['id']) 
      abgeschl = ZustaendigkeitList(where = 'ey = %s' % jahr
                                     + ' and mit_id = %d ' %m['id'])
      res.append(abfr5_t % (m['na'], len(neuel), 
                            len(laufendl), len(abgeschl)) )
      a = a + len(neuel)
      b = b + len(laufendl)
      c = c + len(abgeschl)

    res.append(abfr5ges_t % (a, b, c))
    res.append(fuss_t)

    return string.join(res, '')


class formabfr6(Request.Request):
  """Auswahl von Kategorie(n) für die Fachstatistikabfrage."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    if self.form.has_key('file'):
      file = self.form['file']
    else:
      self.last_error_message = "Keine Wahl fuer Kategorie(n) erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    
    tabellen1 = TabelleList(where = "klasse = 'Fachstatistik'")
    if len(tabellen1) == 1:
      fstat = tabellen1[0]
      fsfelder = fstat['felder']
      fsfelder.sort('name')

    tabellen2 = TabelleList(where = "klasse = 'Fachstatistikleistung'")
    if len(tabellen2) == 1:
      fstatlei = tabellen2[0]
      leifelder = fstatlei['felder']
      leifelder.sort('name')

    tabellen3 = TabelleList(where = "klasse = 'Fachstatistikelternproblem'")
    if len(tabellen3) == 1:
      fstatpbe = tabellen3[0]
      pbefelder = fstatpbe['felder']
      pbefelder.sort('name')

    tabellen4 = TabelleList(where = "klasse = 'Fachstatistikkindproblem'")
    if len(tabellen4) == 1:
      fstatpbk = tabellen4[0]
      pbkfelder = fstatpbk['felder']
      pbkfelder.sort('name')

      # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    if file == 'abfrkat':
      header = {'titel': 'Statistikabfrage: Kategorienwahl',
                'ueberschrift': "Statistikabfrage: Kategorienwahl" }
    else:
      header = {'titel': 'Statistikabfrage: Kategoriewahl',
                'ueberschrift': "Statistikabfrage: Kategoriewahl" }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuefs_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)

    if file == 'abfrkat':
      res.append(formkopfv_t % "formabfr6a")
      res.append(selectmbg_t % {'name' : 'feldid', 'size' : '12'})
    else:
      res.append(formkopfv_t % "formabfr6b")
      res.append(selectbg_t % {'name' : 'feldid', 'size' : '12'})

    for f in fsfelder:
      if f.get('kat_code'):
        res.append(codelisteos_t % f)
      if f['feld'] == 'mit_id':
        res.append(codelisteos_t % {'id' : f['id'], 'name' : "Mitarbeiter" })

    if file == 'abfritem':
      for l in leifelder:
        if l.get('kat_code'):
          res.append(codelisteos_t % l)
      for e in pbefelder:
        if e.get('kat_code'):
          res.append(codelisteos_t % e)
      for k in pbkfelder:
        if k.get('kat_code'):
          res.append(codelisteos_t % k)

    res.append(selectend_t)
    res.append(formsubmitv_t % ("Okay","Reset") )
    res.append(fuss_t)

    return string.join(res, '')


class formabfr6a(Request.Request):
  """Auswahl von Items mehrerer Kategorien für die Fachstatistikabfrage."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stellen = get_all_codes('stzei')
    stelle = self.stelle
    
    if self.form.has_key('feldid'):
      feldid = self.form.get('feldid')
      if type(feldid) is type(''):
        feldid = [feldid]
        if len(feldid) == 0 :
          return "Keine Kategorie gewählt."
    else:
      self.last_error_message = "Keine Kategorie erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Statistikabfage: Itemwahl aus mehreren Kategorien',
              'ueberschrift':
              "Statistikabfage: Itemwahl aus mehreren Kategorien" }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuefs_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "abfr6a")
    res.append(thitemauswb_t % today())
    mksel(res, codeliste_t, stellen, 'id', stelle['id'])
    res.append(fsabfrtabende_t)
    res.append(itemausw_t)
    for f in feldid:
      feld = Feld(int(f))
      res.append(itemausw1_t % feld)
      if feld['feld'] == 'mit_id':
        mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'ben', user)
        res.append(itemausw2_t)
      else:
        codeliste = get_codes(feld['kat_code'])
        mksel(res, codeliste_t, codeliste)
        res.append(itemausw2_t)
    res.append(tabende_t)
    res.append(abfr6acomment_t)
    res.append(formsubmitv_t % ("Okay","Reset") )
    res.append(fuss_t)

    return string.join(res, '')


class formabfr6b(Request.Request):
  """Auswahl von Items einer Kategorie der Fachstatistik."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stelle = self.stelle
    stellen = get_all_codes('stzei')
    
    if self.form.has_key('feldid'):
      feldid = self.form.get('feldid')
      feld = Feld(int(feldid))
    else:
      self.last_error_message = "Keine Kategorie erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)      

    if feld.has_key('kat_code'):
      if feld['kat_code']:
        codeliste = get_all_codes(feld['kat_code'])

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Statistikabfrage: Auswahl von Items aus 1 Kategorie',
              'ueberschrift':
              "Statistikabfrage: Auswahl von Items aus 1 Kategorie" }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuefs_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "abfr6b")
    res.append(thitemauswb_t % today())
    mksel(res, codeliste_t, stellen, 'id', stelle['id'])
    res.append(fsabfrtabende_t)
    if feld['feld'] == 'mit_id':
      res.append(itemauswb3_t % {'name' : feld['name']} )
      for m in mitarbeiterliste:
        res.append(itemauswb_t % {'id' : m['id'], 'name' : feld['name']})
        res.append(itemauswb1_t % {'id' : m['id'], 'name' : m['na']})
    else:
      res.append(itemauswb3_t % {'name' : feld['name']} )
      for c in codeliste:
        res.append(itemauswb_t % {'id' : c['id'], 'name' : feld['name']})
        res.append(itemauswb1_t % c)
    res.append(tabende_t)
    res.append(itemauswb2_t % feld)  
    res.append(formsubmitv_t % ("Okay","Reset") )
    res.append(fuss_t)

    return string.join(res, '')


class abfr6a(Request.Request):
  """Ergebnis der Fachstatistikabfrage (formabfr6a)."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    try:
      year = check_int_not_empty(self.form, 'year', "Fehler beim Jahr",)
      year_op = check_str_not_empty(self.form, 'year_op', 
                                    "Fehler beim Vergleichsoperator",)
      stz = check_int_not_empty(self.form, 'stz',
                                "Fehler beim Stellenzeichen", -1)
    except EBUpdateError, e:
      return  '<HTML><BODY>' + str(e) + '</BODY></HTML>'


    if self.form.has_key('feldid'):
      feldid = self.form.get('feldid')
      if type(feldid) is type(''):
        feldid = [feldid]
    else:
      self.last_error_message = "Keine Kategorie erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
      
    if self.form.has_key('codeid'):
      codeid = self.form.get('codeid')

    if stz == -1:
      stelle = {'name': 'Alle Beratungsstellen'}
      query_stelle = ''
      query_anz_stelle = " und Stelle = 'alle Beratungsstellen'"
    else:
      stelle = Code(id=stz)
      query_stelle = " and stz = %s" % stz
      query_anz_stelle = " und Stelle '%(name)s' " % stelle

    query = ''
    query_anzeige = ''
    for f in feldid:
      konj = self.form.get('konj')
      feld = self.form.get('%s_feld' % f)
      op = self.form.get('%s_op' % f)
      codeid = self.form.get('%s_codeid' % f)

      if feld == 'mit_id':
        query = "%s %s %s %s " % (konj, feld, op, codeid) + query

        feldobj = Feld(int(f))
        feldname = feldobj['name']
        mitarbeiter = Mitarbeiter(int(codeid))
        if konj == 'and':
          konj = 'und'
        else: konj = 'oder'
        query_anzeige = "%s %s %s '%s' " % (konj, feldname, 
                                  op, mitarbeiter['na']) + query_anzeige
      else:
        code = Code(int(codeid))
        if code['mini'] and code['maxi']:
          mini = code['mini']
          op1 = '>'
          maxi = code['maxi']
          op2 = '<'
          query = "%s (%s %s %d and %s %s %d) " % (konj, feld, op1, mini, 
                                                   feld, op2, maxi) + query

          feldobj = Feld(int(f))
          feldname = feldobj['name']
          codename = code['name']
          if konj == 'and':
            konj = 'und'
          else: konj = 'oder'
          query_anzeige = "%s (%s %s '%d' und %s %s '%d') " % (konj, feldname, 
                               op1, mini, feldname, op2, maxi) + query_anzeige
        else:
          query = "%s %s %s %s " % (konj, feld, op, codeid) + query

          feldobj = Feld(int(f))
          feldname = feldobj['name']
          codename = code['name']
          if konj == 'and':
            konj = 'und'
          else: konj = 'oder'
          query_anzeige = "%s %s %s '%s' " % (konj, feldname, 
                                          op, codename) + query_anzeige

    if query[0] == 'a':
      query_anzeige = "(" + query_anzeige[3:] + ")" + " und Jahr %s %s %s " % (year_op, year, query_anz_stelle)
      query = query[3:]
    else:
      query_anzeige = "(" + query_anzeige[4:] + ")" + " und Jahr %s %s %s " % (year_op, year, query_anz_stelle)
      query = query[3:]

    fsl_alle = FachstatistikList(where = "jahr %s %s " % (year_op, year))
    fsl = FachstatistikList (where = '( %s ' % query
                             + ') and jahr %s %s %s' % (year_op, 
                                  year, query_stelle) )

    if len(fsl) > 0:
      pass
    else:
      self.last_error_message = "Keine Datensätze gefunden."
      return self.EBKuSError(REQUEST, RESPONSE)      

    alle = len(fsl_alle)
    gesamt = len(fsl)

    tabellen = TabelleList(where = "klasse = 'Fachstatistik'")
    if len(tabellen) == 1:
      fstat = tabellen[0]
      felder = fstat['felder']

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Fachstatistik, Abfrageergebnis',
              'ueberschrift':
              "Fachstatistikabfrageergebnis "
              + "vom %(day)d.%(month)d.%(year)d" % today() }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuefs_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(gesamtzahl_t % (gesamt, alle, query_anzeige))
    ausgabe = fstat_ausgabe(res, felder, fsl, mitarbeiterliste)
    res.append(fuss_t)

    return string.join(res, '')



class abfr6b(Request.Request):
  """Ergebnis der Fachstatistikabfrage (formabfr6b)."""
  
  permissions = Request.ABFR_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user

    try:
      year = check_int_not_empty(self.form, 'year', "Fehler beim Jahr",)
      year_op = check_str_not_empty(self.form, 'year_op', 
                                    "Fehler beim Vergleichsoperator",)
      feldid = check_int_not_empty(self.form, 'feldid', "Keine ID für das Feld")
      stz = check_int_not_empty(self.form, 'stz',
                                "Fehler beim Stellenzeichen", -1)
    except EBUpdateError, e:
      return  '<HTML><BODY>' + str(e) + '</BODY></HTML>'

    if self.form.has_key('codeid'):
      codeid = self.form.get('codeid')
      if type(codeid) is type(''):
        codeid = [codeid]
    else:
      self.last_error_message = "Keine Datensätze gefunden."
      return self.EBKuSError(REQUEST, RESPONSE)      

    if stz == -1:
      stelle = {'name': 'Alle Beratungsstellen'}
      query_stelle = ''
      query_anz_stelle = " und Stelle = 'alle Beratungsstellen'"
    else:
      stelle = Code(id=stz)
      query_stelle = " and fachstat.stz = %s " % stz
      query_anz_stelle = " und Stelle = '%(name)s' " % stelle

    feld = self.form.get('%s_feld' % feldid)
    query = ''
    query_anzeige = ''
    for c in codeid:
      konj = self.form.get('%s_konj' % c)
      op = self.form.get('%s_op' % c)

      if feld == 'le':
        query = "%s fachstatlei.%s %s %s " % (konj, feld, op, c) + query
        code = Code(int(c))
        feldobj = Feld(int(feldid))
        feldname = feldobj['name']
        codename = code['name']
        if konj == 'and':
          konj = 'und'
        else: konj = 'oder'
        query_anzeige = "%s %s %s '%s' " % (konj, feldname, 
                                          op, codename) + query_anzeige
      elif feld == 'pbe':
        query = "%s fachstatelternproblem.%s %s %s " % (konj, feld, op, c) + query
        code = Code(int(c))
        feldobj = Feld(int(feldid))
        feldname = feldobj['name']
        codename = code['name']
        if konj == 'and':
          konj = 'und'
        else: konj = 'oder'
        query_anzeige = "%s %s %s '%s' " % (konj, feldname, 
                                          op, codename) + query_anzeige

      elif feld == 'pbk':
        query = "%s fachstatkindproblem.%s %s %s " % (konj, feld, op, c) + query
        code = Code(int(c))
        feldobj = Feld(int(feldid))
        feldname = feldobj['name']
        codename = code['name']
        if konj == 'and':
          konj = 'und'
        else: konj = 'oder'
        query_anzeige = "%s %s %s '%s' " % (konj, feldname, 
                                          op, codename) + query_anzeige

      elif feld == 'mit_id':
        query = "%s %s %s %s " % (konj, feld, op, c) + query

        feldobj = Feld(int(feldid))
        feldname = feldobj['name']
        mitarbeiter = Mitarbeiter(int(c))
        if konj == 'and':
          konj = 'und'
        else: konj = 'oder'
        query_anzeige = "%s %s %s '%s' " % (konj, feldname, 
                                  op, mitarbeiter['na']) + query_anzeige
      else:
        code = Code(int(c))
        if code['mini'] != None and code['maxi'] != None:
          mini = code['mini']
          op1 = '>='
          maxi = code['maxi']
          op2 = '<='
          query = "%s (%s %s %d and %s %s %d) " % (konj, feld, op1, mini, 
                                                   feld, op2, maxi) + query

          feldobj = Feld(int(feldid))
          feldname = feldobj['name']
          codename = code['name']
          if konj == 'and':
            konj = 'und'
          else: konj = 'oder'
          query_anzeige = "%s (%s %s '%d' und %s %s '%d') " % (konj, feldname, 
                               op1, mini, feldname, op2, maxi) + query_anzeige

        else:
          query = "%s %s %s %s " % (konj, feld, op, c) + query

          feldobj = Feld(int(feldid))
          feldname = feldobj['name']
          codename = code['name']
          if konj == 'and':
            konj = 'und'
          else: konj = 'oder'
          query_anzeige = "%s %s %s '%s' " % (konj, feldname, 
                                          op, codename) + query_anzeige

    if query[0] == 'a':
      query_anzeige = "(" + query_anzeige[3:] + ")" + " und Jahr %s %s %s" % (year_op, year, query_anz_stelle)
      query = query[3:]
    else:
      query_anzeige = "(" + query_anzeige[4:] + ")" + " und Jahr %s %s %s " % (year_op, year, query_anz_stelle)
      query = query[3:]

    if feld == 'le':

    #
    # Die Abfrage muss alle Felder in der richtigen Reihenfolge enthalten !
    # Bei Änderungen der Tabelle Fachstatistik muss diese Select-Abfrage
    # immer angepasst werden !
    #
      s = SQL("""SELECT distinct fachstat.id, fachstat.mit_id, fachstat.fall_id, 
                     fachstat.fall_fn, fachstat.jahr, fachstat.stz,
                     fachstat.bz, fachstat.gs, fachstat.ag, fachstat.fs, 
                     fachstat.zm, fachstat.ep, fachstat.ka, fachstat.gr,
                     fachstat.hkm, fachstat.hkv, fachstat.bkm, fachstat.bkv,
                     fachstat.agkm, fachstat.agkv,fachstat.sd, fachstat.ba1, 
                     fachstat.ba2, fachstat.pbk, fachstat.pbe, fachstat.bg, 
                     fachstat.kat, fachstat.kkm, fachstat.kkv,
                     fachstat.kki, fachstat.kpa, fachstat.kfa, fachstat.ksoz, 
                     fachstat.kleh, fachstat.kerz, fachstat.kson, fachstat.no,
                     fachstat.no2, fachstat.no3, fachstat.zeit
         FROM fachstat, fachstatlei
         WHERE fachstat.id = fachstatlei.fstat_id %(CONDITIONS)s""")

      query = ' and (%s ' % query + ') and fachstat.jahr %s %s %s ' % (year_op, 
                                           year, query_stelle)
      fsl =  FachstatistikList().byQuery(s, CONDITIONS = query)

    elif feld == 'pbe':
  #
  # Die Abfrage muss alle Felder in der richtigen Reihenfolge enthalten !
  # Bei Änderungen der Tabelle Fachstatistik muss diese Select-Abfrage
  # immer angepasst werden !
  #
      s = SQL("""SELECT distinct fachstat.id, fachstat.mit_id, fachstat.fall_id, 
                     fachstat.fall_fn, fachstat.jahr, fachstat.stz,
                     fachstat.bz, fachstat.gs, fachstat.ag, fachstat.fs, 
                     fachstat.zm, fachstat.ep, fachstat.ka, fachstat.gr,
                     fachstat.hkm, fachstat.hkv, fachstat.bkm, fachstat.bkv,
                     fachstat.agkm, fachstat.agkv,fachstat.sd, fachstat.ba1, 
                     fachstat.ba2, fachstat.pbk, fachstat.pbe, fachstat.bg, 
                     fachstat.kat, fachstat.kkm, fachstat.kkv,
                     fachstat.kki, fachstat.kpa, fachstat.kfa, fachstat.ksoz, 
                     fachstat.kleh, fachstat.kerz, fachstat.kson, fachstat.no,
                     fachstat.no2, fachstat.no3, fachstat.zeit
         FROM fachstat, fachstatelternproblem
         WHERE fachstat.id = fachstatelternproblem.fstat_id %(CONDITIONS)s""")

      query = ' and (%s ' % query + ') and fachstat.jahr %s %s %s ' % (year_op, 
                                           year, query_stelle)
      fsl =  FachstatistikList().byQuery(s, CONDITIONS = query)

    elif feld == 'pbk':

    #
    # Die Abfrage muss alle Felder in der richtigen Reihenfolge enthalten !
    # Bei Änderungen der Tabelle Fachstatistik muss diese Select-Abfrage
    # immer angepasst werden !
    #
      s = SQL("""SELECT distinct fachstat.id, fachstat.mit_id, fachstat.fall_id, 
                     fachstat.fall_fn, fachstat.jahr, fachstat.stz,
                     fachstat.bz, fachstat.gs, fachstat.ag, fachstat.fs, 
                     fachstat.zm, fachstat.ep, fachstat.ka, fachstat.gr,
                     fachstat.hkm, fachstat.hkv, fachstat.bkm, fachstat.bkv,
                     fachstat.agkm, fachstat.agkv,fachstat.sd, fachstat.ba1, 
                     fachstat.ba2, fachstat.pbk, fachstat.pbe, fachstat.bg, 
                     fachstat.kat, fachstat.kkm, fachstat.kkv,
                     fachstat.kki, fachstat.kpa, fachstat.kfa, fachstat.ksoz, 
                     fachstat.kleh, fachstat.kerz, fachstat.kson, fachstat.no,
                     fachstat.no2, fachstat.no3, fachstat.zeit
         FROM fachstat, fachstatkindproblem
         WHERE fachstat.id = fachstatkindproblem.fstat_id %(CONDITIONS)s""")

      query = ' and (%s ' % query + ') and fachstat.jahr %s %s %s ' % (year_op, 
                                           year, query_stelle)
      fsl =  FachstatistikList().byQuery(s, CONDITIONS = query)

    else:

      fsl = FachstatistikList (where = ' (%s ' % query + ') and jahr %s %s %s ' % (year_op, year, query_stelle) )

    if len(fsl) > 0:
      pass
    else:
      return  '<HTML><BODY>' + "Sorry. Keine Datensätze gefunden" + '</BODY></HTML>'

    fsl_alle = FachstatistikList(where = "jahr %s %s " % (year_op, year))
    alle = len(fsl_alle)
    gesamt = len(fsl)

    tabellen = TabelleList(where = "klasse = 'Fachstatistik'")
    if len(tabellen) == 1:
      fstat = tabellen[0]
      felder = fstat['felder']

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Fachstatistik, Abfrageergebnis',
              'ueberschrift':
              "Fachstatistikabfrageergebnis "
              + "vom %(day)d.%(month)d.%(year)d" % today() }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuefs_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(gesamtzahl_t % (gesamt, alle, query_anzeige))
    ausgabe = fstat_ausgabe(res, felder, fsl, mitarbeiterliste)
    res.append(fuss_t)

    return string.join(res, '')





