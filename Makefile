#
# run nbprune on all notebooks to produce a version without the corrections
#
# requirements:
# 	make requirements
# - or simply
# 	pip install nbprune
#

SOLUTIONS = $(shell find . -name '*.py' -o -name '*.md' \
  | egrep -- '-corrige\.|-howto\.|\.teacher' \
  | grep -v .ipynb_checkpoints)

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

tocs: jb/_toc-python.yml jb/_toc-ds.yml

jb/_toc-python.yml: .nbhosting/nbhosting.yaml
	$$HOME/git/nbhosting/scripts/nbh-to-jb-toc.py $< $@ -t python

jb/_toc-ds.yml: .nbhosting/nbhosting.yaml
	$$HOME/git/nbhosting/scripts/nbh-to-jb-toc.py $< $@ -t data-science
