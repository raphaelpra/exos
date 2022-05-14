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
  title: 'création de facture'
---

# génération de facture

+++

## le problème

+++

on veut automatiser la rédaction de factures à partir d'une liste d'items et de prix

+++

exemple d'utilisation, imaginons qu'on a les données suivantes :

```{code-cell} ipython3
company_address = """Tribeca Inc.,
Somerset House – New Wing
Lancaster Place
London WC2R 1LA
"""

thanks_message = "Thanks for shopping with us today!"

currency = '€'

items = [
    ("Books", 25.0, 2),
    ("Monitor", 250.0, 1),
    ("Computer", 500.0, 1),
]
```

à partir de ces données on pourrait imaginer plusieurs APIs pour produire des factures comme ceci

+++

### v0 : une fonction

+++

l'API la plus simple évidemment ce serait tout simplement ceci

+++

```python
invoice = generate_invoice(
    items, company_address, thanks=thanks_message, currency='$', items)
print(invoice)
```

```{code-cell} ipython3
# à vous d'écrire cette fonction
def generate_invoice():
    pass
```

```{code-cell} ipython3
invoice = generate_invoice(
    items, company_address, thanks=thanks_message, currency='$')
print(invoice)
```

#### suggestions / indices

* dans un premier temps, affichez le contenu de `company_address` tel quel
  * ensuite définissez une fontion - par exemple `center_address` qui se charge seulement de centrer l'adresse dans une certaine largeur
* les formats de f-string ont un trait très pratique ici

```{code-cell} ipython3
texte = "tutu"
largeur = 10
```

```{code-cell} ipython3
# on peut utiliser une variable AUSSI pour la largeur du format
# ici je prends 10 caractères, et je justifie mon texte à droite (le >)
#         ↓  ↓↓↓↓↓
f"X{texte:>{largeur}}X"
```

```{code-cell} ipython3
# et on peut aussi centrer (le ^) ou justifier à gauche (<)
#         ↓
f"X{texte:^{largeur}}X"
```

#### variante

est-ce que ça ne serait pas pratique que les deux derniers paramètres soient optionnels ?

+++

### v1 : une classe

+++

mais on peut aussi imaginer ceci par exemple

+++

```python
generator = InvoiceGenerator(address=company_address, 
                             thanks=thanks_message,
                            currency='$')
print(generator.invoice(items))
```

+++

### exemple de résultat

+++

ce qui dans les deux cas produirait une sortie dans le genre de la suivante

+++

```
**************************************************
                  Tribeca Inc.,                   
            Somerset House – New Wing             
                 Lancaster Place                  
                 London WC2R 1LA                  
++++++++++++++++++++++++++++++++++++++++++++++++++
     Product Name     #  Item Price       
            Books     2  25.0             
          Monitor     1  250.0            
         Computer     1  500.0            
--------------------------------------------------
            Total        800.00$
++++++++++++++++++++++++++++++++++++++++++++++++++
        Thanks for shopping with us today!        
**************************************************

```

+++

---

+++

