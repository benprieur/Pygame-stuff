import pygame, sys

pygame.init()
pygame.mixer.init()

# COULEURS
COULEUR_BLANCHE = pygame.Color(255, 255, 255)

# FENETRE DE 400 SUR 400
ECRAN = pygame.display.set_mode((400,400))
ECRAN.fill(COULEUR_BLANCHE)
pygame.display.set_caption("Chapitre 5, du son")

SUITE = True

# FOND SONORE
SIFFLEMENT = pygame.mixer.music.load("sifflement.ogg")
pygame.mixer.music.play(1, 0.0)

# EFFETS SONORES
COQ = pygame.mixer.Sound("coq.ogg")
CORNEILLE = pygame.mixer.Sound("corneille.ogg")
VELO = pygame.mixer.Sound("vélo.ogg")

# BOUCLE DE JEU
while SUITE:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      SUITE = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        SUITE = False
      elif event.key == pygame.K_o:
        COQ.play()
      elif event.key == pygame.K_c:
        CORNEILLE.play()
      elif event.key == pygame.K_v:
        VELO.play()
      elif event.key == pygame.K_DOWN:
        VOLUME = pygame.mixer.music.get_volume() - 0.1
        pygame.mixer.music.set_volume(VOLUME)
        COQ.set_volume(VOLUME)
        CORNEILLE.set_volume(VOLUME)
        VELO.set_volume(VOLUME)
      elif event.key == pygame.K_UP:
        VOLUME = pygame.mixer.music.get_volume() + 0.1
        pygame.mixer.music.set_volume(VOLUME)
        COQ.set_volume(VOLUME)
        CORNEILLE.set_volume(VOLUME)
        VELO.set_volume(VOLUME)

  pygame.display.flip()