#!/usr/local/bin/python

## Fuer Windows muss in der ersten Zeile dieser Datei: (statt der obigen)
## der Windows-Pfad fuer Python stehen, wie z.B.
## #!C:\Programme\python20\python.exe -u

## Fuer Linux einen symbolischen Link im CGI-BIN Verzeichnis
## auf diese Datei setzen. Dann start.py aufrufen.
## 
## Url: http://ihr_server/cgi-bin/name_des_Links/menu
##

import sys, string, socket, os
from config import PORT

port = int(PORT)

env = os.environ

## Dies ist ein ganz furchtbarer Hack, damit die Pfade, die sich
## auf Python Skripte beziehen (Endung .py), mit Bobo funktionieren
## if env.has_key('PATH_INFO'):
##   env['PATH_INFO'] = string.replace(env['PATH_INFO'], '.py', '')

if not env.has_key('REMOTE_USER'):
  env['REMOTE_USER'] = '%' 

if not env.has_key('HTTP_PRAGMA'):
  env['HTTP_PRAGMA'] = 'no-cache' 

if not env.has_key('Cache-Control'):
  env['Cache-Control'] = 'no-cache' 

if env.has_key('CONTENT_LENGTH'):
  inl = int(env['CONTENT_LENGTH'])
else:
  inl = 0

envitems = os.environ.items()
envl = []
for name, value in envitems:
  envl.append("%s=%s" % (name,value))
envstr = string.join(envl, '\000')

if inl: instr = sys.stdin.read(inl)
else: instr = ''

tosend = '%9d%s%9d%s' % (len(envstr), envstr, inl, instr)

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(('localhost', port))
  s.send(tosend)
  s.shutdown(1)

  sbuffer = []
  while 1:
    data = s.recv(1024)
    if not data: break
    sbuffer.append(data)
  s.close()

  buffer = string.join(sbuffer, '')
  olen = string.atoi(buffer[:9])
  out = buffer[9:(olen + 9)]
  #err = buffer[(olen + 18):]

  print out

except:
  print """Content-type: text/plain

Server geht nicht. Bitte starten.
"""
# Da kann noch die URL zum starten rein.







