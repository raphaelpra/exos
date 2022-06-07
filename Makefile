SOLUTIONS = $(shell find . -name '*.py' | egrep -- '-solution|-corrige|/\.solutions' | grep -v .ipynb_checkpoints)

all: prune

prune:
	nbprune $(SOLUTIONS)