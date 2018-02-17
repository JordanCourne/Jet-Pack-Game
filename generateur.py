### - generateur.py - ###
"""
Date de la création du fichier : 24/07/2017
Date de la dernière édition du fichier : 19/08/2017
"""

### import ###
import pygame, random
from pygame.locals import *

from objets import Asteroide, Acide
from game import Temps

class Generateur() :

    objetImage = None

    def __init__(self, typeObjet) :
        self.listObjet = []
        self.nombreObjetParSeconde = 0.3

        self.tempsNiveau = Temps()
        self.tempsNiveau.startChrono()

        self.tempsAttente = Temps()
        self.tempsAttente.setTempsRefence(10)

        self.changerTypeObjet(typeObjet)

    def changerTypeObjet(self, typeObjet) :
        self.typeObjet = typeObjet
        if self.typeObjet == "ASTEROIDE" :
            self.objetImage = pygame.image.load("asteroide.png").convert_alpha()
        elif self.typeObjet == "ACIDE" :
            self.objetImage = pygame.image.load("Pluie acide.png").convert_alpha()
        self.tempsNiveau.startChrono()
        self.nombreObjetParSeconde = 0.3

    def creerObjet(self, fenetre, posX = None) :
        if self.typeObjet == "ASTEROIDE" :
            self.listObjet.append(Asteroide(self.objetImage, fenetre))
        elif self.typeObjet == "ACIDE" :
            self.listObjet.append(Acide(self.objetImage, fenetre, posX))

    def regulerObjet(self, fenetre) :
        for i in range(len(self.listObjet)) :
            if self.listObjet[i].horsCadre(fenetre) :
                del self.listObjet[i]
                self.regulerObjet(fenetre)
                break

    def actualiserObjet(self, fenetre, dt) :
        for objets in self.listObjet:
            objets.actualiserObj(fenetre, dt)

    def afficherHitboxObjet(self, fenetre) :
        for objets in self.listObjet :
            objets.afficherHitbox(fenetre)

    def getListObjet(self) :
        return self.listObjet

    def genererObjet(self, fenetre) :
        if self.typeObjet == "ASTEROIDE" :
            self.genererAsteroide(fenetre)
        elif self.typeObjet == "ACIDE" :
            self.genererAcide(fenetre)

    def genererAsteroide(self, fenetre) :
        self.nombreObjetParSeconde = 0.03 * int(self.tempsNiveau.tempsEcoule() /10) * 10  + 0.25
        if self.nombreObjetParSeconde != 0 :
            if self.tempsAttente.tempsEcoule() >= (1/self.nombreObjetParSeconde) :
                self.tempsAttente.startChrono()
                self.creerObjet(fenetre)

    def genererAcide(self, fenetre) :
        self.nombreObjetParSeconde = 0.06 * int(self.tempsNiveau.tempsEcoule() /10) * 10  + 0.4
        if self.nombreObjetParSeconde != 0 :
            if self.tempsAttente.tempsEcoule() >= (1/self.nombreObjetParSeconde) :
                self.tempsAttente.startChrono()
                posX = random.randint(0, fenetre.getTailleFenetreL())
                nbPluie = random.randint(1, 3)
                for i in range(nbPluie) :
                    self.creerObjet(fenetre, posX)

    def stopGeneration(self) :
        self.tempsNiveau.stopChrono()
        self.tempsAttente.stopChrono()

    def reprendreGeneration(self) :
        self.tempsNiveau.reprendreChrono()
        self.tempsAttente.reprendreChrono()
            
        
