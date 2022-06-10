import pygame as pg
from random import randint

# on initialise pygame et on crée une fenêtre de 400x300 pixels
pg.init()
screen = pg.display.set_mode((400, 300))

# on crée aussi un objet "horloge"
clock = pg.time.Clock()

# enfin on boucle à l'infini pour faire le rendu de chaque image
while True:
    # l'objet "clock" permet de limiter le nombre d'images par secondes
    # ici pour cette démo on demande 1 image par seconde
    clock.tick(1)

    # on génère une couleur (Rouge, Vert, Bleu) au hasard
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    # et on colorie l'écran avec cette couleur
    screen.fill(random_color)

    # enfin on met à jour la fenêtre avec tous les changements
    pg.display.update()
