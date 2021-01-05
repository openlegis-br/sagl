"""
  >>> from five.grok.ftests.site.folder_site import *
  >>> universe = getRootFolder()

  >>> universe._setObject("earth", World(id="earth"))
  'earth'

  >>> from zope.site.hooks import setSite, setHooks
  >>> setSite(universe.earth)
  >>> setHooks()

  >>> universe.earth.objectIds()
  ['energy']
  >>> universe.earth.energy
  <ConfigurableEnergyManager at /earth/>
  >>> from zope import component
  >>> from zope.interface.verify import verifyObject
  >>> manager = component.getUtility(IEnergyManager)
  >>> manager
  <ConfigurableEnergyManager at /earth/>
  >>> manager.aq_parent
  <World at ...>
  >>> verifyObject(IEnergyManager, manager)
  True
  >>> manager.power_on()
  Light Red On!
  >>> universe.earth.energy.cool_option = 'Blue'
  >>> manager.power_on()
  Light Blue On!

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


class ConfigurableEnergyManager(grok.LocalUtility):

    grok.implements(IEnergyManager)

    cool_option = 'clean'

    def power_on(self):
        print "Light "+ self.cool_option + " On!"

    def power_off(self):
        print "Light " + self.cool_option + " Off!"


def setup_energy(manager):
    manager.cool_option = 'Red'

class World(grok.Container, grok.Site):

    grok.local_utility(ConfigurableEnergyManager, IEnergyManager,
                       public=True,
                       name_in_container='energy',
                       setup=setup_energy)

