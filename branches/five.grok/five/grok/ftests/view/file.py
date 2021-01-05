"""
  >>> from five.grok.ftests.view.file import *
  >>> id = getRootFolder()._setObject("manfred", Mammoth(id='manfred'))

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/manfred/@@painting")
  >>> print browser.contents
  <html>
  <body>
  <h1>Hello, world manfred!</h1>
  </body>
  </html>

"""
from five import grok

class Mammoth(grok.Model):

    def __init__(self, id):
        super(Mammoth, self).__init__(id=id)
        self.id = id

class Painting(grok.View):
    pass

painting = grok.PageTemplateFile("zope2_template.pt")
