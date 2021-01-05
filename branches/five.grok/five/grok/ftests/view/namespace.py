"""
  >>> from five.grok.ftests.view.namespace import *
  >>> id = getRootFolder()._setObject("manfred", Mammoth(id='manfred'))

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/manfred")
  >>> print browser.contents
  <html>
  <body>
  <h1>Hello I am manfred!</h1>
  </body>
  </html>

"""
from five import grok

class Mammoth(grok.Model):

    def __init__(self, id):
        super(Mammoth, self).__init__(id)
        self.id = id

class Index(grok.View):

    def namespace(self):
        return {'name': self.context.id}

index = grok.PageTemplate("""\
<html>
<body>
<h1>Hello I am <tal:name tal:replace="name" />!</h1>
</body>
</html>
""")
