---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: 'lancer un sous-process'
---

# gestion de sous-processus

```{code-cell} ipython3
import subprocess
```

## forker un autre programme

+++

### lancer un autre programme : un autre Python

+++

by the way, on peut accéder au chemin du Python courant comme ceci

```{code-cell} ipython3
# on n'en a pas complètement besoin, mais bon

import sys
sys.executable
```

```{code-cell} ipython3
fullpath = sys.executable
fullpath
```

```{code-cell} ipython3
# avec Python -c je peux passer du code à python sur la ligne de commande

! python -c "print('bien le bonjour de Python')"
```

## le + simple

```{code-cell} ipython3
completed = subprocess.run(['ls', '-l'])
completed.returncode
```

pour lancer un programme depuis Python

```{code-cell} ipython3
# command = [sys.executable, "-c", "print('bonjour de Python')"]
command = ["python", "-c", "print('bonjour de Python')"]

completed = subprocess.run(command)
completed.returncode
```

returncode=0 signifie que ça a fonctionné, mais on n'a pas vu le résultat

+++

## capture de stdout/stderr

```{code-cell} ipython3
# pareil mais pour lire la sortie
completed = subprocess.run(command, stdout=subprocess.PIPE)
completed.returncode
```

```{code-cell} ipython3
# cette fois on a capturé la sortie standard
# sauf que ce sont des bytes...

type(completed.stdout)
```

```{code-cell} ipython3
# ... qu'il faut decoder comme du texte 

output = completed.stdout.decode()
print(output)
```

## rediriger la sortie

```{code-cell} ipython3
with open('subprocess.stdout', 'w') as writer:
    completed = subprocess.run(command, stdout=writer)
```

```{code-cell} ipython3
!cat subprocess.stdout
```

## quelques astuces pratiques

+++

### shell=True

```{code-cell} ipython3
command_oneline = """python -c "print('hello de Python')" """

completed = subprocess.run(command_oneline, shell=True, stdout=subprocess.PIPE)
print(f"{completed.returncode=}, {completed.stdout.decode()=}")
```

### text=True

```{code-cell} ipython3
# si on sait que la sortie est du texte
# comme ça on n'a pas besoin de decoder
completed = subprocess.run(
    command, stdout=subprocess.PIPE, text=True)
print(f"{completed.returncode=}, {completed.stdout=}")
```

## pour aller plus loin

+++

Si maintenant on veut pouvoir contrôler plus finement le déroulement
notamment lire les sorties / fournir les entrées 
de manière intelligente, il faut avoir recours à `Popen.communicate()` https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate

+++

***
