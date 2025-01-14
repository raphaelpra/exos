### TP : Création d’un outil CLI en Python pour récupérer des blagues

#### Objectifs du TP

- Manipuler les modules `requests` et `argparse` en Python.
- Créer un outil en ligne de commande (CLI).
- Consommer une API web pour récupérer des données.

---

#### Prérequis

1. Connaissance de base du langage Python.
2. Savoir créer des fonctions et manipuler des bibliothèques.
3. Accès à internet pour installer des bibliothèques et tester l’outil.

---

#### Description de l’exercice

Vous allez développer un programme en Python qui permet de récupérer des blagues à partir de l’API :

```
https://github.com/15Dkatz/official_joke_api
```

Cet outil devra être utilisable via la ligne de commande, où l’utilisateur pourra spécifier une catégorie de blagues (exemple : `programming`, `general`, etc.).

---

#### Déroulé

1. **Initialisation du projet**

   - Créez un fichier Python intitulé `fetch_jokes.py`.
   - Importez les modules nécessaires :
     ```python
     # À compléter : Importer les modules nécessaires
     import argparse
     import requests
     ```

2. **Création de l'outil CLI**

   - Configurez un parser d’arguments avec le module `argparse`.
   - Ajoutez un argument pour que l’utilisateur puisse spécifier la catégorie de la blague :
     ```python
     parser = argparse.ArgumentParser(description="Outil pour récupérer des blagues depuis une API.")
     # À compléter : Ajouter un argument pour la catégorie
     ```

3. **Requête vers l’API**

   - Identifiez les URL utilisables de l’API pour récupérer des blagues par catégorie.
   - Réalisez une requête GET avec le module `requests` :
     ```python
     url = f"https://official-joke-api.appspot.com/jokes/{args.category}/random"
     response = "Fixme" # À compléter pour effectuer une requête GET (chercher doc requests)

     if response.status_code == 200:
         # À compléter pour extraire et afficher les données de la réponse
     else:
         # À compléter pour gérer les erreurs de requête
     ```

4. **Améliorations**

   - Affichez un message d’aide si l'utilisateur ne précise pas de catégorie.
   - Ajoutez une option pour afficher l’intégralité de la réponse JSON pour diagnostic (exemple : `--debug`).

5. **Test de l'outil**

   - Lancez le script avec différentes catégories pour tester son fonctionnement :
     ```bash
     python fetch_jokes.py --category programming
     ```
   - Testez des catégories inexistantes pour vérifier la gestion des erreurs :
     ```bash
     python fetch_jokes.py --category invalid
     ```

---

#### Critères de réussite

- Le programme doit afficher une blague de la catégorie spécifiée ou un message d’erreur approprié si la catégorie n’existe pas.
- Le code doit être lisible, bien commenté et suivre les bonnes pratiques Python.
- L’outil doit gérer correctement les erreurs liées aux requêtes (ex : URL incorrecte, API hors service).

---

#### Pour aller plus loin

- Ajoutez une fonctionnalité permettant de récupérer plusieurs blagues à la fois.
- Implémentez une option pour sauvegarder les blagues dans un fichier texte.
- Gérez un mode interactif où l'utilisateur peut choisir une nouvelle blague sans relancer le script.

