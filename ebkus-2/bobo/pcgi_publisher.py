#!/usr/local/bin/python

#     Copyright 
#
#       Copyright 1996 Digital Creations, L.C., 910 Princess Anne
#       Street, Suite 300, Fredericksburg, Virginia 22401 U.S.A. All
#       rights reserved.  Copyright in this software is owned by DCLC,
#       unless otherwise indicated. Permission to use, copy and
#       distribute this software is hereby granted, provided that the
#       above copyright notice appear in all copies and that both that
#       copyright notice and this permission notice appear. Note that
#       any product, process or technology described in this software
#       may be the subject of other Intellectual Property rights
#       reserved by Digital Creations, L.C. and are not licensed
#       hereunder.
#
#     Trademarks 
#
#       Digital Creations & DCLC, are trademarks of Digital Creations, L.C..
#       All other trademarks are owned by their respective companies. 
#
#     No Warranty 
#
#       The software is provided "as is" without warranty of any kind,
#       either express or implied, including, but not limited to, the
#       implied warranties of merchantability, fitness for a particular
#       purpose, or non-infringement. This software could include
#       technical inaccuracies or typographical errors. Changes are
#       periodically made to the software; these changes will be
#       incorporated in new editions of the software. DCLC may make
#       improvements and/or changes in this software at any time
#       without notice.
#
#     Limitation Of Liability 
#
#       In no event will DCLC be liable for direct, indirect, special,
#       incidental, economic, cover, or consequential damages arising
#       out of the use of or inability to use this software even if
#       advised of the possibility of such damages. Some states do not
#       allow the exclusion or limitation of implied warranties or
#       limitation of liability for incidental or consequential
#       damages, so the above limitation or exclusion may not apply to
#       you.
#
#
# Revision 1.2  1998/05/10 15:03:12  atms
# Juergs Aenderungen
#
# Revision 1.6  1997/01/20 13:58:22  brian
# The publisher component of pcgi now transparently supports threads if they are
# available on the target platform, doing all I/O in separate threads if possible.
# This should let the publisher achieve higher performance in some cases, since
# the application only actually blocks for the duration of the python application
# call rather than blocking until a pcgi-wrapper has finished reading the results
# of a call.
#
# Revision 1.1  1996/12/12 17:12:43  brian
# Added a new version of pcgi_publisher to the CVS project that detects whether threads are available, and if so handles connection IO in a separate thread. Preliminary testing shows it to be quite stable, but lacking the time to do more testing at the moment I decided it would be safer to add the new version as threaded_pcgi_publisher.py for now.
#

import sys, os, socket
from string import atoi, find, joinfields, splitfields, join
from ebkus.config import PORT
import time


try:    from cStringIO import StringIO
except: from StringIO import StringIO


sockfile= None
publish = None
mustdie = 0



def cleanup():
  if sockfile:
    try:    os.unlink(sockfile)
    except: pass


def handle_request(modname, conn):

  global mustdie

  sbuffer=[]
  while 1:
    data = conn.recv(1024)
    if not data: break
    sbuffer.append(data)
  buffer = joinfields(sbuffer, '')
  
  # Parse our pcgi protocol
  elen        = atoi(buffer[:9])
  environment = buffer[9:(elen + 9)]
  input       = buffer[(elen + 18):]

##   log.log('pcgi_publisher.py.buffer: %s' % buffer)

##   log.log('pcgi_publisher.py.handle_request: received:\n\
##   elen:        %s\n\
##   environment: %s (more ...)\n\
##   input:       %s ' % (elen, environment[:50], input[:50]))

  # Rebuild the env and stdin
  env = {}
  ev = splitfields(environment, '\000')
  for x in ev:
    ox = find(x, '=')
    if x[(ox+1):] and (x[(ox+1):] != ': '):
      env[x[0:ox]] = x[(ox+1):]
  sin, sout, serr = StringIO(input), StringIO(), StringIO()

  clock = time.time
  t1=clock()

  try:    publish(modname, stdin=sin, stdout=sout, stderr=serr, environ=env)
  except: mustdie=1

  t2=clock()
  ms = (1000*(t2-t1))


  OUT, ERR = sout.getvalue(), serr.getvalue()

##   log.log('pcgi_publisher.py.handle_request: publish returned:\n\
##   OUT: %s\n\
##   ERR: %s' % (OUT, ERR))

##   log.log('pcgi_publisher.py.handle_request: Sending result to wrapper')

  stat = find(OUT, 'Status: 200 OK')
  envstr = []
  for e in env.items():
    envstr.append("%s=%s" % (e[0],e[1]))
  envstr = join(envstr, '\n')
  if stat < 0:
    received = 'Publisher received from wrapper: \n\nEnvironment:\n%s\n\nStandardIn:\n%s' % (envstr, input)
    print "\nERROR", 50*'*'
    print received
    print 50*'-'
    print 'Application returned: \n\nStandardOut:\n %s\nStandardErr:\n%s' % (OUT, ERR)
    print "ERROR", 50*'*'
    print
  else:
    print 'Publisher received from wrapper: \n\nEnvironment:\n%s\n\nStandardIn:\n%s' % (envstr, input)
    print 'Publisher OK, %2.2f ms' % ms

  conn.send('%9d%s%9d%s' % (len(OUT), OUT, len(ERR), ERR))

##  log.log('pcgi_publisher.py.handle_request: Sending succeeded')

  conn.close()
  if mustdie:
    cleanup()
    sys.exit(1)


def main():

  myport = int(PORT)
  # Save our process id
##   pf = open(sys.argv[2], 'w')
##   pf.write(str(os.getpid()))
##   pf.close()

  #log.lognew('pcgi_publisher.py: PID %s written to %s' % (os.getpid(), sys.argv[2]))

  # Find module to publish, insert path info
  d, s = os.path.split(sys.argv[4])
  module_name = splitfields(s, '.')[0]
  sys.path.insert(0, d)

# ich glaube das brauchen wir nicht
#  sys.path.insert(0, sys.argv[3])
#  os.chdir(sys.argv[3])


  # Should know enough now to import the publisher...
  global publish
  import cgi_module_publisher
  #print cgi_module_publisher.__file__
  publish = cgi_module_publisher.publish_module

  # Create a listening socket
  global sockfile
  sockfile = sys.argv[1]
  if (os.name == 'nnposix'):
    try:    os.unlink(sockfile)
    except: pass
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(sockfile)
    # log.log('pcgi_publisher.py: AF_UNIX socket bound to %s' % sockfile)
  else:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', myport)) 
##     host, port = sock.getsockname()
##     if not host or host == '0.0.0.0':
##       host = sock.gethostname()
##     hostname, hostnames, hostaddrs = sock.gethostbyaddr(host)
##     if '.' not in hostname:
##       for host in hostnames:
##         if '.' in host:
##           hostname = host
##           break
##     pcgi_server = hostname
##     pcgi_port   = port
##     sinfo = open(sockfile, 'w')
##     sinfo.write("%s\n%s\n" % (pcgi_server, pcgi_port))
##     sinfo.close()
#  sock.listen(512)
  sock.listen(5)

  #log.log('pcgi_publisher.py: Listening')

  print "Current module: %s" % module_name
  print "Current path: %s" % sys.path
  print
  while 1:
    print 'Listening (host: %s port: %s)' % sock.getsockname()
    # Handle requests, in a new thread if available
    connection, addr = sock.accept()
##     log.log('pcgi_publisher.py: Connection accepted: conn: %s addr: %s' \
##             %(connection, addr))
    try:   handle_request(module_name, connection)
    except socket.error, args:
##      log.log('pcgi_publisher: Socket error in handle_request: %s' % args)
      if mustdie:
        cleanup()
        sys.exit(1)
    except:
        cleanup()
        sys.exit(1)
        

if __name__ == '__main__':
  main()

## if os.environ.has_key('REQUEST_METHOD'): main()
## else: pass 






