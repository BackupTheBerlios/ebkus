#!/usr/local/bin/python

#
#  Notizdatei zum Ausprobieren von Codefragmenten !
#
#          NO! YES
# tabs ok?  ^

#          YES! NO
# tabs ok?  ^

import sys
sys.path.append('../lib')
from ebapih import *
from templates import *
import string

opendb()


##al=AkteList(where="na = 'Vinzer-Davis'")
##for  a in al:
##  print a['na'],a['letzter_fall__fn'], a['id'], a['bezugspersonen'],a['einrichtungen']

## eg = Elterngruppe(1)
## bp = Bezugsperson(2)
## miteg = MitgliedElterngruppe()
## a = eg['id']
## miteg['eg_id'] = a
## b = bp['id']
## miteg['bezugsp_id'] = b
## miteg.insert()

## megl = MitgliedElterngruppeList(where = 'bezugsp_id = %s' % '1')
## print megl
##sys.exit(0)


##f=Fall(4)
##f.show()
## ml=XMitarbeiterList(where='id=0')
## ml[0].show()
## ml.deleteall()
## ## print a.items()
## ## for k,v in a[.items():
## ##   print k,v
## print a['faelle']
## print a.getinv('faelle')

## print Mitarbeiter(8)['leistungen'].getIds()
## print Fall(4)['leistungen'].getIds()

## for f in a['faelle']:
##   print f['id'], f['fn'], 'Status:', f['status__code'], f['akte_id__na__id']
##   print 'Leistungen: '
##   for l in f['leistungen']:
##     print l['id']

## nl = Leistung()
## ## nl.new()
## ## print 'Neue Id:' , nl['id']

## ## nl['fall_id'] = f['id']
## ## nl['mit_id'] = 8 
## ## nl['le'] = 117
## ## nl.insert()
  
## print Mitarbeiter(8)['leistungen'].getIds()
## print Fall(4)['leistungen'].getIds()
## l=LeistungList(where='id > 10000')
## l.deleteall()
## print Mitarbeiter(8)['leistungen'].getIds()
## print Fall(4)['leistungen'].getIds()

## import dbapp
## print dbapp._InverseRegistry

## closedb()
## import sql, dbapp
## sql.debug=0
## dbapp.cache_on()
## import klkarte, timing
## form = {'akid' : 4}
## timing.timer1(klkarte.klkarte, (form,))
## timing.timer1(klkarte.klkarte, (form,))
## timing.timer1(klkarte.klkarte, (form,))
## print 'Undo'
## timing.timer1(dbapp.undo_cached_fields)
## timing.timer1(klkarte.klkarte, (form,))
## timing.timer1(klkarte.klkarte, (form,))
## print 'Undo'
## timing.timer1(dbapp.undo_cached_fields)
## timing.timer1(klkarte.klkarte, (form,))
## timing.timer1(klkarte.klkarte, (form,))

##klkarte.main()
## dbapp.cache_on()
## opendb()
## s1=klkarte.klkarte_display(4)
## dbapp.cache_off()
## s2=klkarte.klkarte_display(4)
## if s1 == s2:
##   print 'ALLES OK'
## else:
##   print 'ALARM!!!!!!!!!!!!'
## print s1
## print s1
## sys.exit(0)

## fs = FallList('akte_id', 4)
## print fs
## a = Fall()
## print a['akte_id__id']
## print a['akte_id__vn']
## print a.getInverseKey('akte_id')

## opendb()
## import dbapp, sql
## sql.debug=0

#Akte()._test_consistency()

#print Akte.conditionalfields
## ak=AkteList(where='')
## for a in ak:
##   print a['id'], a['href_thbperson'], a['aktueller_fall__id'], a['aktuell']


#e=Einrichtungskontakt(100024)
#e.show()
#dbapp.cache_off()
## import ebs
## form = {'akid' : 5}
## print ebs.klkarte(form)
## print ebs.klkarte(form)
## print ebs.klkarte(form)
## e=a['einrichtungen']
## print e


## ak=EinrichtungskontaktList(where='akte_id = 5')
## for a in ak:
##   print a['id'], a['na'], a['akte_id'],a['akte_id__na']
## print
## ak=BezugspersonList(where="")
## for a in ak:
##   print a['id'], a['na'], a['akte_id'],a['akte_id__na']

## al=AkteList(where='')
## for a in al:
##   print 'LF:', a['id'], a['aktueller_fall__id'], 'AKT:', a['aktuell'],\
##      'HREF:', a['href_thzustaendig'], a['stfarbe'], a['staktion'] 

## fl = FallList(where='')
## for f in fl:
##   print f['id'],
##   print f['akte_id__letzter_fall__self__fn'],
##   print f['akte_id__self__id__letzter_fall__id']

#  print 'LEISTUNGEN:',f['akte_id__letzter_fall__leistungen']

#print a.getInverseKey('faelle')

## def ameth(self, callingkey):
##   print callingkey, self['vn'], self['na']

## a['tmp'] = 'Erwin'


## for a in AkteList(where=''):
##   print a.get('tmp')


## Für Alternative HREFS:
## Tabelle aus:

## key, testkey, truestring, falsestring 



## Akte.attributemethods = {}
## Akte.attributemethods['matt'] = ameth

## a['matt']

#print a.attributemethods['matt']

## s = SubAkte(1)
## s['matt']

#f=Fall(2) # gibt's nicht bei mir. Referentielle Integrität verletzt. Muß 
# Exception liefern.

## c=CodeList('kat_code', 'fspb')
## d=CodeList(c)

## m=Fall(0)
## m.show()
## ml = MitarbeiterList(where='')
## for m in ml:
##   print m['id'],m['na'],m['vn']
##   print m['stat'], m['stat__name'],  m['stat__kat_id__name']
##   print m['benr'], m['benr__name'],  m['benr__kat_id__name']






## al = AkteList(where='id < 30')
## a5 = Akte(5)
## fn = a5['faelle']
## print fn[0]['akte']
## for a in al:
##   print a['vn'], a['na'],a['gb']
## #  print akte.db.vn, akte.db.na, akte.db.gb
##   faelle = a['faelle']
##   bp = a['bezugspersonen']
##   print 'Bezugspersonen'
##   for l in bp:
##     print '  ', l['vn'], l['na'], l['plz'], l['ort']
## print 'Fälle'
## faelle = FallList(where='',order = 'id')
## for f in faelle:
##   print f['id'], f['fn'], 'Status:', f['status__code']
##   print 'Leistungen I: '
##   for l in f['leistungen']:
##     print '  ', l['le__name'], '(',l['le__code'],')'
##   print 'Leistungen II: '
##   for l in f.getinv('leistungen', 'le', 104):
##     print '  ', l['le__name'], '(',l['le__code'],')'
##   print 'Zustaendigkeiten: '
##   for l in f['zustaendigkeiten']:
##     print '  ', l['mit_id__vn'], l['mit_id__na']



## ll = LeistungList(where = '')
## ll.sort('fall_id')
## for l in ll:
##   print l
##   print

## fl = FeldList('verwtyp', cc('verwtyp', 'f'))
## print len(fl)
## for f in fl:
##   print f['name']


## fs = FachstatistikList(where= 'fall_id <> 0')

## print len(fs)
## for f in fs:
##   print f['fall_id__akte_id__na'], f['fall_id__akte_id__vn'],f['fall_id__status__code']
##   ll = LeistungList(where = 'fall_id = ' + str(f['fall_id']))
##   for l in ll:
##     print l['le__name']
## print
## print string.find('asd__ASD', 'ds__')
#tidl = TabellenIDList(where = '', order = 'minid desc')
#minid = int('%(minid)d' % tidl[0]) + 100000

#druckt die Felder aller Tabellen in HTML-Format

## tl = TabelleList(where ='',order = 'name')
## for t in tl:
##   print "<P><table border cellspacing=1 cellpadding=4  bgcolor=#FFFFFF><tr><th colspan=2> %(name)s </th></tr><tr><td><B><em>Name</em></B></td><td><B><em>Feld</B></em> </td></tr>" % t
##   fl = FeldList(where = 'tab_id = %s' % t['id'], order = 'id' )
##   for f in fl:
##     print "<tr><td> %(name)s </td><td> %(feld)s </td></tr>" % f
##   print "</table><BR></P>"

  
closedb()




