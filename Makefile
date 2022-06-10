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
