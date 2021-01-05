"""
  >>> from five.grok.ftests.site.local_site import *
  >>> universe = getRootFolder()

  >>> universe["earth"] = World(id="earth")
  >>> from zope.location import interfaces
  >>> from zope.interface.verify import verifyObject
  >>> verifyObject(interfaces.ISite, universe.earth)
  True

  >>> from zope.site.hooks import setSite, setHooks
  >>> setSite(universe.earth)
  >>> setHooks()

  >>> from zope import component
  >>> manager = component.getUtility(IEnergyManager)
  >>> manager
  <EnergyManager at ...>
  >>> manager.aq_parent
  <World at ...>
  >>> verifyObject(IEnergyManager, manager)
  True

  >>> from grokcore.component.interfaces import IContext
  >>> IContext.providedBy(manager)
  True

  >>> from zope.annotation.interfaces import IAttributeAnnotatable
  >>> IAttributeAnnotatable.providedBy(manager)
  True

"""

from zope.interface import Interface
from five import grok


class IEnergyManager(Interface):

    def power_on():
        """Power up the world.
        """

    def power_off():
        """Shutdown the world.
        """


class EnergyManager(grok.LocalUtility):

    grok.implements(IEnergyManager)

    def power_on(self):
        print "Light On!"

    def power_off(self):
        print "Light Off!"


class World(grok.Model, grok.Site):

    grok.local_utility(EnergyManager, IEnergyManager)



