#!/bin/sh

# Linux:
# Startscript für EBKuS. Nach ebkus_server.sh kopieren !
#

zeit=`date "+%s"`
LOGFILE="ebkus_log-$zeit"
cd /home/ebkus/public_html/ebkus
/usr/bin/nohup ./start.py &> /tmp/$LOGFILE &
/bin/chmod 0600 /tmp/$LOGFILE
