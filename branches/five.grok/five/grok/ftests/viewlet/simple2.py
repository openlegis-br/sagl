"""
  >>> from five.grok.ftests.viewlet.simple2 import *
  >>> id = getRootFolder()._setObject("manfred", Mammoth(id='manfred'))

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/manfred/@@painting")
  >>> print browser.contents
  <html>
  <body>
  <p>Classic art is not recent.</p>
  <p>Mordern art is recent</p>
  </body>
  </html>

"""
from five import grok

class Mammoth(grok.Model):
    pass

class Painting(grok.View):
    pass

painting = grok.PageTemplate("""\
<html>
<body>
<tal:replace tal:replace="structure provider:art" />
</body>
</html>
""")

class Art(grok.ViewletManager):

    grok.view(Painting)

class Modern(grok.Viewlet):

    grok.view(Painting)
    grok.viewletmanager(Art)

    def render(self):
        return u'<p>Mordern art is recent</p>'

class Classic(grok.Viewlet):

    grok.view(Painting)
    grok.viewletmanager(Art)

classic = grok.PageTemplate("""\
<p>Classic art is not recent.</p>
""")
