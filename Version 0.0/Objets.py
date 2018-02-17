import pygame
from pygame.locals import *

posDepX = -100
posDepY = -100
posArrX = 1000
posArrY = 1000
hauteurAsteroide = 0
largeurAsteroide = 0
vitesse = 1

def initialisationAsteroide(asteroide) :
    hauteurAsteroide = asteroide.get_height()
    largeurAsteroide = asteroide.get_width()
    asteroide = pygame.transform.scale(asteroide, (300,int(300 * hauteurAsteroide / largeurAsteroide)))
    return asteroide

def getPosAsteroide() :
    return (posDepX, posDepY)

def actualiserPosAsteroide() :
    pass

def determinerVitesse() :
    pass
