'''
plugin_1: A simple "Hello World" plugin.
'''

def name():
    '''Function returning the plugin name.'''
    return "plugin_1"

def description():
    '''Function returning a string describing the plugin.'''
    return "My first QGIS python plugin!"

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
    return "AMCG"

def email():
    '''Function returning the contact e-mail for the plugin.'''
    return "noMail"

def classFactory(interface):
    '''Function returning an instance of the class
       encapsulating the plugin.'''
    #Open log-file
    f = open('plugin_1.log','w')
    f.write("Loading plugin_1 into QGIS.\n")
    f.close()
    #Create plugin_1 instance
    from plugin_1 import plugin_1
    plugin_1_instance = plugin_1(interface)
    f = open('plugin_1.log','a')
    f.write("plugin_1 instance created, returning to QGIS.\n")
    f.close()
    return plugin_1_instance
