SOLUTIONS = $(shell find . -name '*.py' -o -name '*.md' \
  | egrep -- '-corrige\.|-howto\.|\.teacher' \
  | grep -v .ipynb_checkpoints)

FLAGS = -v

all: prune

prune:
	nbprune $(FLAGS) $(SOLUTIONS)

list:
	@ls -1 $(SOLUTIONS)