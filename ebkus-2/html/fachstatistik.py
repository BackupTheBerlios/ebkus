
"""Module für die Fachstatistik."""

import string 

from ebkus.app import Request
from ebkus.app.ebapi import Akte, Fall, Fachstatistik, FachstatistikList, cc, today
from ebkus.app.ebapih import get_codes, mksel, get_all_codes
from ebkus.html.templates import *


class fsneu(Request.Request):
  """Neue Fachstatistik eintragen. (Tabelle: Fachstatistik)"""
  
  permissions = Request.STAT_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    fallid = self.form.get('fallid')

    # Mit Fall-ID oder ohne Fall-ID. Ausserdem: Es können pro Fall
    # mehrere Fachstatistiken (genau 1 pro Jahr) vorhanden sein.

    if fallid:

      fall = Fall(int(fallid))
      anmeldungl = fall['anmeldung']
      akte = fall['akte']
      letzter_fall = akte['letzter_fall']
      leistungen = fall['leistungen']  
      jahr = '%(year)s' % today()
      vorjahr = int(jahr) - 1
      fstatliste = FachstatistikList(where = 'fall_id = %(id)d' % fall
                                     + " and jahr = %d" % vorjahr, 
                                     order = 'jahr')
      if len(fstatliste) >= 1:
        fstatvorjahr = fstatliste[-1]
        fsleistungen = fstatvorjahr['leistungen']
        fskindprobleme = fstatvorjahr['fachstatkindprobleme']
        fselternprobleme = fstatvorjahr['fachstatelternprobleme']
      else:
        fstatvorjahr = None
    else:
      fallid = None

    stellenzeichen = get_codes('stzei')
    regionen = get_codes('fsbz')
    geschlechter = get_codes('gs')
    altersgruppen = get_codes('fsag')
    altersgruppeneltern = get_codes('fsagel')
    familienarten = get_codes('fsfs')
    zugangsarten = get_codes('fszm')
    psychotherfahrungen = get_codes('fsep')
    geschwisterreihel = get_codes('fsgr')
    herkunftelternl = get_codes('fshe')
    berufelternl = get_codes('fsbe')
    finanzdruckl = get_codes('fssd')
    beratungsanlaesse = get_codes('fsba')
    problembereicheeltern = get_codes('fspbe')
    problembereichekinder = get_codes('fspbk')
    massnahmen = get_codes('fsle')
    abschlussl = get_codes('fsbg')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    if fallid and fstatvorjahr:
      header = {'titel': 'Fachstatistik aus dem Vorjahr ',
                'ueberschrift':
                "Fachstatistikformular aus dem Vorjahr, %d, "
                % vorjahr + " ins neue Jahr &uuml;bernehmen - Klient: %(vn)s %(na)s"
                % akte }
    else:
      if fallid:
        header = {'titel': 'Neues Fachstatistikformular',
                  'ueberschrift':
                  "Neues Fachstatistikformular f&uuml;r '%(vn)s %(na)s' ausf&uuml;llen"
                  % akte}
      else:
        header = {'titel': 'Neues Fachstatistikformular',
                  'ueberschrift':
                  "Neues Fachstatistikformular ausf&uuml;llen - <B>f&uuml;r nicht in der DB eingetragenen Klienten</B>" }

    # Fuer FORM-HIDDEN-VALUES

    hidden ={'file': 'fseinf'}
    fsid = Fachstatistik().getNewId()
    hiddenid ={'name': 'fsid', 'value': fsid}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    if fallid:
      res.append(fsneumenu_t %   letzter_fall + "<base font=2>")
    else:
      res.append(menuemin_t + "<base font=2>")
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    if fallid:
      res.append(fsneuformkopf_t % "klkarte")
    else:
      res.append(fsneuformkopf_t % "feedback")
    res.append(formhiddenvalues_t % hidden)
    res.append(formhiddennamevalues_t % hiddenid)

    if fallid:
      res.append(fsfallnummer_t % fall)
    else:
      res.append(fsfallnummer_t % ({'fn' : '', 'id': ''}))

    # Fachstatistik aus dem Vorjahr zur Übernahme

    if fallid and fstatvorjahr:
      mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'id', fstatvorjahr['mit_id'])
      res.append(fsstelle_t)
      mksel(res, codelistecode_t, stellenzeichen, 'id', fstatvorjahr['stz'])
      res.append(fsjahr_t %  today() ) 
      res.append(fsregion_t)
      mksel(res, codelistecode_t, regionen, 'id', fstatvorjahr['bz'])
      res.append(fsgeschlecht_t)
      mksel(res, codeliste_t, geschlechter, 'id', fstatvorjahr['gs'])
      res.append(fsaltersgruppe_t)
      mksel(res, codeliste_t, altersgruppen, 'id', fstatvorjahr['ag'])
      res.append(fsgeschwisterreihe_t)
      mksel(res, codeliste_t, geschwisterreihel, 'id', fstatvorjahr['gr'])
      if fstatvorjahr['ka'] == None:
        ka = ''
      else:
        ka = fstatvorjahr['ka']
      res.append(fskinderzahl_t % ka)
      res.append(fsfamilienstatus_t)
      mksel(res, codeliste_t, familienarten, 'id', fstatvorjahr['fs'])
      res.append(fszugangsmodus_t)
      mksel(res, codeliste_t, zugangsarten, 'id', fstatvorjahr['zm'])
      res.append(fspsychotherfahrung_t)
      mksel(res, codeliste_t, psychotherfahrungen, 'id', fstatvorjahr['ep'])
      res.append(fsfinanzdruck_t)
      mksel(res, codeliste_t, finanzdruckl, 'id', fstatvorjahr['sd'])
      res.append(fsberufmutter_t)
      mksel(res, codeliste_t, berufelternl, 'id', fstatvorjahr['bkm'])
      res.append(fsberufvater_t)
      mksel(res, codeliste_t, berufelternl, 'id', fstatvorjahr['bkv'])
      res.append(fsherkunftmutter_t)
      mksel(res, codeliste_t, herkunftelternl, 'id', fstatvorjahr['hkm'])
      res.append(fsherkunftvater_t)
      mksel(res, codeliste_t, herkunftelternl, 'id', fstatvorjahr['hkv'])
      res.append(fsaltermutter_t)
      mksel(res, codeliste_t, altersgruppeneltern, 'id', fstatvorjahr['agkm'])
      res.append(fsaltervater_t)
      mksel(res, codeliste_t, altersgruppeneltern, 'id', fstatvorjahr['agkv'])
      res.append(fsberatungsanlass1_t)
      mksel(res, codeliste_t, beratungsanlaesse, 'id', fstatvorjahr['ba1'])
      res.append(fsberatungsanlass2_t)
      mksel(res, codeliste_t, beratungsanlaesse, 'id', fstatvorjahr['ba2'])
      res.append(fsproblemkind_t)
      mksel(res, codeliste_t, problembereichekinder, 'id', fstatvorjahr['pbk'])
      res.append(fsproblemeltern_t)
      mksel(res, codeliste_t, problembereicheeltern, 'id', fstatvorjahr['pbe'])
      res.append(fsproblemspektrumkind_t)
      pbkids = []
      for f in fskindprobleme:
        pbkids.append(f['pbk'])
      mksel(res, codeliste_t, problembereichekinder, 'id', pbkids)
      res.append(fsproblemkindnot_t % fstatvorjahr['no2']) ##
      res.append(fsproblemspektrumeltern_t)
      pbeids = []
      for f in fselternprobleme:
        pbeids.append(f['pbe'])
      mksel(res, codeliste_t, problembereicheeltern, 'id', pbeids)
      res.append(fsproblemelternnot_t % fstatvorjahr['no3']) ##
      res.append(fsmassnahmen_t)
      fsleiids = []
      for f in fsleistungen:
        fsleiids.append(f['le'])
      mksel(res, codeliste_t, massnahmen, 'id', fsleiids)
      #  print 'ARGS:', ( codeliste_t, massnahmen, 'id', fsleistungen.getIds())

      res.append(fszahlkontakte_t % Fachstatistik() )
      mksel(res, codeliste_t, abschlussl)
      res.append(fsupdnotizsubmit_t % fstatvorjahr )

    else:

      # Fachstatistik, leere Karte, u.U. mit Werten aus der Akte, falls
      # fallid vorhanden

      mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'ben', user)

      if fallid:
        res.append(fsstelle_t % fall)
        mksel(res, codelistecode_t, stellenzeichen, 'id', fall['akte_id__stzak'])
      else:
        res.append(fsstelle_t)
        mksel(res, codelistecode_t, stellenzeichen, 'id', self.stelle['id'])

      res.append(fsjahr_t % today())
      res.append(fsregion_t + firstvalueleer_t)
      mksel(res, codeliste_t, regionen)
      res.append(fsgeschlecht_t + firstvalueleer_t)
      mksel(res, codeliste_t, geschlechter)
      res.append(fsaltersgruppe_t + firstvalueleer_t)
      mksel(res, codeliste_t, altersgruppen)
      res.append(fsgeschwisterreihe_t + firstvalueleer_t)
      mksel(res, codeliste_t, geschwisterreihel)
      res.append(fskinderzahl_t % '')
      res.append(fsfamilienstatus_t + firstvalueleer_t)
      for f in familienarten:
        if fallid and fall['akte_id__fs'] == f['id']:
          f['sel'] = 'selected'
        else:
          f['sel'] = ''
        res.append(codeliste_t % f)
      res.append(fszugangsmodus_t + firstvalueleer_t)
      mksel(res, codeliste_t, zugangsarten)
      res.append(fspsychotherfahrung_t + firstvalueleer_t)
      mksel(res, codeliste_t, psychotherfahrungen)
      res.append(fsfinanzdruck_t + firstvalueleer_t)
      mksel(res, codeliste_t, finanzdruckl)
      res.append(fsberufmutter_t + firstvalueleer_t)
      mksel(res, codeliste_t, berufelternl)
      res.append(fsberufvater_t + firstvalueleer_t)
      mksel(res, codeliste_t, berufelternl)
      res.append(fsherkunftmutter_t + firstvalueleer_t)
      mksel(res, codeliste_t, herkunftelternl)
      res.append(fsherkunftvater_t + firstvalueleer_t)
      mksel(res, codeliste_t, herkunftelternl)
      res.append(fsaltermutter_t + firstvalueleer_t)
      mksel(res, codeliste_t, altersgruppeneltern)
      res.append(fsaltervater_t + firstvalueleer_t)
      mksel(res, codeliste_t, altersgruppeneltern)
      res.append(fsberatungsanlass1_t + firstvalueleer_t)
      mksel(res, codeliste_t, beratungsanlaesse)
      res.append(fsberatungsanlass2_t + firstvalueleer_t)
      mksel(res, codeliste_t, beratungsanlaesse)
      res.append(fsproblemkind_t + firstvalueleer_t)
      mksel(res, codeliste_t, problembereichekinder)
      res.append(fsproblemeltern_t + firstvalueleer_t)
      mksel(res, codeliste_t, problembereicheeltern)
      res.append(fsproblemspektrumkind_t )
      mksel(res, codeliste_t, problembereichekinder)
      res.append(fsproblemkindnot_t % '')
      res.append(fsproblemspektrumeltern_t )
      mksel(res, codeliste_t, problembereicheeltern)
      res.append(fsproblemelternnot_t % '')
      res.append(fsmassnahmen_t)
      mksel(res, codeliste_t, massnahmen)
      res.append(fszahlkontakte_t  + firstvalueleer_t)
      mksel(res, codeliste_t, abschlussl)
      res.append(fsnotizsubmit_t)
    res.append(fuss_t)

    return string.join(res, '')


class updfs(Request.Request):
  """Fachstatistik ändern. (Tabelle: Fachstatistik)"""
  
  permissions = Request.STAT_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    if self.form.has_key('fsid'):
      id = self.form.get('fsid')
    else:
      self.last_error_message = "Keine ID für die Fachstatistik erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)
    fstat = Fachstatistik(int(id))
    fsleistungen = fstat['leistungen']
    fskindprobleme = fstat['fachstatkindprobleme']
    fselternprobleme = fstat['fachstatelternprobleme']
    fallid = fstat.get('fall_id')

    # Mit Fall-ID oder ohne Fall-ID. Ausserdem: Es können pro Fall
    # mehrere Fachstatistiken (genau 1 pro Jahr) vorhanden sein.

    if fallid:
      fall = Fall(int(fstat['fall_id']))
      akte = fall['akte']

    stellenzeichen = get_codes('stzei')
    regionen = get_codes('fsbz')
    geschlechter = get_codes('gs')
    altersgruppen = get_codes('fsag')
    altersgruppeneltern = get_codes('fsagel')
    familienarten = get_codes('fsfs')
    zugangsarten = get_codes('fszm')
    psychotherfahrungen = get_codes('fsep')
    geschwisterreihel = get_codes('fsgr')
    herkunftelternl = get_codes('fshe')
    berufelternl = get_codes('fsbe')
    finanzdruckl = get_codes('fssd')
    beratungsanlaesse = get_codes('fsba')
    problembereicheeltern = get_codes('fspbe')
    problembereichekinder = get_codes('fspbk')
    massnahmen = get_codes('fsle')
    abschlussl = get_codes('fsbg')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    if fallid:
      header = {'titel': 'Fachstatistik &auml;ndern', 'ueberschrift': "Fachstatistik f&uuml;r '%(vn)s %(na)s' &auml;ndern" % akte}
    else:
      header = {'titel': 'Fachstatistik &auml;ndern',
                'ueberschrift':
                "Fachstatistik &auml;ndern - f&uuml;r nicht in der DB eingetragenen Klienten" }

    # Fuer FORM-HIDDEN-VALUES

    hidden ={'file': 'updfs'}

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    if fallid:
      res.append(fsneumenu_t % fall)
    else:
      res.append(menuemin_t )
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    if fallid:
      res.append(fsneuformkopf_t % "klkarte")
    else:
      res.append(fsneuformkopf_t % "feedback")
    res.append(formhiddenvalues_t % hidden)
    res.append(fsupdfallnummer_t % fstat)
    mksel(res, mitarbeiterliste_t, mitarbeiterliste, 'id', fstat['mit_id'])
    res.append(fsstelle_t % fstat)
    mksel(res, codelistecode_t, stellenzeichen, 'id', fstat['stz'])
    res.append(fsjahr_t % ({'year' : fstat['jahr']}))
    res.append(fsregion_t)
    mksel(res, codeliste_t, regionen, 'id', fstat['bz'])
    res.append(fsgeschlecht_t)
    mksel(res, codeliste_t, geschlechter, 'id', fstat['gs'])
    res.append(fsaltersgruppe_t)
    mksel(res, codeliste_t, altersgruppen, 'id', fstat['ag'])
    res.append(fsgeschwisterreihe_t)
    mksel(res, codeliste_t, geschwisterreihel, 'id', fstat['gr'])
    if fstat['ka'] == None:
      ka = ''
    else:
      ka = fstat['ka']
    res.append(fskinderzahl_t % ka)
    res.append(fsfamilienstatus_t)
    mksel(res, codeliste_t, familienarten, 'id', fstat['fs'])
    res.append(fszugangsmodus_t)
    mksel(res, codeliste_t, zugangsarten, 'id', fstat['zm'])
    res.append(fspsychotherfahrung_t)
    mksel(res, codeliste_t, psychotherfahrungen, 'id', fstat['ep'])
    res.append(fsfinanzdruck_t)
    mksel(res, codeliste_t, finanzdruckl, 'id', fstat['sd'])
    res.append(fsberufmutter_t)
    mksel(res, codeliste_t, berufelternl, 'id', fstat['bkm'])
    res.append(fsberufvater_t)
    mksel(res, codeliste_t, berufelternl, 'id', fstat['bkv'])
    res.append(fsherkunftmutter_t)
    mksel(res, codeliste_t, herkunftelternl, 'id', fstat['hkm'])
    res.append(fsherkunftvater_t)
    mksel(res, codeliste_t, herkunftelternl, 'id', fstat['hkv'])
    res.append(fsaltermutter_t)
    mksel(res, codeliste_t, altersgruppeneltern, 'id', fstat['agkm'])
    res.append(fsaltervater_t)
    mksel(res, codeliste_t, altersgruppeneltern, 'id', fstat['agkv'])
    res.append(fsberatungsanlass1_t)
    mksel(res, codeliste_t, beratungsanlaesse, 'id', fstat['ba1'])
    res.append(fsberatungsanlass2_t)
    mksel(res, codeliste_t, beratungsanlaesse, 'id', fstat['ba2'])
    res.append(fsproblemkind_t)
    mksel(res, codeliste_t, problembereichekinder, 'id', fstat['pbk'])
    res.append(fsproblemeltern_t)
    mksel(res, codeliste_t, problembereicheeltern, 'id', fstat['pbe'])
    res.append(fsproblemspektrumkind_t)
    pbkids = []
    for f in fskindprobleme:
      pbkids.append(f['pbk'])
    mksel(res, codeliste_t, problembereichekinder, 'id', pbkids)
    res.append(fsproblemkindnot_t % fstat['no2']) 
    res.append(fsproblemspektrumeltern_t)
    pbeids = []
    for f in fselternprobleme:
      pbeids.append(f['pbe'])
    mksel(res, codeliste_t, problembereicheeltern, 'id', pbeids)
    res.append(fsproblemelternnot_t % fstat['no3']) 
    res.append(fsmassnahmen_t)
    fsleiids = []
    for f in fsleistungen:
      fsleiids.append(f['le'])
    mksel(res, codeliste_t, massnahmen, 'id', fsleiids)
    #  print 'ARGS:', ( codeliste_t, massnahmen, 'id', fsleistungen.getIds())
    res.append(fsupdzahlkontakteabschluss_t % fstat)
    mksel(res, codeliste_t, abschlussl, 'id', fstat['bg'])
    res.append(fsupdnotizsubmit_t % fstat )
    res.append(fuss_t)

    return string.join(res, '')


class updfsausw(Request.Request):
  """Wahl der Fachstatistik zum Ändern. (Tabelle: Fachstatistik)"""
  
  permissions = Request.STAT_PERM

  def processForm(self, REQUEST, RESPONSE):
    mitarbeiterliste = self.getMitarbeiterliste()
    user = self.user
    mitarbeiter = self.mitarbeiter
    stelle = self.stelle
    stellenzeichen = get_all_codes('stzei')

    # Mit Fall-ID oder ohne Fall-ID. Ausserdem: Es können pro Fall
    # mehrere Fachstatistiken (genau 1 pro Jahr) vorhanden sein.

    if self.form.has_key('fallid'):
      fallid = self.form.get('fallid')
      try: 
        fsl = FachstatistikList(where = 'fall_id = %s and mit_id = %s and stz = %s'
                                % (fallid, mitarbeiter['id'], stelle['id']),
                              order = 'jahr,fall_fn')
      except:
        return '<HTML><BODY>' + "Keine Fachstatistik vorhanden" + '</BODY></HTML>'
      fall = Fall(int(fallid))
      akte = Akte(fall['akte_id'])
      letzter_fall = akte['letzter_fall']
      
      header = {'titel': 'Fachstatistikformular zum &Auml;ndern ausw&auml;hlen',
                'ueberschrift':
                "Fachstatistikformular f&uuml;r Fallnr.<em> '%(fn)s',</em> Klient <em> '%(akte_id__vn)s, %(akte_id__na)s'</em> zum &Auml;ndern ausw&auml;hlen"
                % fall}

    else:
      if mitarbeiter['benr'] == cc('benr','bearb'):
        fsl = FachstatistikList(where = 'mit_id = %s and stz = %s' 
                                % (mitarbeiter['id'], stelle['id']),
                                order = 'jahr,fall_fn')
      elif mitarbeiter['benr'] == cc('benr','verw'):
        fsl = FachstatistikList(where = 'stz = %s' % (stelle['id']), order = 'jahr,fall_fn')

      header = {'titel': 'Fachstatistikformular zum &Auml;ndern ausw&auml;hlen',
                'ueberschrift':
                "Fachstatistikformular zum &Auml;ndern ausw&auml;hlen" }

    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    if self.form.has_key('fallid'):
      res.append(fsneumenu_t %   letzter_fall)
    else:
      res.append(menuemin_t)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(formkopfv_t % "updfs")
    if self.form.has_key('fallid'):
      res.append(thupdstausw_t % ("Fachstatistik", "5", "fsid") )
    else:
      res.append(thupdstausw_t % ("Fachstatistik", "16", "fsid") )
    mksel(res, updfsausw1_t, fsl )
    res.append(updstausw2_t)
    res.append(tabende_t)
    res.append(formsubmitv_t % ("Okay", "Reset") )
    res.append(fuss_t)

    return string.join(res, '')



