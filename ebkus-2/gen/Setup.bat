#!C:\Programme\python21\python.exe

# Setup fuer EBKuS-Datenbankanwendung
# Ein vernünftiges Batch-Script sollte noch 
# Windows-Anwendern geschrieben werden.

# PATH=$PATH;C:\Programme\python21;
# PYTHONPATH=C:\Programme\python21;C:\Programme\ebkus

python genschema.py 

python genebapi.py 

python migrate.py 

echo "Setup abgeschlossen"





