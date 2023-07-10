#
# run nbprune on all notebooks to produce a version without the corrections
#
# requirements:
# 	make requirements
# - or simply
# 	pip install nbprune
#


# PRUNE
SOLUTIONS = $(shell find . -name '*.py' -o -name '*.md' \
  | egrep -- '-corrige\.|\.teacher' \
  | egrep -v '.ipynb_checkpoints|_build')

PRUNEFLAGS = -v

all: prune

prune:
	nbprune $(PRUNEFLAGS) $(SOLUTIONS)

prune-in:
	@ls -1 $(SOLUTIONS)
prune-out-all:
	@nbprune -l $(SOLUTIONS)
prune-out:
	@nbprune -L $(SOLUTIONS)
prune-diff:
	@nbprune -d $(SOLUTIONS)
.PHONY: all prune prune-in prune-out-all prune-out prune-diff


requirements:
	pip install nbprune
.PHONY: requirements


# ARTEFACTS
artefacts:
	find . -name ARTEFACTS | xargs update-artefacts.sh
.PHONY: artefacts


# EXEC
exec:
	./execute-all-notebooks.sh -v
exec-clean:
	./execute-all-notebooks.sh -x -c -v
.PHONY: exec exec-clean


# table of contents: inject the contents from nbhosintg into jb
jb/_toc-python.yml: .nbhosting/nbhosting.yaml
	$$HOME/git/nbhosting/scripts/nbh-to-jb-toc.py $< $@ -t python

jb/_toc-ds.yml: .nbhosting/nbhosting.yaml
	$$HOME/git/nbhosting/scripts/nbh-to-jb-toc.py $< $@ -t data-science
toc: jb/_toc-python.yml jb/_toc-ds.yml
.PHONY: toc


# BOOKS
book-python:
	PYDEVD_DISABLE_FILE_VALIDATION=1 jupyter-book build --toc jb/_toc-python.yml --config jb/_config.yml --path-output book-python .
book-ds:
	PYDEVD_DISABLE_FILE_VALIDATION=1 jupyter-book build --toc jb/_toc-ds.yml --config jb/_config.yml --path-output book-ds .
book:
	@echo choose the book you want to build
	@echo make book-python
	@echo or
	@echo make book-ds
.PHONY: book-python book-ds book
