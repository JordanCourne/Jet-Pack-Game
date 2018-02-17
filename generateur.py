### - generateur.py - ###
"""
Date de la création du fichier : 24/07/2017
Date de la dernière édition du fichier : 27/07/2017
"""

### import ###
import pygame, random
from pygame.locals import *

from objets import Asteroide
from game import Temps

class Generateur() :

    def __init__(self, hauteurAsteroide, vitesseObjet) :
        self.asteroideImage = pygame.image.load("asteroide.png").convert_alpha()
        self.listAsteroide = []

        self.hauteurObjet = hauteurAsteroide
        self.vitesseObjet = vitesseObjet

        self.tempsNiveau = Temps()
        self.tempsNiveau.startChrono()

        self.tempsAttente = Temps()
        self.tempsAttente.setTempsRefence(10)

        self.nombreAsteroideParSeconde = 0.3

    def creerAsteroide(self, fenetre) :
        self.listAsteroide.append(Asteroide(self.asteroideImage, fenetre, self.hauteurObjet, self.vitesseObjet))
        
    def regulerAsteroide(self, fenetre) :
        listeElementASupprime = []
        for i in range(len(self.listAsteroide)) :
            if self.listAsteroide[i].horsCadre(fenetre) :
                listeElementASupprime.append(i)

        for i in listeElementASupprime :
            del self.listAsteroide[i]

    def actualiserAsteroide(self, fenetre, dt) :
        for asteroide in self.listAsteroide :
            asteroide.actualiserObj(fenetre, dt)

    def afficherHitboxAsteroide(self, fenetre) :
        for asteroide in self.listAsteroide :
            asteroide.afficherHitbox(fenetre)

    def getListAsteroide(self) :
        return self.listAsteroide

    def genererAsteroide(self, fenetre) :
        self.nombreAsteroideParSeconde = 0.03 * int(self.tempsNiveau.tempsEcoule() /10) * 10  + 0.25
        if self.nombreAsteroideParSeconde != 0 :
            if self.tempsAttente.tempsEcoule() >= (1/self.nombreAsteroideParSeconde) :
                self.tempsAttente.startChrono()
                self.creerAsteroide(fenetre)

    def stopGeneration(self) :
        self.tempsNiveau.stopChrono()
        self.tempsAttente.stopChrono()

    def reprendreGeneration(self) :
        self.tempsNiveau.reprendreChrono()
        self.tempsAttente.reprendreChrono()
            
        
