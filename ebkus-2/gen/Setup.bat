#!C:\Programme\python21\python.exe

# Setup fuer EBKuS-Datenbankanwendung
# Ein vernünftiges Batch-Script sollte noch 
# von Windows-Anwendern erstellt werden.

# PATH=$PATH;C:\Programme\python21;
# PYTHONPATH=$PYTHONPATH;C:\Programme\python21;C:\Programme\ebkus

python genschema.py 

python genebapi.py 

python migrate.py 

echo "Setup abgeschlossen"





