---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"run_control": {"frozen": false, "read_only": false}}

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
</div>

+++ {"run_control": {"frozen": false, "read_only": false}}

# Première partie

* On vous demande d'écrire une classe `Echo`
* qui répond à toutes les méthodes dont le nom  fait 3 lettres
* et qui dans ce cas retourne le nom de la méthode concaténé 3 fois

+++ {"run_control": {"frozen": false, "read_only": false}}

```
>>> echo = Echo()
>>> echo.foo()
'foofoofoo'
>>> echo.bar()
'barbarbar'
>>> echo.six()
'sixsixsix''
```

+++ {"run_control": {"frozen": false, "read_only": false}}

## Indices

* une seule méthode `__getattr__` suffit
* elle doit renvoyer une méthode
* ou lever l'exception AttributeError

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
slideshow:
  slide_type: slide
---
class Echo:
    def __getattr__(self, attrname):
        if len(attrname) == 3:
            # on pourrait écrire tripler()
            # mais pour inspecter ce qui nous est vraiment passé
            def tripler(*args, **kwds):
                # print("incoming", args, kwds)
                return attrname * 3
            return tripler
        else:
            raise AttributeError(f"No such method {attrname} length = {len(attrname)} != 3")
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
slideshow:
  slide_type: slide
---
echo = Echo()
echo.foo()
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
echo.bar()
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
try:
    echo.foobar()
except AttributeError as e:
    print("OOPS", e)
```

+++ {"run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "slide"}}

# Deuxième partie

+++ {"run_control": {"frozen": false, "read_only": false}}

* on veut maintenant une classe Proxy
* qu'on crée à partir d'une instance de `Echo`
* et d'une blacklist (une liste de mots de 3 lettres)
* et qui répond là encore à toutes les méthodes
* dont le nom fait 3 lettres
* en sous-traitant à son instance de `Echo`
* sauf pour les méthodes dans la blacklist

+++ {"run_control": {"frozen": false, "read_only": false}}

## Indices

* très similaire au précédent
* attention à bien appeler la méthode de `echo` 
  * une fois que vous l'avez localisée

+++

```
>>> blacklist = [ 'six', 'two', 'four']
>>> echo2 = BlacklistEcho(blacklist)
>>> echo2.foo()
'foofoofoo'
>>> echo2.six()
... raise AttributeError

```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
slideshow:
  slide_type: slide
---
class BlacklistEcho(Echo):
    def __init__(self, blacklist):
        super().__init__()
        self.blacklist = blacklist
    def __getattr__(self, attrname):
        if attrname in self.blacklist:
            raise AttributeError("blacklisted method {attrname}")
        return super().__getattr__(attrname)
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
slideshow:
  slide_type: slide
---
blacklist = [ 'six', 'two', 'four']

echo2 = BlacklistEcho(blacklist)

echo2.foo()
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
try:
    echo2.six()
except AttributeError as e:
    print("OOPS", e)
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
try:
    echo2.foobar()
except AttributeError as e:
    print("OOPS", e)
```
