#!/usr/local/bin/python


import string
from ebkus.gen import genEb

import schemadata

filename = 'ebapigen.py'

if __name__ == '__main__':
  f = genEb.generate_ebapi(schemadata.schemainfo)
  file = open('../app/%s' % filename, 'w')
  file.write(f.getvalue())
  f.close()
  file.close()
  print '----> ', filename, 'generiert'  
