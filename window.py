### - window.py - ###
"""
Date de la création du fichier : 04/07/2017
Date de la dernière édition du fichier : 24/09/2017
"""

### import ###
import pygame
from pygame.locals import *

class Window :
    formatFenetreL = 16
    formatFenetreH = 9
    
    def __init__(self, tailleFenetreLargeur) :
        self.tailleFenetreL = tailleFenetreLargeur
        self.tailleFenetreH = int(self.tailleFenetreL * self.formatFenetreH / self.formatFenetreL)
            #Affichage Fenetre
        pygame.init()
        self.window = pygame.display.set_mode((self.tailleFenetreL, self.tailleFenetreH), pygame.HWSURFACE)
        pygame.display.set_caption("Jet Pack Game")
            #Fond
        self.fondBleute = (215,250,255)
        self.fondRouge = (255,215,250)
        self.fondVert = (250,255,215)
        self.fondTerre = pygame.image.load("Fond Terre.png").convert()
        self.fondTerre = pygame.transform.smoothscale(self.fondTerre, (self.tailleFenetreL, self.tailleFenetreH))
        self.fondVenus = pygame.image.load("Fond Venus.png").convert()
        self.fondVenus = pygame.transform.smoothscale(self.fondVenus, (self.tailleFenetreL, self.tailleFenetreH))
        self.window.blit(self.fondTerre, (0,0))

    def fermerFenetre(self) :
        pygame.quit()

    def afficherFond(self, niveau) :
        if niveau == 1 :
            self.window.blit(self.fondTerre, (0,0))
        elif niveau == 2 :
            self.window.blit(self.fondVenus, (0,0))
        elif niveau == 3 :
            pygame.draw.rect(self.window, self.fondRouge, (0,0, self.tailleFenetreL, self.tailleFenetreH))
        else :
            pygame.draw.rect(self.window, self.fondBleute, (0,0, self.tailleFenetreL, self.tailleFenetreH))

    def actualiser(self) :
        pygame.display.flip()

    def getWindow(self) :
        return self.window

    def getTailleFenetreH(self) :
        return self.tailleFenetreH

    def getTailleFenetreL(self) :
        return self.tailleFenetreL
