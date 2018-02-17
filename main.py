"""
Nom : Jet Pack Game
Présentation du jeu (à venir)
Par Jordan Courné
Version : 0.2 ( Pré-Pré Alpha)
"""
### - main.py - ###
"""
Date de la création du fichier : 03/07/2017
Date de la dernière édition du fichier : 19/07/2017
"""

### import ###
import pygame
from pygame.locals import *

import time
from window import Window
from character import Character
from game import Event, Collision, Temps, Texte
from objets import Asteroide
from menu import Menu

### Main ###
tailleFenetreLargeur = 1300
hauteurPersonnage = int(tailleFenetreLargeur / 32.5) # égal à 40   quand tailleFenetreLargeur = 1300
hauteurAsteroide = int(tailleFenetreLargeur / 4.3333) # environ égal à 300 quand tailleFenetreLargeur = 1300
vitesseObjet = tailleFenetreLargeur / 1083.3333 # environ égal à 1.2 quand tailleFenetreLargeur = 1300
vitessePerso = tailleFenetreLargeur / 650 # environ égal à 2 quand tailleFenetreLargeur = 1300

# Gestion très provisoire du temps d'apparition des asteroides
tempsDap = 3
tempsEcoule = Temps()
tempsEcoule.startChrono()
#

fenetre = Window(tailleFenetreLargeur)
character = Character(tailleFenetreLargeur, hauteurPersonnage, vitessePerso, fenetre)
listAsteroide = []

repeat = True
##Merde, coder avec le cul mais ca marche (à changer)
time1 = True
x = 0.0005
score = 0
#
menu = Menu(tailleFenetreLargeur, fenetre)
menu.afficherMenu(fenetre)
fenetre.actualiser()

choix = 0
#la boucle est provisoire :
while choix != 1 :
    choix = menu.selection(fenetre)
    if choix == 1 :
        pass
    elif choix == 2 :
        pass #options
    else :
        fenetre.fermerFenetre()
        exit()

while repeat == True :
    #Merde, coder avec le cul mais ca marche (à changer)
    score += 1
    tempsDap -= x

    if tempsDap < 2 :
        x = 0.0004
    if tempsDap < 1.5 :
        x = 0.0003
    if tempsDap < 1 :
        x = 0.0001
    if tempsDap < 0.5 :
        x = 0.00005
    if tempsDap <= 0.3 and time1 :
        x = 0.00002
        print("Beau Score, bravo !")
        time1 = False

    #print(x)
    #print(tempsDap)
    
    if tempsDap < tempsEcoule.tempsEcoule() :
        listAsteroide.append(Asteroide(tailleFenetreLargeur, hauteurAsteroide, vitesseObjet, fenetre))
        tempsEcoule.startChrono() 
    #

    Event.obsevateurEvenement(fenetre)
    fenetre.afficherFond()
    character.actualiserPerso(fenetre)

    for asteroide in listAsteroide :
        asteroide.actualiserObj(fenetre)

    ## Ecris vite fait, a modifier
    listeElementASupprime = []
    for i in range(len(listAsteroide)) :
        if listAsteroide[i].horsCadre(fenetre) :
            listeElementASupprime.append(i)

    for i in listeElementASupprime :
        del listAsteroide[i]
    #
    
    """#Affichage Hitbox
    for asteroide in listAsteroide :
        asteroide.afficherHitbox(fenetre)
    character.afficherHitbox(fenetre)"""

    for asteroide in listAsteroide :
        if Collision.collision(character.hitbox(), asteroide.hitbox()) :
            # Gestion extremement provisoire du game over
            repeat = False
            #
            pass
        elif Collision.collision(asteroide.hitbox(), character.hitbox()) :
            # Gestion extremement provisoire du game over
            repeat = False
            #
            pass
    
    fenetre.actualiser()
    time.sleep(0.0003)

#totalement porvisoire
# Gestion provisoire du texte/police/game over
score = Texte("Score Joueur : " + str(int(score/100)),(0,0,0), int(fenetre.getTailleFenetreL()/25),(int(fenetre.getTailleFenetreL()/3),int(fenetre.getTailleFenetreH()/3))) 
score.afficherTexte(fenetre)
messageGO = Texte("Game Over",(0,0,0), int(fenetre.getTailleFenetreL()/25),(int(fenetre.getTailleFenetreL()/3),int(fenetre.getTailleFenetreH()/2)))
messageGO.afficherTexte(fenetre)
fenetre.actualiser()
#
repeat = True
while repeat :
    Event.obsevateurEvenement(fenetre)

fenetre.fermerFenetre()
