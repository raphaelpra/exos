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

FLAGS = -v

all: prune

prune:
	nbprune $(FLAGS) $(SOLUTIONS)

list-in:
	@ls -1 $(SOLUTIONS)

list-all-out:
	@nbprune -l $(SOLUTIONS)
list-out:
	@nbprune -L $(SOLUTIONS)
diff-commands:
	@nbprune -d $(SOLUTIONS)

requirements:
	pip install nbprune


# EXEC
exec:
	./execute-all-notebooks.sh -v

exec-clean:
	./execute-all-notebooks.sh -x -c -v


# BOOKS

tocs: jb/_toc-python.yml jb/_toc-ds.yml

jb/_toc-python.yml: .nbhosting/nbhosting.yaml
	$$HOME/git/nbhosting/scripts/nbh-to-jb-toc.py $< $@ -t python

jb/_toc-ds.yml: .nbhosting/nbhosting.yaml
	$$HOME/git/nbhosting/scripts/nbh-to-jb-toc.py $< $@ -t data-science

book-python:
	jupyter-book build --toc jb/_toc-python.yml --config jb/_config.yml .
book-ds:
	jupyter-book build --toc jb/_toc-ds.yml --config jb/_config.yml .

book:
	@echo choose the book you want to build
	@echo make book-python
	@echo or
	@echo make book-ds
