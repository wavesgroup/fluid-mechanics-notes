.PHONY: all clean

all: notes

notes: notes.tex
	pdflatex -halt-on-error -shell-escape $<
	makeindex notes.idx
	pdflatex -halt-on-error -shell-escape $<
	pdflatex -halt-on-error -shell-escape $<

clean:
	$(RM) *.aux *.bbl *.blg *.cut *fdb_latexmk *.fls *.idx *.ind *.ilg *.log *.out *.pdf *.toc
