#!/usr/local/bin/python

## Fuer Windows muss in der ersten Zeile dieser Datei: (statt der obigen)
## der Windows-Pfad fuer Python stehen u. der Parameter -u, wie z.B.
## #!C:\Programme\python21\python.exe -u


import os, string
from ebkus.config import PUBLISHING_MODULE, CGI_BIN_PATH

## server_module = sys.argv[1]
## print server_module

cwd = os.getcwd()
server_module = cwd + '/%s' % PUBLISHING_MODULE

res = os.system('bobo/pcgi_publisher.py \
bobo/pcgitime.socket \
bobo/pcgitime.pid \
%s ' % CGI_BIN_PATH + server_module)


