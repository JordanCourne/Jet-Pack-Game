### - objets.py - ###
"""
Date de la création du fichier : 04/07/2017
Date de la dernière édition du fichier : 26/07/2017
"""

### import ###
import pygame, random
from pygame.locals import *

class Objets :

    def __init__(self, fenetre, largeurObj, hauteurObj, vitesse, objet) :
        self.largeurObj = largeurObj
        self.hauteurObj = hauteurObj
        self.vitesse = vitesse
        self.objet = objet

        self.posDepX = random.randint(- 2*self.largeurObj, fenetre.getTailleFenetreL() + self.largeurObj)
        self.posDepY = - self.hauteurObj
        self.posArrX = random.randint(0, fenetre.getTailleFenetreL() - self.largeurObj)
        self.posArrY = fenetre.getTailleFenetreH()

        self.posActX = self.posDepX
        self.posActY = self.posDepY

    def setVitesse(self, vitesse) :
        self.vitesse = vitesse

    def hitbox(self) :
        self.hautGaucheX = self.posActX + (self.largeurObj / 15)
        self.hautGaucheY = self.posActY + (self.hauteurObj / 5)
        self.basDroitX = self.posActX + self.largeurObj  - (self.largeurObj / 15)
        self.basDroitY = self.posActY + self.hauteurObj  - (self.hauteurObj / 10)
        return (self.hautGaucheX, self.hautGaucheY, self.basDroitX, self.basDroitY)

    def afficherHitbox(self, fenetre) :
        pygame.draw.line(fenetre.getWindow(), (255,0,0), (self.hitbox()[0], self.hitbox()[1]), (self.hitbox()[0], self.hitbox()[3]))
        pygame.draw.line(fenetre.getWindow(), (255,0,0), (self.hitbox()[2], self.hitbox()[1]), (self.hitbox()[2], self.hitbox()[3]))
        pygame.draw.line(fenetre.getWindow(), (255,0,0), (self.hitbox()[0], self.hitbox()[1]), (self.hitbox()[2], self.hitbox()[1]))
        pygame.draw.line(fenetre.getWindow(), (255,0,0), (self.hitbox()[0], self.hitbox()[3]), (self.hitbox()[2], self.hitbox()[3]))

    def horsCadre(self, fenetre) :
        if self.posActY > fenetre.getTailleFenetreH() :
            return True
        return False

    def afficherObj(self, fenetre) :
        fenetre.getWindow().blit(self.objet, (self.posActX, self.posActY))

    def actualiserObj(self, fenetre, dt) :
        self.posActY += self.vitesse * dt
        self.posActX = int(((self.posArrX - self.posDepX)*self.posActY + (self.posArrY - self.posDepY)*self.posDepX - (self.posArrX - self.posDepX)*self.posDepY) / (self.posArrY - self.posDepY))        
        self.afficherObj(fenetre)

class Asteroide(Objets) :

    def __init__(self, asteroide, fenetre, hauteurAsteroide, vitesse) :
        self.asteroide = asteroide

        self.hauteurAst = self.asteroide.get_height()
        self.largeurAst = self.asteroide.get_width()
        self.asteroide = pygame.transform.smoothscale(self.asteroide, (hauteurAsteroide, int(hauteurAsteroide * self.hauteurAst / self.largeurAst)))
        self.hauteurAst = self.asteroide.get_height()
        self.largeurAst = self.asteroide.get_width()

        Objets.__init__(self, fenetre, self.largeurAst, self.hauteurAst, vitesse, self.asteroide)

        self.afficherObj(fenetre)
