
"""Module für die Administration und Feedback"""


import string

from ebkus.app import Request
from ebkus.app import ebupd
from ebkus.app.ebapi import Akte, Fachstatistik, Jugendhilfestatistik, Code, Mitarbeiter, Kategorie
from ebkus.html.templates import *


class admin(Request.Request):
  """Für Admineinträge in der DB."""
  
  permissions = Request.ADMIN_PERM

  def processForm(self, REQUEST, RESPONSE):
    file = self.form.get('file')

    if not file or file == 'admin': 
      self.last_error_message = "Keine Dateneingabe erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)


    if self.einfuege_oder_update_operationen.get(file):
      einfuegen = self.einfuegen_oder_update(file)
      return self.admin_display()

    return self.ebkus.dispatch(file, REQUEST, RESPONSE)

  einfuege_oder_update_operationen = {
    'miteinf' : ('mitid', Mitarbeiter),
    'updmit' : ('mitid', Mitarbeiter),
    'codeeinf' : ('codeid', Code),
    'updcode' : ('codeid', Code),
    'removeakten' : ('akid', Akte),
    }

  def einfuegen_oder_update(self, file):
    function = getattr(ebupd, file)
    function(self.form)
    return ''

  def admin_display(self):
    """Feedback"""
    
    # Headerblock, Menü u. Überschrift fuer das HTML-Template
    header = {'titel': 'Feedback',
              'ueberschrift': "Feedback"}

    # Liste der Templates als String
    res = []
    res.append(header_t % header)
    res.append(menueadmin_t)
    res.append(linielang_t)
    res.append(feedback_t)
    return string.join(res, '')


class feedback(Request.Request):
  """Für Einfügen der Statistik ohne Fallnummer."""
  
  permissions = Request.STAT_PERM

  def processForm(self, REQUEST, RESPONSE):
    file = self.form.get('file')

    if not file or file == 'feedback': 
      self.last_error_message = "Keine Dateneingabe erhalten"
      return self.EBKuSError(REQUEST, RESPONSE)

    if self.einfuege_oder_update_operationen.get(file):
      einfuegen = self.einfuegen_oder_update(file)
      return self.feedback_display()

    return self.ebkus.dispatch(file, REQUEST, RESPONSE)

  einfuege_oder_update_operationen = {
    'fseinf' : ('fsid', Fachstatistik),
    'fseinf' : ('fsid', Fachstatistik),
    'jgheinf' : ('jghid', Jugendhilfestatistik),
    'jgheinf' : ('jghid', Jugendhilfestatistik),
    }

  def einfuegen_oder_update(self, file):
    function = getattr(ebupd, file)
    function(self.form)
    return ''

  def feedback_display(self):
    """Feedback"""
    
    # Headerblock, Menü u. Überschrift fuer das HTML-Template
    header = {'titel': 'Feedback', 'ueberschrift': "Feedback"}

    # Liste der Templates als String
    res = []
    res.append(header_t % header)
    res.append(menuemin_t)
    res.append(linielang_t)
    res.append(feedback_t)
    return string.join(res, '')



