### - character.py - ###
"""
Date de la création du fichier : 04/07/2017
Date de la dernière édition du fichier : 20/08/2017
"""

### import ###
import pygame
from pygame.locals import *

from game import Event

class Character :
    
    def __init__(self, hauteurPersonnage, vitessePerso, fenetre) :
        self.charac = pygame.image.load("personnage.png").convert_alpha()

        self.hauteurPerso = self.charac.get_height()
        self.largeurPerso = self.charac.get_width()
        self.charac = pygame.transform.smoothscale(self.charac, (hauteurPersonnage, int(hauteurPersonnage * self.hauteurPerso / self.largeurPerso)))
        self.hauteurPerso = self.charac.get_height()
        self.largeurPerso = self.charac.get_width()

        self.posPersoX = int(fenetre.getTailleFenetreL()/2 - self.largeurPerso/2)
        self.posPersoY = int(fenetre.getTailleFenetreH() - self.hauteurPerso)
        self.vitesse = vitessePerso

        self.compteurFlamme = 0
        self.flammes = []
        self.flammes.append(pygame.image.load("flammes\\flammes000.png").convert_alpha())
        hauteurFlammes = self.flammes[0].get_height()
        largeurFlammes = self.flammes[0].get_width()
        hauteurTransformee = int(hauteurPersonnage * 2)
        largeurTransformee = int(hauteurTransformee * hauteurFlammes / largeurFlammes)
        self.flammes[0] = pygame.transform.smoothscale(self.flammes[0], (hauteurTransformee, largeurTransformee))
        for i in range(135) :
            Event.observateurQuit(fenetre)
            i += 1
            if i < 10 :
                self.flammes.append(pygame.image.load("flammes\\flammes00"+ str(i) +".png").convert_alpha())
            elif i < 100 :
                self.flammes.append(pygame.image.load("flammes\\flammes0"+ str(i) +".png").convert_alpha())
            else :
                self.flammes.append(pygame.image.load("flammes\\flammes"+ str(i) +".png").convert_alpha())
            self.flammes[i] = pygame.transform.smoothscale(self.flammes[i], (hauteurTransformee, largeurTransformee))

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

    def afficherFlammes(self, fenetre) :
        fenetre.getWindow().blit(self.flammes[self.compteurFlamme], (self.posPersoX - (self.largeurPerso/2),self.posPersoY + (self.hauteurPerso/2)))
        self.compteurFlamme += 1
        if self.compteurFlamme >= 136 :
            self.compteurFlamme = 0

    def actualiserPerso(self, fenetre, dt) :
        self.touchesPresse = pygame.key.get_pressed()
        if self.touchesPresse[K_UP] and self.dansCadre(fenetre, self.posPersoX, self.posPersoY - 1.75 * self.vitesse * dt) :
            self.posPersoY -= 1.75 * self.vitesse * dt
            self.afficherFlammes(fenetre)
        elif self.touchesPresse[K_UP] :
            self.posPersoY = 0
            self.afficherFlammes(fenetre)
            
        if self.touchesPresse[K_DOWN] and self.dansCadre(fenetre, self.posPersoX, self.posPersoY + 0.5 * self.vitesse * dt) :
            self.posPersoY += 0.5 * self.vitesse * dt
        elif self.touchesPresse[K_DOWN] :
            self.posPersoY = fenetre.getTailleFenetreH() - self.hauteurPerso
            
        if self.touchesPresse[K_LEFT] and self.dansCadre(fenetre, self.posPersoX - 0.75 * self.vitesse * dt, self.posPersoY) :
            self.posPersoX -= 0.75 * self.vitesse * dt
        elif self.touchesPresse[K_LEFT] :
            self.posPersoX = 0
        
        if self.touchesPresse[K_RIGHT] and self.dansCadre(fenetre, self.posPersoX + 0.75 * self.vitesse * dt, self.posPersoY) :
            self.posPersoX += 0.75 * self.vitesse * dt
        elif self.touchesPresse[K_RIGHT] :
            self.posPersoX = fenetre.getTailleFenetreL() - self.largeurPerso

        if self.dansCadre(fenetre, self.posPersoX, self.posPersoY + 0.5 * self.vitesse * dt) :
            self.posPersoY += 0.5 * self.vitesse * dt
        else :
            self.posPersoY = fenetre.getTailleFenetreH() - self.hauteurPerso
            
        self.afficherPerso(fenetre)
        
    def dansCadre(self, fenetre, posFuturX, posFuturY) :
        if posFuturX >= 0 and posFuturX <= (fenetre.getTailleFenetreL() - self.largeurPerso) :
            if posFuturY >= 0 and posFuturY <= (fenetre.getTailleFenetreH() - self.hauteurPerso) :
                return True
        return False
