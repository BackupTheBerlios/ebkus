#!/usr/local/bin/python


import string
from ebkus.gen import schemagen
from ebkus.gen import schemadata
from ebkus.gen import genEb

if __name__ == '__main__':
  # Falls test = 1, werden real keine Einträge in die Datenbank gemacht
  test = 0

  if test:
    print "***************************************"
    print "TEST LAUF"
    print "***************************************"
    print
  else:
    print "***************************************"
    print "ES IST ERNST!!"
    print "***************************************"
    print
  
  # Um auf die Liste der alten Tabellen zuzugreifen

# Hier stehen die Daten für das neue Schema
  schema_str = schemadata.schemainfo
  schemagen.generate_schema(schema_str, test)
