.PHONY: all clean

all: notes

notes: notes.tex
	pdflatex -halt-on-error $@
	makeindex notes.idx
	pdflatex -halt-on-error $@
	pdflatex -halt-on-error $@

clean:
	$(RM) *.aux *.bbl *.blg *.cut *fdb_latexmk *.fls *.idx *.ind *.ilg *.log *.out *.pdf *.toc
