.PHONY: all clean

all: book

book: fluid-mechanics-book.tex
	pdflatex -halt-on-error -shell-escape $<
	makeindex fluid-mechanics-book.idx
	pdflatex -halt-on-error -shell-escape $<
	pdflatex -halt-on-error -shell-escape $<

clean:
	$(RM) *.aux *.bbl *.blg *.cut *fdb_latexmk *.fls *.idx *.ind *.ilg *.log *.out *.pdf *.toc
