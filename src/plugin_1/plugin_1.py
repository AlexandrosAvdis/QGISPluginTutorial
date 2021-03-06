'''
plugin_1: A simple "Hello World" plugin.
'''
import PyQt4.QtCore as PyQtCore
import PyQt4.QtGui as PyQtGui
import Qt_resources

class plugin_1:
      '''
      Class encapsulating the plugin functionality.
      '''

      def __init__(self, interface):
          #Write to log-file
          f = open('plugin_1.log','a')
          f.write("Initialising plugin_1 instance.\n")
          f.close()
          #Must save reference to interface
          self.interface = interface

      def initGui(self):
          '''
          Method setting up QGIS GUI(the main window).
          '''
          #Write to log-file
          f = open('plugin_1.log','a')
          f.write("Changing QGIS GUI to reflect plugin addition.\n")
          f.close()
          #Create a PyQt icon for plugin_1. Tie that icon to a PyQt action
          plugin_1_icon = PyQtGui.QIcon(":/plugins/plugin_1/icon.png")
          self.action = PyQtGui.QAction(plugin_1_icon,"plugin 1, Hello World!", \
                                        self.interface.mainWindow() \
                                       )
          #Add a new entry to the menu and the icon to the toolbar.
          self.interface.addToolBarIcon(self.action)
          self.interface.addPluginToMenu("Plugin_1", self.action)
          #Connect the apppropriate signal from the action to a method in this class
          PyQtCore.QObject.connect(self.action, PyQtCore.SIGNAL("triggered()"), \
                                   self.sayHello \
                                  )

      def unload(self):
          '''
          Method cleaning-up QGIS GUI when user chooses to unload the
          plugin.
          '''
          #Write to log-file
          f = open('plugin_1.log','a')
          f.write("Resetting QGIS GUI to prior plugin-addition state.")
          f.write(" Bye World, see you soon!\n")
          f.close()
          self.interface.removeToolBarIcon(self.action)
          self.interface.removePluginMenu("Plugin_1", self.action)

      def sayHello(self):
          '''
          Write Hello World! in log-file.
          '''
          #Write to log-file
          f = open('plugin_1.log','a')
          f.write("Hello World!\n")
          f.close()
