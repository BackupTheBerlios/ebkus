
"""Module für die Klientenkarte."""

import string

from ebkus.app import Request
from ebkus.app import ebupd
from ebkus.app import ebapi
from ebkus.app.ebapih import get_all_codes
from ebkus.html.templates import *


class klkarte(Request.Request):
  """Klientenkarte."""
  
  permissions = Request.KLKARTE_PERM

  def processForm(self, REQUEST, RESPONSE):
    file = self.form.get('file')

    # Fall 1 Klientenkarte direkt darstellen
    if not file or file == 'klkarte': 
      fallid = self.form.get('fallid')
      akid = self.form.get('akid')
      mitid = self.mitarbeiter['id']
      if akid: akid = int(akid)
      elif fallid: fallid = int(fallid)
      else:
        self.last_error_message = "Keine Men&uuml;auswahl erhalten"
        return self.EBKuSError(REQUEST, RESPONSE)
      return self.klkarte_display(akid, fallid, mitid)

    # Fall 2 erst einfuegen oder updaten, dann Klientenkarte darstellen
    if self.einfuege_oder_update_operationen.get(file):
      akid = self.einfuegen_oder_update(file)
      # damit Klientenkarte nicht als Ergebnis eines POST
      # dargestellt wird
      RESPONSE.redirect('klkarte?akid=%s' % akid)
      return ''

    # Fall 3 Dokumenten- Update- oder Einfuegeformular anzeigen
    # Folgende URLs haben denselben Effekt:
    # 1)  http://localhost/efb/ebs/klkarte?file=akteneu
    # 2)  http://localhost/efb/ebs/akteneu
    # Variante 1) nützlich wg. Aufruf aus menu.
    # Könnte auch mit redirect gelöst werden.

    if file == 'dokkarte':
      fallid = self.form.get('fallid')
      if fallid: fallid = int(fallid)
      else:
        self.last_error_message = "Keine Men&uuml;auswahl erhalten"
        return self.EBKuSError(REQUEST, RESPONSE)
      RESPONSE.redirect('dokkarte?fallid=%s' % fallid)
      return ''

    # Achtung, das folgende wird nicht gehen, da die
    # Auswahl der Prozedur von den Parametern abhängig
    # gemacht wurde:
#        elif file == 'updjghausw' and (fallid or akid):
#          import updjgh
#          return updjgh.updjgh(form, RESPONSE)
#        elif file == 'updjghausw' and not fallid:
#          import updjghausw
#          return updjghausw.updjghausw(form, RESPONSE)
    return self.ebkus.dispatch(file, REQUEST, RESPONSE)

  einfuege_oder_update_operationen = {
    'akteeinf': ('akid', ebapi.Akte), 
    'perseinf': ('akid', ebapi.Akte),
    'einreinf': ('akid', ebapi.Akte),
    'anmeinf': ('fallid', ebapi.Fall),
    'leisteinf': ('fallid', ebapi.Fall),
    'zusteinf': ('fallid', ebapi.Fall),
    'zdaeinf': ('fallid', ebapi.Fall),
    'updakte': ('akid', ebapi.Akte),
    'updpers': ('bpid', ebapi.Bezugsperson),
    'updeinr': ('einrid', ebapi.Einrichtungskontakt),
    'updanm': ('anmid', ebapi.Anmeldung),
    'updleist': ('leistid', ebapi.Leistung),
    'updzust': ('zustid', ebapi.Zustaendigkeit),
    'updfall': ('fallid', ebapi.Fall),
    'waufneinf': ('fallid', ebapi.Fall),
    'zdareinf': ('fallid', ebapi.Fall),
    'fseinf': ('fsid', ebapi.Fachstatistik),
    'updfs': ('fsid', ebapi.Fachstatistik),
    'jgheinf': ('jghid', ebapi.Jugendhilfestatistik),
    'updjgh': ('jghid', ebapi.Jugendhilfestatistik),
    'fseinf': ('fsid', ebapi.Fachstatistik)
    }

  def einfuegen_oder_update(self, file):
    function = getattr(ebupd, file)
    function(self.form)
    # Dies ist eine Art die Akte herauszufinden, auf die
    # sich das Einfuegen oder das Update bezog.
    # Es wäre vielleicht besser, die akid immer als
    # hidden Variable mitzuführen.
    id_name, klass = self.einfuege_oder_update_operationen.get(file)
    akid = klass(int(self.form[id_name]))['akte__id']
    return akid

  def klkarte_display(self, akid, fallid = None, mitid=None):
    "Darstellung der Klientenkarte."

    if not akid and fallid:
      fall = ebapi.Fall(fallid)
      akte = ebapi.Akte(fall['akte_id'])
    else:
      akte = ebapi.Akte(akid)
    bezugspersonen = akte['bezugspersonen']
    einrichtungen = akte['einrichtungen']
    faelle = akte['faelle']

    faelle.sort('bgy', 'bgm', 'bgd')
    bezugspersonen.sort('verw__sort')
    einrichtungen.sort('status', 'na')

    # Aktueller bzw. letzter Fall, Wiederaufnehmbarkeit

    letzter_fall = akte['letzter_fall']
    aktueller_fall = akte['aktueller_fall']
    wiederaufnehmbar =  akte['wiederaufnehmbar']

    # Headerblock fuer das HTML-Template

    header = {'titel': 'Klientenkarte'}


    res = []
    res.append(header_t % header)

    if aktueller_fall:
      res.append(menueklk1_t % aktueller_fall)
      res.append(menueklk2_t % akte)
      res.append(menueklk3_t % aktueller_fall)
    else:
      if wiederaufnehmbar:
        res.append(menuewaufn_t % letzter_fall)
      else:
        res.append(menuezdar_t % letzter_fall)

    res.append(linielang_t)

    res.append(akten1_t % akte)
    if akte['ber'] != '' or akte['fs'] != ebapi.cc('fsfs', '999') or akte['no'] !='':
      res.append(akten2_t % akte)

    for b in bezugspersonen:
      res.append(bezugspersonen1_t % b)
      if b['ber'] != '' or b['fs'] != ebapi.cc('fsfs', '999') or b['no'] != '':
        res.append(bezugspersonen2_t % b)

    res.append(einrichtungs_kopf1_t % akte)
    if einrichtungen:
      res.append(einrichtungs_kopf2_t)
      for e in einrichtungen:
        res.append(einrichtung_t % e)

    res.append(anmeldung_kopf_t % akte)
    for f in faelle:
      for a in f['anmeldung']:
        res.append(anmeldung_t % a)

    res.append(leistungs_kopf_t % akte)
    for f in faelle:
      for l in f['leistungen']:
        res.append(leistungs_t % l)
        if l['ey'] == 0:
          res.append(leistungsendeleer_t)
        else:
          res.append(leistungsendedatum_t % l)

    res.append(bearbeiter_kopf_t % akte)
    for f in faelle:
      for z in f['zustaendigkeiten']:
        res.append(bearbeiter_t % z)
        if z['ey'] == 0:
          res.append(bearbeiterendeoffen_t)
        else:
          res.append(bearbeiterendedatum_t % z)

    res.append(fall_kopf_t % akte)
    for f in faelle:
      res.append(fall_t % f)
      if f['aktuell'] == 1:
        res.append(falloffen_t)
      else:
        res.append(fallendedatum_t % f)

    res.append(statistik_t % akte)
    for f in faelle:
      for fs in f['fachstatistiken']:
        if fs['jahr']:
          res.append(fstatistikupd_t % fs)
    res.append(jghstatistik_t % akte)
    for f in faelle:
      for js in f['jgh_statistiken']:
        if js['ey']:
          res.append(jghstatistikupd_t % js)
    res.append(tabende_t)

    res.append(notiz_t)
    if akte['no']:
      res.append(notizakte_t % akte)
    for b in bezugspersonen:
      if b['no']:
        res.append(notizbperson_t % b)
    for e in einrichtungen:
      if e['no']:
        res.append(notizeinr_t % e)
    for f in faelle:
      for a in f['anmeldung']:
        if a['no']:
          res.append(notizanm_t % a)

    for f in faelle:
      fallgruppen = ebapi.FallGruppeList(
        where = 'fall_id = %s' % f['id'])
      for g in fallgruppen:
        res.append(klkartegruppef_t % f)
        res.append(klkartegruppehref_t % g)

    for b in bezugspersonen:
      bezugspersongruppen = ebapi.BezugspersonGruppeList(
        where = 'bezugsp_id = %s' % b["id"])
      for e in bezugspersongruppen:
        res.append(klkartegruppeb_t % b)
        res.append(klkartegruppehref_t % e)

    res.append(fussklk_t % akte)
    res.append(fuss_t)

    return string.join(res, '')





