DOCUMENT=QGISPluginTutorial

ROOT_TEX_FILE=$(DOCUMENT).tex
ALL_TEX_FILES=$(wildcard */*.tex) $(wildcard *.tex)
ALL_BIB_FILES=$(wildcard */*.bib) $(wildcard *.bib)
PDF_DOCUMENT=$(DOCUMENT).pdf

default: $(PDF_DOCUMENT)

$(PDF_DOCUMENT):$(ALL_TEX_FILES) $(ALL_BIB_FILES)
	@echo "****************************Building $(PDF_DOCUMENT)..."
	@pdflatex -shell-escape $(ROOT_TEX_FILE)
	@bibtex $(DOCUMENT)
	@pdflatex -shell-escape $(ROOT_TEX_FILE)
	@pdflatex -shell-escape $(ROOT_TEX_FILE)
	@echo "****************************Building $(PDF_DOCUMENT) complete."

clean:
	@rm -f */*.aux *.aux *.log *.nav *.out *.snm *.toc *.pdf *.bbl *.blg
	@echo "****************************Cleaning complete."

view:
	evince $(PDF_DOCUMENT) &
