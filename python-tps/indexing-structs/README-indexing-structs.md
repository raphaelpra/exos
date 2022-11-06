---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -jupytext.custom_cell_magics, -language_info.version, -language_info.codemirror_mode.version,
    -language_info.codemirror_mode, -language_info.file_extension, -language_info.mimetype,
    -toc, -vscode
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
  title: un index de structs
---

# les dicts comme struct ou comme index

+++

dans ce petit exercice on va utiliser
* le dict pour gérer des enregistrements (en C on dirait des *structs*)
* le dict pour indexer un grand nombre de données pour accélérer les recherches
* et l'ensemble pour détecter les collisions et calculer le nombre d'entrées uniques dans une collection

***disclaimer***: gardez à l'esprit le caractère pédagogique de l'exercice,  
car pour ce genre de choses, dans la vraie vie, on pourrait aussi utiliser une dataframe pandas...

+++

## parsing

on veut pouvoir lire des fichiers texte qui ressemblent à celui-ci
```
Marie Durand 25 Décembre 2002
Jean Dupont 12 Novembre 2001
Camille Saint-Nazaire 15 Avril 2000
```

on suppose dans tout ce TP qu'il y a **unicité du (nom x prénom)**  
i.e. on n'est pas confronté au cas où deux personnes ont le même nom et le même prénom


* écrivez une fonction qui lit ce genre de fichiers et qui retourne les données sous la forme d'une liste de dictionnaires;  
* quelles seraient les clés à utiliser pour ces dictionnaires ?
* testez votre fonction sur ce fichier

+++

## génération de données de test

à partir des deux fichiers joints:

* `last_names.txt`  
  (dérivé de <https://fr.wikipedia.org/wiki/Liste_des_noms_de_famille_les_plus_courants_en_France>)
* `first_names.txt`  
  (dérivé de <https://fr.wikipedia.org/wiki/Liste_des_pr%C3%A9noms_les_plus_donn%C3%A9s_en_France>)

* fabriquez un jeu de données aléatoires contenant 5000 personnes  
  avec la contrainte qu'il y ait en sortie **unicité du nom x prénom**  
* pour les dates de naissance tirez au sort une date entre le 01/01/2000 et le 31/12/2004
* rangez cela dans le fichier `data-big.txt`

+++

## accélération des recherches

* utilisez `%%timeit` pour mesurer le temps moyen qu'il faut pour chercher une personne dans la liste à partir de son nom et prénom
* comment pourrait-on faire pour accélérer ce travail? 
* écrivez le code qui va bien et mesurez le gain de performance pour la recherche

+++

## calcul du nombre de prénoms distincts

+++

* calculez le nombre de prénoms distincts présents dans les données

+++

***
