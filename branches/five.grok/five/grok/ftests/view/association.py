"""
  >>> from five.grok.ftests.view.association import *
  >>> id = getRootFolder()._setObject("manfred", Mammoth(id='manfred'))

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/manfred/@@art")
  >>> print browser.contents
  <html>
  <body>
  <h1>Art is beautiful!</h1>
  </body>
  </html>

"""
from five import grok

class Mammoth(grok.Model):
    pass

class Art(grok.View):

    grok.template("painting")

