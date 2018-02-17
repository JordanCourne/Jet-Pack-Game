### - game.py - ###
"""
Date de la création du fichier : 04/07/2017
Date de la dernière édition du fichier : 10/07/2017
"""

### import ###
import pygame
from pygame.locals import *

class Event :
    
    def __init__(self) :
        pass
    
    def obsevateurEvenement(self) :
        for event in pygame.event.get() :
            if event.type == QUIT :
                print("Fermeture de la fenêtre")
                return False
        return True

class Collision :

    def __init__(self) :
        pass

    def collision(self, obj1, obj2) :
        if obj1[0] >= obj2[0] and obj1[0] <= obj2[2] :
            if obj1[1] >= obj2[1] and obj1[1] <= obj2[3]:
                return True
            elif obj1[3] >= obj2[1] and obj1[3] <= obj2[3]:
                return True
        elif obj1[2] >= obj2[0] and obj1[2] <= obj2[2] :
            if obj1[1] >= obj2[1] and obj1[1] <= obj2[3]:
                return True
            elif obj1[3] >= obj2[1] and obj1[3] <= obj2[3]:
                return True
        else :       
            return False 
