#!/usr/local/bin/python
# coding: latin-1
"""
Skript zur Erzeugung des amtlichen Datensatzes für die Bundesjugendhilfestatistik

Aufruf von der Kommandozeile im Verzeichnis, wo diese Datei steht:

            jghexport.py <jahr>

Die Datei wird in das Exportverzeichnis (daten/export)
geschrieben. Der Name ist jgh_<jahr>.txt, also z.B. jgh_1998.txt.
Das Exportverzeichnis muß bereits existieren.

Ein Protokoll der Datensätze mit zusätzlicher Angabe der Fallnummer und der
Mitarbeiterkennung wird auf die Konsole geschrieben.

Falls ein Datensatz in der Datenbank keine laufende Nummer (Feld 'lnr') hat,
wird eine neue Nummer erzeugt, die um 1 größer ist, als alle bisher verwendeten
laufenden Nummern.

Jeder Datensatz wird fortlaufend an den nächsten geschrieben (ohne ein EOL).

Hinweis: Der Export der JGH-Statistik ist auf der Master-Datenbank
auszufuehren, nachdem die verschiedenen Datenbanken einer Stelle
in diese Hauptdatenbank eingelesen wurden (vgl. Script: dbexport.py)
"""


# Kommenentarzeichen hier und im Code entfernen, falls Zeilenende
# bebraucht wird.
# Zeilende fuer Unix
#EOL = '\n'
# Zeilenende, kann für Windows/DOS verändert werden.
#EOL = '\r\n' # für DOS/Win

import sys, string, time, glob, os
print os.getcwd()
print sys.path
sys.path.append(os.getcwd())

from ebkus.db import sql
from ebkus.config import config
from ebkus.app.ebapi import JugendhilfestatistikList

sql.opendb()

MAX_LNR = None
jghstatliste = JugendhilfestatistikList(where = 'lnr > 0', order = 'lnr')
if jghstatliste:
    MAX_LNR = len(jghstatliste)
    
def get_laufende_nummer(r):
    """Ermittlung der laufenden Nummer (Feld 'lnr')
    Falls das lnr Feld eines Datensatzes 0 oder NULL (None) ist, wird
    MAX_LNR inkrementiert und in die Datenbank geschrieben.
    MAX_LNR wird mit der höchsten vorhandenen laufenden Nummer
    in der Tabelle initialisiert.
    """
    global MAX_LNR
    lnr = r['lnr']
    if lnr is None or lnr < 1:
        if MAX_LNR is None:
            MAX_LNR = 0
        MAX_LNR = MAX_LNR + 1
        r.update({'lnr': MAX_LNR})
        lnr = MAX_LNR
    return lnr
    
def jghexport(jahr):
    """JGH-Statistik Exportdatei für ein Jahr erstellen.
    Die Datei wird in das Exportverzeichnis (daten/export)
    geschrieben. Der Name ist jgh_<jahr>.txt, also z.B. jgh_1998.txt.
    """
    
    filename = os.path.join(config.INSTANCE_HOME, 'daten', 'export', 'jgh_%s.txt' % jahr)
    filename_web = os.path.join(config.DOCUMENT_ROOT, 'daten', 'export', 'jgh_%s.txt' % jahr)
    f = open(filename, 'w+')
    
    #fuer die erstellung der dateien im apacheverzeichnis, damit über browser sichtbar
    # msg 2002-03-04
    f_web = open(filename_web, 'w+')
    
    ##  sql.opendb()
    
    jghl = JugendhilfestatistikList (where = 'ey =  %s' % jahr, order = 'id')
    print "Erzeugen der Datei mit den Datensätzen für die Jugendhilfestatistik für %s" %jahr
    print
    print "Datum: %s" % time.strftime("%c", time.localtime(time.time()))
    print "Datei: %s" % filename
    print "Anzahl der Datensätze: %s" % len(jghl)
    print
    print "Datensätze (vorangestellt zusätzlich Fallnummer und Mitarbeiterkennung):"
    print
    for record in jghl:
        cur_record = get_datensatz(record)
        f.write(cur_record)
        f_web.write(cur_record)
    f.close()
    f_web.close()
    print
    
    
def check_code(str, length, leer_code = None):
    assert len(str) == length
    if not leer_code is None and str == leer_code:
        str = ' '*length
    return str
    
def check_gsa(gsa, gsu):
    """Falls das gsu-Feld 1 ist (Geschwisteranzahl unbekannt), wird das
    gsa Feld immer mit Leerzeichen gefüllt. Sonst wird die Zahl aus gsa
    übernommen. """
    if gsu == '1':
        return '  1'
    else:
        return "%02d " % gsa
        
def get_datensatz(r):
    l = [
      check_code(r['rbz__code'], 1),
      check_code(r['kr__code'], 2),
      check_code(r['gm__code'], 3),
      check_code(r['gmt__code'], 3),
      "%05d" % get_laufende_nummer(r),
      check_code(r['traeg__code'], 1),
      "%02d" % r['bgm'],
      "%d" % r['bgy'],
      "%02d" % r['em'],
      "%d" % r['ey'],
      check_code(r['bgr__code'], 1),
      check_code(r['gs__code'], 1),
      check_code(r['ag__code'], 1),
      check_code(r['fs__code'], 2),
      check_code(r['hke__code'], 1),
      check_gsa(r['gsa'], r['gsu__code']),
      check_code(r['zm__code'], 1),
      check_code(r['ba0__code'], 1, '0'),
      check_code(r['ba1__code'], 1, '0'),
      check_code(r['ba2__code'], 1, '0'),
      check_code(r['ba3__code'], 1, '0'),
      check_code(r['ba4__code'], 1, '0'),
      check_code(r['ba5__code'], 1, '0'),
      check_code(r['ba6__code'], 1, '0'),
      check_code(r['ba7__code'], 1, '0'),
      check_code(r['ba8__code'], 1, '0'),
      check_code(r['ba9__code'], 1, '0'),
      check_code(r['schw__code'], 1),
      check_code(r['fbe0__code'], 1, '0'),
      check_code(r['fbe1__code'], 1, '0'),
      check_code(r['fbe2__code'], 1, '0'),
      check_code(r['fbe3__code'], 1, '0'),
      ' '*28,
    #    EOL, # Zeilenende
    ]
    daten_satz = string.join(l, '')
    assert len(daten_satz) == 80        #+len(EOL)
    print "%-10s%-10s%s" % (r['fall_fn'], r['mit_id__ben'], daten_satz[:54])
    return daten_satz
    
if __name__ == '__main__':
    sys.argv.append('2000')
    jahr = None
    try:
        jahr = int(sys.argv[1])
        assert jahr > 1995 and jahr < 2500
    except:
        print "Kein gültiges Jahr: '%s'" % jahr
        sys.exit(1)
    jghexport(jahr)
    
    
    
    
    
    
