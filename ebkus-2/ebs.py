"""Das Module, in dem Bobo Objekte zum 'publishen' findet.
Publiziert wird der Wert von bobo_application, eine Instanz der
Klasse EBKuS."""

import sys

# config.py muss im selben Verzeichnis stehen
from ebkus import config
sys.path.insert(0, '%s/' % config.EBKUSHOME )

print 'EBS PATH:', sys.path

from ebkus.db import sql
sql.debug = 0
from ebkus.db import dbapp
# dbapp.cache_off()
dbapp.cache_on()

from ebkus.app import EBKuS
bobo_application = EBKuS.EBKuS()
__bobo_hide_tracebacks__ = None

