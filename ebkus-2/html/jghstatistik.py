
"""Module für die Jugendhilfestatistik."""

import string 

from ebkus.app import Request
from ebkus.app.ebapi import Akte, Fall, Jugendhilfestatistik, Code, JugendhilfestatistikList, cc, today
from ebkus.app.ebapih import get_codes, mksel, get_all_codes
from ebkus.html.templates import *


class jghneu(Request.Request):
  """Neue Jugendhilfestatistik eintragen. (Tabelle: Jugendhilfestatistik.)"""
  
  permissions = Request.STAT_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    fallid = self.form.get('fallid')

    # Mit Fall-ID, sonst ohne Fall-ID. 
    # Pro Fall kann es nur 1 Jugendhilfestatistik geben.

    if fallid:
      fall = Fall(int(fallid))
      akte = fall['akte']
      fn = fall['fn']
      bgd = fall['bgd']
      bgm = fall['bgm']
      bgy = fall['bgy']
    else:
      fallid = None
      fn = ''
      bgd = ''
      bgm = ''
      bgy = '%(year)s' % today()

    geschwisterfaelle = get_codes('gfall')
    stellenzeichen = get_codes('stzei')
    bezirke = get_codes('rbz')
    kreise = get_codes('kr')
    gemeinde = get_codes('gm')
    gemeindeteile = get_codes('gmt')
    traeger = get_codes('traeg')
    beendigungsgruende = get_codes('bgr')
    geschlechter = get_codes('gs')
    altersgruppen = get_codes('ag')
    lebtbeipersonen = get_codes('fs')
    staatsangehoerigkeiten = get_codes('hke')
    erstekontaktaufnahmel = get_codes('zm')
    berschwerpunkte = get_codes('schw')

    # Headerblock, Menü u. Überschrift für das HTML-Template

    if fallid:
      header = {'titel': 'Neues Bundesjugendhilfestatistikformular',
                'ueberschrift':
                "Neues Bundesjugendhilfestatistikformular f&uuml;r '%(vn)s %(na)s' ausf&uuml;llen"
                % akte}
    else:
      header = {'titel': 'Neues Bundesjugendhilfestatistikformular',
                'ueberschrift':
                "Neues Bundesjugendhilfestatistikformular ausf&uuml;llen - f&uuml;r nicht in der DB eingetragenen Klienten" }

    # Für FORM-HIDDEN-VALUES

    hidden ={'file': 'jgheinf'}
    jghid = Jugendhilfestatistik().getNewId()
    hiddenid ={'name': 'jghid', 'value': jghid}
    hiddenid2 ={'name': 'stz', 'value': self.stelle['id']}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    if fallid:
      res.append(fsneumenu_t % fall)
    else:
      res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    if fallid:
      res.append(jghneuformkopf_t % ({'action': 'klkarte', 'id': fallid}))
    else:
      res.append(jghneuformkopf_t % ({'action': 'feedback', 'id': ''}))
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(formhiddennamevalues_t % hiddenid2)
    res.append(jghmitarbeiter_t)
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'ben', user)
    res.append(jghfall_t % ({'fall_fn' : fn} ))
    mksel(res,codeliste_t, geschwisterfaelle, 'name', 'Nein')
    res.append(jghbezirk_t)
    mksel(res, codeliste_t, bezirke)
    res.append(jghkreis_t)
    mksel(res, codeliste_t, kreise)
    res.append(jghgemeinde_t)
    mksel(res, codelistecode_t, gemeinde)
    res.append(jghgemeindeteil_t)
    mksel(res, codelistecode_t, gemeindeteile)
    res.append(jghtraeger_t)
    mksel(res, codeliste_t, traeger)
    #res.append(jghbeginn_t % ({'bgd': '', 'bgm': bgm , 'bgy' : bgy[:3]} ))
    res.append(jghbeginn_t % ({'bgd': '', 'bgm': bgm , 'bgy' : bgy} ))
    res.append(jghende_t % today() + firstvalueleer_t)
    mksel(res, codeliste_t, beendigungsgruende)
    res.append(jghgeschlecht_t + firstvalueleer_t)
    mksel(res, codeliste_t, geschlechter)
    res.append(jghalter_t + firstvalueleer_t)
    mksel(res, codeliste_t, altersgruppen)
    res.append(jghkindlebtbei_t + firstvalueleer_t)
    mksel(res, codeliste_t, lebtbeipersonen)
    res.append(jghstaatsangehoerigkeit_t + firstvalueleer_t)
    mksel(res, codeliste_t, staatsangehoerigkeiten)
    res.append(jghgeschwisterzahl_t % Code(cc('gsu', '1')) + firstvalueleer_t)
    mksel(res, codeliste_t, erstekontaktaufnahmel)
    res.append(jghberatungsanlass_t)
    res.append(codelisteos_t % Code(cc('ba0', '1')) )
    res.append(codelisteos_t % Code(cc('ba1', '1')) )
    res.append(codelisteos_t % Code(cc('ba2', '1')) )
    res.append(codelisteos_t % Code(cc('ba3', '1')) )
    res.append(codelisteos_t % Code(cc('ba4', '1')) )
    res.append(codelisteos_t % Code(cc('ba5', '1')) )
    res.append(codelisteos_t % Code(cc('ba6', '1')) )
    res.append(codelisteos_t % Code(cc('ba7', '1')) )
    res.append(codelisteos_t % Code(cc('ba8', '1')) )
    res.append(codelisteos_t % Code(cc('ba9', '1')) )
    res.append(jghberatungsschwerpunkt_t )
    mksel(res, codeliste_t, berschwerpunkte)
    res.append(jghansaetzekind1_t )
    res.append(radio_t % Code(cc('fbe0', '1' )) )
    res.append(jghansaetzekind2_t )
    res.append(radio_t % Code(cc('fbe0', '2')) )
    res.append(jghansaetzeeltern1_t )
    res.append(radio_t % Code(cc('fbe1', '1')) )
    res.append(jghansaetzeeltern2_t )
    res.append(radio_t % Code(cc('fbe1', '2')) )
    res.append(jghansaetzefamilie_t % Code(cc('fbe2', '1')) )
    res.append(jghansaetzeumfeld_t % Code(cc('fbe3', '1')) )
    res.append(formsubmit_t)
    res.append(fuss_t)

    return string.join(res, '')


class updjgh(Request.Request):
  """Jugendhilfestatistik ändern. (Tabelle: Jugendhilfestatistik)"""
  
  permissions = Request.STAT_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    fallid = self.form.get('fallid')
    id = self.form.get('jghid')

    # Mit Fall-ID, sonst ohne Fall-ID. 
    # Pro Fall kann es nur 1 Jugendhilfestatistik geben.

    if fallid:
      fall = Fall(int(fallid))
      akte = fall['akte']
      jghstatl = fall['jgh_statistiken']
      letzter_fall = akte['letzter_fall']
      if len(jghstatl) < 1:
        self.last_error_message = "Kein Bundesstatistikeintrag erhalten"
        return self.EBKuSError(REQUEST, RESPONSE)

      jghstat = jghstatl[0]

    elif id:
      jghstat = Jugendhilfestatistik(int(id))
      fallid = jghstat.get('fall_id')
      if fallid:
        fall = Fall(int(fallid))
        akte = fall['akte']
    else:
      self.last_error_message = "Keine Bundesstatistik-ID erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)

    geschwisterfaelle = get_codes('gfall')
    stellenzeichen = get_codes('stzei')
    bezirke = get_codes('rbz')
    kreise = get_codes('kr')
    gemeinde = get_codes('gm')
    gemeindeteile = get_codes('gmt')
    traeger = get_codes('traeg')
    beendigungsgruende = get_codes('bgr')
    geschlechter = get_codes('gs')
    altersgruppen = get_codes('ag')
    lebtbeipersonen = get_codes('fs')
    staatsangehoerigkeiten = get_codes('hke')
    erstekontaktaufnahmel = get_codes('zm')
    berschwerpunkte = get_codes('schw')
    ansaetzekind = get_codes('fbe0')
    ansaetzeeltern = get_codes('fbe1')
    ansaetzefamilie = get_codes('fbe2')
    ansaetzeumfeld = get_codes('fbe3')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    if fallid:
      header = {'titel': 'Bundesjugendhilfestatistik &auml;ndern',
                'ueberschrift':
                "Bundesjugendhilfestatistik f&uuml;r '%(vn)s %(na)s' &auml;ndern"
                % akte}
    else:
      header = {'titel': 'Bundesjugendhilfestatistik &auml;ndern',
                'ueberschrift': "Bundesjugendhilfestatistik &auml;ndern - f&uuml;r nicht in der DB eingetragenen Klienten"}

    # Fuer FORM-HIDDEN-VALUES

    hidden ={'file': 'updjgh'}
    hiddenid ={'name': 'jghid', 'value': '%(id)d' %jghstat } 
    hiddenid2 ={'name': 'stz', 'value': self.stelle['id']}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    if fallid:
      res.append(fsneumenu_t % akte['letzter_fall'])
    else:
      res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    if fallid:
      res.append(jghneuformkopf_t % ({'action': 'klkarte', 'id': fallid}))
    else:
      res.append(jghneuformkopf_t % ({'action': 'feedback', 'id': ''}) )
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)
    res.append(formhiddennamevalues_t % hiddenid2)
    res.append(jghmitarbeiter_t)
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'id', jghstat['mit_id'])
    res.append(jghfall_t % jghstat )
    mksel(res,codeliste_t, geschwisterfaelle, 'name', 'Nein')
    res.append(jghbezirk_t)
    mksel(res, codeliste_t, bezirke, 'id', jghstat['rbz'])
    res.append(jghkreis_t)
    mksel(res, codeliste_t, kreise, 'id', jghstat['kr'])
    res.append(jghgemeinde_t)
    mksel(res, codelistecode_t, gemeinde, 'id', jghstat['gm'])
    res.append(jghgemeindeteil_t)
    mksel(res, codelistecode_t, gemeindeteile, 'id', jghstat['gmt'])
    res.append(jghtraeger_t)
    mksel(res, codeliste_t, traeger, 'id', jghstat['traeg'])
    res.append(jghbeginnupd_t % jghstat)
    res.append(jghendeupd_t % jghstat)
    mksel(res, codeliste_t, beendigungsgruende, 'id', jghstat['bgr'])
    res.append(jghgeschlecht_t)
    mksel(res, codeliste_t, geschlechter, 'id', jghstat['gs'])
    res.append(jghalter_t)
    mksel(res, codeliste_t, altersgruppen, 'id', jghstat['ag'] )
    res.append(jghkindlebtbei_t )
    mksel(res, codeliste_t, lebtbeipersonen, 'id', jghstat['fs'])
    res.append(jghstaatsangehoerigkeit_t )
    mksel(res, codeliste_t, staatsangehoerigkeiten, 'id', jghstat['hke'])
  ## Geschwisterzahl sollte auch bei 'leer' moeglich. (0 ist reserviert fuer
  ## 0 Geschwister,),  wenn Zahl unbekannt ist.
    if jghstat['gsu'] == cc('gsu', '1'):
      check = 'checked'
    else:
      check = ''
    if jghstat['gsa'] == None:
      gsa = ''
    else:
      gsa = jghstat['gsa']
    res.append(jghgszahlupd_t % ({'gsa': gsa , 
                                  'gsu': cc('gsu', '1'), 'check': check }))
    mksel(res, codeliste_t, erstekontaktaufnahmel, 'id', jghstat['zm'])
    res.append(jghberatungsanlass_t)
    d = Code(cc('ba0', '1') )
    if jghstat['ba0'] == cc('ba0', '1'):
      d['sel'] = 'selected'
    else:
      d['sel'] = ''
    res.append(codeliste_t % d)
    d = Code(cc('ba1', '1') )
    if jghstat['ba1'] == cc('ba1', '1'):
      d['sel'] = 'selected'
    else:
      d['sel'] = ''
    res.append(codeliste_t % d)
    d = Code(cc('ba2', '1') )
    if jghstat['ba2'] == cc('ba2', '1'):
      d['sel'] = 'selected'
    else:
      d['sel'] = ''
    res.append(codeliste_t % d)
    d = Code(cc('ba3', '1') )
    if jghstat['ba3'] == cc('ba3', '1'):
      d['sel'] = 'selected'
    else:
      d['sel'] = ''
    res.append(codeliste_t % d)
    d = Code(cc('ba4', '1') )
    if jghstat['ba4'] == cc('ba4', '1'):
      d['sel'] = 'selected'
    else:
      d['sel'] = ''
    res.append(codeliste_t % d)
    d = Code(cc('ba5', '1') )
    if jghstat['ba5'] == cc('ba5', '1'):
      d['sel'] = 'selected'
    else:
      d['sel'] = ''
    res.append(codeliste_t % d)
    d = Code(cc('ba6', '1') )
    if jghstat['ba6'] == cc('ba6', '1'):
      d['sel'] = 'selected'
    else:
      d['sel'] = ''
    res.append(codeliste_t % d)
    d = Code(cc('ba7', '1') )
    if jghstat['ba7'] == cc('ba7', '1'):
      d['sel'] = 'selected'
    else:
      d['sel'] = ''
    res.append(codeliste_t % d)
    d = Code(cc('ba8', '1') )
    if jghstat['ba8'] == cc('ba8', '1'):
      d['sel'] = 'selected'
    else:
      d['sel'] = ''
    res.append(codeliste_t % d)
    d = Code(cc('ba9', '1') )
    if jghstat['ba9'] == cc('ba9', '1'):
      d['sel'] = 'selected'
    else:
      d['sel'] = ''
    res.append(codeliste_t % d)
    res.append(jghberatungsschwerpunkt_t)
    mksel(res, codeliste_t, berschwerpunkte, 'id', jghstat['schw'])
    res.append(jghansaetzekind1_t )
    if jghstat['fbe0'] == cc('fbe0', '1'):
      res.append(radiocheck_t % Code(cc('fbe0', '1')) )
    else:
      res.append(radio_t % Code(cc('fbe0', '1')) )
    res.append(jghansaetzekind2_t )
    if jghstat['fbe0'] == cc('fbe0', '2'):
      res.append(radiocheck_t % Code(cc('fbe0', '2')) )
    else:
      res.append(radio_t % Code(cc('fbe0', '2')) )
    res.append(jghansaetzeeltern1_t )
    if jghstat['fbe1'] == cc('fbe1', '1'):
      res.append(radiocheck_t % Code(cc('fbe1', '1')) )
    else:
      res.append(radio_t % Code(cc('fbe1', '1')) )
    res.append(jghansaetzeeltern2_t )
    if jghstat['fbe1'] == cc('fbe1', '2'):
      res.append(radiocheck_t % Code(cc('fbe1', '2')) )
    else:
      res.append(radio_t % Code(cc('fbe1', '2')) )
    res.append(jghansaetzefam_t)
    if jghstat['fbe2'] == cc('fbe2', '1'):
      res.append(radiocheck_t % Code(cc('fbe2', '1')) )
    else:
      res.append(radio_t % Code(cc('fbe2', '1')) )
    res.append(jghansaetzeumf_t )
    if jghstat['fbe3'] == cc('fbe3', '1'):
      res.append(radiocheck_t % Code(cc('fbe3', '1')) )
    else:
      res.append(radio_t % Code(cc('fbe3', '1')) )
    res.append(jghupdende_t)
    res.append(formsubmit_t)
    res.append(fuss_t)

    return string.join(res, '')


class updjghausw(Request.Request):
  """Auswahl der Jugendhilfestatistik zum Ändern.
  (Tabelle: Jugendhilfestatistik)"""
  
  permissions = Request.STAT_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    stelle = self.stelle
    stellenzeichen = get_all_codes('stzei')
    fallid = self.form.get('fallid')
    mitarbeiter = self.mitarbeiter

    if fallid:
      jgh = JugendhilfestatistikList(where = 'fall_id = %s and mit_id = %s and stz = %s'
                                     % (fallid, mitarbeiter['id'], stelle['id']),
                               order = 'ey,fall_fn')
      if len(jgh) != 1:
        return '<HTML><BODY>' + "%s Jugendhilfestatistik(en) f&uuml; diesen Fall erhalten" % len(jgh) + '</BODY></HTML>'

      fall = Fall(int(fallid))
      akte = Akte(fall['akte_id'])
      letzter_fall = akte['letzter_fall']

    else:
      if mitarbeiter['benr'] == cc('benr','bearb'):
        jgh = JugendhilfestatistikList(where = 'mit_id = %s and stz = %s' 
                               % (mitarbeiter['id'], stelle['id']),
                               order = 'ey,fall_fn')
      elif mitarbeiter['benr'] == cc('benr','verw'):
        jgh = JugendhilfestatistikList(where = 'stz = %s' % (stelle['id']), order = 'ey,fall_fn')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    if fallid:
      header = {'titel': 'Jugendhilfestatistikformular zum &Auml;ndern ausw&auml;hlen',
                'ueberschrift':
                "Jugendhilfestatistikformular f&uuml;r Fallnr.<em> '%(fn)s',</em> Klient <em> '%(akte_id__vn)s, %(akte_id__na)s'</em> zum &Auml;ndern ausw&auml;hlen"
                % fall}
    else:
       header = {'titel': 'Jugendhilfestatistikformular zum &Auml;ndern ausw&auml;hlen',
                 'ueberschrift': "Jugendhilfestatistikformular zum &Auml;ndern ausw&auml;hlen"}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    if fallid:
      res.append(fsneumenu_t % letzter_fall)
    else:
      res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "updjgh")
    if fallid:
     res.append(thupdstausw_t % ("Jugendhilfestatistik", "1", "jghid") )
    else:
       res.append(thupdstausw_t % ("Jugendhilfestatistik", "16", "jghid") )
    mksel(res, updjghausw1_t, jgh )
    res.append(updstausw2_t)
    res.append(tabende_t)
    res.append(formsubmitv_t % ("Okay", "Reset") )
    res.append(fuss_t)

    return string.join(res, '')




