### - objets.py - ###
"""
Date de la création du fichier : 04/07/2017
Date de la dernière édition du fichier : 10/07/2017
"""

### import ###
import pygame, random
from pygame.locals import *

class Objets :

    def __init__(self, fenetre, largeurObj, hauteurObj, vitesse, objet) :
        self.vitesse = vitesse

        self.posDepX = random.randint(- 2*largeurObj, fenetre.getTailleFenetreL() + largeurObj)
        self.posDepY = - hauteurObj
        self.posArrX = random.randint(0, fenetre.getTailleFenetreL() - largeurObj)
        self.posArrY = fenetre.getTailleFenetreH()

        self.posActX = self.posDepX
        self.posActY = self.posDepY

    def setVitesse(vitesse) :
        self.vitesse = vitesse

class Asteroide(Objets) :

    def __init__(self, tailleFenetreLargeur, hauteurAsteroide, vitesse, fenetre) :
        self.asteroide = pygame.image.load("asteroide.png").convert_alpha()

        self.hauteurAst = self.asteroide.get_height()
        self.largeurAst = self.asteroide.get_width()
        self.asteroide = pygame.transform.scale(self.asteroide, (hauteurAsteroide, int(hauteurAsteroide * self.hauteurAst / self.largeurAst)))
        self.hauteurAst = self.asteroide.get_height()
        self.largeurAst = self.asteroide.get_width()

        Objets.__init__(self, fenetre, self.largeurAst, self.hauteurAst, vitesse, self.asteroide)

        self.afficherAst(fenetre)

    def hitbox(self) :
        self.hautGaucheX = self.posActX + (self.largeurAst / 15)
        self.hautGaucheY = self.posActY + (self.hauteurAst / 5)
        self.basDroitX = self.posActX + self.largeurAst - (self.largeurAst / 15)
        self.basDroitY = self.posActY + self.hauteurAst - (self.hauteurAst / 10)
        return (self.hautGaucheX, self.hautGaucheY, self.basDroitX, self.basDroitY)

    def horsCadre(self, fenetre) :
        if self.posActY > fenetre.getTailleFenetreH() :
            return True
        return False

    def afficherAst(self, fenetre) :
        fenetre.getWindow().blit(self.asteroide, (self.posActX, self.posActY))

    def actualiserAst(self, fenetre) :
        self.posActY += self.vitesse
        self.posActX = int(((self.posArrX - self.posDepX)*self.posActY + (self.posArrY - self.posDepY)*self.posDepX - (self.posArrX - self.posDepX)*self.posDepY) / (self.posArrY - self.posDepY))        
        self.afficherAst(fenetre)
