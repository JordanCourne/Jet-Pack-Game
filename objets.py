### - objets.py - ###
"""
Date de la création du fichier : 04/07/2017
Date de la dernière édition du fichier : 18/08/2017
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

    def __init__(self, asteroide, fenetre) :
        self.asteroide = asteroide
        hauteurChercher = int(fenetre.getTailleFenetreL() / 4.3333) # environ égal à 300 quand tailleFenetreLargeur = 1300
        self.vitesse = fenetre.getTailleFenetreL() / 3.6109 # environ égal à 360 quand tailleFenetreLargeur = 1300 et vitessePerso environ égal à 600

        self.hauteurAst = self.asteroide.get_height()
        self.largeurAst = self.asteroide.get_width()
        self.asteroide = pygame.transform.smoothscale(self.asteroide, (hauteurChercher, int(hauteurChercher * self.hauteurAst / self.largeurAst)))
        self.hauteurAst = self.asteroide.get_height()
        self.largeurAst = self.asteroide.get_width()

        Objets.__init__(self, fenetre, self.largeurAst, self.hauteurAst, self.vitesse, self.asteroide)

        self.afficherObj(fenetre)

class Acide(Objets) :

    def __init__(self, acide, fenetre, posX) :
        self.objet = acide
        hauteurAcide = int(fenetre.getTailleFenetreL() / 20) # environ égal à 65 quand tailleFenetreLargeur = 1300
        self.vitesse = fenetre.getTailleFenetreL() / 2.5 # environ égal à 360 quand tailleFenetreLargeur = 1300 et vitessePerso environ égal à 600

        self.hauteurAcide = self.objet.get_height()
        self.largeurAcide = self.objet.get_width()
        self.objet = pygame.transform.smoothscale(self.objet, (hauteurAcide, int(hauteurAcide * self.hauteurAcide / self.largeurAcide)))
        self.largeurObj = self.objet.get_width()
        self.hauteurObj = self.objet.get_height()

        if posX == None :
            self.posActX  = random.randint(-self.largeurObj, fenetre.getTailleFenetreL())
        else :
            self.posActX = random.randint(- 2*self.largeurObj, 2*self.largeurObj) + posX - (self.largeurObj/2)
        self.posActY = random.randint(- 4*self.hauteurObj, -self.hauteurObj)

        self.afficherObj(fenetre)

    def actualiserObj(self, fenetre, dt) :
        self.posActY += self.vitesse * dt
        #self.posActX = self.posActX
        self.afficherObj(fenetre)
