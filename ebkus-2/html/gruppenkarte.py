
"""Module für die Gruppenkarte."""

import string

from ebkus.app import Request
from ebkus.app import ebupd
from ebkus.app.ebapi import Gruppe, Akte, Fall, Bezugsperson, GruppendokumentList, cc
from ebkus.html.templates import *


class gruppenkarte(Request.Request):
  
  permissions = Request.GRUPPENKARTE_PERM

  def processForm(self, REQUEST, RESPONSE):
    file = self.form.get('file')

    # Fall 1 Gruppenkarte direkt darstellen
    if not file or file == 'gruppenkarte': 
      gruppeid = self.form.get('gruppeid')
      mitid = self.mitarbeiter['id']
      if gruppeid: gruppeid = int(gruppeid)
      else:
        self.last_error_message = "Keine Men&uuml;auswahl erhalten"
        return self.EBKuSError(REQUEST, RESPONSE)
      return self.gruppenkarte_display(gruppeid, mitid)

    # Fall 2 erst einfuegen oder updaten, dann Klientenkarte darstellen
    if self.einfuege_oder_update_operationen.get(file):
      gruppeid = self.einfuegen_oder_update(file)
      # damit Klientenkarte nicht als Ergebnis eines POST
      # dargestellt wird
      RESPONSE.redirect('gruppenkarte?gruppeid=%s' % gruppeid)
      return ''

    # Fall 3 Dokumenten- Update- oder Einfuegeformular anzeigen
    # Folgende URLs haben denselben Effekt:
    # 1)  http://localhost/efb/ebs/gruppenkarte?file=gruppeneu
    # 2)  http://localhost/efb/ebs/gruppeneu
    # Variante 1) nützlich wg. Aufruf aus menu.
    # Könnte auch mir redirect gelöst werden.

    if file == 'dokkarte':
      gruppeid = self.form.get('gruppeid')
      if gruppeid: gruppeeid = int(gruppeid)
      else:
        self.last_error_message = "Keine Men&uuml;auswahl erhalten"
        return self.EBKuSError(REQUEST, RESPONSE)
      RESPONSE.redirect('dokkarte?gruppeid=%s' % gruppeid)
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
    'gruppeeinf' : ('gruppeid', Gruppe),
    'gruppeteilneinf' : ('gruppeid', Gruppe),
    'uploadgreinf' : ('gruppeid', Gruppe),
    'dokgreinf' : ('gruppeid', Gruppe),
    'updgr' : ('gruppeid', Gruppe),
    'updgrvermeinf' : ('gruppeid', Gruppe),
    'updgrteiln' : ('gruppeid', Gruppe),
    'removeteiln' : ('gruppeid', Gruppe),
    'removegrdoks' : ('gruppeid', Gruppe)
    }

  def einfuegen_oder_update(self, file):
    function = getattr(ebupd, file)
    function(self.form)
    # Dies ist eine Art die Gruppe herauszufinden, auf die
    # sich das Einfuegen oder das Update bezog.
    # Es wäre vielleicht besser, die akid immer als
    # hidden Variable mitzuführen.
    id_name, klass = self.einfuege_oder_update_operationen.get(file)
    gruppeid = klass(int(self.form[id_name]))['gruppe__id']
    return gruppeid

  def gruppenkarte_display(self, gruppeid, mitid=None):
    "Darstellung der Gruppenkarte."

    gruppe = Gruppe(gruppeid)

    bezugspersonen = gruppe['bezugspersonen']
    bezugspersonen.sort('bezugsp_id__na','bezugsp_id__vn')
    faelle = gruppe['faelle']
    faelle.sort('fall_id__akte_id__na','fall_id__akte_id__vn')

    dokl = GruppendokumentList(where = 'gruppe_id = %s'
                           % (gruppe['id']), order = 'vy,vm,vd')

    beraternotizen = GruppendokumentList(where = 'gruppe_id = %s and art = %s and mit_id = %s' %
            (gruppe['id'], cc('dokart', 'bnotiz'), self.mitarbeiter['id']),
                           order = 'vy,vm,vd')

    # Headerblock, Menue u. Uberschrift fuer das HTML-Template

    header = {'titel': 'Gruppenkarte',
              'ueberschrift':
              "Dokumentenindex der Gruppe &quot;%(name)s, %(bgd)s.%(bgm)s.%(bgy)s-%(ed)s.%(em)s.%(ey)s&quot; " % gruppe}


    # Liste der Templates als String

    res = []
    res.append(header_t % header)
    res.append(menuegruppe_t % gruppe)
    res.append(linielang_t)
    res.append(ueberschrift_t % header)
    res.append(dokausgabe1_t % ('<A name="anotiz">Gruppenakte</A>'))

    aktendokl = []
    for d in dokl:
      if d['art'] != cc('dokart', 'bnotiz'):
        aktendokl.append(d)
    for a in aktendokl:
        res.append(dokausgabe2b_t % a)
    res.append(dokausgabe3_t)
    res.append(tabende_t)

    res.append(dokausgabe1_t % ('<A name="bnotiz">Beraternotizen</A>'))
    for b in beraternotizen:
        res.append(dokausgabe2b_t % b)
    res.append(dokausgabe3_t)
    res.append(tabende_t)

    if beraternotizen or aktendokl:
      res.append(dokausgabe1_t % ('<A name="print">Printausgabe</A>'))
      if aktendokl:
        res.append(dokausgabe5b_t % gruppe )
      if beraternotizen:
        res.append(dokausgabe4b_t % gruppe )
      res.append(dokausgabe6_t)
      res.append(tabende_t)

    if bezugspersonen or faelle:
      res.append(dokausgabe1_t % ('<A name="teiln">Teilnehmerliste</A>'))
      for f in faelle:
        fall = Fall(f['fall_id'])
        akte = Akte(fall['akte_id'])
        res.append(teiln1_t % akte)
        res.append(teiln2_t % f)

      for b in bezugspersonen:
        bezugsp = Bezugsperson(b['bezugsp_id'])
        res.append(teiln1b_t % bezugsp)
        res.append(teiln2b_t % b)

      res.append(teiln3_t)
      res.append(tabende_t)

    if dokl:
      res.append(formkopfv_t % 'suchetxt.py')
      res.append(formhiddennamevalues_t % ({'name' : 'gruppeid' ,
                                            'value' : gruppeid}))
      res.append(dokausgabe7_t % ('<A name="suche">Suche in den Texten</A>', ''))

    if dokl or bezugspersonen or faelle:
      res.append(top_t)
      res.append(fuss_t)
    else:
      res.append(fussmin_t)

    return string.join(res, '')
