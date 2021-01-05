"""
  >>> from five.grok.ftests.view.index import *
  >>> root_folder = getRootFolder()
  >>> mammoth = Mammoth('manfred')
  >>> id = root_folder._setObject("manfred", mammoth)

The default view name for a model is 'index':

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/manfred")
  >>> print browser.contents
  <html>
  <body>
  <h1>Hello, world!</h1>
  Color: <span>Blue</span>
  Color: <span>Blue</span>
  URL: <span>http://localhost/manfred/index</span>
  </body>
  </html>

"""
from five import grok

class Mammoth(grok.Model):
    teeth = u"Blue"

class Index(grok.View):
    pass

index = grok.PageTemplate("""\
<html>
<body>
<h1>Hello, world!</h1>
Color: <span tal:content="python:context.teeth">green</span>
Color: <span tal:content="context/teeth">green</span>
URL: <span tal:content="view/url">url</span>
</body>
</html>
""")
