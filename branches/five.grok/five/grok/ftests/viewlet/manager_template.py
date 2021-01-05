"""
  >>> from five.grok.ftests.viewlet.manager_template import *
  >>> id = getRootFolder()._setObject("manfred", Mammoth(id='manfred'))

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/manfred/@@painting")
  >>> print browser.contents
  <html>
  <body>
  <p>Moderne art is sometimes <b>special</b></p>
  </body>
  </html>

"""
from five import grok

class Mammoth(grok.Model):
    pass

class Painting(grok.View):
    pass

class Art(grok.ViewletManager):

    grok.view(Painting)

painting = grok.PageTemplate("""\
<html>
<body>
<tal:replace tal:replace="structure provider:art" />
</body>
</html>
""")

art = grok.PageTemplate("""\
<p>Moderne art is sometimes <b>special</b></p>
""")
