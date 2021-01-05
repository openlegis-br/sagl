"""
  >>> from five.grok.ftests.view.redirect import *
  >>> id = getRootFolder()._setObject("manfred", Mammoth(id='manfred'))

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False 
  >>> browser.open("http://localhost/manfred/@@redirect")
  >>> browser.url
  'http://localhost/manfred/@@newhome'
"""
from five import grok

class Mammoth(grok.Model):
    pass

class Redirect(grok.View):
    grok.context(Mammoth)

    def render(self):
        self.redirect('http://localhost/manfred/@@newhome')


class NewHome(grok.View):
    grok.context(Mammoth)

    def render(self):
        return "I am redirected to Here"
