import pygame, sys

pygame.init()

# COULEURS
COULEUR_BLANCHE = pygame.Color(255, 255, 255)
COULEUR_NOIRE = pygame.Color(0, 0, 0)
COULEUR_ROUGE = pygame.Color(255, 0, 0)
COULEUR_VERTE = pygame.Color(0, 255, 0)
COULEUR_BLEUE = pygame.Color(0, 0, 255)

# FENETRE DE 400 SUR 400
ECRAN = pygame.display.set_mode((400,400))
ECRAN.fill(COULEUR_BLANCHE)
pygame.display.set_caption("Chapitre 4")

SUITE = True
debut_ligne = 0, 0
COULEUR = COULEUR_NOIRE
EPAISSEUR = 1

# BOUCLE DE JEU
while SUITE:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      SUITE = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        SUITE = False
      elif event.key == pygame.K_r:
        COULEUR = COULEUR_ROUGE
      elif event.key == pygame.K_v:
        COULEUR = COULEUR_VERTE
      elif event.key == pygame.K_b:
        COULEUR = COULEUR_BLEUE
      elif event.key == pygame.K_n:
        COULEUR = COULEUR_NOIRE
      elif event.key == pygame.K_p:
        EPAISSEUR = EPAISSEUR +1
      elif event.key == pygame.K_m:
        EPAISSEUR = EPAISSEUR - 1
        if EPAISSEUR < 1:
          EPAISSEUR = 1
      elif event.key == pygame.K_s:
        pygame.image.save(ECRAN, "MonDessin.png")
    elif event.type == pygame.MOUSEMOTION:
       fin_ligne = pygame.mouse.get_pos()
       if pygame.mouse.get_pressed() == (1, 0, 0):
         pygame.draw.line(ECRAN, COULEUR, debut_ligne, fin_ligne, EPAISSEUR)
       debut_ligne = fin_ligne

  pygame.display.flip()