"""
  >>> from five.grok.ftests.form.form import *
  >>> id = getRootFolder()._setObject("manfred", Mammoth(id='manfred'))

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False

  We can test the display form as default view:

  >>> browser.open("http://localhost/manfred")
  >>> print browser.contents
  <html>...
  ... Name ...
  ... Age ...
  </html>

  But we have an edition form:

  >>> browser.open("http://localhost/manfred/edit")
  >>> browser.getControl('Name').value = 'Arthur'
  >>> browser.getControl('Age').value = '325'
  >>> browser.getControl('Apply').click()
  >>> 'Updated' in browser.contents
  True

  And if we look back to the display form, we will see new values:

  >>> browser.open("http://localhost/manfred")
  >>> print browser.contents
  <html>...
  ... Name ...
  ... Arthur ...
  ... Age ...
  ... 325 ...
  </html>

"""

from five import grok
from zope import interface, schema
from zope.schema.fieldproperty import FieldProperty

class IMammoth(interface.Interface):

    name = schema.TextLine(title=u"Name")
    age = schema.Int(title=u"Age")


class Mammoth(grok.Model):

    grok.implements(IMammoth)

    name = FieldProperty(IMammoth['name'])
    age = FieldProperty(IMammoth['age'])


class Edit(grok.EditForm):

    grok.context(IMammoth)


class Index(grok.DisplayForm):

    grok.context(IMammoth)

