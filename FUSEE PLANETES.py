import pygame
from random import *

pygame.init()

HAUTEUR_FENETRE = 600
LARGEUR_FENETRE = 600

COULEUR_FOND = (255, 255, 250)
ECRAN = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))

# booléen de gestion de la boucle
ARRET_JEU = False

# Variables FUSEE
XX_FUSEE = 210
YY_FUSEE = 300
LARGEUR_FUSEE = 88
HAUTEUR_FUSEE = 175
MOUVEMENT_XX_FUSEE = 0


# Variables PLANETES
XX_PLANETE = randint(30, 130)
YY_PLANETE = 20
LARGEUR_PLANETE = 111
HAUTEUR_PLANETE = 80
XX_ENTRE_PLANETES = 350
YY_ENTRE_PLANETE = 125
VITESSE_PLANETES = 3

# Points et divers
POINTS = 0
FONT = pygame.font.Font(None, 24)
SCORE = FONT.render("0 points", 1, (255, 0, 0))

# IMAGES
IMG_FUSEE = pygame.image.load("img/FUSEE.png")
IMG_PLANETE_GAUCHE = pygame.image.load("img/PLANETE.png")
IMG_PLANETE_DROITE = pygame.image.load("img/PLANETE.png")

pygame.display.set_caption("PREMIER JEU")

while not ARRET_JEU:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ARRET_JEU = True
            if event.key == pygame.K_RIGHT:
                MOUVEMENT_XX_FUSEE = 4
        elif event.type == pygame.KEYUP:
            MOUVEMENT_XX_FUSEE = -4


        if XX_FUSEE < -10 or XX_FUSEE > LARGEUR_FENETRE:
            ARRET_JEU = True

    ECRAN.fill(COULEUR_FOND)

    ECRAN.blit(IMG_PLANETE_GAUCHE, (XX_PLANETE, YY_PLANETE))
    ECRAN.blit(IMG_PLANETE_DROITE, (XX_PLANETE + XX_ENTRE_PLANETES, YY_PLANETE + YY_ENTRE_PLANETE))

    YY_PLANETE = YY_PLANETE + VITESSE_PLANETES

    if YY_PLANETE > HAUTEUR_FENETRE:
        XX_PLANETE = randint(55, 150)
        YY_PLANETE = 25
        POINTS = POINTS + 1
        SCORE = FONT.render(str(POINTS) + " points", 1, (255, 0, 0))

    # PLANETE GAUCHE COLLISION
    POINT_BAS_DROIT_PREMIERE_PLANETE_X = XX_PLANETE + LARGEUR_PLANETE
    POINT_BAS_DROIT_PREMIERE_PLANETE_Y = YY_PLANETE + HAUTEUR_PLANETE

    if POINT_BAS_DROIT_PREMIERE_PLANETE_X > XX_FUSEE:
        if POINT_BAS_DROIT_PREMIERE_PLANETE_Y > YY_FUSEE:
            if POINT_BAS_DROIT_PREMIERE_PLANETE_Y < YY_FUSEE + HAUTEUR_FUSEE:
                ARRET_JEU = True

    # PLANETE DROITE COLLISION
    POINT_BAS_GAUCHE_DEUXIEME_PLANETE_X = XX_PLANETE + XX_ENTRE_PLANETES
    POINT_BAS_GAUCHE_DEUXIEME_PLANETE_Y = YY_PLANETE + YY_ENTRE_PLANETE + HAUTEUR_PLANETE

    if XX_FUSEE + LARGEUR_FUSEE > POINT_BAS_GAUCHE_DEUXIEME_PLANETE_X:
        if XX_FUSEE < POINT_BAS_GAUCHE_DEUXIEME_PLANETE_Y:
            if XX_FUSEE + HAUTEUR_FUSEE > POINT_BAS_GAUCHE_DEUXIEME_PLANETE_Y:
                ARRET_JEU = True

    XX_FUSEE = XX_FUSEE + MOUVEMENT_XX_FUSEE
    ECRAN.blit(SCORE, (20, 580))
    ECRAN.blit(IMG_FUSEE, (XX_FUSEE, YY_FUSEE))
    pygame.display.update()
