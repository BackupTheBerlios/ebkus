####################################################################
# Enth�lt die Daten, welche nach der Generierung in die Datenbank
# eingelesen werden.
#
# Code und Kategorien f�r die Datenbank;
# Code- und Kategorienlisten zur Klientenverwaltung und Fachstatistik;
# Mitarbeiterliste (Administrator ist Pflicht!)
#
#######################################################################
#
# Stellt die von dem Programm ben�tigte Menge an Kategorien und Merkmalen
# f�r die EFBen von Berlin Friedrichshain und Kreuzberg zur Verf�gung.     
# (alternativ zu migrdata.py in migrate.py als Moduls importieren)
#

#
# liste code
#
# Code;Merkmalsname;Code der Kategorie;Bereichsminimum;Bereichsmaximum
#

code_list_str = \
"""s;Schl�ssel;verwtyp
f;Fremdschl�ssel;verwtyp
k;Kategorie;verwtyp
b;Bereichskategorie;verwtyp
p;Primitiv;verwtyp
36;PLZ 10997, 10999;fsbz
61;PLZ 10961, 10963, 10965, 10967, 10969;fsbz
LR1;Lebensraum 1;fsbz
LR2;Lebensraum 2;fsbz
LR3;Lebensraum 3;fsbz
LR4;Lebensraum 4;fsbz
LR5;Lebensraum 5;fsbz
LR6;Lebensraum 6;fsbz
LR7;Lebensraum 7;fsbz
LR8;Lebensraum 8;fsbz
LR9;Lebensraum 9;fsbz
LR10;Lebensraum 10;fsbz
LR11;Lebensraum 11;fsbz
LR12;Lebensraum 12;fsbz
andere; andere;fsbz
999;keine Angabe;fsbz
1;m;gs
2;w;gs
1;0-2;fsag
2;3-5;fsag
3;6-9;fsag
4;10-13;fsag
5;14-17;fsag
6;18-20;fsag
7;21-26;fsag
8;vor d. Schw.;fsag
9;pr�natal;fsag
999;keine Angabe;fsag
1;bis 20;fsagel
2;21-26;fsagel
3;27-44;fsagel
4;45-54;fsagel
5;55-64;fsagel
6;65-74;fsagel
7;75-;fsagel
999;keine Angabe;fsagel
1;�ltestes Kind;fsgr
2;mittleres Kind;fsgr
3;j�ngstes Kind;fsgr
4;Einzelkind;fsgr
5;Zwillinge;fsgr
999;keine Angabe;fsgr
0;kein Kind;fska;0;0
1;1 Kind;fska;1;1
2;2 Kinder;fska;2;2
3;3 Kinder;fska;3;3
4;4 Kinder u. mehr;fska;4;100
999;keine Angabe;fska
1;verheiratet, leibl. Eltern;fsfs
2;unverheiratet, leibl. Eltern;fsfs
3;wechselnd bei Km u. Kv;fsfs
4;Mutter u. Stiefvater;fsfs
5;Vater u. Stiefmutter;fsfs
6;alleinerziehende Mutter;fsfs
7;alleinerziehender Vater;fsfs
8;Verwandte;fsfs
9;Pflegefamilie;fsfs
10;Sonderpflege;fsfs
11;Adoptivfamilie;fsfs
12;Heim;fsfs
13;Wohngemeinschaft;fsfs
14;eigene Wohnung;fsfs
15;obdachlos;fsfs
16;sonstige;fsfs
999;keine Angabe;fsfs
1;Selbstmelder;fszm
2;Klient/Bekannte;fszm
3;ASD;fszm
4;KJGD/KJPD;fszm
5;Kita/Hort;fszm
6;Schule;fszm
7;Schulpsychologie;fszm
8;Kinder-/Jugendbetreuung;fszm
9;Medizinische Einrichtung;fszm
10;Gericht;fszm
11;Sonstige;fszm
999;keine Angabe;fszm
1;Entwicklungs-, Verhaltensauff. in d. Familie;fsba
2;Entwicklungs-, Verhaltensauff. in d. Kita;fsba
3;Entwicklungs-, Verhaltensauff. in d. Schule;fsba
4;Entwicklungs-, Verhaltensauff. im sonst. Umfeld;fsba
5;Entwickungs- , Verhaltensauff., sonstige;fsba
6;Leistungsproblem in der Schule/Ausbildung;fsba
7;Lebensproblem der Jugendlichen;fsba
8;Abl�sungsproblem des Jugendlichen;fsba
9;Krise der Jugendlichen;fsba
10;sexueller Missbrauch;fsba
11;�berforderung der Eltern;fsba
12;Erziehungsunsicherheiten;fsba
13;Familienkonflikt;fsba
14;Paarkonflikt;fsba
15;Trennungsproblem der Eltern;fsba
16;Sorge- oder Umgangsrecht;fsba
17;Begleiteter Umgang;fsba
18;akute Krise des Ratsuchenden;fsba
19;Begleitung vor u. nach Fremdunterbringung;fsba
20;Stellungnahme KJHG-Psychotherapie;fsba
21;Stellungnahme f�r anderen Dienst;fsba
22;Gerichtsgutachten;fsba
23;sonstiges;fsba
999;keine Angabe;fsba
1;ja;fsep
2;nein;fsep
999;keine Angabe;fsep
1;unproblematisch;fssd
2;starker finanz. Druck;fssd
3;Verschuldung;fssd
4;unbekannt;fssd
999;keine Angabe;fssd
1;nicht berufst�tig;fsbe
2;Vollzeit angestellt;fsbe
3;Teilzeit angestellt;fsbe
4;Schichtarbeit;fsbe
5;selbst�ndig;fsbe
6;arbeitslos;fsbe
7;Sozialhilfe;fsbe
8;berentet;fsbe
9;in Ausbildung;fsbe
10;sonstige;fsbe
999;keine Angabe;fsbe
1;BRD;fshe
2;T�rkei;fshe
3;Europa;fshe
4;Ost-Europa;fshe
5;arabische L�nder;fshe
6;Afrika;fshe
7;Asien;fshe
8;Nordamerika;fshe
9;Lateinamerika;fshe
10;Australien;fshe
11;andere L�nder;fshe
999;keine Angabe;fshe
1;Krankheit, Behinderung;fspbe
2;Alkohol-, Drogenkonsum;fspbe
3;chronifizierte psychische Erkrankung;fspbe 
4;Opfer famili�rer Gewalt, sex. Missbrauchs;fspbe
5;starke Traumatisierung (Krieg, Folter);fspbe
6;�berforderung;fspbe
7;Isolation und Kontaktschwierigkeiten;fspbe
8;sonstige;fspbe
999;keine Angabe;fspbe
1;allg. Erziehungs-, Entwicklungsproblem;fspbk
2;neurotische oder psychosomatische Reaktion;fspbk
3;Vernachl�ssigung, Verwahrlosung;fspbk
4;Opfer von Gewalt, Misshandlung;fspbk
5;Sexueller Missbrauch (Opfer);fspbk
6;Alkohol-, Drogenkonsum;fspbk
7;strafbares Verhalten;fspbk
8;Schulleistungsproblem;fspbk
9;Schulverweigerung;fspbk
10;soziale Kontaktschwierigkeit, Isolation;fspbk
11;aggressives Verhalten;fspbk
12;Gewaltbereitschaft des Jugendlichen;fspbk
13;berufliche Perspektive;fspbk
14;Behinderung;fspbk
15;Suizidgef�hrdung;fspbk
16;Esst�rung;fspbk
17;traumat. Verlust, Tod einer Bezugsperson;fspbk
18;sonstige;fspbk
999;keine Angabe;fspbk
1;Erziehungsberatung;fsle
2;Trennungs-, Scheidungsberatung, Mediation;fsle
3;Begleiteter Umgang;fsle
4;Familienberatung, -therapie;fsle
5;Paarberatung, -therapie;fsle
6;Einzelbetreuung Kind;fsle
7;Einzelbetreuung Jugendlicher;fsle
8;Einzelbetreuung Erwachsener;fsle
9;Einzelpsychotherapie Kind;fsle
10;Einzelpsychotherapie Jugendlicher;fsle
11;Einzelpsychotherapie Erwachsener;fsle
12;Gruppentherapie Kinder;fsle
13;Gruppentherapie Jugendliche;fsle
14;Gruppentherapie Erwachsene;fsle
15;Arbeit im sozialen Umfeld;fsle
16;Diagnostik;fsle
17;Hilfeplanung;fsle
18;Schriftliche Arbeit f�r Klienten;fsle
19;Begleitung KJHG-Therapie;fsle
20;Fachdienstliche Stellungnahme;fsle
21;Gerichtsgutachten;fsle
22;sonstige;fsle
999;keine Angabe;fsle
1;1-5;fskat;1;5
2;6-20;fskat;6;20
3;21-30;fskat;21;30
4;31-40;fskat;31;40
5;41-50;fskat;41;50
6;mehr als 50;fskat;51;
1;einvernehmlich;fsbg
2;kein Termin seit 6 Mon.;fsbg
3;Weiterverweisung;fsbg
4;Abbruch: Klient;fsbg
5;Abbruch: Therapeut;fsbg
6;Abbruch: sonstiges;fsbg
7;noch offen;fsbg
999;keine Angabe;fsbg
1;Mutter;klerv
2;Vater;klerv
3;Geschwister;klerv
4;Halbgeschw.;klerv
5;Stiefmutter;klerv
6;Stiefvater;klerv
7;Grossmutter;klerv
8;Grossvater;klerv
9;verwandt;klerv
10;Pflegemutter;klerv
11;Pflegevater;klerv
12;Adoptivmutter;klerv
999;k. Angabe;klerv
1;ASD;klinsta
2;KJGD/KJPD;klinsta
3;Kita/Hort;klinsta
4;Schule;klinsta
5;Heim;klinsta
6;Wohngemeinschaft;klinsta
7;Freizeiteinr.;klinsta
8;Arzt;klinsta
9;Klinik;klinsta
10;Gericht;klinsta
11;Schulpsychologie;klinsta
12;Sonstige;klinsta
999;keine Angabe;klinsta
i;im Dienst;status
a;nicht im Dienst;status
A;EFB-Mehringdamm;stzei
B;EFB-Wienerstr.;stzei
C;EFB-Friedrichshain;stzei
admin;Administrator;benr
bearb;Fallbearbeiter;benr
verw;Verwaltung;benr
l;laufender Fall;stand
zdA; zu den Akten;stand
t;Notiz wichtig;notizbed
f;Notiz;notizbed
t;ist im Verteiler;vert
f;nicht im Verteiler;vert
ja;aktuelle Einrichtung;einrstat
nein;fr�here Einrichtung;einrstat
1;Berlin;rbz
06;Kreuzberg;kr
05;Friedrichshain;kr
000;N.N.;gm
000;N.N.;gmt
1;Tr�ger der �ffentl. JGH;traeg
2;Tr�ger der freien JGH;traeg
1;Beratung wurde einvernehmlich beendet;bgr
2;letzter Kontakt liegt mehr als 6 M. zur�ck;bgr
3;Weiterverweisung;bgr
1;unter 3;ag
2;3 - unter 6;ag
3;6 - unter 9;ag
4;9 - unter 12;ag
5;12 - unter 15;ag
6;15 - unter 18;ag
7;18 - unter 21;ag
8;21 - unter 24;ag
9;24 - unter 27;ag
01;bei Eltern;fs
02;bei 1 Elternteil mit Stiefelternteil;fs
03;bei alleinerziehendem Elternteil;fs
04;bei Grosseltern, Verwandten;fs
05;in einer Pflegestelle;fs
06;in einem Heim;fs
07;in einer Wohngemeinschaft;fs
08;in eigener Wohnung;fs
09;ohne feste Unterkunft;fs
10;an unbekanntem Ort;fs
1;deutsch;hke
2;nicht-deutsch;hke
3;unbekannt;hke
0;kein Geschwister;gsa;0;0
1;1 Geschwister;gsa;1;1
2;2 Geschwister;gsa;2;2
3;3 Geschwister;gsa;3;3
4;mehr als 3 Geschwister;gsa;4;20
0;bekannt;gsu
1;unbekannt;gsu            
1;jungen Menschen selbst;zm
2;Eltern gemeinsam;zm
3;Mutter;zm
4;Vater;zm
5;soziale Dienste;zm
6;Sonstige;zm
1;Entwicklungsauff�lligkeiten;ba0  
0;leer;ba0
1;Beziehungsprobleme;ba1
0;leer;ba1
1;Schule-/Ausbildungsprobleme;ba2
0;leer;ba2
1;Straftat d. Jugendl./jungen Vollj�hrigen;ba3
0;leer;ba3
1;Suchtprobleme des jungen Menschen;ba4
0;leer;ba4
1;Anzeichen f�r Kindesmisshandlung;ba5
0;leer;ba5
1;Anzeichen f�r sexuellen Missbrauch;ba6
0;leer;ba6
1;Trennung/Scheidung der Eltern;ba7
0;leer;ba7
1;Wohnungsprobleme;ba8
0;leer;ba8
1;sonstige Probleme in u. mit der Familie;ba9
0;leer;ba9
1;Erziehungs-/Familienberatung;schw
2;Jugendberatung;schw
3;Suchtberatung;schw
1;allein;fbe0
2;in der Gruppe;fbe0
0;leer;fbe0
1;allein;fbe1
2;in der Gruppe;fbe1
0;leer;fbe1
1;in der Familie;fbe2
0;leer;fbe2
1;im sozialen Umfeld;fbe3
0;leer;fbe3
txt;text/plain;mimetyp
asc;text/plain;mimetyp
html;text/html;mimetyp
htm;text/html;mimetyp
pdf;application/pdf;mimetyp
ps;application/postscript;mimetyp
bnotiz;Beraternotiz;dokart
Vm;Vermerk;dokart
anotiz;Aktennotiz;dokart
Brief;Brief;dokart
Prot;Protokoll;dokart
Dok;Dokument;dokart
Antrag;Antrag;dokart
Bericht;Bericht;dokart
Stellung;Stellungnahme;dokart
Befund;Befunddokument;dokart
Gutacht;Gutachten;dokart
Beschein;Bescheinigung;dokart
Sonstig;Sonstiges;dokart
Kinder;Kinder;teiln
Jugendl;Jugendliche;teiln
Eltern;Eltern;teiln
V�ter;V�ter;teiln
M�tter;M�tter;teiln
Altgem;Altersgemischt;teiln
Familien;Familien;teiln
Erzieher;ErzieherInnen;teiln
Lehrer;Lehrer;teiln
Paare;Paare;teiln
sonstige;sonstige;teiln
Eabend;Elternabend;grtyp
Kurs;Kurs;grtyp
Therapie;Therapiegruppe;grtyp
Seminar;Seminar;grtyp
Selbster;Selbsterfahrung;grtyp
Superv;Supervision;grtyp
sonstige;sonstige;grtyp
1;Nein;gfall
2;Ja;gfall
A;DBSite A;dbsite;1;300000
B;DBSite B;dbsite;300001;600000
"""

bereichs_kategorien_str = "fska fskat gsa dbsite"


##
## liste kategorie
##
## Kategorien-Code;Name der Kategorie
##

kategorie_list_str = \
"""verwtyp;Feldverwendungstyp; Kategorie f�r das Feld der Metatabelle
fsbz;Region
fsag;Altersgruppe Kind/Jugendliche
fsagel;Altersgruppe Eltern
fsgr;Geschwisterreihe
fska;Kinderanzahl
fsfs;Lebensmittelpunkt des Kindes
fszm;Empfohlen von
fsba;Problemlage bei der Anmeldung
fsep;Erfahrung in Psychotherapie
fssd;Finanzielle Situation der Familie
fsbe;Beruf der Eltern
fshe;Herkunftsland der Eltern
fspbe;Problemspektrum Eltern
fspbk;Problemspektrum Kind, Jugendliche
fsle;Erbrachte Leistungen
fskat;Anzahl der Termine
fsbg;Beendigungsgrund
klerv;Verwandtschaftsgrad
klinsta;Einrichtungskontakt
status;Mitarbeiterstatus
stzei;Dienststelle
benr;Benutzungsrecht
stand;Bearbeitungsstand
notizbed;Notizbedeutung
vert;im Verteiler
einrstat;Aktueller Kontakt
rbz;Regierungsbezirk    
kr;Kreis               
gm;Gemeinde             
gmt;Gemeindeteil        
traeg;Jugendhilfe-Tr�ger
bgr;Beendigungsgrund
gs;Geschlecht 
ag;Alter
fs;Junger Mensch lebt bei
hke;Staatsangeh�rigkeit
zm;1. Kontakt durch
gsa;Geschwisteranzahl
gsu;Kenntnis der Geschwisterzahl
ba0;Beratungsanlass 0
ba1;Beratungsanlass 1
ba2;Beratungsanlass 2
ba3;Beratungsanlass 3
ba4;Beratungsanlass 4
ba5;Beratungsanlass 5
ba6;Beratungsanlass 6
ba7;Beratungsanlass 7
ba8;Beratungsanlass 8
ba9;Beratungsanlass 9
schw;Beratungsschwerpunkt
fbe0;beim jungen Menschen
fbe1;bei den Eltern
fbe2;in der Familie
fbe3;im sozialen Umfeld
mimetyp;Mime Typ
dokart;Der Eintrag ist
teiln;Teilnehmer/innnen
grtyp;Gruppentyp
gfall;Geschwisterfall
dbsite;Datenbank-Site
"""

##
## Mitarbeiterliste f�r Ersteintrag
##
## Vorname;Nachname;ben;status;benr;stzei
## Beispiel:
## Admin;Administrator;Admin;i;admin;A
## Gast;Gast;Gast;i;bearb;A
## Susi;Meier;Susi;i;verw;A
## Elfi;Hansen;Elfi;i;bearb;B

mitarbeiter_list_str = \
"""Admin;Administrator;Admin;i;admin;A
Gast;Gast;Gast;i;bearb;A
Susi;Meier;Susi;i;verw;A
Elfi;Hansen;Elfi;i;bearb;A
Ursi;Siebert;Ursi;i;bearb;B
Willi;Finger;Willi;i;bearb;B
"""
