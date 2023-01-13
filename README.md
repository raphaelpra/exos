# flotpython companion

this repo contains exercises and TPs that complement the Python MOOC

as a general rule, the auto-corrected exercises mentioned in the MOOC are
[bundled in the main course repo](https://github.com/flotpython/course) repo -
that was historically for technical reasons, although it is not clear that it's
still relevant

in any case, in the present repo I try to gather all the other, generally more
informal, material for practising Python and/or the Data-Science ecosystem

## there is no runtime tool here !

also note that, as opposed to the auto-corrected exercises mentioned above,
there is a **deliberate choice to not provide a notebooks infrastructure** or
any other online runtime tool here  
this is because we want our students to become autonomous, so it means they are
supposed to solve all these problems **on their own laptop**, where they are
expected to have acquired the skills for installing and managing a decent
software stack (typically bash + vscode + python + ipython + jupyter)  
the fact that most of the material is written as a notebook is mostly a
convenience, both for authoring (outputs are up-to-date), and of course in cases
where the starting material is a notebook itself

## contents

the material is organized along these 2 categories (pure Python, and the
Data-Science ecosystem) and in each category we try to make a distinction
between

* `exos`: short, simple one-shot assignments
* `tps`: more elaborate assignments, with several steps, that let students
  achieve something
* `howtos`: more for reading than for practising, that can be recipes to achieve
  some common tasks

as well as, less interesting probably:

* `samples`: miscell pieces of code that can come in handy
* `reading`: the idea was to gather full-length projects, that students could
  read; may disappear on the long run, and merged with `samples`

## formats

as noted above, most of the contents is written as notebooks; all notebooks are
jupytext-encoded using either `py:percent` or `md:myst` formats  
also all notebooks have their filename prefix ending in `-nb` to help the
distinction between notebooks and pure Python or pure markdown

## online

these 2 categories are available online here, with an attempt to organize each
content into meaningful sections:

* [pure-Python: start here](https://nbhosting.inria.fr/builds/python-exos/python/latest/README.html)
* [pure-Python: start here](https://nbhosting.inria.fr/builds/python-exos/data-science/latest/README.html)

## note on autoreload in ipython or notebooks

**the problem**: you are in `ipython` or in a notebook and you do

```
from my_module import my_function
my_function(...)
```

then later on, you modify `my_module.py` under vs-code, and you want to try the
new version; your first idea is to redo the import to load the new version into
your interpreter

when then, **BEWARE** because **a second `import` will not reload the file**  
this is intended, and desirable, because loading a module is costly; so the
interpreter caches its loaded modules, and long story short, you can re-imoport
as much as you want, you still run the old code !

**to work around this situation**: with the trick that follows, you won't even
need to re-import, you will just need to re-run `my_function()` and you will use
the latest version (provided that the new module actually has no error that
prevents it from loading, of course)

you just need to add in a file named

```
~/.ipython/profile_default/ipython_config.py
```

the following lines

```python
c.InteractiveShellApp.exec_lines = []
c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
c.InteractiveShellApp.exec_lines.append('%autoreload 2')
```

to achieve that, if you have bash-compatible terminal (like for example on
windows: git for bash), you can just cut-and-paste the following snippet to
configure that on your computer:

```bash
mkdir -p ~/.ipython/profile_default
cat >> ~/.ipython/profile_default/ipython_config.py << EOF
c.InteractiveShellApp.exec_lines = []
c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
c.InteractiveShellApp.exec_lines.append('%autoreload 2')
EOF
```
