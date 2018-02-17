### - score.py - ###
"""
Date de la création du fichier : 30/07/2017
Date de la dernière édition du fichier : 16/08/2017
"""

### import ###
import pygame, random
from pygame.locals import *

from game import Temps

class Score :

    def __init__(self) :
        self.scoreTime = Temps()
        self.niveauActuel = 0

    def startTempsJeu(self) :
        self.scoreTime.startChrono()

    def stopTempsJeu(self) :
        self.scoreTime.stopChrono()

    def reprendreTempsJeu(self) :
        self.scoreTime.reprendreChrono()

    def score(self) :
        return int(self.scoreTime.tempsEcoule())

    def tempsScore(self) :
        return self.scoreTime.tempsEcoule()
