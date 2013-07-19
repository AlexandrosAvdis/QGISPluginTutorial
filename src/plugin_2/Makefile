RESOURCE_FILES = Qt_resources.py

compile: $(RESOURCE_FILES)

install:
	sudo ln -fs $(PWD) /usr/share/qgis/python/plugins/plugin_2

%.py : %.qrc
	pyrcc4 -o $@  $<

clean:
	rm -f $(RESOURCE_FILES) *.pyc
