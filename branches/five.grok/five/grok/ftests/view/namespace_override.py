"""
  >>> from five.grok.ftests.view.namespace_override import *
  >>> id = getRootFolder()._setObject("manfred", Mammoth(id='manfred'))

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/manfred")
  >>> print browser.contents
  <html>
  <body>
  <h1>Hello!</h1>
  </body>
  </html>

"""
from five import grok

class Mammoth(grok.Model):

    def __init__(self, id):
        super(Mammoth, self).__init__(id)
        self.id = id


class CustomViewClass(object):

    def hello(self):
        return u'Hello'


class Index(grok.View):

    def namespace(self):
        return {'view': CustomViewClass()}

