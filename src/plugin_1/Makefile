RESOURCE_FILES = Qt_resources.py

compile: $(RESOURCE_FILES)

install:
	cd ~/.qgis; mkdir -p python/plugins/
	ln -fst ~/.qgis/python/plugins/ $(PWD)

%.py : %.qrc
	pyrcc4 -o $@  $<

clean:
	rm -f $(RESOURCE_FILES) *.pyc
