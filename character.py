### - character.py - ###
"""
Date de la création du fichier : 04/07/2017
Date de la dernière édition du fichier : 18/07/2017
"""

### import ###
import pygame
from pygame.locals import *

class Character :
    
    def __init__(self, tailleFenetreLargeur, hauteurPersonnage, vitessePerso, fenetre) :
        self.charac = pygame.image.load("perso 1.png").convert_alpha()

        self.posPersoX = int(tailleFenetreLargeur/5)
        self.posPersoY = int(tailleFenetreLargeur/5)
        self.vitesse = vitessePerso

        self.hauteurPerso = self.charac.get_height()
        self.largeurPerso = self.charac.get_width()
        self.charac = pygame.transform.scale(self.charac, (hauteurPersonnage, int(hauteurPersonnage * self.hauteurPerso / self.largeurPerso)))
        self.hauteurPerso = self.charac.get_height()
        self.largeurPerso = self.charac.get_width()

        self.afficherPerso(fenetre)

    def hitbox(self) :
        self.hautGaucheX = self.posPersoX + (self.largeurPerso / 15)
        self.hautGaucheY = self.posPersoY
        self.basDroitX = self.posPersoX + self.largeurPerso - (self.largeurPerso / 15)
        self.basDroitY = self.posPersoY + self.hauteurPerso
        return (self.hautGaucheX, self.hautGaucheY, self.basDroitX, self.basDroitY)

    def afficherHitbox(self, fenetre) :
        pygame.draw.line(fenetre.getWindow(), (0,255,0), (self.hitbox()[0], self.hitbox()[1]), (self.hitbox()[0], self.hitbox()[3]))
        pygame.draw.line(fenetre.getWindow(), (0,255,0), (self.hitbox()[2], self.hitbox()[1]), (self.hitbox()[2], self.hitbox()[3]))
        pygame.draw.line(fenetre.getWindow(), (0,255,0), (self.hitbox()[0], self.hitbox()[1]), (self.hitbox()[2], self.hitbox()[1]))
        pygame.draw.line(fenetre.getWindow(), (0,255,0), (self.hitbox()[0], self.hitbox()[3]), (self.hitbox()[2], self.hitbox()[3]))

    def afficherPerso(self, fenetre) :
        fenetre.getWindow().blit(self.charac, (self.posPersoX, self.posPersoY))

    def actualiserPerso(self, fenetre) :
        self.touchesPresse = pygame.key.get_pressed()
        if self.touchesPresse[K_UP] and self.dansCadre(fenetre, self.posPersoX, self.posPersoY - self.vitesse) :
            self.posPersoY -= self.vitesse
        if self.touchesPresse[K_DOWN] and self.dansCadre(fenetre, self.posPersoX, self.posPersoY + self.vitesse) :
            self.posPersoY += self.vitesse
        if self.touchesPresse[K_LEFT] and self.dansCadre(fenetre, self.posPersoX - self.vitesse, self.posPersoY) :
            self.posPersoX -= self.vitesse
        if self.touchesPresse[K_RIGHT] and self.dansCadre(fenetre, self.posPersoX + self.vitesse, self.posPersoY) :
            self.posPersoX += self.vitesse
        self.afficherPerso(fenetre)
        
    def dansCadre(self, fenetre, posFuturX, posFuturY) :
        if posFuturX >= 0 and posFuturX <= (fenetre.getTailleFenetreL() - self.largeurPerso) :
            if posFuturY >= 0 and posFuturY <= (fenetre.getTailleFenetreH() - self.hauteurPerso) :
                return True
        return False
