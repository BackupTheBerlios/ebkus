#!/usr/local/bin/python


########################################################
# HTML Templates
#
# Alle Templatenamen enden in '_t'
# Die Templates stehen ausserhalb der Funktionsdefinition!
#########################################################


#########################
# Fuer mehrere HTML-Files
#########################


type_t =  "Content-type: text/html\n"
typevalue_t =  "Content-type: %(mtyp__name)s\n"


header_t = """
<HTML>
<HEAD><TITLE> %(titel)s </TITLE>
<!-- <meta http-equiv="expires" content="0"> //-->
<meta name="robots" content="noindex">
<meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
<meta http-equiv="Content-Style-Type" content="text/css">
<STYLE type="text/css">
<!-- BODY { background-color:#EFEFEF; color:#000000; font-family:Helvetica,Arial,sans-serif; font-style:normal; font-variant:normal; }
p,h1,h2,h3,h4,h5,h6,ul,ol,li,div,td,th,address,blockquote,nobr,b,i
     { font-family: Helvetica,Arial,sans-serif; font-style:normal; font-variant:normal; }
//-->
</STYLE>
</HEAD>
<BODY bgcolor=#EFEFEF><div align=left><P> """


menueneu_t = """
<A HREF="menu">Men&uuml;</A> .
<A HREF="menugruppe">Gruppenkartei</A> |
<A HREF="klkarte?akid=%(akte_id)d&fallid=%(id)d">Klientenkarte</A>
"""

menuemin_t = """
<A HREF="menu">Men&uuml</A> .
<A HREF="menugruppe">Gruppenkartei</A> |
<A HREF="formabfr3">Suche</A>
"""

menueklk1_t = """
<A HREF="menu">Men&uuml;</A> .
<A HREF="menugruppe">Gruppenkartei</A> |
<B>Neu: </B>
<A HREF="akteneu?file=akteneu">Neuaufnahme</A> . 
<A HREF="persneu?akid=%(akte_id)d&fallid=%(id)d">Familie</A> . 
<A HREF="einrneu?akid=%(akte_id)d&fallid=%(id)d">Einrichtung</A> . """

menueklk2_t = """ 
%(href_thanmeldung)s . """

menueklk3_t = """
<A HREF="leistneu?akid=%(akte_id)d&fallid=%(id)d">Leistung</A> . 
<A HREF="zustneu?akid=%(akte_id)d&fallid=%(id)d">Bearbeiter</A> . 
<A HREF="vermneu?akid=%(akte_id)d&fallid=%(id)d">Vermerk</A> .
<A HREF="upload?akid=%(akte_id)d&fallid=%(id)d">Dateiimport</A> .
<A HREF="fsneu?akid=%(akte_id)d&fallid=%(id)d">Fachstatistik</A> . 
<A HREF="jghneu?akid=%(akte_id)d&fallid=%(id)d">Bundesstatistik</A> . 
<A HREF="zda?akid=%(akte_id)d&fallid=%(id)d">z.d.A.</A> |
<B>Anzeige: </B>
Klientenkarte . 
<A HREF="vorblatt?akid=%(akte_id)d&fallid=%(id)d" target="_new">Vorblatt</A> .
<A HREF="dokkarte?akid=%(akte_id)d&fallid=%(id)d">Akte</A> |
<A HREF="formabfr3">Suche</A> 
"""

menuezdar_t = """
<A HREF="menu">Men&uuml;</A> .
<A HREF="menugruppe">Gruppenkartei</A> |
<B>Neu: </B>
<A HREF="akteneu?file=akteneu">Neuaufnahme</A> . 
<A HREF="zdar?akid=%(akte_id)d&fallid=%(id)d">z.d.A Rückgängig</A> |
<B>Anzeige: </B>
Klientenkarte . 
<A HREF="vorblatt?akid=%(akte_id)d&fallid=%(id)d" target="_new">Vorblatt</A> .
<A HREF="dokkarte?akid=%(akte_id)d&fallid=%(id)d">Akte</A> |
<A HREF="formabfr3">Suche</A>
"""

menuewaufn_t = """
<A HREF="menu">Men&uuml;</A> .
<A HREF="menugruppe">Gruppenkartei</A> | 
<B>Neu: </B>
<A HREF="akteneu?file=akteneu">Neuaufnahme</A> . 
<A HREF="waufnneu?akid=%(akte_id)d&fallid=%(id)d">Wiederaufnahme</A> | 
<B>Anzeige: </B>
Klientenkarte .
<A HREF="vorblatt?akid=%(akte_id)d&fallid=%(id)d" target="_new">Vorblatt</A> .
<A HREF="dokkarte?akid=%(akte_id)d&fallid=%(id)d">Akte</A> |
<A HREF="formabfr3">Suche</A>
"""

menuedok_t = """
<A HREF="menu">Men&uuml;</A> .
<A HREF="menugruppe">Gruppenkartei</A> |
<B>Text: </B>
<A HREF="vermneu?akid=%(akte_id)d&fallid=%(id)d">Neu</A> .
<A HREF="updvermausw?akid=%(akte_id)d&fallid=%(id)d">&Auml;ndern</A> .
<A HREF="upload?akid=%(akte_id)d&fallid=%(id)d">Dateiimport</A> .
<A HREF="dokkarte#suche?%(akte_id)d&fallid=%(id)d">Textsuche</A> .
<A HREF="rmdok?akid=%(akte_id)d&fallid=%(id)d">L&ouml;schen</A> |
<B>Anzeige: </B>
<A HREF="klkarte?akid=%(akte_id)d&fallid=%(id)d">Klientenkarte</A> .
<A HREF="vorblatt?akid=%(akte_id)d&fallid=%(id)d" target="_new">Vorblatt</A> .
<A HREF="dokkarte?akid=%(akte_id)d&fallid=%(id)d">Akte</A> |
<A HREF="formabfr3">Suche</A>
"""

menuedokzda_t = """
<A HREF="menu">Men&uuml;</A> .
<A HREF="menugruppe">Gruppenkartei</A> |
<B>Neu: </B>
<B>Anzeige: </B>
<A HREF="klkarte?akid=%(akte_id)d&fallid=%(id)d">Klientenkarte</A> .
<A HREF="vorblatt?akid=%(akte_id)d&fallid=%(id)d" target="_new">Vorblatt</A> .
<A HREF="dokkarte?akid=%(akte_id)d&fallid=%(id)d">Akte</A> |
<A HREF="formabfr3">Suche</A>
"""

menuegruppe_t = """
<A HREF="menu">Men&uuml;</A> .
<A HREF="menugruppe">Gruppenkartei</A> | 
<B>Gruppe: </B>
<A HREF="gruppeneu">Neu</A> .
<A HREF="updgruppe?gruppeid=%(id)d">&Auml;ndern</A> |
<B>Teilnehmer: </B>
<A HREF="gruppeteilnausw?gruppeid=%(id)d">Neu</A> .
<A HREF="gruppenkarte#teiln?gruppeid=%(id)d">&Auml;ndern</A> .
<A HREF="gruppeteiln?gruppeid=%(id)d" target="_new">Anzeigen</A> .
<A HREF="rmteiln?gruppeid=%(id)d">L&ouml;schen</A> |
<B>Text: </B>
<A HREF="vermneu?gruppeid=%(id)d">Neu</A> .
<A HREF="updvermausw?gruppeid=%(id)d">&Auml;ndern</A> .
<A HREF="upload?gruppeid=%(id)d">Dateiimport</A> .
<A HREF="gruppenkarte#suche?gruppeid=%(id)d">Textsuche</A> .
<A HREF="rmdok?gruppeid=%(id)d">L&ouml;schen</A> |
<B>Anzeige: </B>
<A HREF="gruppenkarte?gruppeid=%(id)d">Gruppenakte</A> |
<A HREF="formabfr3">Suche</A>
"""

menuefs_t = """
<A HREF="menu">Men&uuml;</A> .
<A HREF="menugruppe">Gruppenkartei</A> | 
<B>Statistik: </B>
<A HREF="fsabfr">Fachstatistik</A> .
<A HREF="formabfr6?file=abfritem">Items einer Kategorie</A> .
<A HREF="formabfr6?file=abfrkat"> ein Item je Kategorie</A> |
<A HREF="jghabfr">Bundesstatistik</A> |
<A HREF="formabfr3">Suche</A>
"""

menueadmin_t = """
<A HREF="menu">Men&uuml;</A> .
<A HREF="menugruppe">Gruppenkartei</A> |
<B>Kategorien: </B>
<A HREF="codelist">Alle</A> .
<A HREF="codetab?tabelle=Fachstatistik"> Fachstatistik</A> .
<A HREF="codetab?tabelle=Fachstatistikleistung"> Leistung</A> .
<A HREF="codetab?tabelle=Mitarbeiter"> Mitarbeiter</A> |
<B>Mitarbeiter: </B> 
<A HREF="mitneu">Neueintrag</A> .
<A HREF="mitausw">&Auml;ndern</A> |
<B>Akten:</B>
<A HREF="rmakten">Akten l&ouml;schen</A> .
<A HREF="rmgruppen">Gruppen l&ouml;schen</A> |
<B>Stellenabgleich:</B> 
<A HREF="formabfrdbexport">Datenaustausch</A> .
<A HREF="stellenabgleich">Protokoll</A> |
<B>Bundesstatistik:</B>
<A HREF="formabfrjghexport">Exportdatei erstellen</A> .
<A HREF="jghexportlist">Downloadliste</A> |
<A HREF="formabfr3">Suche</A>
"""

menuecode_t = """
<A HREF="menu">Men&uuml;</A> .
<A HREF="menugruppe">Gruppenkartei</A> |
<B>Kategorien: </B>
<A HREF="codelist"> Alle</A> .
<A HREF="codetab?tabelle=Fachstatistik"> Fachstatistik</A> .
<A HREF="codetab?tabelle=Fachstatistikleistung"> Leistung</A> .
<A HREF="codetab?tabelle=Mitarbeiter">Mitarbeiter</A> |
<A HREF="formabfr3">Suche</A>
"""

menuemit_t = """
<A HREF="menu">Men&uuml;</A> .
<A HREF="menugruppe">Gruppenkartei</A> |
<B>Mitarbeiter: </B>
<A HREF="mitneu">Neueintrag</A> .
<A HREF="mitausw">&Auml;ndern</A> |
<A HREF="codetab?tabelle=Mitarbeiter">Merkmale zu Mitarbeiter</A> |
<A HREF="formabfr3">Suche</A>
"""

fuss_t = """
</P>
<div align="left"><P>
<IMG SRC="/icons/blue.gif" ALT="Linie" WIDTH=750 HEIGHT=6>
</P><P>
<A HREF="menu">Menü</A> . <A HREF="menugruppe">Gruppenkartei</A>
</P>
</DIV>
</BODY>
</HTML>
"""

fussmin_t = """
</P>
</DIV>
</BODY>
</HTML>
"""

linielang_t = """
</P>
<div align="left"><P>
<IMG SRC="/icons/blue.gif" ALT="Linie" WIDTH=750 HEIGHT=6><BR>
</P>
<P>
"""

liniekurz_t ="""
</P>
<div align="center"><P>
<IMG SRC="/icons/blue.gif" ALT="Linie" WIDTH=550 HEIGHT=4><P>
</P><P>
"""

ueberschrift_t = """
<div align="center">
<H4> %(ueberschrift)s </H4>
"""

formkopfneu_t = """
<FORM ACTION="klkarte" METHOD="post">
<table border=1 cellspacing=1 cellpadding=6 bgcolor=#FFCCCC>
    <th align="center"> %(akte_id__vn)s %(akte_id__na)s, %(akte_id__gb)s </th>
    <th align="right"><em> %(fn)s </em></th>
    </tr>
</table>
<input type="hidden" value="%(akte_id)d" name="akid">
<input type="hidden" value="%(id)d" name="fallid">
"""

formkopfdokneu_t = """
<FORM ACTION="dokkarte" METHOD="post">
<table border=1 cellspacing=1 cellpadding=6 bgcolor=#FFCCCC>
    <th align="center"> %(akte_id__vn)s %(akte_id__na)s, %(akte_id__gb)s </th>
    <th align="right"><em> %(fn)s </em></th>
    </tr>
</table>
<input type="hidden" value="%(akte_id)d" name="akid">
<input type="hidden" value="%(id)d" name="fallid">
"""
formkopfdokgrneu_t = """
<FORM ACTION="gruppenkarte" METHOD="post">
<table border=1 cellspacing=1 cellpadding=6 bgcolor=#FFCCCC>
    <th align="center"> %(name)s </th>
    <th align="right"><em> %(gn)s </em></th>
    </tr>
</table>
<input type="hidden" value="%(id)d" name="gruppeid">
"""

formhiddenvalues_t = """
<input type="hidden" value="%(file)s" name="file">
"""

formhiddennamevalues_t = """
<input type="hidden" value="%(value)s" name="%(name)s">
"""

formsubmit_t = """
<div align="left"><P>
<B> <input type="submit" value="Speichern">
    <input type="reset"  value="Reset">
</B>
</FORM>
"""

formkopfv_t = """
<FORM ACTION="%s" METHOD="post">
"""
formsubmitv_t = """
<div align="left"><P>
<B> <input type="submit" value="%s">
    <input type="reset"  value="%s"></B>
</FORM>
    """

formsubmitv2_t = """
<div align="left"><P>
<B> <input type="submit" value="%s"></B>
</FORM>
    """

selectbg_t = """
      <select name="%(name)s" size=%(size)s>
      """

selectmbg_t = """
      <select multiple name="%(name)s" size=%(size)s >
      """

firstvalueleer_t = """
      <option value=" " selected > """

codeliste_t = """ 
      <option value="%(id)d" %(sel)s > %(name)s """

codelistecode_t = """
      <option value="%(id)d" %(sel)s > %(code)s """


codelisteos_t = """ 
      <option value="%(id)d" > %(name)s """

selectend_t = """
      </select>
      """


checkbox_t = """
      <input type="checkbox" value="%(id)d" name="%(name)s" %(check)s >"""

mitarbeiterliste_t = """
      <option value="%(id)d" %(sel)s > %(na)s """

radio_t = """
<input type="radio" value="%(id)d" name="%(kat_code)s" > """

radiocheck_t = """
<input type="radio" value="%(id)d" name="%(kat_code)s" checked > """


tabende_t = """</tr></table> """


feedback_t = """
      <P>
      <P>
      <div align="left">
      <B>Die &Auml;nderungen in der Datenbank wurden ausgef&uuml;hrt.</B> """


error_t = """
      <HTML><BODY> %s </BODY></HTML>
"""

################
# Klientenkarte
################


akten1_t = """
</P>
<div align="left">
<P>
<table border=1 bgcolor=#FFFFFF width=100%% cellpadding=2 cellspacing=1> 
  <th align="center" colspan=9 bgcolor=#FFFFFF>
    %(href_thbperson)s</th>
  </tr><tr>
<th align="center" width=4%% bgcolor=#FFFFCC>  Vrw. </th>
<th align="center" width=15%% bgcolor=#FFFFCC> Vorname </th>
<th align="center" width=25%% bgcolor=#FFFFCC> Name </th>
<th align="center" width=6%% bgcolor=#FFFFCC>  geb.  </th>
<th align="center" width=25%% bgcolor=#FFFFCC> Str.  </th>
<th align="center" width=6%% bgcolor=#FFFFCC>  Plz.  </th>
<th align="center" width=8%% bgcolor=#FFFFCC>  Ort   </th>
<th align="center" width=8%% bgcolor=#FFFFCC>  Tel.  </th>
<th align="center" width=8%% bgcolor=#FFFFCC>  Dtel. </th>
</tr><tr>
<td align="left" bgcolor=#FFFFCC>&#160; Klient </td>
<td align="left" bgcolor=#FFCCCC>&#160;<B> %(vn)s </B></td> 
<td align="left" bgcolor=#FFCCCC>&#160;<B> %(href_updakte)s </B></td> 
<td align="left" bgcolor=#FFCCCC>&#160;<B> %(gb)s </B></td> 
<td align="left" bgcolor=#FFFFFF>&#160; %(str)s </td> 
<td align="left" bgcolor=#FFFFFF>&#160; %(plz)s </td> 
<td align="left" bgcolor=#FFFFFF>&#160; %(ort)s </td> 
<td align="left" bgcolor=#FFFFFF>&#160; %(tl1)s </td> 
<td align="left" bgcolor=#FFFFFF>&#160; %(tl2)s  </td> 
</tr>"""

akten2_t = """
<tr> 
<td align="left" bgcolor=#FFFFFF cellpadding=0>&#160; </td>
<td align="left" colspan=3 bgcolor=#FFFFFF cellpadding=0> 
&#160; Ausbildung: %(ber)s </td> 
<td align="left" colspan=2 bgcolor=#FFFFFF cellpadding=0> 
&#160; bei %(fs__name)s </td> 
<td align="right" colspan=3 bgcolor=#FFFFFF cellpadding=0> 
&#160; %(href_no)s </td> 
</tr> """

bezugspersonen1_t = """
  <tr>
  <td align="left" bgcolor=#FFFFCC>&#160; %(verw__name)s </td>
  <td align="left" bgcolor=#FFFFFF>&#160; %(href_updpersvn)s   </td>
  <td align="left" bgcolor=#FFFFFF>&#160; %(href_updpersna)s   </td>
  <td align="left" bgcolor=#FFFFFF>&#160; %(gb)s   </td>
  <td align="left" bgcolor=#FFFFFF>&#160; %(str)s  </td>
  <td align="left" bgcolor=#FFFFFF>&#160; %(plz)s  </td>
  <td align="left" bgcolor=#FFFFFF>&#160; %(ort)s  </td>
  <td align="left" bgcolor=#FFFFFF>&#160; %(tl1)s  </td>
  <td align="left" bgcolor=#FFFFFF>&#160; %(tl2)s  </td>
  </tr>"""

bezugspersonen2_t = """
  <tr>
  <td align="left" bgcolor=#FFFFFF cellpadding=0>&#160;</td>
  <td align="left" colspan=3 bgcolor=#FFFFFF cellpadding=0>
  &#160; Beruf/Ausb: %(ber)s </td>
  <td align="left" colspan=2 bgcolor=#FFFFFF cellpadding=0>
  &#160; bei&#160; %(fs__name)s </td>
  <td align="right" colspan=3 bgcolor=#FFFFFF cellpadding=0>
  &#160; %(href_no)s </td>
  </tr> """

einrichtungs_kopf1_t =  """
</table>

<table border=1  bgcolor=#FFFFFF cellspacing=1 cellpadding=3 width="100%%">
<th align="center" colspan=5> 
%(href_theinrichtung)s </th>
</tr> """

einrichtungs_kopf2_t = """
<tr>
<th align="center" bgcolor=#FFFFCC> Art </th>
<th align="center" bgcolor=#FFFFCC> Name, Adresse, Ansprechperson </th>
  <th align="center" bgcolor=#FFFFCC> Tel1 </th>
  <th align="center" bgcolor=#FFFFCC> Tel2 </th>
  <th align="center" bgcolor=#FFFFCC>  aktuell </th>
  </tr> """

einrichtung_t =  """
  <tr>
  <td align="left" bgcolor=#FFFFCC>&#160; %(insta__name)s </td>
  <td align="left" >&#160; %(href_updeinrna)s 
  &#160;&#160;&#160;&#160;&#160;&#160;%(href_no)s </td>
  <td align="left">&#160; %(tl1)s </td>
  <td align="left">&#160; %(tl2)s </td>
  <td align="left">&#160; %(status__code)s </td>
  </tr> """

anmeldung_kopf_t = """
</table> 

<table border=1 bgcolor=#FFFFFF cellspacing=1 cellpadding=2 width="100%%">
<th align="center" colspan=2 bgcolor=#FFFFFF>
  <B> %(href_thanmeldung)s </B></th>
  </tr> """

anmeldung_t = """
<tr>
<td align="left" width=15%% bgcolor=#FFFFCC>&#160; %(href_updanm)s </td>
<td align="left" width=85%% >

&#160; %(von)s  am&#160; %(ad)d.%(am)d.%(ay)d. Tel.:&#160; %(mtl)s 
&#160;&#160;&#160;&#160;&#160; %(href_no)s </td>
</tr><tr>
<td align="left" bgcolor=#FFFFCC>&#160; Zugangsmodus </td>
<td align="left" >&#160; %(zm__name)s  auf Empfehlung von &#160; %(me)s 
</td>
</tr><tr>
<td align="left" bgcolor=#FFFFCC>&#160; Anmeldegrund </td> 
<td align="left">&#160; %(mg)s </td>
</tr> """

leistungs_kopf_t = """
</table> 

<table border=0 cellspacing=0 cellpadding=0 width="100%%"><td valign="top">
<table border=1 bgcolor=#FFFFFF cellspacing=1 cellpadding=3 width="100%%">
<th align="center" colspan=4> %(href_thleistung)s </th>
</tr><tr>
<th align="center" bgcolor=#CCFFFF> Mitarbeiter </th>
<th align="center" bgcolor=#FFFFCC> Leistung </th>
<th align="center" bgcolor=#FFFFCC> am </th>
<th align="center" bgcolor=#FFFFCC> bis </th>
</tr> """

leistungs_t =  """
<tr>
<td align="left" bgcolor=#CCFFFF>&#160; %(href_updleist)s </td>
<td align="left"> %(le__name)s </td>
<td align="left"> %(bgd)d.%(bgm)d.%(bgy)d </td> """

leistungsendeleer_t = """
<td align="left">&#160; </td>
</tr> """

leistungsendedatum_t = """
<td align="left">&#160; %(ed)d.%(em)d.%(ey)d </td>
</tr> """

bearbeiter_kopf_t = """
</table>

</td><td valign="top">
<table border=1 bgcolor=#FFFFFF cellspacing=1 cellpadding=3 width="100%%">
<th align="center" colspan=3> %(href_thzustaendig)s </th>
</tr><tr>
<th align="center" bgcolor=#CCFFFF> Bearbeiter </th>
<th align="center" bgcolor=#FFFFCC> Beginn </th>
<th align="center" bgcolor=#FFFFCC> Ende </th>
</tr> """

bearbeiter_t = """
<tr>
<td align="left" bgcolor=#CCFFFF> %(href_updzust)s </td>
<td align="left"> %(bgd)d.%(bgm)d.%(bgy)d </td> """

bearbeiterendeoffen_t = """
<td align="left"> offen </td>
</tr> """

bearbeiterendedatum_t = """
<td align="left"> %(ed)d.%(em)d.%(ey)d </td>
</tr> """

fall_kopf_t =  """
</table>

</td><td valign="top">
<table border=1 cellspacing=1 cellpadding=3 width="100%%">
<th align="center" bgcolor=%(stfarbe)s colspan=3> %(href_thstand)s </th>
</tr><tr>
<th align="center" bgcolor=#CCFFFF> Fallnr. </th>
<th align="center" bgcolor=#FFFFCC> Beginn </th>
<th align="center" bgcolor=#FFFFCC> z.d.A. </th>
</tr>"""

fall_t = """
<tr>
<td align="left" bgcolor=#CCFFFF> %(href_updfall)s </td>
<td align="left" bgcolor=#FFFFFF> %(bgd)d.%(bgm)d.%(bgy)d </td> """

falloffen_t = """
<td align="left" bgcolor=#FFFFFF> offen </td>
</tr> """

fallendedatum_t = """
<td align="left" bgcolor=#FFFFFF> %(zdad)d.%(zdam)d.%(zday)d </td>
</tr> """

statistik_t = """
</table></td></tr>
</table>

<table border=1 bgcolor=#FFFFFF cellspacing=1 cellpadding=3>
<th align="center"> %(href_fstatistik)s </th> """

fstatistikupd_t = """
<th align="center"> %(href_updfs)s </th> """

jghstatistik_t = """
<th align="center"> %(href_jghstatistik)s </th> """

jghstatistikupd_t = """
<th align="center"> %(href_updjgh)s </th> """

notiz_t = """
<P><div align="left">
<table bgcolor=#FFFFCC> 
<th align="center"> <A name="notiz"> Notiz zu</A></th>
</tr>
</table>
<P>
"""
notizakte_t = """
%(vn)s %(na)s: <em> %(no)s </em><BR>"""
notizbperson_t ="""
%(vn)s %(na)s: <em> %(no)s</em> <BR>"""
notizeinr_t ="""
%(insta__name)s %(na)s: <em> %(no)s </em><BR>"""
notizanm_t ="""
Anmeldung: <em> %(no)s </em><BR>"""

klkartegruppef_t = """
%(akte_id__vn)s %(akte_id__na)s: """

klkartegruppeb_t = """
%(vn)s %(na)s: """

klkartegruppehref_t = """
<A HREF="gruppenkarte?gruppeid=%(gruppe_id)s">Gruppenkarte - Nr.: %(gruppe_id__gn)s</A><BR>"""

klkartegruppe_t = """
 Gruppenkarte - Nr.: %(gruppe_id__gn)s</A><BR>"""

fussklk_t = """
<BR></P>
<div align="right"><P><A HREF="klkarte?akid=%(id)d">Zum Anfang der Seite</A>
"""


##################################
# Neue Akte und neuer Fall anlegen
##################################

akteneu_t = """
<div align="center">
<FORM ACTION="klkarte" METHOD="post"> 
<div align="center">
<table border=1 cellspacing=1 cellpadding=6 >
    <th align="center" colspan=2 bgcolor=#FFCCCC> Kind, Jugendlicher, junger Erwachsene </th></tr>
</table>
<table border=1 cellspacing=1 cellpadding=8>
<tr>
   <td align="left"> <B> Vorname </B> </td>
   <td> <input size=21 maxlength=35  name="va"> </td>
   <td align="left"><B> Name</B> </td>
   <td> <input size=22  maxlength=35 name="na"> </td>
   </tr><tr>
   <td align="left"> <B> Ausbild. </B> </td>
   <td> <input size=21 maxlength=30 name="ber"> </td>
   <td align="left">  <B> geb. </B> </td>
   <td> <input size=10 maxlength=10 name="gb"> </td>
    </tr><tr>
    <td  align="left"> <B> Str. </B> </td>
    <td> <input size=21 maxlength=35 name="str"> </td>
    <td colspan="2" align="left"> <B> Plz. </B> 
        <input size=5 maxlength=5 name="plz">
                   &#160;<B> Ort </B>  
        <input size=13 maxlength=35 name="ort"> </td>
    </tr><tr>
    <td colspan="2" align="left"> <B> Tel </B>
              <input size=10 maxlength=20 name="tl1">
                                  &#160;<B> Dtel </B>
              <input size=10 maxlength=20 name="tl2"> </td>
    <td colspan="2" align="center"><B> bei </B>
        <select name="fs">
        <option value="" selected> """

akteneuno_t = """ 
     </select></td>
     </tr><tr>
     <td align="left" colspan="4"> <B> Notiz </B> 
            <input size=57 maxlength="255" name="no"></td>
     </tr><tr>
     <td colspan="2" align="center"> <B> Bearbeiter </B>
          <select name="zumitid"> """

akteneufallbg_t = """
     </select></td>
  <td colspan="2" align="center"> <B>Beginn</B>
  <input type="text" size=2 maxlength=2 value=""  name="zubgd"><B>.</B>
  <input type="text" size=2 maxlength=2 value="%(month)d" name="zubgm"><B>.</B>
  <input type="text" size=4 maxlength=4 value="%(year)d" name="zubgy"></td>
  </tr>
</table>
<table border=1 cellspacing=1 cellpadding=8>
    <th align="center">Mitarbeiter</th>
    <th align="center">Leistung</th>
    <th align="center">am</th>
    </tr><tr>
    <td align="left">
       <select name="lemitid"> """

akteneuleist_t = """ </select></td>
    <td align="left">
          <select name="le">"""

akteneuleistbg_t = """ 
       </select></td>
    <td align left><input size=2 maxlength=2 value="" name="lebgd">
        <input size=2 maxlength=2 value="%(month)d" name="lebgm">
        <input size=4 maxlength=4 value="%(year)d"  name="lebgy"></td>
     </tr>
</table>"""


###########################################
# Klientendaten in der Tabelle Akte updaten
###########################################

updaktena_t = """
<table border=1 cellspacing=1 cellpadding=8 >
   <tr>
   <td align="left"> <B> Vorname </B> </td>
   <td><input size=21 maxlength=35  value="%(vn)s" name="vn"> </td>
   <td align="left"><B> Name</B> </td>
   <td> <input size=22  maxlength=35 value="%(na)s" name="na"> </td>
   </tr><tr>
   <td align="left"><B> Ausbild. </B> </td>
   <td> <input size=21 maxlength=30 value="%(ber)s" name="ber"> </td>
   <td align="left"><B> geb. </B> </td>
    <td> <input size=10 maxlength=10 value="%(gb)s" name="gb"> </td>
    </tr><tr>
    <td  align="left"><B> Str. </B> </td>
    <td> <input size=21 maxlength=35 value="%(str)s" name="str"> </td>
    <td colspan="2" align="left"><B> Plz. </B> 
         <input size=5 maxlength=5 value="%(plz)s" name="plz"> 
                           &#160;<B> Ort </B>
        <input size=13 maxlength=35 value="%(ort)s" name="ort"> </td>
    </tr><tr>
    <td colspan="2" align="left"><B> Tel </B> 
        <input size=10 maxlength=20 value="%(tl1)s" name="tl1">
                    &#160;<B> Dtel </B> 
        <input size=10 maxlength=20 value="%(tl2)s" name="tl2"></td>
    <td colspan="2" align="center"><B> bei </B>
        <select name="fs"> """

updakteno_t = """ 
     </select></td>
     </tr><tr>
     <td align="left" colspan="4"> <B> Notiz </B> 
            <input size=57 maxlength="255" value="%(no)s" name="no"></td>
     </tr>
</table> """


#############
# persneu
#############


persneuverw1_t = """
<table border=1 cellspacing=1 cellpadding=8>
  <th align="center" colspan=4>     
    <select name="verw">"""

persneuna_t = """
    </select></th>
    </tr><tr>
    <td align="left"><B> Vorname </B> </td>     
    <td>   <input size=21 maxlength=35  name="vn"></td>
    <td align="left"><B> Name </B> </td>
    <td>    <input size=22 maxlength=35 value="%(na)s" name="na"></td>
    </tr><tr>
    <td align="left"><B> Beruf </B> </td>
      <td>  <input size=21 maxlength=30 name="ber"></td>
    <td align="left"><B> geb. </B> </td>
     <td>   <input size=10 maxlength=10 name="gb"></td>
    </tr><tr>
    <td  align="left"><B> Str. </B> </td>
      <td>  <input size=21 maxlength=35 name="str"></td>
    <td colspan="2" align="left"><B> Plz. </B> 
           <input size=5 maxlength=5  name="plz">
              &#160; <B> Ort </B>  
        <input size=13 maxlength=35 name="ort"> </td>
    </tr><tr>
    <td colspan="2" align="left"><B> Tel </B>
                      <input size=10 maxlength=20 name="tl1">
        &#160; <B> Dtel </B> <input size=10 maxlength=20 name="tl2"></td>
    <td colspan="2" align="left"><B> bei </B>
        <select name="fs">
        <option value="">  """

persneunot_t = """
</select></td>
    </tr><tr>
    <td align="left" colspan=4><B> Notiz </B> 
        <input size=50 maxlength=255 name="no">
        <input type="checkbox" value="%(nobed)s"  name="nobed" > <B> Wichtig </B></td>
     </tr>
</table> 
<input type="hidden" value="%(vrt)s" name="vrt">"""


persneuakte_t = """
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFFFFF>
   <th div align="center" colspan=9> Eltern, Geschwister, Verwandte </th>
   </tr><tr>
    <th align="center"> Vrw. </th>
    <th align="center"> Vorname </th>
    <th align="center"> Name </th>
    <th align="center"> geb. </th>
    <th align="center"> Str. </th>
    <th align="center"> Plz. </th>
    <th align="center"> Ort </th>
    <th align="center"> Tel. </th>
    <th align="center"> Dtel. </th>
   </tr><tr>
    <td align="left">&#160; Klient
    <td align="left">&#160; %(vn)s </td>
    <td align="left">&#160; %(na)s </td>
    <td align="left">&#160; %(gb)s </td>
    <td align="left">&#160; %(str)s </td>
    <td align="left">&#160; %(plz)s </td>
    <td align="left">&#160; %(ort)s </td>
    <td align="left">&#160; %(tl1)s </td>
    <td align="left">&#160; %(tl2)s </td>
    </tr>"""

persneubpersonen_t = """
    <tr><td align="left">&#160; %(verw__name)s </td>
    <td align="left">&#160; %(vn)s </td>
    <td align="left">&#160; %(na)s </td>
    <td align="left">&#160; %(gb)s </td>
    <td align="left">&#160; %(str)s </td>
    <td align="left">&#160; %(plz)s </td>
    <td align="left">&#160; %(ort)s </td>
    <td align="left">&#160; %(tl1)s </td>
    <td align="left">&#160; %(tl2)s </td> 
    </tr> """


######################
# Bezugpserson updaten
######################

updpersna_t = """
<input type="hidden" value="%(id)d" name="bpid" >
<table border=1 cellspacing=1 cellpadding=8><tr>
      <td align="left"> <B>Vorname</B> </td>     
      <td> <input size=21 maxlength=35  value="%(vn)s" name="vn">
      <td align="left"> <B>Name</B> </td> 
      <td><input size=22 maxlength=35 value="%(na)s" name="na"> </td>
      </tr><tr>
      <td align="left"> <B>Beruf</B> </td>
      <td> <input size=21 maxlength=30 value="%(ber)s" name="ber"> </td>
      <td align="left"> <B>geb.</B> </td> 
      <td> <input size=10 maxlength=10 value="%(gb)s" name="gb"> </td>
      </tr><tr>
      <td  align="left"> <B>Str.</B> </td>
      <td> <input size=21 maxlength=35 value="%(str)s" name="str"> </td>
      <td colspan="2" align="left"> <B>Plz.</B> 
          <input size=5 maxlength=5 value="%(plz)s"  name="plz">
              &#160; <B>Ort</B>  
          <input size=13 maxlength=35 value="%(ort)s"  name="ort"> 
      </tr><tr>
      <td colspan="2" align="left"> <B>Tel</B> 
          <input size=10 maxlength=20 value="%(tl1)s" name="tl1">
               &#160;<B>Dtel</B> 
            <input size=10 maxlength=20 value="%(tl2)s" name="tl2">
      <td colspan="2" align="center"> <B>ist</B> 
             <select name="verw"> """

updpersfs_t = """
       </select>
       </tr><tr>
       <td colspan="2" align="left" > <B>lebt bei</B>
             <select name="fs"> """

updpersnot_t = """ 
       </select> </td>
       <td colspan="2"> &#160;   </td>
       </tr><tr>
       <td align="left" colspan="4"> <B>Notiz</B> 
          <input size=50 maxlength="255" value="%(no)s" name="no">
          <input type="checkbox" value="%(nobed)d" name="nobed" %(check)s > 
          <B>Wichtig</B>
       </tr>
</table> 
<input type="hidden" value="%(vrt)s" name="vrt">"""


########################
# Einrichtungskontaktneu
########################

theinrneu_t = """
<div align="center">
<table border=1 cellspacing=1 cellpadding=8>
     <tr>
     <th align="center"> Art </th>
     <th align="center"> Name </th>
     <th align="center"> Tel1 </th>
     <th align="center"> Tel2 </th>
     </tr><tr>
     <td align="left"><select name="insta"> """


einrneuna_t = """
        </select>
      </td><td align="left">
        <input type="text" size=25 maxlength=80 name="na"></td>
      <td align="left">
        <input type="text" size=10 maxlength=20 name="tl1">
       </td><td align="left">           
        <input type="text" size=10 maxlength=20 name="tl2"></td>
       </tr><tr>
       <td align="left" colspan=4> <B>Notiz</B>&#160;
         <input type="text" size=60 maxlength=255 name="no">
         <input type="checkbox" value="%(nobed)s" name="nobed" > <B> Wichtig </B></td>
       </tr>
</table> 
<input type="hidden" value="%(status)s" name="status">
"""

theinrneueinrichtungen_t = """
<div align="center">
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFFFFF>
    <tr>
    <th align="center">Art</th>
    <th align="center">Name</th>
    <th align="center">Tel1</th>
    <th align="center">Tel2</th> 
    <th align="center">Aktualit&auml;t</th>
    </tr>"""

einrneueinrichtungen_t = """
     <tr>
     <td align="left">&#160; %(insta__name)s</td>
     <td align="left">&#160; %(na)s </td>
     <td align="left">&#160; %(tl1)s </td>
     <td align="left">&#160; %(tl2)s </td>
     <td align="center">&#160; %(status__code)s </td>
     </tr><tr>
     <td align="left" colspan=5><B> %(nobed__name)s: </B> %(no)s </td>
     </tr> """
keineeinrneu_t = """
<div align="center"> Bisher keine Einrichtung eingetragen. """

#############################
# Einrichtungskontakt updaten
############################


updeinrna_t = """
        </select>
      </td><td align="left">
        <input type="text" size=25 maxlength=80 value="%(na)s" name="na"></td>
      <td align="left">
        <input type="text" size=10 maxlength=20 value="%(tl1)s" name="tl1"></td>
      <td align="left">         
        <input type="text" size=10 maxlength=20 value="%(tl2)s" name="tl2"></td>
       </tr><tr>
       <td align="left" colspan=4><B>Notiz</B>
         <input type="text" size=60 maxlength=255 value="%(no)s" name="no">"""

updeinraktuell_t = """       
         <B> Wichtig </B></td></tr>
</table> 
<input type="hidden" value="%(status)d" name="status">
<input type="hidden" value="%(id)d" name="einrid">
"""

##############
# Anmeldung neu
##############

anmneuvon_t = """
<table border=1 cellspacing=1 cellpadding=8>
 <tr><td align="left"> <B>gemeldet von</B> </td>
     <td><input type="text" size=25 maxlength=35 value="%(von)s" name="von"> </td>
     <td align="left"> <B>am</B>&#160; 
       <input type="text" size=2  maxlength=2  value="%(ad)d" 
               name="ad"><B>.</B>
       <input type="text" size=2  maxlength=2 value="%(am)d" 
               name="am"><B>.</B> 
       <input type="text" size=4 maxlength=4 value="%(ay)d" 
               name="ay"> </td>
     <td>       <B>Tel.</B>&#160; 
       <input type="text" size=15 maxlength=20 value="%(mtl)s" name="mtl"> </td>
  </tr><tr> <td align="left"> <B>Zugangsart</B> </td>
      <td> <select name="zm"> """

anmneuempfehlung_t = """
     </select> </td>
     <td>  <B>auf Empfehlung von</B> </td> 
     <td>  <input type="text" size=19 maxlength=35 value="" name="me"> </td>
     </tr><tr>
     <td align="left"> <B>Anmeldegr.</B>&#160; 
      <td colspan="3"> <input type="text" size=70 maxlength=255 value="" name="mg"> </td>
      </tr><tr>
     <td align="left"> <B>Notiz</B>&#160; </td> 
      <td colspan="3"> <input type="text" size=70 maxlength=255 value="" name="no"> </td>
    </tr>
</table> """


############################
# Anmeldeinformation updaten
############################

updanmempfehlung_t = """
     </select> </td>
     <td> <B>auf Empfehlung von</B> </td> 
     <td> <input type="text" size=19 maxlength=35 value="%(me)s" name="me"></td>
     </tr><tr>
     <td align="left" > <B>Anmeldegr.</B> &#160; 
      <td colspan="3"> <input type="text" size=58 maxlength=255 value="%(mg)s" name="mg"> </td>
      </tr><tr>
     <td align="left"> <B>Notiz</B>&#160;  </td>
      <td colspan="3"> <input type="text" size=70 maxlength=255 value="%(no)s" name="no"> </td>
    </tr>
</table>
<input type="hidden" value="%(id)d" name="anmid"> """


###################
# Leistung einfuegen
###################

thleistneu_t = """
<table border=1 cellspacing=1 cellpadding=8>
      <th align="center">Mitarbeiter</th>
      <th align="center">Leistung</th>
      </tr><tr>
      <td align="left">
      <select name="mitid"> """

leistneu_t = """
      </select></td>
      <td align="left">
      <select name="le">"""

leistneubg_t = """
    </select>
    </table>
    <table border=1 cellspacing=1 cellpadding=8>
    <th align="center">am</th>
    <th align="center">bis</th>
    </tr><tr>
    <td align="left">
    <input type="text" size=2 maxlength=2 value="%(day)d" name="bgd"><B>.</B>
    <input type="text" size=2 maxlength=2 value="%(month)d" name="bgm"><B>.</B>
    <input type="text" size=4 maxlength=4 value="%(year)d" name="bgy"></td>
    <td align="left">
    <input type="text" size=2 maxlength=2 name="ed"><B>.</B>
    <input type="text" size=2 maxlength=2 name="em"><B>.</B>
    <input type="text" size=4 maxlength=4 name="ey">
    </table>"""

thleistungsliste_t = """
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFFFFF>
    <th align="center">Mitarbeiter</th>
    <th align="center">Leistungen</th>
    <th align="center">am</th>
    <th align="center">bis</th>
    </tr> """

leistungsliste_t = """
    <tr>
    <td align="left">%(mit_id__na)s </td>
    <td align="left">%(le__name)s </td>
    <td align="left">%(bgd)d<B>.</B>%(bgm)d<B>.</B>%(bgy)d</td>
    <td align="left">%(ed)d<B>.</B>%(em)d<B>.</B>%(ey)d</td>
    </tr> """

keineleistungneu_t = """
<div align="center"> Bisher keine Leistung eingetragen. """

##################
# Leistung aendern
##################

leistdatum_t = """
    </select>
    </table>
    <table border=1 cellspacing=1 cellpadding=8>
    <th align="center">am</th>
    <th align="center">bis</th>
    </tr><tr>
    <td align="left">
    <input type="text" size=2 maxlength=2 value="%(bgd)d" name="bgd"><B>.</B>
    <input type="text" size=2 maxlength=2 value="%(bgm)d" name="bgm"><B>.</B>
    <input type="text" size=4 maxlength=4 value="%(bgy)d" name="bgy"></td>
    <td align="left">
    <input type="text" size=2 maxlength=2 value="%(ed)d" name="ed"><B>.</B>
    <input type="text" size=2 maxlength=2 value="%(em)d" name="em"><B>.</B>
    <input type="text" size=4 maxlength=4 value="%(ey)d" name="ey">
    </table>
    <input type="hidden" value="%(id)d" name="leistid"> """

###################
# Zustaendigkeit neu
###################

thzustneu_t = """
<table border=1 cellspacing=1 cellpadding=8>
    <th align="center">Bearbeiter</th>
    <th align="center">Beginn</th>
    </tr><td align="left">
    <select name="mitid"> """

zustneudatum_t = """ 
     </select></td> 
     <td align="left"> 
     <input type="text" size=2 maxlength=2 value="%(day)d" name="bgd"><B>.</B> 
     <input type="text" size=2 maxlength=2 value="%(month)d" name="bgm"><B>.</B>
     <input type="text" size=4 maxlength=4 value="%(year)d" name="bgy"></td> 
     </tr> 
</table> """ 

zustende_t = """
    <div align="center"><P> Die bisherige Zust&auml;ndigkeit von <em><B>
   '%(mit_id__vn)s %(mit_id__na)s' </B></em>wird mit obigem Datum
   ausgetragen.</P>
   <input type="hidden" value="%(mit_id__id)d" name="aktuellmitid">
   <input type="hidden" value="%(id)d" name="aktuellzustid"> """

thzustaendigkeiten_t = """
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFFFFF>
    <th align="center">Bearbeiter</th>
    <th align="center">Beginn</th>
    <th align="center">Ende</th>
    </tr> """

zustaendigkeiten_t = """
    <tr>
    <td align="left">&#160;%(mit_id__na)s</td>
    <td align="left">&#160;%(bgd)d.%(bgm)d.%(bgy)d </td>
    <td align="left">&#160;%(ed)d.%(em)d.%(ey)d </td>
    </tr> """

########################
# Zustaendigkeit aendern
########################

thupdzust_t = """
<table border=1 cellspacing=1 cellpadding=8>
    <th align="center">Bearbeiter</th>
    <th align="center">Beginn</th>
    <th align="center">Ende</th>
    </tr><td align="left">
    <select name="mitid"> """


updzustdatum_t = """
    <select></td>
    <td align="left"> 
     <input type="text" size=2 maxlength=2 value="%(bgd)d" name="bgd"><B>.</B>
     <input type="text" size=2 maxlength=2 value="%(bgm)d" name="bgm"><B>.</B>
     <input type="text" size=4 maxlength=4 value="%(bgy)d" name="bgy"></td>
     <td align="left">     
     <input type="text" size=2 maxlength=2 value="%(ed)d" name="ed"><B>.</B>
     <input type="text" size=2 maxlength=2 value="%(em)d" name="em"><B>.</B>
     <input type="text" size=4 maxlength=4 value="%(ey)d" name="ey"></td>
    </tr>
</table> 
    <input type="hidden" value="%(id)d" name="zustid">

<P>
<div align="center"> F&uuml;r Bearbeiterwechsel wie -endedatum und
z.d.A.-Eintrag den Tabellenkopf (Bearbeiter bzw. Stand) in der
Klientenkarte anklicken. (hier nur Korrekturen).  """

#########################
# Fallabschluss eintragen
#########################

thzda_t = """
<table border=1 cellspacing=1 cellpadding=8>
   <th align="center"> Beginn </th>
   <th align="center"> Abschlussdatum</th>
   </tr><tr>
   <td align="center">
   <B>%(bgd)d.%(bgm)d.%(bgy)d </B></td>
   <td align="center"> """

zdadatum_t = """
   <input type="text" size=2 maxlength=2  name="zdad"><B>.</B>
   <input type="text" size=2 maxlength=2 value="%(month)d" name="zdam"><B>.</B>
   <input type="text" size=4 maxlength=4 value="%(year)d" name="zday">
   </tr>
</table>

"""

########################################
# z.d.A. (zu den Akten) Eintrag updaten
########################################


updzda_t = """
<table border=1 cellspacing=1 cellpadding=8>
   <th align="center"> Beginn
   <th align="center"> 
   <input type="text" size=2 maxlength=2 value="%(bgd)d" name="bgd"><B>.</B>
   <input type="text" size=2 maxlength=2 value="%(bgm)d" name="bgm"><B>.</B>
   <input type="text" size=4 maxlength=4 value="%(bgy)d" name="bgy"></th>
   </tr>
</table> 

<P> Bei einer Korrektur gegebenfalls das Beginndatum des ersten zust&auml;ndigen Bearbeiters ebenfalls &auml;ndern. 

"""


###################################
# z.d.A. Eintrag rueckgaengig machen
###################################

zdarzust1_t = """
<div align="center">
<P>
<B>Neue Zust&auml;ndigkeit</B> 
    <select name="zumitid">"""

zdarzust2_t = """ </select> 
<B>Beginn</B>&#160;
<input type="text" size=2 maxlength=2 name="bgd"  value="%(day)d"><B>.</B>
<input type="text"  size=2 maxlength=4 name="bgm" value="%(month)d"><B>.</B>
<input type="text"  size=4 maxlength=4 name="bgy" value="%(year)d">
</P>
"""

###############################
# Fall-Wiederaufnahme eintragen
###############################

waufnakte_t = """
<div align="center">
<FORM ACTION="klkarte" METHOD="post"> 
<input type="hidden" value="%(id)d" name="akid">
<div align="center">
<table border=1 cellspacing=1 cellpadding=8>
   <tr>
   <td align="left"> <B> Vorname </B> </td> 
   <td> <input size=21 maxlength=35  value="%(vn)s" name="vn"> </td>
   <td align="left"><B> Name</B> </td>
   <td> <input size=22 maxlength=35 value="%(na)s" name="na"> </td>
   </tr><tr>
   <td align="left"><B> Ausbild. </B> </td>
   <td> <input size=21 maxlength=30 value="%(ber)s" name="ber"> </td>
   <td align="left"><B> geb. </B> </td>
   <td> <input size=10 maxlength=10 value="%(gb)s" name="gb"> </td>
    </tr><tr>
    <td  align="left"><B> Str. </B> </td>
    <td> <input size=21 maxlength=30 value="%(str)s" name="str"> </td>
    <td colspan="2" align="left"><B> Plz. </B> 
         <input size=5 maxlength=5 value="%(plz)s" name="plz">
                  &#160; <B> Ort </B>  
        <input size=13 maxlength=35 value="%(ort)s" name="ort"> </td>
    </tr><tr>
    <td colspan="2" align="left"><B> Tel </B> 
         <input size=10 maxlength=20 value="%(tl1)s" name="tl1">
                   &#160; <B> Dtel </B> 
                   <input size=10 maxlength=20 value="%(tl2)s" name="tl2"></td>
    <td colspan="2" align="center"><B> bei </B>
        <select name="fs"> """

waufnakteno_t = """ 
     </select></td>
     </tr><tr>
     <td align="left" colspan="4"> <B> Notiz </B> 
            <input size=57 maxlength="255" value="%(no)s" name="no"></td>
     </tr><tr>
     <td colspan="2" align="center"><B> Bearbeiter </B>
          <select name="zumitid"> """

waufnfallbg_t = """
     </select></td>
  <td colspan="2" align="center"> <B>Beginn</B>
  <input type="text" size=2 maxlength=2 value=""  name="zubgd"><B>.</B>
  <input type="text" size=2 maxlength=2 value="%(month)d" name="zubgm"><B>.</B>
  <input type="text" size=4 maxlength=4 value="%(year)d" name="zubgy"></td>
  </tr>
</table>
<table border=1 cellspacing=1 cellpadding=8>
    <th align="center">Mitarbeiter</th>
    <th align="center">Leistung</th>
    <th align="center">am</th>
    </tr><tr>
    <td align="left">
       <select name="lemitid"> """

waufnleist_t = """ </select></td>
    <td align="left">
          <select name="le">"""

waufnleistbg_t = """ 
       </select></td>
    <td align left><input size=2 maxlength=2 value="" name="lebgd">
        <input size=2 maxlength=2 value="%(month)d" name="lebgm">
        <input size=4 maxlength=4 value="%(year)d"  name="lebgy"></td>
     </tr>
</table>"""


#############
# Auswahlmenu
#############

auswahlmenu_t = """
</P>
<div align="center">
<P>
<FORM ACTION="klkarte" METHOD="post">

<table cellpadding="8">
<th valign="top"><table>
    <tr>
    <th align="center" bgcolor=#FFFFBB><big>Neu</big></th>
    </tr><tr>
    <td align="left">
    <input type="radio" value="akteneu" name="file"><B> Neuaufnahme</B>
    </td></tr><tr>
    <td align="left">    
    <input type="radio" value="fsneu" name="file"><B> Fachstatistik</B>
    </td></tr><tr>
    <td align="left">
    <input type="radio" value="jghneu" name="file"><B> Bundesstatistik</B>
    </td></tr><tr>
    <td align="left">
    <!--    <A HREF="gruppeneu">Neue Gruppe</A> //--->
    <input type="radio" value="gruppeneu" name="file"><B> Gruppe</B> 
    </td></tr><tr>
    <td>&#160; </td>
    </tr><tr>
    <th align="center"  bgcolor=#FFFFBB> <big> Suche </big> </th>
    </tr><tr>
    <td align="left">
    <input type="radio" value="formabfr3" name="file"><B> Klientenkarte </B></td>
    </tr><tr>
    <td align="left">
    <input type="radio" value="formabfr3" name="file"> <B> Gruppenkarte </B></td>
    </td></tr><tr>
    <td>&#160; </td>
    </tr><tr>
    <th>
     <B><input type="submit" value="Okay">
     <input type="reset"  value="Reset"></B>
     </tr>
</table></th>

<th valign="top"><table>
    <tr>
    <th align="center"  bgcolor=#FFFFBB> <big> &Auml;ndern</big></th>
    </tr><tr>
    <td align="left">
    <input type="radio" value="updfsausw" name="file"><B> Fachstatistik</B></td>
    </tr><tr>
    <td align="left">
    <input type="radio" value="updjghausw" name="file"><B> Bundesstatistik</B></td>
    </tr><tr>
    <td>&#160; </td>
    </tr><tr>
    <th align="center"  bgcolor=#FFFFBB> <big> Ansicht</big></th>
    </tr><tr><td align="left">
    <input type="radio" value="klkarte" name="file"><B> Klientenkarte</B></td>
    </tr><tr>
    <td align="left">
    <input type="radio" value="vorblatt" name="file"><B> Aktenvorblatt</B></td>
    </tr><tr><td align="left">
    <input type="radio" value="dokkarte" name="file"><B> Akte</B></td>
    </tr><tr><td align="left">
    <td>&#160;</td>
    </tr>
</table></th>

<th valign="top"><table><th align="center" bgcolor=#FFCCCC> <big>Klient</big></th>
    </tr><tr>
    <td align="left">
    <select size=15 name="fallid"> """


klientauswahl_t = """
<option value="%(fall_id)s" >%(mit_id__na)s | %(fall_id__akte_id__vn)s %(fall_id__akte_id__na)s, %(fall_id__akte_id__gb)s | %(fall_id__fn)s """

menusubmit_t = """
     </select>
     </td>
     </tr>
</table></th>
</tr>
</table>

<br>
<table cellpadding=8>
     <tr>
     <th valign="top" align="left"> Gruppenkartei <A HREF="menugruppe">hier</A> &#160;&#160;&#160; </th>
     <th align="left"> Abfragen <A HREF="#Abfrage">hier</A> &#160;&#160;&#160;</th>
     <th align="left" >  Administration <A HREF="#Admin">hier</A> </th>
     <th>&#160;&#160;&#160;&#160;&#160;&#160;   </th>
</tr>
</table>
</form> """

abfragen_t = """
</P><P>
<div align="center">
<IMG SRC="/icons/blue.gif" WIDTH=600 HEIGHT=5><BR><BR>
</P><P>

<div align="center">
<table>
<th valign="top"><table> 
   <th align="center" bgcolor=#FFFFBB><big> <A name="Abfrage"> Abfragen</A></big></th>
   </tr><tr>
   <td align="left"> </td>
   </tr><tr>
   <td align="left"> <B> Suche </B> </td>
   </tr><tr>
   <td align="left">&#160;&#160;&#160; <A HREF="formabfr3"> Klientenkarte</A></td>
   </tr><tr>
   <td align="left">&#160;&#160;&#160; <A HREF="formabfr3"> Gruppenkarte</A> </td>
   </tr><tr>
   <td align="left"> <B> Beratungen </B> </td>
   <tr></tr>
   <td align="left">&#160;&#160;&#160;
   <A HREF="abfr1?o=laufend&ed=0"> laufende</A></td></tr><tr>
   <td align="left">&#160;&#160;&#160; 
   <A HREF="abfr1?o=zda&ed=0"> abgeschlossene</A></td>
   </tr><tr>
   <td align="left">&#160;&#160;&#160; 
   <A HREF="abfr1?o=alle&ed=0"> alle</A></td></tr><tr>
   <td align="left">&#160;&#160;&#160;  
   <A HREF="formabfr2"> ab Fallnummer ?</A></td>
   </tr><tr>
   <td align="left"> <B> Statistik </B> </td>
   </tr><tr>
   <td align="left">&#160;&#160;&#160; 
   <A HREF="formabfr4"> Neumeldungen u. z.d.A.</A></td>
   </tr><tr>
   <td align="left">&#160;&#160;&#160; 
   <A HREF="formabfr5"> Klienten pro Mitarbeiter</A></td>
   </tr><tr>
   <td align="left">&#160;&#160;&#160; 
   <A HREF="fsabfr"> Fachstatistik</A></td>
   </tr><tr>
   <td align="left">&#160;&#160;&#160;&#160;&#160;  
   <A HREF="formabfr6?file=abfritem"> Itemauswahl</A></td>
   </tr><tr>
   <td align="left">&#160;&#160;&#160;&#160;&#160;  
   <A HREF="formabfr6?file=abfrkat"> Kategorienauswahl</A></td>
   </tr>
   <tr>
   <td align="left">&#160;&#160;&#160; 
   <A HREF="jghabfr"> Bundesstatistik</A></td></tr><tr>
   </tr>
</table> """

administration_t = """
<th valign="top"><table><td>&#160;&#160;&#160;</td></tr></table>
<th valign="top"><table>
   <th align="center" bgcolor=#FFF5EE>
   <big> <A name="Admin"> Administration</A></big></th>
   </tr><tr>
   <td></td>
   </tr><tr>

   <td align="left"><B> Kategorien </B> </td>
   </tr><tr>
   <td align="left" >&#160;&#160;&#160; 
   <A HREF="codelist"> alle </A></td>
    </tr><tr>
   <td align="left" cellpadding=8>&#160;&#160;&#160;
   <A HREF="codetab?tabelle=Fachstatistik"> Fachstatistik</A></td>
     </tr><tr>
    <td align="left">&#160;&#160;&#160; 
    <A HREF="codetab?tabelle=Fachstatistikleistung"> Leistungen</A></td>
    </tr><tr>
   <td align="left">&#160;&#160;&#160; <A HREF="codetab?tabelle=Mitarbeiter"> 
     Mitarbeiter</A></td>
   </tr><tr>
   <td align="left"> <B> Mitarbeiter </B>
   </tr><tr>
   <td align="left">&#160;&#160;&#160;
   <A HREF="mitneu"> Neueintrag</A></td>
   </tr><tr>
   <td align="left">&#160;&#160;&#160; 
   <A HREF="mitausw"> &Auml;nderung</A></td>
   </tr><tr>
   <td align="left"><B> Akten </B> </td>
   </tr><tr>
   <td align="left">&#160;&#160; <A HREF="rmakten">l&ouml;schen</A></td>
   </tr><tr>
   <td align="left"><B> Stellenabgleich </B></td>
   </tr><tr>
   <td align="left">&#160;&#160;&#160; <A HREF="formabfrdbexport">Datenaustausch</A> </td> 
   </tr><tr>
   <td align="left">&#160;&#160;&#160; <A HREF="stellenabgleich">Protokolle</A> </td> 
   </tr><tr>
   <td align="left"> <B> Bundesstatistik </B></td>
   </tr><tr>
   <td align="left">&#160;&#160;&#160; <A HREF="formabfrjghexport">exportieren</A> </td>
   </tr><tr>
   <td align="left">&#160;&#160;&#160; <A HREF="jghexportlist">Downloadliste</A> </td>
   </tr><tr>
</table></th>
 """

dokumentation_t = """
<th valign="top"><table><td>&#160;&#160;&#160;</td></tr></table>
<th valign="top"><table>   
   <th align="center" bgcolor=#FFFFBB>
   <big> <A name="Doc"> Dokumentation</A></big></th>
   </tr><tr>
   <td></td>
   </tr><tr>
   <td align="left"><B> ICD 10 </B> </td>
   </tr><tr>
   <td align="left" >&#160;&#160;&#160;
   <A HREF="%sdoc/icd-10/index.html" target="_new">ICD-10 SGB V</A></td>
    </tr><tr>
   <td align="left"><B> EBKuS </B> </td>
   </tr><tr>
   <td align="left" >&#160;&#160;&#160; 
   <A HREF="%sdoc/ebkus/index.html" target="_new">Beschreibung</A></td>
      </tr><tr>
    </table></th>
    </table>
    </P><P>
    """

menufuss_t = """
</P><P>
<div align="right"><A HREF="#top">Seite Hoch</A>
</P>
<div align="center"><P>
<IMG SRC="/icons/blue.gif" WIDTH=550 HEIGHT=5><BR>
</P>
</DIV>
</BODY>
</HTML> """

top_t = """
<div align="right"><A HREF="#top">Seite Hoch</A>"""

##############################
# Neuer Text (Textararea)
#############################

vermneu_t = """ 
<table border=1 cellspacing=1 cellpadding=8>
<tr>
<td align="left"><B>Betr.: </B></td>
<td align="left"><input type="text" size=46 maxlength=255 name="betr"></td>
<td align="right"> 
<input type="text" size=2 maxlength=2 value="%(day)d" name="vd"><B>.</B> 
<input type="text" size=2 maxlength=2 value="%(month)d" name="vm"><B>.</B>
<input type="text" size=4 maxlength=4 value="%(year)d" name="vy"></td> 
</tr>
<tr>
<td align="left" colspan=3><textarea wrap="off" rows="25" cols="70" name="text"></textarea></td>
</tr>"""

vermneu2_t = """
<tr>
<td colspan="3">
 <B>Mitabeiter:</B> %(na)s 
<input type="hidden" name="mitid" value="%(id)s">
&#160;&#160;&#160;&#160;&#160;&#160;
<B>Der Text ist ein(e):</B> <select name="art">
 """

vermneu3_t = """
</select></td>
</tr></table>
"""

###############################
# Vermerkauswahlbox zum Aendern
###############################

vermausw_t = """
<table border=1 cellspacing=1 cellpadding=8>
<tr>
<th >Textauswahl</th>
</tr><tr>
<td><select name="dokid" size=15>"""

vermausw2_t = """
<option value="%(id)d"> %(vd)d.%(vm)d.%(vy)d | %(art__name)s | %(betr)s
"""

vermausw3_t = """ </select></td>
</tr>
</table>"""

##############################
# Vermerk aendern
#############################

vermupd_t = """ 
<table border=1 cellspacing=1 cellpadding=8>
<tr>
<td align="left"><B>Betr.: </B></td>
<td align="left"><input type="text" size=46 maxlength=255 name="betr" value="%(betr)s"></td>
<td align="right"> 
<input type="text" size=2 maxlength=2 value="%(vd)d" name="vd"><B>.</B> 
<input type="text" size=2 maxlength=2 value="%(vm)d" name="vm"><B>.</B>
<input type="text" size=4 maxlength=4 value="%(vy)d" name="vy"></td> 
</tr>
<tr>
<td align="left" colspan=3><textarea wrap="off" rows=25 cols=70 name="text">%(text)s</textarea></td>
</tr>
<td colspan=3>
<B>Mitabeiter:</B> %(mit_id__na)s 
<input type="hidden" name="mitid" value="%(mit_id)d">
&#160;&#160;&#160;&#160;&#160;&#160; <B>Der Text ist ein(e):</B> <select name="art">"""


##############################
# Alle Einträge lesen
#############################

vermlesen_t = """
<p>
<div align="left">
<table border=1 cellspacing=1 bgcolor="#FFFFFF" width="100%%">
<tr>
<td><B>%(art__name)s.:</B> %(betr)s </td>
<td align="right"> <B>%(vd)d.%(vm)d.%(vy)d</B> </td>
</tr><tr>
<td colspan=2>%(text)s </td>
</tr><tr>
<td colspan=2><B>MitarbeiterIn: </B> %(mit_id__na)s </td>
</table>
</p>
"""

vermerkausgabe1_t = """
<div align="center">
<table width="80%%">
<tr>
<th align="left">Vermerkindex</A></th>
</tr><tr>
<td><p>
<ul>
"""

vermerkausgabe2_t = """
<li> <A HREF="#%(id)d">%(vd)d.%(vm)d.%(vy)d</A>: %(betr)s (%(mit_id__na)s)</li>
"""

vermerkausgabe3_t = """
</ul></p>
<p>
<hr>
</p></td>
"""

vermerkausgabe4_t = """
</tr><tr>
<td>
<p>
<B><A name="%(id)d">%(art__name)s vom %(vd)d.%(vm)d.%(vy)d</A></B>, %(mit_id__na)s<BR>
<B>Betr.: %(betr)s </B>
</p>

<p>
%(text_html)s
<br>
</p>
<p><hr></p>
</td>"""

##############################
# Dokument löschen. Auswahlbox
###############################

rmverm_t = """
<table border=1 cellspacing=1 cellpadding=8>
<tr>
<th>Markierte Dokumente l&ouml;schen!</th>
</tr><tr>
<td align="center"><DL><DO><select name="dokids" multiple size=15>"""

rmverm2_t = """
<option value="%(id)d"> %(vd)d.%(vm)d.%(vd)d | %(art__name)s | %(betr)s
"""

rmverm3_t = """ </select></DL></DO> </td>
</tr>
</table>"""

#####################
# Dokumentenupload
#####################

uploadformh_t = """
<form action="%s" method="POST" enctype="multipart/form-data">
"""

formularh_t = """
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFCCCC>
    <th align="center"> %(akte_id__vn)s %(akte_id__na)s, %(akte_id__gb)s </th>
    <th align="right"><em> %(fn)s </em></th>
    </tr>
</table>
<input type="hidden" value="%(akte_id)d" name="akid">
<input type="hidden" value="%(id)d" name="fallid">
"""
formulargrh_t = """
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFCCCC>
    <th align="center"> %(name)s </th>
    <th align="right"><em> %(gn)s </em></th>
    </tr>
</table>
<input type="hidden" value="%(id)d" name="gruppeid">
"""

uploadform_t = """
<table border=1 cellspacing=1 cellpadding=8>
<tr>
<td align="left"><B>Betr.:</B> </td>
<td> <input type="text" size="50" maxlength="255" name="betr"> 
<input type="text" size=2 maxlength=2 value="%(day)d" name="vd"><B>.</B> 
<input type="text" size=2 maxlength=2 value="%(month)d" name="vm"><B>.</B>
<input type="text" size=4 maxlength=4 value="%(year)d" name="vy"></td> 
</tr><tr>
<td><B>Datei:</B> </td>
<td> <input name="datei" maxlength="1000000" type="file" size="50"><quote><B>&#160;&#160; *.pdf, *.txt, *.html</B></quote> </td>
""" 

uploadform2_t = """
</tr><tr>
<td colspan="2">
 <B>Mitabeiter:</B> %(na)s 
<input type="hidden" name="mitid" value="%(id)s">
&#160;&#160;&#160;&#160;&#160;&#160;
<B>Die Datei ist ein(e):</B> <select name="art"> 
"""

uploadform3_t = """
</select></td>
</tr></table>
"""

uploadhinweis_t = """
<div align="center"><B>Hinweis:</B> Bitte nur Dateien mit den Endungen
<quote><B>*.pdf</B> (Portable Document Format), <B>*.txt</B> (Text/Ascii) oder <B>*.html</B> </quote> f&uuml;r den Import in die Akte verwenden. 
<div align="left">
"""

##########################
# Dokumente anzeigen
##########################

dokausgabe1_t = """
<div align="center">
<table width="80%%">
<tr>
<th align="left">%s</th>
</tr><tr>
<td><p>
<dl>"""

dokausgabe2_t = """
<dt> <A HREF="dokview?fallid=%(fall_id)d&dokid=%(id)d" target="_new">%(vd)d.%(vm)d.%(vy)d</A>:</dt>
<dd><B>%(art__name)s:</B> %(betr)s (%(mit_id__na)s)</dd>
"""

dokausgabe2b_t = """
<dt> <A HREF="dokview?gruppeid=%(gruppe_id)d&dokid=%(id)d" target="_new">%(vd)d.%(vm)d.%(vy)d</A>:</dt>
<dd><B>%(art__name)s:</B> %(betr)s (%(mit_id__na)s)</dd>
"""

dokausgabe3_t = """
</dl></p>
<p>
<hr>
</p></td>
"""

dokausgabe4_t = """
<dt><B>Beraternotizen:</B> <A HREF="dokview2?fallid=%(id)d&art=bnotiz" target="_new">Text-Format</A> oder <A HREF="print_pdf?fallid=%(id)d&art=bnotiz" target="_new">PDF-Format</A></dt>
<dd> </dd>
"""

dokausgabe4b_t = """
<dt><B>Beraternotizen:</B> <A HREF="dokview2?gruppeid=%(id)d&art=bnotiz" target="_new">Text-Format</A> oder <A HREF="printgr_pdf?gruppeid=%(id)d&art=bnotiz" target="_new">PDF-Format</A></dt>
<dd> </dd>
"""

dokausgabe5_t = """
<dt><B>Aktentexte:</B> <A HREF="dokview2?fallid=%(id)d&art=anotiz" target="_new">Text-Format</A> oder <A HREF="print_pdf?fallid=%(id)d&art=anotiz" target="_new">PDF-Format</A></dt>
<dd> </dd>
"""
dokausgabe5b_t = """
<dt><B>Aktentexte:</B> <A HREF="dokview2?gruppeid=%(id)d&art=anotiz" target="_new">Text-Format</A> oder <A HREF="printgr_pdf?gruppeid=%(id)d&art=anotiz" target="_new">PDF-Format</A></dt>
<dd> </dd>
"""

dokausgabe6_t = """
</dl></p>
<p>
Es sind in der Printausgabe die Texte zusammengefasst, welche im Browser-Formular eingetippt oder als Text(Ascii)-Dateien (Endung *.txt) importiert wurden. Die importierten Dateien im PDF-Format (*.pdf) oder HTML-Format (*.html) sind einzeln aufzurufen und auszudrucken.
<hr>
</p></td>
"""
dokausgabe7_t = """
<div align="center">
<table width="80%%">
<tr>
<th align="left">%s</th>
</tr><tr>
<td><p>
<B>Suche</B> <input type="text" width="15" maxlength="60" value="%s" name="expr">
&#160;&#160;&#160;&#160;<input type="submit" value="Okay">
</form>
</td></table>"""

dokausgabe8_t = """
<dd>Zeile %s</dd>"""


################################
# Akten loeschen
################################


rmakten_t = """
<table border=1 cellspacing=1 cellpadding="8" bgcolor=#FFFFFF>
<tr>
<th bgcolor=#FFF5EE>Akten und Gruppen l&ouml;schen!</th>
</tr><tr>
<td> <P><B>Alle Akten und Gruppen der Stelle, die vor: <BR> 
<input type="text"  size="2" maxlength="2" name="frist" value="%d"> Monaten geschlossen wurden, sollen gelöscht werden!</B><BR> (Die Statistiken bleiben erhalten.) </P></td>
</tr>
</table>"""

rmakten2_t = """
<table border=1 cellspacing=1 cellpadding="8" bgcolor=#FFFFFF>
<tr>
<th bgcolor=#FFF5EE>Akten und Gruppen l&ouml;schen!</th>
</tr><tr>
<td> <P><B>Sollen alle Akten und Gruppen der Stelle, die vor: <BR>
%s Monaten, - %s.%s - geschlossen wurden,
jetzt gelöscht werden!</B><BR> (Die Statistiken bleiben erhalten.)</td>
</P></tr>
</table>"""

############################
# Neues Fachstatistikformular
############################

fsneumenu_t = """
<A HREF="menu">Men&uuml;</A> |
<A HREF="klkarte?akid=%(akte_id)d&fallid=%(id)d"> Klientenkarte</A> | 
<A HREF="dokkarte?akid=%(akte_id)d&fallid=%(id)d"> Akte</A> | 
<A HREF="formabfr3"> Suche</A>"""

fsneuformkopf_t = """
<FORM ACTION="%s" METHOD="post">"""

fsfallnummer_t = """    
<input type="hidden" value="%(id)s" name="fallid">
<table border=1 cellspacing=1  cellpadding="8" >
<tr>
<th align="center" colspan="4" ><B> Fallnr. </B>
   <input size=9  maxlength=9  value="%(fn)s" name="fall_fn">
    &#160;&#160;&#160;<A name="neu">&#160;<B>Mitarbeiter</B></A>     
    <select name="mitid">"""

fsstelle_t = """
    </select>
   <B>&#160;&#160;&#160;Stelle </B>
   <select name="stz"> """

fsjahr_t = """
    </select>
   <B>&#160;&#160;&#160; Jahr </B> 
   <input type="text" size=4 maxlength=4 value="%(year)d" name="jahr">
   </th></tr> """

fsregion_t = """
   <tr>
   <td colspan="2"> <B>Region </B> </td>
   <td colspan="2"> <select name="bz"> """
   
fsgeschlecht_t = """
   </select></td>
   </tr><tr>
   <td> <B>Geschlecht </B> </td>
   <td> <select name="gs"> """

fsaltersgruppe_t = """
    </select> </td>
    <td> <B>Alter Kind</B> </td>
    <td> <select name="ag">"""

fsgeschwisterreihe_t = """
    </select></td>
   </tr><tr>
   <td> <B>Geschwisterreihe</B> </td>
   <td> <select name="gr"> """

fskinderzahl_t = """
   </select></td>
   <td> <B>Kinderzahl im Haushalt</B> </td>
   <td> <input size=1 maxlength="2" value="%s" name="ka"> </td>"""

fsfamilienstatus_t = """
    </select></td>
    </tr><tr>
    <td> <B>Lebensmittelpunkt des Kindes</B> </td>
    <td> <select name="fs">"""

fszugangsmodus_t = """
    </select></td>
    <td> <B>Empfohlen von</B></td> 
    <td> <select name="zm"> """

fspsychotherfahrung_t = """
    </select></td> 
    </tr><tr>
    <td> <B>Erfahrung in Psychotherapie</B> </td>
    <td> <select name="ep"> """

fsfinanzdruck_t = """   
        </select></td>
        <td> <B>Finanz. Situation der Familie</B> </td>
        <td> <select name="sd"> """

fsberufmutter_t = """
     </select></td>
     </tr><tr>
     <td> <B>Beruf der Mutter</B> </td>
     <td> <select name="bkm">"""
                   
fsberufvater_t = """
       </select> </td>
       <td> <B>Beruf des Vaters</B> </td>
       <td> <select name="bkv"> """
        
fsherkunftmutter_t = """
     </select></td>
     </tr><tr>
     <td> <B>Herkunftsland der Mutter</B> </td>
     <td> <select name="hkm"> """

fsherkunftvater_t = """            
     </select> </td>
     <td> <B>Herkunftsland des Vaters</B> </td>
     <td> <select name="hkv"> """

fsaltermutter_t = """
     </select></td>
     </tr><tr>
     <td> <B>Alter der Mutter</B> </td>
     <td> <select name="agkm"> """

fsaltervater_t = """
     </select> </td>
     <td> <B>Alter des Vaters</B> </td>
     <td> <select name="agkv"> """

fsberatungsanlass1_t = """
        </select></td>
      </tr><tr> 
        <td colspan="2"> <B>Problemlagen bei der Anmeldung 1. </B> </td> 
        <td colspan="2"> <select name="ba1"> """

fsberatungsanlass2_t = """
        </select></td>
       </tr><tr>    
       <td colspan="2"> <B>Problemlagen bei der Anmeldung 2. </B> </td>
       <td colspan="2"> <select name="ba2"> """
        
fsproblemkind_t = """    
        </select></td>
        </tr><tr>
        <td colspan="2"> <B>Hauptproblematik Kind/Jugendliche</B> </td>
        <td colspan="2">  <select name="pbk"> """ 

fsproblemeltern_t = """
        </select></td>
        </tr><tr>
        <td colspan="2"> <B>Hauptroblematik der Eltern</B> </td>
        <td colspan="2"> <select name="pbe"> """

fsproblemspektrumkind_t = """
        </select></td>
        </tr><tr>
        <td align="center" colspan="2" >
        <DL><DO> <B>Problemspektrum Kind/Jugendliche</B> <BR>
          <select name="pbkind" multiple size="8"> """

fsproblemkindnot_t = """
        </select></DO></DL> <P>
        <B>Andersgeartete Problemlage</B><BR>
        <input size="33" maxlength="255" value="%s" name="no2"></P></td> """

fsproblemspektrumeltern_t = """
        <td  align="center" colspan="2">
        <DL><DO> <B>Problemspektrum Eltern</B> <BR>
        <select name="pbeltern" multiple size="8"> """

fsproblemelternnot_t = """
        </select></DO></DL> <P> 
        <B>Andersgeartete Problemlage</B><BR>
        <input size="33" maxlength="255" value="%s" name="no3"></P></td> """

fsmassnahmen_t = """
        </tr><tr>
        <td align="center" colspan="2" rowspan="3">
        <DL><DO><B>Erbrachte Leistungen</B><BR>
        <select name="le" multiple size=10 > """

fszahlkontakte_t = """
        </select></DO></DL><BR><font size="-1">
                           f&uuml;r die Mehrfachankreuzungen evtl. Strg u.
                           Maus dr&uuml;cken </font></td>
        <td colspan="2" align="center"> <B>Häufigkeit der Kontakte mit</B> <BR>
        <B>Km</B> <input size=2 maxlength=2 name="kkm">
        <B>Kv</B> <input size=2 maxlength=2 name="kkv">
        <B>Kind</B> <input size=2 maxlength=2 name="kki">
        <B>Fam.</B>  <input size=2 maxlength=2 name="kfa">
        <B>Paar</B> <input size=2 maxlength=2 name="kpa"><BR>
        <B>Soz.</B> <input size=2 maxlength=2 name="ksoz">
        <B>Lehr.</B> <input size=2 maxlength=2 name="kleh">
        <B>Erz.</B>  <input size=2 maxlength=2 name="kerz">
        <B>Sonst.</B> <input size=2 maxlength=2 name="kson"><BR>
        <div align="left"><P>
        <B>&#160;Terminsumme</B> <input size=2 maxlength=2 name="kat">
        </P></div> 
        </td>
        </tr><tr>
        <td> <B>&#160;Abschluss</B> </td>
        <td> <select name="bg"> """

fsnotizsubmit_t = """
        </select></td>
        </tr><tr>
        <td align="center" colspan="2">
        <B><input type="submit" value="Speichern"> </B>
        <input type="reset"  value="Reset"> </td>
        </tr><tr>
        <td>  <B>Notiz</B> </td>
        <td colspan="3"> <input size=70 maxlength="255" name="no"> </td>
        </tr>
</table>
</FORM>
<P> """

######################
# Fachstatistik aendern
######################

fsupdfallnummer_t = """    
   <input type="hidden" value="%(id)s" name="fsid">
   <input type="hidden" value="%(fall_id)s" name="fallid">
<table border=1 cellspacing=1  cellpadding="8">
    <tr>
    <th align="center" colspan="4" >&#160;<B>Fallnr. </B>
   <input size=9  maxlength=9 value="%(fall_fn)s" name="fall_fn">
    &#160;&#160;<B>Mitarbeiter</B>
    <select name="mitid">"""


fsupdzahlkontakteabschluss_t = """
        </select></DO></DL> <BR>
                        <font size="-1">hier f&uuml;r die Mehrfachantworten
                        Strg u. Maus dr&uuml;cken </font></td>
        <td align="center" colspan="2"> <B>Häufigkeit der Kontakte mit</B><BR> 
        <B>Km</B> <input size=2 maxlength=2 value="%(kkm)s" name="kkm">
        <B> Kv</B> <input size=2 maxlength=2 value="%(kkv)s" name="kkv">
        <B> Kind</B> <input size=2 maxlength=2 value="%(kki)s" name="kki">
        <B>Fam.</B>  <input size=2 maxlength=2 value="%(kfa)s" name="kfa">
        <B>Paar</B> <input size=2 maxlength=2 value="%(kpa)s" name="kpa"><BR>
        <B>Soz.</B> <input size=2 maxlength=2 value="%(ksoz)s" name="ksoz">
        <B>Lehr.</B> <input size=2 maxlength=2 value="%(kleh)s" name="kleh">
        <B>Erz.</B>  <input size=2 maxlength=2 value="%(kerz)s" name="kerz">
        <B>Sonst.</B> <input size=2 maxlength=2 value="%(kson)s" name="kson"><BR>
        <div align="left"><P>
        <B>&#160; Terminsumme</B> <input size=2 maxlength=2 value="%(kat)s" name="kat"></P></div></td>
        </tr><tr>
        <td> <B>&#160; Abschluss</B> </td>
         <td> <select name="bg"> """

fsupdnotizsubmit_t = """
        </select> </td>
        </tr><tr>
        <td align="center" colspan="2">
        <B><input type="submit" value="Speichern"> </B>
        <input type="reset"  value="Reset">
        </tr><tr>
        <td> <B>Notiz</B> </td>
        <td colspan="3"> <input size=70 maxlength="255" value="%(no)s" name="no"> </td>
       </tr> 
</table>
</FORM>
<P> """

####################################
# Neues Bundesstatistikformular
####################################

jghneuformkopf_t = """
<FORM ACTION="%(action)s" METHOD="post"> 
<input type="hidden" value="%(id)s" name="fallid"> """

jghmitarbeiter_t = """
<P>
<table border=1 cellspacing=0 cellpadding="8">
   <tr>
   <th align="left"> &#160; Mitarbeiter &#160;
   <select name="mitid"> """


jghfall_t = """
   </select> &#160;&#160; Fallnr. &#160;
   <input type="text" size=9 maxlength=9 value="%(fall_fn)s" name="fall_fn" >
   &#160;&#160; zus&auml;tzl. Geschwisterkind &#160; <select name="gfall"> """

jghbezirk_t = """
   </select>
   </th>
   </tr><tr>
   <td >&#160; <B>Land</B> &#160; <select name="rbz"> """

jghkreis_t = """
   </select> &#160;&#160; <B>Kreis</B> &#160;<select name="kr"> """

jghgemeinde_t = """
   </select> &#160;&#160; <B>Gemeinde</B> &#160; <select name="gm"> """

jghgemeindeteil_t = """
   </select> &#160;&#160; <B>Gemeindeteil</B> &#160; <select name="gmt"> """

jghtraeger_t = """
</select></td>
</tr></table>
</P>
<P>
<table border=0 cellspacing=0 cellpadding="0">
<tr>
<td valign="top" align="left">
<table border=1 cellspacing=1 cellpadding="8">
    <tr>
    <td  align="center">
    <select name="traeg"> """

jghbeginn_t = """
    </select></td>
    </tr><tr>
    <td><div align="center"><P><B>Beratungs-</B></div></P>
    <div align=left><P>
    <B>&#160;Beginn&#160;</B>
    <input type="hidden" value="%(bgd)s" name="bgd">
    <input type="text" size=2 maxlength=2  value="%(bgm)s" name="bgm"><B>.</B>
    <input type="text" size=4 maxlength=4  value="%(bgy)s" name="bgy"> """
    
jghende_t = """
     &#160;&#160;&#160;
     <B>Ende&#160;</B>
     <input type="hidden" value="%(day)d" name="ed">
     <input type="text" size=2 maxlength=2 value="%(month)d" name="em"><B>.</B>
     <input type="text" size=4 maxlength=4 value="%(year)d" name="ey"> 
     </P></div></td>
     </tr>
     <tr>
     <td align="center"><P> <B>Beendigungsgrund</B></P> <P>
     <select name="bgr"> """

jghgeschlecht_t = """
     </select> </P> </td>
     </tr>
    <tr>
    <td align="left"> &#160;<B>Geschlecht</B>&#160; 
       <select name="gs"> """

jghalter_t = """    
    </select> 
     &#160;&#160;&#160;<B>Alter</B>&#160;
    <select name="ag"> """

jghkindlebtbei_t = """
    </select> </td>
    </tr>
    <tr>
    <td align="left"> &#160;<B>lebt</B> &#160;
        <select name="fs"> """

jghstaatsangehoerigkeit_t = """
    </select> </td>
    </tr><tr>
    <td align="left"> &#160;<B>Staatsangehörigkeit</B>&#160;
      <select name="hke"> """           

jghgeschwisterzahl_t = """
    </select> </td>
    </tr><tr>
    <td align="left">&#160;<B>Geschwisterzahl</B>&#160;
    <input type="text" name="gsa" size=2 maxlength=2> &#160;&#160;&#160; 
    <B>unbekannt</B>&#160; <input type="checkbox" value="%(id)d" name="gsu"></td>
    </tr><tr>
    <td align="left">&#160;
    <B>1. Kontakt durch</B>&#160;
     <select name="zm"> """         

jghberatungsanlass_t = """
    </select></td>
    </tr>
    </table>
    </td> <td valign="top"  align="left" >
    <table border=1 cellspacing=1 cellpadding="8">
    <tr>
    <td align="center"> <B>Beratungsanlass</B><BR> 
    <em><small>bis zu 2 Ankreuzungen</em></small><P>
    <P>
    <select name="ba"  multiple size=7 > """

jghberatungsschwerpunkt_t = """
    </select></P><P>
    <em><small>evtl. Steuerungstaste u. Maus drücken</em></small></P></td>
    </tr><tr>
    <td align="center"><B>Beratungsschwerpunkt</B> <P>
    <select name="schw"> """

jghansaetzekind1_t = """
    </select></P> </td>
    </tr><tr>
    <td align="center"> <B>Beratung bzw. Therapie setzt an</B><BR>
    <em><small>bis zu 2 Ankreuzungen der hauptsächlichen Formen</em></small> </td>
    </tr><tr>
    <td align="left"> &#160;bei dem jungen Menschen <em><small>&#160;nur 1 Ankreuzung</em></small><BR>
    &#160;allein """

jghansaetzekind2_t = """
        &#160;&#160;&#160;in der Gruppe """

jghansaetzeeltern1_t = """
    &#160;&#160; </td>
    </tr><tr>
    <td align="left"> &#160;bei den Eltern <em><small>&#160;nur 1 Ankreuzung</em></small>
    <BR>&#160;allein """

jghansaetzeeltern2_t = """
     &#160;&#160;&#160;in der Gruppe """

jghansaetzefamilie_t = """
          &#160;&#160; </td>
    </tr>
    <tr>
    <td align="left"> &#160;in der Familie <input type="checkbox" value="%(id)d" name="%(kat_code)s" > """

jghansaetzeumfeld_t = """
    &#160;&#160;&#160; im sozialen Umfeld <input type="checkbox" value="%(id)d" name="%(kat_code)s" > &#160;&#160; </td>
    </tr>
</table>
</td></tr>
</table></P> """


##############################
# Bundesstatistik aendern
##############################

jghcodeliste_t = """ 
      <option value="%(id)d" %(sel)s > %(name)s """

jghbeginnupd_t = """
    </select></td>
    </tr><tr>
    <td align="left"><div align="center"><P><B>Beratungs-</B></div></P>
    <div align=left><P>
    <B>&#160;Beginn&#160;</B>
    <input type="hidden" value="" name="bgd">
    <input type="text" size=2 maxlength=2  value="%(bgm)s" name="bgm"><B>.
    <input type="text" size=4 maxlength=4  value="%(bgy)s" name="bgy"> """
    
jghendeupd_t = """
     &#160;&#160;&#160;
     <B>Ende&#160;</B>
     <input type="text" size=2 maxlength=2 value="%(em)s" name="em"><B>.
     <input type="text" size=4 maxlength=4 value="%(ey)s" name="ey">
     </P></div></td></tr>
     <tr>
     <td align="center"><P><B>Beendigungsgrund</B><BR></P><P>
     <select name="bgr"> """

jghgszahlupd_t = """
    </select> </td>
    </tr><tr>
    <td align="left">&#160;<B>Geschwisterzahl</B>&#160;
    <input type="text" value="%(gsa)s" name="gsa" size=2 maxlength=2> &#160;&#160;&#160;
    <B>unbekannt</B> <input type="checkbox" value="%(gsu)s" name="gsu" %(check)s></td>
    </tr><tr>
    <td align="left">&#160;
    <B>1. Kontakt durch</B> 
    <select name="zm"> """         

jghansaetzefam_t = """
          &#160;&#160;</td>
    </tr>
    <tr>
    <td align="left">&#160;in der Familie  """

jghansaetzeumf_t = """
    &#160;&#160; im sozialen Umfeld """

jghupdende_t = """
    &#160;&#160;</td>
    </tr>
</table>
</td></tr>
</table> """

######################################
# Statistikformular-Auswahl zum Update
######################################

thupdstausw_t = """
<table><th align="center" bgcolor=#FFFFCC> <big> %s </big></th>
    </tr><tr>
    <td align="left">
    <select size=%s name="%s"> """

updfsausw1_t = """
     <option value="%(id)s" >%(fall_fn)s | %(jahr)s | %(mit_id__na)s """

updjghausw1_t = """
     <option value="%(id)s" >%(fall_fn)s | %(ey)s | %(mit_id__na)s """

updstausw2_t = """
    </select></td>"""

#####################
# Aktenvorblatt
#####################

vkopf_t = """
<basefont size=2><B>Aktenvorblatt vom %(day)d.%(month)d.%(year)d </B><P> """

vakten1_t = """
<div align="left">
<table border=1  width=100%% cellspacing=1 cellpadding=2 bgcolor=#FFFFFF> 
  <th align="center" colspan=9 >
    Eltern, Geschwister, Verwandte</th>
  </tr><tr>
<th align="center" width=3%% ><font size=2><em>  Vrw. </em></th>
<th align="center" width=15%% ><font size=2><em> Vorname </em></th>
<th align="center" width=25%% ><font size=2><em> Name </em></th>
<th align="center" width=6%% ><font size=2><em>  geb. </em> </th>
<th align="center" width=30%% ><font size=2><em> Str.  </em> </th>
<th align="center" width=6%% ><font size=2><em>  Plz.  </em></th>
<th align="center" width=5%% ><font size=2><em>  Ort  </em> </th>
<th align="center" width=8%% ><font size=2><em>  Tel. </em> </th>
<th align="center" width=8%% ><font size=2><em>  Dtel. </em></th>
</tr><tr>
<td align="left" >&#160;<font size=2><em> Klient </em></td>
<td align="left" ><font size=2>&#160;<B> %(vn)s </B></td> 
<td align="left" ><font size=2>&#160;<B> %(na)s </B></td> 
<td align="left" ><font size=2>&#160;<B> %(gb)s </B></td> 
<td align="left" ><font size=2>&#160; %(str)s </td> 
<td align="left" ><font size=2>&#160; %(plz)s </td> 
<td align="left" ><font size=2>&#160; %(ort)s </td> 
<td align="left" ><font size=2>&#160; %(tl1)s </td> 
<td align="left" ><font size=2>&#160; %(tl2)s  </td> 
</tr>"""

vakten2_t = """
<tr> 
<td align="left"  cellpadding=0><font size=1>&#160; </td>
<td align="left" colspan=3    cellpadding=0><font size=1> 
&#160;<em> Ausbildung: </em>%(ber)s </td> 
<td align="left" colspan=2    cellpadding=0><font size=1> 
&#160; <em> bei &#160;</em> %(fs__name)s </td> 
<td align="rigth" colspan=3    cellpadding=0> <font size=1> 
&#160; %(nobedakte)s </td> 
</tr> """

vbezugspersonen1_t = """
  <tr>
  <td align="left" ><font size=2>&#160;<em> %(verw__name)s </em></td>
  <td align="left" ><font size=2>&#160; %(vn)s   </td>
  <td align="left" ><font size=2>&#160; %(na)s   </td>
  <td align="left" ><font size=2>&#160; %(gb)s   </td>
  <td align="left" ><font size=2>&#160; %(str)s  </td>
  <td align="left" ><font size=2>&#160; %(plz)s  </td>
  <td align="left" ><font size=2>&#160; %(ort)s  </td>
  <td align="left" ><font size=2>&#160; %(tl1)s  </td>
  <td align="left" ><font size=2>&#160; %(tl2)s  </td>
  </tr>"""

vbezugspersonen2_t = """
  <tr>
  <td align="left"   cellpadding=0>&#160;</td>
  <td align="left"  colspan=3  cellpadding=0><font size=1>
  &#160; <em>Beruf/Ausb: </em> %(ber)s </td>
  <td align="left"  colspan=2  cellpadding=0><font size=1>
  &#160;<em> bei&#160;</em> %(fs__name)s </td>
  <td align="rigth"  colspan=3  cellpadding=0><font size=1>
  &#160; %(nobed__name)s </td>
  </tr> """

vbezugspersonenzeile_t = """
  <tr>
  <td align="left" ><font size=2>&#160;  </td>
  <td align="left" ><font size=2>&#160;  </td>
  <td align="left" ><font size=2>&#160;  </td>
  <td align="left" ><font size=2>&#160;  </td>
  <td align="left" ><font size=2>&#160;  </td>
  <td align="left" ><font size=2>&#160;  </td>
  <td align="left" ><font size=2>&#160;  </td>
  <td align="left" ><font size=2>&#160;  </td>
  <td align="left" ><font size=2>&#160;  </td>
  </tr>"""

veinrichtungs_kopf1_t =  """
</table>

<table border=1 width=100%% cellspacing=1  cellpadding=2 bgcolor=#FFFFFF>
<th align="center" colspan=5> 
Einrichtungskontakt </th>
</tr> """

veinrichtungs_kopf2_t = """
<tr>
<th align="center" ><font size=2><em> Art </em></th>
<th align="center" ><font size=2><em> Name, Adresse, Ansprechperson </em></th>
  <th align="center" ><font size=2><em> Tel1 </em></th>
  <th align="center" ><font size=2><em> Tel2 </em></th>
  <th align="center" ><font size=2><em>  aktuell </em></th>
  </tr> """

veinrichtung_t =  """
  <tr>
  <td align="left" ><font size=2>&#160; %(insta__name)s </td>
  <td align="left" ><font size=2>&#160; %(na)s 
  &#160;&#160;&#160;&#160;&#160;&#160;%(nobed__name)s </td>
  <td align="left"><font size=2>&#160; %(tl1)s </td>
  <td align="left"><font size=2>&#160; %(tl2)s </td>
  <td align="left"><font size=2>&#160; %(status__code)s </td>
  </tr> """

veinrichtungszeile_t =  """
  <tr>
  <td align="left" ><font size=2>&#160;  </td>
  <td align="left" ><font size=2>&#160;  
  &#160;&#160;&#160;&#160;&#160;&#160; </td>
  <td align="left"><font size=2>&#160;  </td>
  <td align="left"><font size=2>&#160;  </td>
  <td align="left"><font size=2>&#160;  </td>
  </tr> """

vanmeldung_kopf_t = """
</table> 

<div align="left">
<table border=1 cellspacing=1 cellpadding=2 bgcolor=#FFFFFF>
<th align="center" colspan=2 >
  <B> Anmeldeinformation </B></th>
  </tr> """

vanmeldung_t = """
<tr>
<td align="left" ><font size=2>&#160;<em> gemeldet von </em></td>
<td align="left" width=100%% ><font size=2>
&#160; %(von)s  am&#160; %(ad)d.%(am)d.%(ay)d. Tel.:&#160; %(mtl)s 
&#160;&#160;&#160;&#160;&#160; %(nobedanm)s </td>
</tr><tr>
<td align="left" ><font size=2>
&#160;<em> Zugangsmodus </em></td>
<td align="left" ><font size=2>
&#160; %(zm__name)s&#160; <em>auf Empfehlung von </em> %(me)s 
</td>
</tr><tr>
<td align="left" ><font size=2>&#160;<em> Anmeldegrund </em></td> 
<td align="left"><font size=2>&#160; %(mg)s </td>
</tr> """

vleistungs_kopf_t = """
</table> 

<table border=0 cellspacing=0 cellpadding=0 width=100%%><td valign="top" width="40%%">
<table border=1 cellspacing=1 cellpadding=2 width=100%% bgcolor=#FFFFFF>
<th align="center" colspan=4 width=100%%> Leistung </th>
</tr><tr>
<th align="center" ><font size=2><em> Mitarbeiter </em></th>
<th align="center" ><font size=2><em> Leistung </em></th>
<th align="center" ><font size=2><em> am </em></th>
<th align="center" ><font size=2><em> bis </em></th>
</tr> """

vleistungs_t =  """
<tr>
<td align="left" ><font size=2>&#160; %(mit_id__na)s </td>
<td align="left"><font size=2>&#160; %(le__name)s </td>
<td align="left"><font size=2>&#160; %(bgd)d.%(bgm)d. %(bgy)d </td> """

vleistungsendeleer_t = """
<td align="left"><font size=2><font size=2>&#160; </td>
</tr> """

vleistungsendedatum_t = """
<td align="left"><font size=2>&#160; %(ed)d.%(em)d. %(ey)d </td>
</tr> """

vleistungszeile_t =  """
<tr>
<td align="left" ><font size=2>&#160;  </td>
<td align="left"><font size=2>&#160;  </td>
<td align="left"><font size=2>&#160;  </td>
<td align="left"><font size=2>&#160; </td>
</tr> """

vbearbeiter_kopf_t = """
</table>

</td><td valign="top" width="35%%">
<table border=1  cellspacing=1 cellpadding=2 width=100%% bgcolor=#FFFFFF>
<th align="center" colspan=3 width=100%%> Bearbeiter </th>
</tr><tr>
<th align="center" ><font size=2><em> Bearbeiter </em></th>
<th align="center" ><font size=2><em> Beginn </em></th>
<th align="center" ><font size=2><em> Ende </em></th>
</tr> """

vbearbeiter_t = """
<tr>
<td align="left" ><font size=2>&#160; %(mit_id__na)s </td>
<td align="left"><font size=2>&#160; %(bgd)d.%(bgm)d. %(bgy)d </td> """

vbearbeiterendeoffen_t = """
<td align="left"><font size=2>&#160; </td>
</tr> """

vbearbeiterendedatum_t = """
<td align="left"><font size=2>&#160;  %(ed)d.%(em)d. %(ey)d </td>
</tr> """

vbearbeiterzeile_t = """
<tr>
<td align="left" ><font size=2>&#160;  </td>
<td align="left"><font size=2>&#160;  </td>
<td align="left"><font size=2>&#160; </td>
</tr> """

vfall_kopf_t =  """
</table>

</td><td valign="top" width="25%%">
<table border=1 cellspacing=1 cellpadding=2 width=100%% bgcolor=#FFFFFF>
<th align="center" colspan=3 width=100%%> Stand </th>
</tr><tr>
<th align="center" ><font size=2><em> Fallnr. </em></th>
<th align="center" ><font size=2><em> Beginn </em></th>
<th align="center" ><font size=2><em> z.d.A. </em></th>
</tr>"""

vfall_t = """
<tr>
<td align="left" ><font size=2>&#160; %(fn)s </td>
<td align="left" ><font size=2>&#160; %(bgd)d.%(bgm)d. %(bgy)d </td> """

vfalloffen_t = """
<td align="left" >&#160;</td>
</tr> """

vfallendedatum_t = """
<td align="left" ><font size=2>&#160; %(zdad)d.%(zdam)d. %(zday)d </td>
</tr> """

vfallzeile_t = """
<tr>
<td align="left" ><font size=2>&#160;  </td>
<td align="left" ><font size=2>&#160;  </td>
<td align="left" ><font size=2>&#160;</td>
</tr> """

vtabende_t = """
</table></td></tr>
</table> """

vnotiz_t = """
<P><div align="left">
<table > 
<th align="center"> <A name="notiz"> <em> Notiz zu </em></A></th>
</tr>
</table>
"""
vnotizakte_t = """
<font size=2><B> %(vn)s %(na)s: </B><em> %(no)s </em><BR>"""
vnotizbperson_t ="""
<B> %(vn)s %(na)s: </B><em> %(no)s</em> <BR>"""
vnotizeinr_t ="""
<B> %(insta__name)s %(na)s: </B><em> %(no)s </em><BR>"""
vnotizanm_t ="""
<B> Anmeldung: </B><em> %(no)s </em><BR>"""


###########################
# Fachstatistik Abfrage
###########################

fsabfrjahr_t = """
<FORM ACTION="%(file)s"  METHOD="post"> 
<table border=1 cellspacing=1 cellpadding=8>
       <td align="center"> <B>Jahr </B> 
       <td align="left">
       <select name="op">
       <option value="="> gleich
       <option value="<"> kleiner als
       <option value=">"> gr&ouml;sser als 
       </select>
       <input type="text" size="4" maxlength="4" value="%(year)s" name="year"></td>"""

fsabfrstelle_t = """
       </tr>
       <tr>	
       <td align="center">(und) <B>Stelle(n)</B> </td>
        <td align="left" rowspan=2>
        <select name="stz" multiple size=6> """

fsabfrtabende_t = """ 
       </select> </td>
       </tr>
</table> """


#############################
# Fachststatistikergebnis
#############################


gesamtzahl_t = """
<B> Klientenzahl: %d von %d </B><P>
Abfrage: %s <P>
"""

thkategorie_t = """
<HR><div align="center">
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFFFFF>
     <th align="center">&#160; %(name)s </th>
     <th align="center">&#160; S            </th>
     <th align="center">&#160; %% </th>
     </tr> """

thkategoriejgh_t = """
<HR><div align="center">
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFFFFF>
     <th align="center">&#160; %s </th>
     <th align="center">&#160; S            </th>
     <th align="center">&#160; %% </th>
     </tr> """

item_t = """
    <tr>
    <td align="left">  %s </td>
    <td align="right"> %s </td>
    <td align="right"> %.2f </td></tr> """

######################################################################
# Abfrage: Alle, Laufende, abgeschl. Zuständigkeiten; abfr1-abfr3
######################################################################

thabfr1_t = """
<div align="center">
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFFFFF>
    <th align="center">Fallnr.</th>
    <th align="center">Vorname</th>
    <th align="center">Name</th>
    <th align="center">gb</th>
    <th align="center">Bearbeiter</th>
    <th align="center">von</th>
    <th align="center">bis</th>
    <th align="center">Beginn</th>
    <th align="center">z.d.A.</th>
    </tr> """

abfr1_t = """    
    <tr>
    <td align="left"><A HREF="klkarte?akid=%(fall_id__akte_id)d&fallid=%(fall_id)d"> %(fall_id__fn)s</A></td>
    <td align="left">&#160; %(fall_id__akte_id__vn)s </td>
    <td align="left"> %(fall_id__akte_id__na)s </td>
    <td align="left"> %(fall_id__akte_id__gb)s </td>
    <td align="left">  %(mit_id__na)s </td>
    <td align="right"> %(bgd)d.%(bgm)d.%(bgy)d</td>
    <td align="right"> %(ed)d.%(em)d.%(ey)d</td>
    <td align="right"> %(fall_id__bgd)d.%(fall_id__bgm)d.%(fall_id__bgy)d </td>
    <td align="right"> %(fall_id__zdad)d.%(fall_id__zdam)d.%(fall_id__zday)d</td>
    </tr> """

abfr3a_t = """    
    <tr>
    <td align="left"><A HREF="klkarte?akid=%(fall_id__akte_id)d&fallid=%(fall_id)d"> %(fall_id__fn)s</A></td>
    """
abfr3b_t = """
    <td align="left">&#160;  %(vn)s </td>
    <td align="left">         %(na)s </td>
    """
abfr3c_t = """
    <td align="left"> %(fall_id__akte_id__gb)s </td>
    <td align="left"> %(mit_id__na)s </td>
    <td align="right"> %(bgd)d.%(bgm)d.%(bgy)d</td>
    <td align="right"> %(ed)d.%(em)d.%(ey)d</td>
    <td align="right"> %(fall_id__bgd)d.%(fall_id__bgm)d.%(fall_id__bgy)d </td>
    <td align="right"> %(fall_id__zdad)d.%(fall_id__zdam)d.%(fall_id__zday)d</td>
    </tr> """

thabfrgr_t = """
<table cellpadding="8">
<tr>
<th> Gruppe </th><th> Thema </th><th> Beginn </th><th> Ende </th>"""

abfrgr_t = """
</tr><tr>
<td><A HREF="gruppenkarte?gruppeid=%(id)d">%(name)s</A> </td>
<td> %(thema)s </td>
<td> %(bgd)d.%(bgm)d.%(bgy)d </td><td> %(ed)d.%(em)d.%(ey)s </td>"""    

######################################################
# Suchformular für Akten über Name, Vorname, Fallnummer
######################################################

stz_t = """
<table border=1 cellspacing=1 cellpadding="8">
    <th align="center"><select name="stz"> """

suchwort_t = """
    </select>
    <th> <select name="table">
    <option value="akte" selected> Vor- oder Nachname, Klient
    <option value="bezugsperson"> Vor- oder Nachname, Bezugsperson
    <option value="fall"> Beratungsfallnummer
    <option value="gruppe"> Gruppe
    </select>
    </th></tr>
    <tr>
    <td>&#160;<B> Suchausdruck: </B></td>
    <td>&#160;<input type="text" size=30 maxlength=30 name="expr"></td>
    </tr>
</table>"""

suchefallnummer_t = """
    </select>
    <th> <select name="table">
<!--    <option value="akte"> Vor- oder Nachname, Klient
    <option value="bezugsperson"> Vor- oder Nachname, Bezugsperson //-->
    <option value="fall" selected> Beratungsfallnummer
    </select>
    </th></tr>
    <tr>
    <td>&#160;<B> Suchausdruck: </B></td>
    <td>&#160;<input type="text" size=30 maxlength=30 name="expr"></td>
    </tr>
</table>"""

suchhilfe_t = """ 
       <h4>Suchhilfe</h4>
       <div align="left">
       <blockquote>
       <blockquote>
      <ul> 
      <li> Zuerst die Optionen <B>`Stelle'</B> und <B>`Suchart'</B>
      (Klient, Bezugsperson, Beratungsfallnummer, Gruppe)
      ausw&auml;hlen.  
      <li><B>Gross- und Kleinbuchstaben</B> werden nicht unterschieden.  
      <li> Es wird nach W&ouml;rtern gesucht, 
      welche <B>den eingegebenen Suchausdruck
      exakt enthalten.</B><BR> 
      <tt>meier</tt> findet <tt>Angermeier</tt>, <tt>Meierhof</tt>, 
       aber nicht <tt>Maier</tt>.<BR> 
      <tt>-1998%(code)s</tt> findet alle F&auml;lle der %(name)s 
       des Jahres 1998.<BR> 
      <li> <B>Ein Unterstrich <tt>_</tt></B> ersetzt ein einziges beliebiges
      Zeichen im Suchwort. <BR> 
      <tt>Me_er</tt> findet <tt>Meier</tt>, <tt>meyer</tt>, 
      <tt>Mecer-Antares</tt>.<BR> 
      <tt>M__er</tt> findet u.a. <tt>Mayer</tt>, <tt>Meier</tt>, 
       <tt>Sachs-Maler</tt>.
      <li>Die Ergebnisliste zeigt zum je gefundenen Wort <B>den letzten
       bzw. aktuellen Beratungsfall der Akte</B> oder die Gruppen.
      <li>Jeder Mitarbeiter erh&auml;lt bei der 
      Suche nur `seine' Klienten bzw. Gruppen angezeigt.<BR>
      </ul> 
      <div alig="center">
      </blockquote>
      </blockquote>
      """


###########################################################
# Abfrage für Anzahl der Neumeldungen u. zdA's 
###########################################################

thabfr4_t = """
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFFFFF>
    <th align="center">Monat</th>
    <th align="center">Neu</th>
    <th align="center">z.d.A. </th>
    </tr> """

abfr4_t = """
    <tr>
    <td align="right">%d  </td>
    <td align="right">%d  </td>
    <td align="right">%d   </td>
    </tr> """ 

abfr4ges_t = """
    <tr>
    <td align="left"><B> Quartal 1 </B> </td>
    <td align="right"><B> %d </B> </td>
    <td align="right"><B> %d </B> </td>
    </tr>
    <tr>
    <td align="left"><B> Quartal 2 </B> </td>
    <td align="right"><B> %d </B> </td>
    <td align="right"><B> %d </B> </td>
    </tr>
    <tr>
    <td align="left"><B> Quartal 3 </B> </td>
    <td align="right"><B> %d </B> </td>
    <td align="right"><B> %d </B> </td>
    </tr>
    <tr>
    <td align="left"><B> Quartal 4 </B> </td>
    <td align="right"><B> %d </B> </td>
    <td align="right"><B> %d </B> </td>
    </tr>
    <tr>
    <td align="left"><B> Gesamt </B> </td>
    <td align="right"><B> %d </B> </td>
    <td align="right"><B> %d </B> </td>
    </tr>
</table> """


############################################
# Abfrage für Klientenzahlen pro Mitarbeiter
############################################

thformabfr5_t = """
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFFFFF>
<tr>
<th><P> %s f&uuml;r das Jahr: &#160;<input type="text" size="4" maxlength="4" value="%s" name="jahr"></B><BR> """

formabfr5_2_t = """
</P></th></tr>
</table>
"""

thabfr5_t = """
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFFFFF>
<tr>
    <th align="center"> Mitarbeiter </th>
    <th align="center"> Neu %s </th>
    <th align="center"> Laufend </th>
    <th align="center"> Beendet </th>
    </tr> """

abfr5_t = """
    <tr>
    <td align="left"> %s  </td>
    <td align="right"> %s  </td>
    <td align="right"> %s   </td>
    <td align="right"> %s   </td>
    </tr> """ 

abfr5ges_t = """
    <tr>
    <td align="left"><B> Gesamt </B> </td>
    <td align="right"><B> %d </B> </td>
    <td align="right"><B> %d </B> </td>
    <td align="right"><B> %d </B> </td>
    </tr>
</table> """


##########################
# Gruppen, Menü
##########################


auswahlgrmenu_t = """
</P>
<div align="center">
<P>
<FORM ACTION="gruppenkarte" METHOD="post">

<table cellpadding="8">

<th valign="top"><table>
    <th align="center" bgcolor=#FFFFBB><big>Neu</big></th>
    </tr><tr><td align="left">
    <input type="radio" value="gruppeneu" name="file"><B> Gruppe</B>
    </td></tr><tr>
    <td>&#160; </td>
    </tr><tr>
    <th align="center"  bgcolor=#FFFFBB> <big> Ansicht</big></th>
    </tr><tr><td align="left">
    <input type="radio" value="gruppeteiln" name="file"><B> Teilnehmer</B></td>
    </tr><tr><td align="left">
    <input type="radio" value="gruppenkarte" name="file"><B> Gruppenakte</B></td>
    </tr><tr>
    <td>&#160;</td>
    </tr><tr>
    <th align="center"  bgcolor=#FFFFBB> <big> Suche </big> </th>
    </tr><tr><td align="left">
    <input type="radio" value="formabfr3" name="file"><B> Klientenkarte </B></td>
    </tr><tr><td align="left">
    <input type="radio" value="formabfr3" name="file"><B> Gruppenkarte </B></td>
    </tr><tr>
    <td>&#160;</td>
    </tr><tr><td align="left">
     <B><input type="submit" value="Okay">
     <input type="reset"  value="Reset"></B></td>
     </tr>
</table></th>

<th valign="top"><table><th align="center" bgcolor=#FFCCCC> <big>Gruppe</big></th>
    </tr><tr>
    <td align="left">
    <select size=16 name="gruppeid"> """

gruppenauswahl_t = """
<option value="%(gruppe_id)s" >%(mit_id__na)s | %(gruppe_id__name)s"""

menugrsubmit_t = """
     </select>
     </td>
     </tr>
     <tr><td>&#160;</td>
     </tr>
     <tr><th> Klientenkartei <A HREF="menu"> hier</A> </th>
     </tr>
</table></th>
</tr>
</table>
</form>
</P> """


######################################
# Neue Gruppe
######################################

gruppeneu_t = """
<div align="center">
<FORM ACTION="gruppenkarte" METHOD="post"> 
<div align="center">
<table border=1 cellspacing=1 cellpadding=8 bgcolor=#FFCCCC>
    <th align="center"> Gruppe  </th>
    <th align="center"> <em> %(gn)s </em></th>
    </tr>
</table>"""

gruppeneu1_t = """
<table border=1 cellspacing=1 cellpadding="8">
<tr><td> <B>Gruppenname:</B> </td>
<td colspan="2"><input type="text" size="60" maxlength="255" name="name" value=""></td>
</tr><tr>
<td> <B>Thema:</B> </td>
<td colspan="2"> <textarea wrap=off rows="4" cols="60" name="thema"></textarea></td>
</tr><tr>
<td> <B>Beginndatum:</B> </td><td>
  <input type="text" size=2 maxlength=2 value=""  name="bgd"><B>.</B>
  <input type="text" size=2 maxlength=2 value="%(month)d" name="bgm"><B>.</B>
  <input type="text" size=4 maxlength=4 value="%(year)d" name="bgy"> </td><td>
<B>Endedatum:</B>
  <input type="text" size=2 maxlength=2 name="ed"><B>.</B>
  <input type="text" size=2 maxlength=2 name="em"><B>.</B>
  <input type="text" size=4 maxlength=4 name="ey"> </td>
</tr><tr>
<td> <B>Teilnehmer:</B> </td><td>
    <select name="teiln">"""

gruppeneu2_t = """
    </select></td><td> <B>Die Gruppe ist ein(e):</B> <select name="grtyp">"""

gruppeneu3_t = """
    </select> </td>
</tr><tr>
<td rowspan="4"> <B>Mitarbeiter:</B> </td><td> <select multiple size="4" name="mitid" >"""

gruppeneu4_t = """
    </select>
    </td><td rowspan="4">
    <B> Teilnehmerzahl: <input type="text" name="tzahl" size="2" maxlength="3">
    Stundenzahl: <input type="text" name="stzahl" size="3" maxlength="3"> <BR><BR>
    
    <input type="submit" value="Speichern">
    <input type="reset"  value="Reset"></B></td>
</tr></table>
</FORM>"""

##############################
# Update Gruppe
##############################

gruppeupd1_t = """
<table border=1 cellspacing=1 cellpadding="8">
<tr><td> <B>Gruppenname:</B> </td>
<td colspan="2"><input type="text" size="60" maxlength="255" name="name" value="%(name)s"></td>
</tr><tr>
<td> <B>Thema:</B> </td>
<td colspan="2"> <textarea wrap=off rows="4" cols="60" name="thema">%(thema)s</textarea></td>
</tr><tr>
<td> <B>Beginndatum:</B> </td><td>
  <input type="text" size=2 maxlength=2 value="%(bgd)d"  name="bgd"><B>.</B>
  <input type="text" size=2 maxlength=2 value="%(bgm)d" name="bgm"><B>.</B>
  <input type="text" size=4 maxlength=4 value="%(bgy)d" name="bgy"> </td><td>
<B>Endedatum:</B>
  <input type="text" size=2 maxlength=2 value="%(ed)d" name="ed"><B>.</B>
  <input type="text" size=2 maxlength=2 value="%(em)d" name="em"><B>.</B>
  <input type="text" size=4 maxlength=4 value="%(ey)d" name="ey"> </td>
</tr><tr>
<td> <B>Teilnehmer:</B> </td><td>
    <select name="teiln">"""

gruppeupd3_t = """
    </select> </td>
</tr><tr>
<td rowspan="4"> <B>Mitarbeiter:</B> </td><td> """

gruppeupd4_t = """
    </select>
    </td><td rowspan="4">
    <B> Teilnehmerzahl: <input type="text" size="2" maxlength="3" name="tzahl" value="%(tzahl)s"> 
    Stundenzahl: <input type="text" size="3" maxlength="3" name="stzahl" value="%(stzahl)s"> <BR><BR>
    
    <input type="submit" value="Speichern">
    <input type="reset"  value="Reset"></B></td>
</tr></table>
</FORM>"""

#############################################
# Teilnehmer der Gruppe zuordnen und löschen (b)
#############################################


teilnauswahl_t = """
<table border=1 cellspacing=1 cellpadding="8">
<tr>
<th> Fall (Kind/Jugendlicher) </th><th> </th><th> Familienangeh&ouml;rige </th>
</tr><tr>
<td valign="top" align="center"><select multiple size="10" name="fallid">"""

teilnauswahlb_t = """
<table border=1 cellspacing=1 cellpadding="8">
<tr>
<th> Fall (Kind/Jugendlicher) </th><th> </th><th> Familienangeh&ouml;rige </th>
</tr><tr>
<td valign="top" align="center"><select multiple size="10" name="fallid">"""

teilnauswahl1_t = """
  <option value="%(fall_id)s">%(fall_id__akte_id__na)s %(fall_id__akte_id__vn)s| %(fall_id__fn)s"""

teilnauswahl1b_t = """
  <option value="%(id)s">%(fall_id__akte_id__na)s %(fall_id__akte_id__vn)s| %(fall_id__fn)s"""

teilnauswahl2_t = """
        </select></td><td> </td>
<td valign="top" align="center"><select multiple size="10" name="bezugspid">"""
teilnauswahl2b_t = """
        </select></td><td> </td>
<td valign="top" align="center"><select multiple size="10" name="bezugspid">"""

teilnauswahl3_t = """
   <option value="%(id)s">%(na)s %(vn)s | %(fn)s """

teilnauswahl3b_t = """
   <option value="%(id)s">%(bezugsp_id__na)s %(bezugsp_id__vn)s """

teilnauswahl4_t = """
   </select></td>
</tr><tr>
<td colspan="3"> <B>Beginndatum:</B> 
  <input type="text" size=2 maxlength=2 value=""  name="bgd"><B>.</B>
  <input type="text" size=2 maxlength=2 value="%(month)d" name="bgm"><B>.</B>
  <input type="text" size=4 maxlength=4 value="%(year)d" name="bgy">
&#160;&#160;&#160;&#160;  <B>Endedatum:</B>
  <input type="text" size=2 maxlength=2 name="ed"><B>.</B>
  <input type="text" size=2 maxlength=2 name="em"><B>.</B>
  <input type="text" size=4 maxlength=4 name="ey"> </td>
</tr></table>"""

teilnauswahl4b_t = """
    </select></td>
    </tr></table>"""

#############################
# Update 1 Gruppenteilnehmers
#############################

teilnupd_t = """
<table border=1 cellspacing=1 cellpadding="8">
<tr><th colspan="2" align="left">Kind/Jugendliche: %(fall_id__akte_id__vn)s %(fall_id__akte_id__na)s </th>
</tr>"""

teilnupdb_t = """
<table border=1 cellspacing=1 cellpadding="8">
<tr><th colspan="2" align="left">Bezugsperson: %(bezugsp_id__vn)s %(bezugsp_id__na)s </th>
</tr>"""

teilnupd1_t = """
<tr>
<td> <B>Beginndatum:</B>
  <input type="text" size=2 maxlength=2 value="%(bgd)d"  name="bgd"><B>.</B>
  <input type="text" size=2 maxlength=2 value="%(bgm)d" name="bgm"><B>.</B>
  <input type="text" size=4 maxlength=4 value="%(bgy)d" name="bgy"> </td><td>
<B>Endedatum:</B>
  <input type="text" size=2 maxlength=2 value="%(ed)d" name="ed"><B>.</B>
  <input type="text" size=2 maxlength=2 value="%(em)d" name="em"><B>.</B>
  <input type="text" size=4 maxlength=4 value="%(ey)d" name="ey"> </td>
</tr>
</table>
"""

#############################
# Teilnehmerliste für Gruppen
#############################

teiln1_t = """
<dt><A HREF="klkarte?akid=%(id)d">%(vn)s %(na)s</A></dt>
<dd>%(str)s, %(plz)s, %(ort)s. """

teiln1b_t = """
<dt><A HREF="klkarte?akid=%(akte_id)d">%(vn)s %(na)s</A></dt>
<dd>%(str)s, %(plz)s, %(ort)s. """

teiln1c_t = """
<dt>%(vn)s %(na)s</dt>
<dd>%(str)s, %(plz)s, %(ort)s. """

teiln1d_t = """
<dt>%(vn)s %(na)s</dt>
<dd>%(str)s, %(plz)s, %(ort)s. """

teiln2_t = """
%(bgd)s.%(bgm)s.%(bgy)s-<A HREF="updteiln?id=%(id)d&fallid=%(fall_id)d&gruppeid=%(gruppe_id)d">%(ed)s.%(em)s.%(ey)s</A></dd>"""

teiln2b_t = """
%(bgd)s.%(bgm)s.%(bgy)s-<A HREF="updteiln?id=%(id)d&bezugspid=%(bezugsp_id)d&gruppeid=%(gruppe_id)d">%(ed)s.%(em)s.%(ey)s</A></dd>"""

teiln2c_t = """
%(bgd)s.%(bgm)s.%(bgy)s-%(ed)s.%(em)s.%(ey)s</dd>"""

teiln2d_t = """
%(bgd)s.%(bgm)s.%(bgy)s-%(ed)s.%(em)s.%(ey)s</A></dd>"""

teiln3_t = """
</dl><hr></td>"""

###################################
# Mitarbeiter neu aufnehmen
###################################


thmit_t = """
<table border=1 cellspacing=1 cellpadding=8 bgcolor="#FFFFFF">
   <th align="center" bgcolor=#FFF5EE> Vorname </th>
   <th align="center" bgcolor=#FFF5EE> Name </th>
   <th align="center" bgcolor=#FFF5EE> Benutzer </th>
   <th align="center" bgcolor=#FFF5EE> Status </th>
   <th align="center" bgcolor=#FFF5EE> Rechte </th>
   <th align="center" bgcolor=#FFF5EE> Stelle </th>
   </tr> """

mittext_t = """
   <tr> 
   <td align="left"><input type="text" maxlength=20 size=15 name="vn"></td>
   <td align="left"><input type="text" maxlength=25 size=15 name="na"></td>
   <td align="left"><input type="text" maxlength=25 size=15 name="ben"></td>
    """
mitsel1_t = """
   <td align="left"><select name="%s"> """

mitsel2_t = """
    </select></td> """

mitliste_t = """
   <tr> 
   <td align="left"> %(vn)s </td>
   <td align="left"> %(na)s </td>
   <td align="left"> %(ben)s </td>
   <td align="left"> %(stat__name)s </td>
   <td align="left"> %(benr__code)s </td>
   <td align="left"> %(stz__name)s </td>
   </tr> """
hinweis_t = """
   <P><B> Neue Mitarbeiter in jedem Fall immer nur an der DB '%s' 
   eintragen und von dort exportieren, sofern man Daten der einzelnen 
   Datenbanken zusammenf&uuml;hren und gemeinsam nutzen will.</B>
    """

##############################
# Mitarbeiter ändern
##############################

mitlistehrefs_t = """
   <tr> 
   <td align="left"><A HREF="updmit?mitid=%(id)s"> %(vn)s</A></td>
   <td align="left"> %(na)s </td>
   <td align="left"> %(ben)s </td>
   <td align="left"> %(stat__name)s </td>
   <td align="left"> %(benr__code)s </td>
   <td align="left"> %(stz__name)s </td>
   </tr> """

mitupdtext_t = """
   <tr> 
   <td align="left"><input type="text" maxlength=20 size=15 
   value="%(vn)s" name="vn"></td>
   <td align="left"><input type="text" maxlength=25 size=15 
   value="%(na)s" name="na"></td>
   <td align="left"><input type="text" maxlength=25 size=15 
   value="%(ben)s" name="ben"></td>
    """

###########################
# Kategorien und Codeliste
###########################

thkatliste_t = """
<table border=1 cellspacing=1 cellpadding=8 bgcolor="#FFFFFF">
     <th align="center" bgcolor="#FFFFFF"><em> Kategorie </em></th> 
     <th align="center" bgcolor="#FFFFFF"><em> Dokumentation </em></th> 
     <th align="center" bgcolor="#FFFFFF"><em> DB-Tabelle </em></th>
     </tr> """

katliste_t = """
     <tr>
     <td bgcolor=#FFF5EE> <A HREF="codelist#%(id)s"> %(name)s</A></td>
     <td>&#160; %(dok)s   </td>
     <td>
     """
tabliste_t = """ %(tab_id__name)s,  """

katlistende_t = """</td></tr> """

thcodeliste_t = """
    <tr>
    <th align="center"><em> Code </em></th>
    <th align="center"><em> Merkmal </em></th>
    <th align="center"><em> sort </em></th>
    <th align="center"><em> off </em></th>
    <th align="center"><em> ab </em></th>
    <th align="center"><em> Dokumentation </em></th> """

thkat_t = """
    <P>
    <table border=1 cellspacing=1 cellpadding=8 bgcolor="#FFFFFF">
    <th align="center" colspan=6 bgcolor=#FFF5EE>
    <A name="%(id)s"> <A HREF="codeneu?katid=%(id)s"> %(name)s</A></A></th> 
    </tr>"""

codelisten_t = """
    </tr><tr> 
    <td><A HREF="updcode?codeid=%(id)s"> %(code)s</A> </td>
    <td> %(name)s </td>
    <td> %(sort)s </td>
    <td>&#160; %(off)s </td>
    <td>&#160; %(dm)s%(sep)s%(dy)s </td>
    <td>&#160; %(dok)s </td> 
    """

hreftop_t = """
    <P><div align="right">
    <A HREF="%s"> Zur&uuml;ck Top</A> 
    <div align="center">    """


##############################
# Neuen Code eintragen
##############################


thcodeneu_t = """
    <table border=1 cellspacing=1 cellpadding=8 bgcolor="#FFFFFF">
    <th align="center" colspan=5 bgcolor=#FFF5EE> %(name)s </th> 
    </tr>"""

codeneu1_t = """
    <tr>
    <th align="center"><em> Code<sup>1)</sup> </em></th>
    <th align="center"><em> Merkmal </em></th>
    <th align="center"><em> sort<sup>2)</sup> </em></th>
    <th align="center"><em> Minimum<sup>3)</sup> </em></th>
    <th align="center"><em> Maximum </em></th>
    </tr>
    <tr>
    <td><input type="text" size=8 maxlength=8 name="code"></td>
    <td><input type="text" size=30 maxlength=60 name="name"></td>
    <td><select name="sort"> """

codeneu2_t = """
    <option value="%d" %s > %d """

codeneu3_t = """
    </select></td>
    <td><input type="text" size=8 maxlength=8 name="mini"></td>
    <td><input type="text" size=8 maxlength=8 name="maxi"></td>
    </tr>
    """
codeneu4_t = """
    <B>Dokumentation</B><sup>4)</sup> <input type="text" size=55
    maxlength=255 name="dok"><BR> """

codehilfe_t = """
    <P><div align="left">
    <sup>1)</sup> Der Code des Merkmals muss innerhalb der Kategorie 
    einmalig sein.<BR>
    <sup>2)</sup> Eine &Auml;nderung der Sortierzahl schiebt die  
    nachfolgenden um 1 nach 'hinten'. <BR>
    <sup>3)</sup> Bereichsangaben 'Minimum', 'Maximum' dort eintragen, 
    wo im Ursprungsformular Zahlen einzugegeben sind (wie z.B. bei Terminen, Kinderzahl). Minimum und Maximum der ID-Bereiche von Datenbank-Sites bitte so bemessen, dass sp&auml;ter keine aufwendigen &Auml;nderungen erforderlich werden.<BR>
    <sup>4)</sup>maximal 255 Zeichen.</BR>
    Zur Jugendhilfestatistik des Bundes keine neuen Items eintragen (ausser bei    gesetzlichen &Auml;nderungen).<BR>
   <B> Neue Merkmale in jedem Fall immer nur an der DB '%s' eintragen und
    von dort exportieren, sofern man Daten der einzelnen Datenbanken 
    zusammenf&uuml;hren will.</B>
    <div align="center">"""

thkat1_t = """
    <P>
    <table border=1 cellspacing=1 cellpadding=8 bgcolor="#FFFFFF">
    <th align="center" colspan=8 bgcolor=#FFF5EE> %(name)s</A></A></th> 
    </tr>"""

thcodeliste1_t = """
    <tr>
    <th align="center"><em> Code </em></th>
    <th align="center"><em> Merkmal </em></th>
    <th align="center"><em> sort </em></th>
    <th align="center"><em> mini </em></th>
    <th align="center"><em> maxi </em></th>
    <th align="center"><em> off </em></th>
    <th align="center"><em> ab </em></th>
    <th align="center"><em> Dokumentation </em></th> 
    </tr>"""

codelisten1_t = """
    <tr> 
    <td> %(code)s </td>
    <td> %(name)s </td>
    <td> %(sort)s </td>
    <td>&#160; %(mini)s </td>
    <td>&#160; %(maxi)s </td>
    <td>&#160; %(off)s </td>
    <td>&#160; %(dm)s%(sep)s%(dy)s </td>
    <td>&#160; %(dok)s </td> 
    </tr> """

####################
# Codemerkmal ändern
####################

thupdcode_t = """
    <table border=1 cellspacing=1 cellpadding=8 bgcolor="#FFFFFF">
    <th align="center" colspan=8 bgcolor=#FFF5EE> %(name)s </th> 
    </tr>"""

updcode1_t = """
    <tr>
    <th align="center"><em> C<sup>1)</sup> </em></th>
    <th align="center"><em> Merkmal </em></th>
    <th align="center"><em> sort<sup>2)</sup> </em></th>
    <th align="center"><em> Mini<sup>3)</sup> </em></th>
    <th align="center"><em> Maxi</em></th>
    <th align="center"><em> off<sup>4)</sup></em></th>
    <th align="center"><em> Mon.<sup>5)</sup></em></th>
    <th align="center"<em> Jahr<sup>5)</sup> </em></th>
    </tr>
    <tr>
    <td align="center"> %(code)s </td>
    <td><input type="text" size=30 maxlength=60 value="%(name)s" name="name"></td>
    <td><select name="sort"> """

updcode2_t = """
    <option value="%(sort)s" %(sel)s > %(sort)s """

updcode3_t = """
    </select></td>
    <td><input type="text" size=8 maxlength=8
    value="%(mini)s" name="mini"></td>
    <td><input type="text" size=8 maxlength=8 
    value="%(maxi)s" name="maxi"></td>"""

updcode4_t = """
    <td> Ja <input type="checkbox" value="1"  name="off"
    %(check)s ></td> """

updcode5_t = """
    <td><input type="text" size=2 maxlength=2 value="%(dm)s" name="dm"></td>
    <td><input type="text" size=4 maxlength=4 value="%(dy)s" name="dy"></td>
    </tr> """

updcode6_t = """
    <B>Dokumentation</B><sup>6)</sup> <input type="text" size=64
    maxlength=255 value="%(dok)s" name="dok">
    <BR> """

updcodehilfe_t = """
    <P><div align="left">
    <sup>1)</sup> &Auml;nderung am Code ist nicht erlaubt.<BR>
    <sup>2)</sup> Eine &Auml;nderung der Sortierzahl schiebt die  
    nachfolgenden um 1 nach 'hinten'. <BR>
    <sup>3)</sup> Bereichsangaben 'Minimum', 'Maximum' dort eintragen, 
    wo im Ursprungsformular Zahlen einzugegeben sind 
    (wie z.B. bei Terminen, Kinderzahl).<BR>
    <sup>4)</sup>Bei Best&auml;tigung wird das Merkmal in Eingabeformularen 
    nicht mehr angezeigt.<BR>
    <sup>5)</sup>Zur Interpretation der Auswertungsergebnisse, d.h. ab wann 
    1 Merkmal ung&uuml;tig ist. Achtung: Ein R&uuml;ckg&auml;ngigmachen 
    l&ouml;scht das bisherige Datum!</BR>
    <sup>6)</sup>maximal 255 Zeichen.</BR>
    Zur Bundesstatistik keine &Auml;nderungen eintragen, ausser bei 
    gesetzlichen &Auml;nderungen.<BR>
    <B>Inhalts&auml;nderungen in jedem Fall immer nur an der DB '%s'
    eintragen und von dort exportieren, sofern man Daten der einzelnen
    Datenbanken zusammenf&uuml;hren und gemeinsam auswerten will.</B>
    <div align="center">"""


thupdkat1_t = """
    <P>
    <table border=1 cellspacing=1 cellpadding=8 bgcolor="#FFFFFF">
    <th align="center" colspan=8 bgcolor=#FFF5EE>
    <A HREF="codeneu?katid=%(id)s"> %(name)s</A></A></th> 
    </tr>"""

thupdcodeliste_t = """
    <tr>
    <th align="center"><em> Code </em></th>
    <th align="center"><em> Merkmal </em></th>
    <th align="center"><em> sort </em></th>
    <th align="center"><em> Mini </em></th>
    <th align="center"><em> Maxi </em></th>
    <th align="center"><em> off </em></th>
    <th align="center"><em> ab </em></th>
    <th align="center"><em> Dokumentation </em></th> 
    </tr>"""

updcodeliste_t = """
    <tr> 
    <td><A HREF="updcode?codeid=%(id)s"> %(code)s</A></td>
    <td> %(name)s </td>
    <td> %(sort)s </td>
    <td>&#160; %(mini)s </td>
    <td>&#160; %(maxi)s </td>
    <td>&#160; %(off)s </td>
    <td>&#160; %(dm)s%(sep)s%(dy)s </td>
    <td>&#160; %(dok)s </td> 
    </tr> """


##########################################
# Kategorienauswahl: Abfragen Fachstatistik
###########################################


thitemausw_t = """
      <table border>
      <th> und - oder </th>
      <th> Kategorie </th>
      <th> < = > <> </th>
      <th> Item </th>
      </tr>
      <tr>
      <td>&#160; </td>
      <td> Jahr </td>
      <td div align="center">&#160;<select name="year_op">
         <option value = "=" > =
	 <option value = "<" > <
	 <option value = ">" > >
	 <option value = "<=" > <=
	 <option value = ">=" > >=
      </select></td>
      <td div align="center"><input type="text" size="4" maxlength="4" 
      value="%(year)s" name="year" ></td>
      </tr> """

thitemauswb_t = """
Suche Anzahl der Items, wo <BR>
      <table cellpadding="8">
      <td> <B>Jahr</B> </td>
      <td>&#160;<select name="year_op">
         <option value = "=" > =
	 <option value = "<" > <
	 <option value = ">" > >
	 <option value = "<=" > <=
	 <option value = ">=" > >=
      </select>
      <input type="text" size="4" maxlength="4" 
      value="%(year)s" name="year" > </td>
      </tr><tr>
      <td> <B>Stelle</B></td>
       <td> <select name="stz"> 
          <option value=-1 > alle Beratungsstellen """

itemausw_t = """
      und ( a &#160;
      <input type="radio" value="and" name="konj" checked> und /
      oder <input type="radio" value="or" name="konj" > &#160;&#160;b .... )
      zutrifft.<P>
      <table>
      <th> Kategorie </th>
      <th> Item </th>
      </tr>"""

itemausw1_t = """
      <tr>
      <td> <input type="hidden" value="%(id)s" name="feldid" >
           <input type="hidden" value="%(feld)s" name="%(id)s_feld" >
	   <input type="hidden" value="=" name="%(id)s_op">
	   %(name)s
      </td>
      <td> <select name="%(id)s_codeid" >  """

itemausw2_t = """
      </select></td></tr> """

itemauswb3_t = """
            <table>
           <th></th>
           <td>und <B>'%(name)s'</B> ( a oder b oder d ...) ist.</td> 
	   </tr>
	   <tr> 
	   """
itemauswb_t = """
       <tr>
      <td> 
      <input type="hidden" value="or" name="%(id)s_konj" >
      <input type="hidden" value="=" name="%(id)s_op">
      </td>
      """

itemauswb1_t = """<td> <input type="checkbox" value="%(id)s" 
                  name="codeid" > %(name)s </td>
      </tr> """

itemauswb2_t = """
      <input type="hidden" value="%(id)s" name="feldid" >
      <input type="hidden" value="%(feld)s" name="%(id)s_feld" > """

abfr6acomment_t = """
      <P><div align="left">
      <B>Kommentar</B><BR>
      Die Kategorien 'a-z' werden bei der Abfragebedingung 
      entweder alle einzeln mit 'und' bzw. alle einzeln mit 'oder' 
      verbunden sowie insgamt per 'und' mit dem Jahr und der Beratungsstelle.
      """

##############################################
# Bundes-JGH-Statistik erstellen und auflisten
##############################################

jghexportfeedback_t = """
<p>
<table border="3" cellpadding="8" bgcolor=#FFFFFF>
<tr>
<td>
<P>
<UL>
<LI> Exportdatei der Bundesjugendhilfestatistik %(jahr)s f&uuml;r das Statistische Landesamt: <A
HREF="%(ebkusroot)s%(exportdir)s/jgh_%(jahr)s.txt">jgh_%(jahr)s.txt</A></LI>
<LI> Protokolldatei der Bundesjugendhilfestatistik %(jahr)s zur Kontrolle: <A
HREF="%(ebkusroot)s%(exportdir)s/jgh_log_%(jahr)s.txt">jgh_log_%(jahr)s.txt</A></LI>
</UL>
</P>
</td>
</tr></table>
</p>
"""

thjghexportliste_t = """
<p>
<table border="2" cellpadding="8" bgcolor=#FFFFFF>
<tr><th bgcolor=#FFF5EE> Liste der Export- und Logdateien </th>
"""

jghexportliste_t = """
</tr>
<tr align="left">
<td align="left"><P> <A HREF="%s/%s/%s">%s</A> </P> </td>"""

downloadhinweis_t = """
<p>
<font size="-1"><B>Hinweis:</B> Zum Download der Datei die Taste &quot;Shift&quot; mit der linken Maustaste zusammen verwenden.</font>
</p>"""


#####################################################
# Stellenabgleich. Export-Import von Daten 
#####################################################

thexport_t = """
<table border="2" cellpadding="8" bgcolor=#FFFFFF>
<tr><th colspan="3" bgcolor=#FFF5EE > %s </th>
</tr><tr>
<th bgcolor=#FFF5EE> am </th><th bgcolor=#FFF5EE> von </th> <th bgcolor=#FFF5EE> Stelle </th>"""

export_t = """
</tr></tr>
<td> %(datum)s </td><td> %(mit_id__na)s </td><td> %(dbsite__name)s </td>
"""

exporthinweis_t = """
<BR>
<div align="left">
<p>
<font size="-1"><B>Hinweis:</B>
<UL compact>

<LI> Es werden die Klientenkarten und Statistiken in die MasterDB
importiert (ohne Aktendokumente) und von der MasterDB die
statistischen Merkmale und Mitarbeiter f&uuml;r die anderen DBSites
exportiert (siehe Verzeichnis &quot;%s&quot; )</LI>

<LI> Die beim Export erzeugten Dateien der anderen DBSites m&uuml;ssen
vor dem Importieren in das Verzeichnis &quot;%s&quot; der
Serveranwendung kopiert werden</LI>

</UL> </font>
</p></div> """

formexport_t = """
<table>
<tr>
<td> <B>Protokoll:</B> </td><td> <input type="radio" value="l" name="dbexport" checked></td>
</tr><tr>
<td> <B>Import:</B> </td><td> <input type="radio" value="i" name="dbexport"></td>
</tr><tr>
<td> <B>Export:</B> </td><td> <input type="radio" value="e" name="dbexport"></td>
</tr><tr>
<td colspan="2"> """

formexport2_t = """
</td></tr></table>"""







