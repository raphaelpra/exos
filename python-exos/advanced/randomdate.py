"""
exercice pour pratiquer l'écriture et la lecture de fichiers
ici contenant des dates, et la manipulation des dates
"""
import random
from datetime import datetime


def generate_random_date():
    """
    Génère une date aleatoire uniforme
    entre le 1er janvier 2017 et le 15 Juin 2017
    au format "jour mois annee"

    Returns:
        str: la date générée

    Example:
        23 02 2017
    """
    min_date = datetime(2017, 1, 1).toordinal()
    max_date = datetime(2017, 6, 1).toordinal()

    random_date = datetime.fromordinal(random.randint(min_date, max_date))
    # ici la date a le format 1 1 2015
    # return '{random_date.day} {random_date.month} {random_date.year}'
    # ici la date au format 01 01 2015
    return f'{random_date:%d %m %Y}'


# here the expected parameter file_dump_dates is a text file
from typing import TextIO

def write_random_dates_in_file(file_dump_dates: TextIO, nb_lines=1000):
    """
    Écrit dans le fichier file_dump_dates une suite de
    nb_lines dates générées par generate_random_date

    Args:
        file_dump_dates (file): le fichier ouvert en écriture où
            écrire le résultat (et pas un nom de fichier)
        nb_lines (int): le nombre d'échantillons à générer et
            à écrire dans le fichier (défaut 1000)

    """
    for i in range(nb_lines):
        print(f'{generate_random_date()} {i + 1} bla',
              file=file_dump_dates)


def sort_file_dates(file_dump_dates):
    """
    Lit toutes les lignes du fichier file_dump_dates,
    les trie par date, puis écrit le resultat dans un fichier
    dont le nom est ce lui du fichier d'entrée suffixé
    par '.sort'

    Indice, on utilise le module datetime pour les dates
    Si on a L = [1 , 12, 2005], alors on prend
    date = datetime(*L[::-1])

    Args:
        file_dump_dates(file): fichier ouvert en lecture

    """
    # on construit un objet 'sample' par ligne
    # et on les range tous dans samples pour
    # pouvoir les trier
    samples = []
    for line in file_dump_dates:
        # on découpe la ligne
        *date_pieces, lineno, bla = line.split()
        # il faut convertir les 3 morceaux de la date en entiers
        date_ints = [int(x) for x in date_pieces]
        # une ruse de sioux pour retourner les 3 premiers éléments
        # et les passer à datetime
        # c'est comme si on avait fait
        #date = datetime(date_ints[2], date_ints[1], date_ints[0])
        date = datetime(*date_ints[::-1])
        # on range cet élément 'date' comme premier
        # élément de chaque 'sample' - pour trier
        # et on garde aussi lineno et bla
        samples.append([date, lineno, bla])

    samples.sort(key=lambda x: x[0])
    # ça suppose que le fichier passé a un nom..
    sorted_filename = file_dump_dates.name + '.sort'
    with open(sorted_filename, "w") as output:
        for date, lineno, bla in samples:
            output.write(f'{date:%d %m %Y} {lineno} {bla}\n')
    print(f"On a écrit {sorted_filename}")

if __name__ == '__main__':
    with open('randomdate.txt', 'w', encoding='utf-8') as f:
        write_random_dates_in_file(f, 5)
    with open('randomdate.txt', 'r', encoding='utf-8') as f:
        sort_file_dates(f)
