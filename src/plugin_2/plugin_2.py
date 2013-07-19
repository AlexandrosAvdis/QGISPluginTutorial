'''
plugin_2: A simple "Hello World" plugin.
'''
import PyQt4.QtCore as PyQtCore
import PyQt4.QtGui as PyQtGui
import Qt_resources

class plugin_2:
      '''
      Class encapsulating the plugin functionality.
      '''

      def __init__(self, interface):
          #Must save reference to interface
          self.interface = interface

      def initGui(self):
          '''
          Method setting up QGIS GUI(the main window).
          '''
          #Create a PyQt icon for plugin_2. Tie that icon to a PyQt action
          plugin_2_icon = PyQtGui.QIcon(":/plugins/plugin_2/icon.png")
          self.action = PyQtGui.QAction(plugin_2_icon,"plugin 2, Hello World!", \
                                        self.interface.mainWindow() \
                                       )
          #Add a new entry to the menu and the icon to the toolbar.
          self.interface.addToolBarIcon(self.action)
          self.interface.addPluginToMenu("Plugin_2", self.action)
          #Connect the apppropriate signal from the action to a method in this class
          PyQtCore.QObject.connect(self.action, PyQtCore.SIGNAL("triggered()"), \
                                   self.sayHello \
                                  )

      def unload(self):
          '''
          Method cleaning-up QGIS GUI when user chooses to unload the
          plugin.
          '''
          self.interface.removeToolBarIcon(self.action)
          self.interface.removePluginMenu("Plugin_2", self.action)

      def sayHello(self):
          '''
          Create and show dialogue window with Hello-World message
          '''
          #
          helloWorldDialogue = PyQtGui.QMessageBox()
          helloWorldDialogue.setText("Hello World of Python QGIS plugins!")
          helloWorldDialogue.exec_()
