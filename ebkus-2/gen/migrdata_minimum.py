####################################################################
# Enthält die Daten, welche nach der Generierung in die Datenbank
# eingelesen werden.
#
# Code und Kategorien für die Datenbank;
# Code- und Kategorienlisten zur Klientenverwaltung und Fachstatistik;
# Mitarbeiterliste (Administrator ist Pflicht!)
# 
#######################################################################
#
# Stellt die minimale und von dem Programm benötigte 
# Menge an Kategorien und Merkmalen für die Installation zur Verfügung.     
# (alternativ zu migrdata.py in migrate.py als Modul importieren)
#

#
# liste code
#
# Code;Merkmalsname;Code der Kategorie;Bereichsminimum;Bereichsmaximum
#

code_list_str = \
"""s;Schlüssel;verwtyp
f;Fremdschlüssel;verwtyp
k;Kategorie;verwtyp
b;Bereichskategorie;verwtyp
p;Primitiv;verwtyp
999;keine Angabe;fsbz
1;m;gs
2;w;gs
999;keine Angabe;fsag
999;keine Angabe;fsagel
999;keine Angabe;fsgr
0;kein Kind;fska;0;0
1;1 Kind;fska;1;1
2;2 Kinder;fska;2;2
3;3 Kinder;fska;3;3
4;4 Kinder u. mehr;fska;4;100
999;keine Angabe;fska
999;keine Angabe;fsfs
999;keine Angabe;fszm
999;keine Angabe;fsba
999;keine Angabe;fsep
999;keine Angabe;fssd
999;keine Angabe;fsbe
999;keine Angabe;fshe
999;keine Angabe;fspbe
999;keine Angabe;fspbk
999;keine Angabe;fsle
999;keine Angabe;fsbg
1;1-5;fskat;1;5
2;6-20;fskat;6;20
3;21-30;fskat;21;30
4;31-40;fskat;31;40
5;41-50;fskat;41;50
6;mehr als 50;fskat;51;
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
A;EFB-A;stzei
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
nein;frühere Einrichtung;einrstat
1;Berlin;rbz
06;Kreuzberg;kr
000;N.N.;gm
000;N.N.;gmt
1;Träger der öffentl. JGH;traeg
2;Träger der freien JGH;traeg
1;Beratung wurde einvernehmlich beendet;bgr
2;letzter Kontakt liegt mehr als 6 M. zurück;bgr
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
1;Entwicklungsauffälligkeiten;ba0  
0;leer;ba0
1;Beziehungsprobleme;ba1
0;leer;ba1
1;Schule-/Ausbildungsprobleme;ba2
0;leer;ba2
1;Straftat d. Jugendl./jungen Volljährigen;ba3
0;leer;ba3
1;Suchtprobleme des jungen Menschen;ba4
0;leer;ba4
1;Anzeichen für Kindesmisshandlung;ba5
0;leer;ba5
1;Anzeichen für sexuellen Missbrauch;ba6
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
Väter;Väter;teiln
Mütter;Mütter;teiln
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
"""

bereichs_kategorien_str = "fska fskat gsa dbsite"


##
## liste kategorie
##
## Kategorien-Code;Name der Kategorie
##

kategorie_list_str = \
"""verwtyp;Feldverwendungstyp; Kategorie für das Feld der Metatabelle
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
traeg;Jugendhilfe-Träger
bgr;Beendigungsgrund
gs;Geschlecht 
ag;Alter
fs;Junger Mensch lebt bei
hke;Staatsangehörigkeit
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
## Mitarbeiterliste für Ersteintrag
##
## Vorname;Nachname;ben;status;benr;stzei
## Beispiel:
## Admin;Administrator;Admin;i;admin;A
## Gast;Gast;Gast;i;bearb;A
## Susi;Meier;Susi;i;verw;A
## Elfi;Hansen;Elfi;i;bearb;B

mitarbeiter_list_str = \
"""Admin;Administrator;Admin;i;admin;A
"""
