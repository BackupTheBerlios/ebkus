
""" Konfigurationsdatei für EBKuS """


# Hostname des Servers
HOST = 'ihr_pcname.domain.de'
## HOST = 'siesta.in-berlin.de'    

# Datenbank-Site A
SITE = 'A'                    

# Master-Site für mehrere Stellen, Code darf nur hier eingetragen werden,
# falls Daten ausgetauscht werden
MASTER_SITE = 'A'             

# Datenbankname der verwendeten SQL-DB
DATABASE_NAME = 'eb'           
DATABASE_HOST = 'localhost'

# Typ der Datenbank (siehe dbadapter.py fuer die Datenbankmodule)

## DATABASE_TYPE = 'MySQL'
DATABASE_TYPE = 'MySQLdb'
## DATABASE_TYPE = 'mSQL'

CLIKE = 'like'
if DATABASE_TYPE == 'mSQL': CLIKE = 'clike'

# vollstaendiger Pfad fuer EBKuS
EBKUSHOME = '/home/ebkus/public_html/ebkus'   # Linux
# EBKUSHOME = '/home/juerg/html-ref/ebkus'      # Linux
# EBKUSHOME = 'C:\Programme\ebkus'              # Windows

# vollstaendiger URL-Pfad fuer EBKuS (mit SLASH am Ende)
EBKUSROOT = "/~ebkus/ebkus/"           # Linux
# EBKUSROOT = "/~juerg/ebkus/"           # Linux
# EBKUSROOT = "/efb/"               # Windows

# vollstaendiger CGI-BIN Pfad fuer EBKuS (bzw. Pfad des SrciptAlias)
CGI_BIN_PATH = '/usr/local/httpd/efb'   # Linux
# CGI_BIN_PATH = 'C:\Programme\ebkus'     # Windows

# Publishing-Module Name für EBKuS
# (Importiert die Python-Objekte, die "publiziert" werden sollen)
PUBLISHING_MODULE = 'ebs.py'

# Unix-Port-Adresse
PORT = 50010

# Pfad für die Aktendokumente und andere Daten (unterhalb von ebkus!)
DATEN_DIR = 'daten' 
# Pfad für die Export- und Importdateien
EXPORT_DIR = 'daten/export' 
IMPORT_DIR = 'daten/export' 
TEMP_DIR = 'daten/export' 

# Aufbewahrungsfrist der Akten in Monaten nach Abschluss
LOESCHFRIST = 36

# Verzeichnispfad für die Dokumente einer Akte. Jede Akte erhält ein eigenes
# Verzeichnis für die zugehörigen Dokumente.
# Ist AK_DIRS_MAX = 300 , werden z.B. max. je 300 Aktenverzeichnisse
# in insgesamt 300 Verzeichnissen für die SITE A angelegt; 
# also für 90 000 Akten insgesamt.
#
# Aenderungen nur in 100-Reihen vornehmen und immer vor der Installation !
AK_DIRS_MAX = '100'

DATABASE_DIR = None
BACKUP_DIR = None
KEEP_BACKUPS = 'no of days'

