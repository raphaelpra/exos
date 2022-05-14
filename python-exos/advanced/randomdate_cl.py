# -*- coding: utf-8 -*-

"""
exercice pour pratiquer l'écriture et la lecture de fichiers
d'un fichier contenant des dates, et la manipulation des dates
"""
import random
from datetime import datetime

from randomdate import generate_random_date, write_random_dates_in_file

# variante commentaire random
dictionary = """
Doth with his lofty and shrill-sounding Throate
Awake the God of Day: and at his warning,
Whether in Sea, or Fire, in Earth, or Ayre,
The extravagant, and erring Spirit, hyes
"""
dict_words = [x.strip() for x in dictionary.split()]


def generate_comment():
    """
    Génère un commentaire de mots tirés au hasard dans
    dictionary; le nombre de mots lui-même est tiré au
    hasard entre 1 et 3
    """
    how_many = random.randint(1, 4)
    # ça pourrait être aussi une compréhension
    words = (random.choice(dict_words) for i in range(how_many))
    return " ".join(words)


def write_random_dates_in_file(file_dump_dates, nb_line=1000):
    """
    Écrit dans le fichier file_dump_dates une suite de
    nb_lines dates générées par generate_random_date

    Args:
        file_dump_dates (file): le fichier ouvert en écriture où
            écrire le résultat (et pas un nom de fichier)
        nb_lines (int): le nombre d'échantillons à générer et
            à écrire dans le fichier (défaut 1000)

    """
    for i in range(nb_line):
        print(f'{generate_random_date()} {i+1} {generate_comment()}',
              file=file_dump_dates)


class Sample:
    """
    un objet Sample est construit à partir d'une ligne
    du fihier généré dans l'exercice
    il contient 3 éléments:
    date: instance de datetime
    lineno: numéro de ligne (str)
    bla: le commentaire
    """

    def __init__(self, linestr):
        # on découpe la ligne
        # cette fois on s'y prend autrement
        # imaginons que le commentaire peut avoir des espaces..
        jour, mois, annee,  lineno, *words = linestr.split()
        # il faut convertir les 3 morceaux de date en entiers
        date_ints = [int(x) for x in (annee, mois, jour)]
        date = datetime(*date_ints)
        self.date = date
        # on range cet élément 'date' comme premier
        # élément de chaque 'sample' - pour trier
        # et on garde aussi lineno et bla
        self.lineno = lineno
        self.bla = " ".join(words)

    def write(self, outfile):
        outfile.write(f'{self.date:%d %m %Y} {self.lineno} {self.bla}\n')


def sort_file_dates(file_dump_dates):
    """
    Lit dans le fichier file_dump_dates chaque ligne
    et trie toutes les lignes en fonction de la date
    puis écrit le resultat dans un fichier
    file_dump_dates_sorted

    Indice, on utilise le module datetime pour les dates
    Si on a L = [1 , 12, 2005], alors on prend
    date = datetime(*L[::-1])

    """
    # on construit un objet 'sample' par ligne
    # et on les range tous dans samples pour
    # pouvoir les trier
    samples = []
    for line in file_dump_dates:
        samples.append(Sample(line))
    # on trie sur la date du sample
    samples.sort(key=lambda x: x.date)

    # ça suppose que le fichier passé a un nom..
    sorted_filename = file_dump_dates.name + '.sort'
    with open(sorted_filename, "w") as output:
        for sample in samples:
            sample.write(output)
    print(f"On a écrit {len(samples)} lignes dans {sorted_filename}")

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-n", "--number", dest='samples',
                        type=int, default=10,
                        help="nombre d'échantillons")
    args = parser.parse_args()

    with open('randomdate-cl.txt', 'w', encoding='utf-8') as f:
        write_random_dates_in_file(f, args.samples)
    with open('randomdate-cl.txt', 'r', encoding='utf-8') as f:
        sort_file_dates(f)
