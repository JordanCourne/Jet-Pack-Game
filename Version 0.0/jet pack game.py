"""
Code du jeu Jet Pack
Par Jordan Courné
Ce code est codé avec les pieds, c'est un brouillon
"""

import pygame, time, random
from pygame.locals import *
from Objets import *

### Fenetre ###
formatFenetreL = 16
formatFenetreH = 9
tailleFenetreL = 1300
tailleFenetreH = int(tailleFenetreL * formatFenetreH / formatFenetreL)
    #Affichage Fenetre
pygame.init()
fenetre = pygame.display.set_mode((tailleFenetreL, tailleFenetreH))
pygame.display.set_caption("JapGame")
    #Fond
fondBleute = (235,250,255)
pygame.draw.rect(fenetre, fondBleute, (0,0,tailleFenetreL,tailleFenetreH))

### Personnage ###
perso1 = pygame.image.load("perso 1.png").convert_alpha()
hauteurPerso1 = perso1.get_height()
largeurPerso1 = perso1.get_width()
posX = int(tailleFenetreL/5)
posY = int(tailleFenetreL/5)
perso1 = pygame.transform.scale(perso1, (40,int(40 * hauteurPerso1 / largeurPerso1)))
fenetre.blit(perso1, (posX, posY))

### Astéroide ###
#asteroide = pygame.image.load("asteroide.png").convert_alpha()
asteroide = pygame.image.load("asteroide.png").convert_alpha()
asteroide = initialisationAsteroide(asteroide) #Fichier Objets
fenetre.blit(asteroide, getPosAsteroide())

### Rafraîchessement de la fenêtre ###
pygame.display.flip()

### main ###
running = True
pygame.key.set_repeat(150, 3)

while running :
    pygame.draw.rect(fenetre, (235,250,255), (0,0,tailleFenetreL,tailleFenetreH))
    
    for event in pygame.event.get() :
        if event.type == QUIT :
            print("Fermeture de la fenêtre")
            running = False

    touchesPresse = pygame.key.get_pressed()
    if touchesPresse[K_UP] :
        posY -= 1
    if touchesPresse[K_DOWN] :
        posY += 1
    if touchesPresse[K_LEFT] :
        posX -= 1
    if touchesPresse[K_RIGHT] :
        posX += 1

    actualiserPosAsteroide() #Fichier Objets
    
    fenetre.blit(perso1,(posX, posY))
    fenetre.blit(asteroide, getPosAsteroide())
    pygame.display.flip()
    time.sleep(0.0003)
            

