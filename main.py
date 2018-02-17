"""
Nom : Jet Pack Game
Présentation du jeu (à venir)
Par Jordan Courné
Version : 0.1 ( Pré-Pré-Pré Alpha)
"""
### - main.py - ###
"""
Date de la création du fichier : 03/07/2017
Date de la dernière édition du fichier : 11/07/2017
"""

### import ###
import pygame
from pygame.locals import *

import time
from window import Window
from character import Character
from game import Event
from game import Collision
from objets import Asteroide

### Main ###
tailleFenetreLargeur = 1300
hauteurPersonnage = 40
hauteurAsteroide = 300
vitesseObjet = 1.2
# Gestion très provisoire du temps
timeReference = int(time.time()*100)/100
tempsPrecedent = 0
tempsAct = 0
#
# Gestion très provisoire du temps d'apparition des asteroides
tempsDap = 3
temps2P = 0
temps4P = 0
#

fenetre = Window(tailleFenetreLargeur)
character = Character(tailleFenetreLargeur, hauteurPersonnage, fenetre)
listAsteroide = []
listAsteroide.append(Asteroide(tailleFenetreLargeur, hauteurAsteroide, vitesseObjet, fenetre))

evenement = Event()
collision = Collision()

repeat = True
##Merde, coder avec le cul mais ca marche ( à changer)
nbOccurence = 0
time1 = False
x = 0.0005
#
while repeat == True :
    #Merde, coder avec le cul mais ca marche ( à changer)
    nbOccurence +=1
    tempsDap -= x
    if tempsDap < 0.3 :
        tempsDap = 0.3
        if time1 == False :
            print("Beau Score, bravo !")
        time1 = True

    if tempsDap < 2 :
        x = 0.0004
    if tempsDap < 1.5 :
        x = 0.0003
    if tempsDap < 1 :
        x = 0.0001
    if tempsDap < 0.5 :
        x = 0.00005
    if tempsDap <= 0.3 :
        x = 0.00002

    #print(x)
    #print(tempsDap)
    
    if tempsDap < temps2P :
        listAsteroide.append(Asteroide(tailleFenetreLargeur, hauteurAsteroide, vitesseObjet, fenetre))
        temps4P = tempsAct

    temps2P = tempsAct - temps4P
    #

    repeat = evenement.obsevateurEvenement()
    fenetre.afficherFond()
    character.actualiserPerso(fenetre)

    for asteroide in listAsteroide :
        asteroide.actualiserAst(fenetre)

    ## Ecris vite fait, a modifier
    listeElementASupprime = []
    for i in range(len(listAsteroide)) :
        if listAsteroide[i].horsCadre(fenetre) :
            listeElementASupprime.append(i)

    for i in listeElementASupprime :
        del listAsteroide[i]
    #

    """# Test
    for asteroide in listAsteroide :
        pygame.draw.line(fenetre.getWindow(), (255,0,0), (asteroide.hitbox()[0], asteroide.hitbox()[1]), (asteroide.hitbox()[0], asteroide.hitbox()[3]))
        pygame.draw.line(fenetre.getWindow(), (255,0,0), (asteroide.hitbox()[2], asteroide.hitbox()[1]), (asteroide.hitbox()[2], asteroide.hitbox()[3]))
        pygame.draw.line(fenetre.getWindow(), (255,0,0), (asteroide.hitbox()[0], asteroide.hitbox()[1]), (asteroide.hitbox()[2], asteroide.hitbox()[1]))
        pygame.draw.line(fenetre.getWindow(), (255,0,0), (asteroide.hitbox()[0], asteroide.hitbox()[3]), (asteroide.hitbox()[2], asteroide.hitbox()[3]))

    pygame.draw.line(fenetre.getWindow(), (0,255,0), (character.hitbox()[0], character.hitbox()[1]), (character.hitbox()[0], character.hitbox()[3]))
    pygame.draw.line(fenetre.getWindow(), (0,255,0), (character.hitbox()[2], character.hitbox()[1]), (character.hitbox()[2], character.hitbox()[3]))
    pygame.draw.line(fenetre.getWindow(), (0,255,0), (character.hitbox()[0], character.hitbox()[1]), (character.hitbox()[2], character.hitbox()[1]))
    pygame.draw.line(fenetre.getWindow(), (0,255,0), (character.hitbox()[0], character.hitbox()[3]), (character.hitbox()[2], character.hitbox()[3]))
    #Si tu supprime ces lignes, supprime aussi import pygame :)"""

    for asteroide in listAsteroide :
        if collision.collision(character.hitbox(), asteroide.hitbox()) :
            # Gestion extremement provisoire du game over
            repeat = False
            #
            pass
        elif collision.collision(asteroide.hitbox(), character.hitbox()) :
            # Gestion extremement provisoire du game over
            repeat = False
            #
            pass

    # Gestion très provisoire du temps
    tempsAct = int((time.time() - timeReference)*100)/100
    if tempsAct != tempsPrecedent :
        tempsPrecedent = tempsAct
    #
    
    fenetre.actualiser()
    time.sleep(0.0003)

#totalement porvisoire
# Gestion extremement provisoire du game over
gameover = pygame.Surface((500,400))
gameover.fill((255,0,0))
fenetre.getWindow().blit(gameover, (400, 200))
# Gestion très provisoire du texte/police
texte = pygame.font.Font(None, int(fenetre.getTailleFenetreL()/20))
score = texte.render("Score Joueur : " + str(tempsAct),1,(0,0,0),(255,0,0))
fenetre.getWindow().blit(score,(fenetre.getTailleFenetreL()/3,fenetre.getTailleFenetreH()/3))
messageGO = texte.render("Game Over",1,(0,0,0),(255,0,0))
fenetre.getWindow().blit(messageGO,(fenetre.getTailleFenetreL()/3,fenetre.getTailleFenetreH()/2))
fenetre.actualiser()
#
repeat = True
while repeat :
    repeat = evenement.obsevateurEvenement()
