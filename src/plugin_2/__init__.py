'''
plugin_2: A simple "Hello World" plugin, displaying a message in a Qt dialogue-window
'''

def name():
    '''Function returning the plugin name.'''
    return "plugin_2"

def description():
    '''Function returning a string describing the plugin.'''
    return "My second QGIS python plugin!"

def version():
    '''Function returning the version of the plugin.'''
    return "Version 0.1"

def icon():
    '''Function returning the filename of the plugin icon.'''
    return "icon.png"

def qgisMinimumVersion():
    '''Function returning the minimum QGIS version that this
       plugin is operational in.'''
    return "1.8"

def author():
    '''Function stating the author of the plugin.'''
    return "Alexandros Avdis, Applied Modelling and Computation Group (AMCG)"

def email():
    '''Function returning the contact e-mail for the plugin.'''
    return "a.avdis@imperial.ac.uk"

def category():
    '''Function returning the contact e-mail for the plugin.'''
    return "noMail"

def classFactory(interface):
    '''Function returning an instance of the class
       encapsulating the plugin.'''
    #Create plugin_2 instance
    from plugin_2 import plugin_2
    plugin_2_instance = plugin_2(interface)
    return plugin_2_instance
