#!/bin/sh

#Setup fuer EBKuS-Datenbankanwendung
#
#
#

echo -e "\nEBKuS Setup:"
echo -e "\nAchtung! Das Setup legt die Tabellen neu an und loescht\ndie bei frueheren Durchlaeufen erzeugten Tabellen und Daten.\n"
echo -e "Lege das Datenbankschema an."
date >> Setuplog.txt
echo -e "\nLege das Datenbankschema an.\n" >> Setuplog.txt

python genschema.py >> Setuplog.txt     # Legt die Datenbank an

echo -e "Generiere die Datenbankschnittstelle ebapigen."
echo -e "\nGeneriere die Datenbankschnittstelle ebapigen.\n" >> Setuplog.txt

python genebapi.py >> Setuplog.txt      # Generiert die Anwendungsschnittstelle

echo -e "Lese die Kategorien- und Merkmalslisten ein. Bitte etwas Geduld."
echo -e "\nLese die Kategorien- und Merkmalslisten ein. Bitte etwas Geduld.\n" >> Setuplog.txt

python migrate.py >> Setuplog.txt       # Liest die Daten in die Datenbank

echo -e "\nDas Setup ist abgeschlossen.\nZum Start des EBKuS-Servers ./ebkus_server oder ./start.py ausfuehren.\n" >> Setuplog.txt

echo -e "\nDas Setup ist abgeschlossen (Vgl. das Protokoll in Setuplog.txt).\n\nZum Start des EBKuS-Servers\n./ebkus_server.sh (startet den Server als Hintergrundprozess) oder\n./start.py an der Konsole ausfuehren.\n"

date >> Setuplog.txt







