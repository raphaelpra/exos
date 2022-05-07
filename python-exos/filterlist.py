def all_integers(iterable):
    """
    retourne la liste des éléments entiers de iterable
    iterable n'est pas modifié
    """
    return [x for x in iterable if isinstance(x, int)]

def keep_only_integers(liste):
    """
    cette fois on suppose que l'entrée est une liste
    et on **modifie** la liste pour ne garder que les entiers
    """
    # attention à ne pas modifier le sujet du for dans le for
    for x in liste[:]:
        if not isinstance(x, int):
            liste.remove(x)
    # on ne retourne rien pour bien montrer à l'appelant
    # qu'on a fait un effet de bord

if __name__ == '__main__':
    inputs = [
        [1, 2, 3, 4, 'spam', 5, 'beans'],
        [(1, 2), 3, 4, 'spam', 5, 'beans'],
        ]
    for input in inputs:
        print(10*'=')
        print(f"input(0) = {input}")
        print(f"integers = {all_integers(input)}")
        print(f"input(1) = {input}")
        keep_only_integers(input)
        print(f"input(2) = {input}")
