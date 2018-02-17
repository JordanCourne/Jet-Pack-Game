### - game.py - ###
"""
Date de la création du fichier : 04/07/2017
Date de la dernière édition du fichier : 18/08/2017
"""

### import ###
import pygame
from pygame.locals import *
import time

class Event :
    
    def __init__(self) :
        pass

    def observateurQuit(fenetre) :
        for event in pygame.event.get() :
            if event.type == QUIT :
                print("Fermeture de la fenêtre")
                fenetre.fermerFenetre()
                quit()
                
    def obsevateurEvenement(fenetre) :
        for event in pygame.event.get() :
            if event.type == QUIT :
                print("Fermeture de la fenêtre")
                fenetre.fermerFenetre()
                quit()
            if event.type == MOUSEBUTTONUP and event.button == 1 :
                return (True, event.pos[0], event.pos[1], event.pos[0], event.pos[1])
            if event.type == MOUSEMOTION :
                return (False, event.pos[0], event.pos[1], event.pos[0], event.pos[1])
        return (None, None, None, None, None)

    def evenementPause(fenetre) :
        for event in pygame.event.get() :
            if event.type == QUIT :
                print("Fermeture de la fenêtre")
                fenetre.fermerFenetre()
                quit()
            if event.type == KEYDOWN and event.key == K_p :
                return True
            if event.type == ACTIVEEVENT and event.gain == 0 and event.state == 6 :
                return True
            if event.type == ACTIVEEVENT and event.gain == 0 and event.state == 2 :
                return True
        return False

    def evenementUnPause(fenetre) :
        for event in pygame.event.get() :
            if event.type == QUIT :
                print("Fermeture de la fenêtre")
                fenetre.fermerFenetre()
                quit()
            if event.type == KEYDOWN and event.key == K_p :
                return True
            if event.type == ACTIVEEVENT and event.gain == 1 and event.state == 6 :
                return True
            if event.type == ACTIVEEVENT and event.gain == 1 and event.state == 2 :
                return True
        return False
            

class Collision :

    def __init__(self) :
        pass

    def collision(obj1, obj2) :
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

class Temps : 

    def __init__(self) :
        self.tempsReference = 0
        self.tempsStoppe = int(time.time() * 10000)/10000

    def startChrono(self) :
        self.tempsReference = int(time.time() * 10000)/10000
        self.tempsStoppe = int(time.time() * 10000)/10000

    def stopChrono(self) :
        self.tempsStoppe = int(time.time() * 10000)/10000

    def reprendreChrono(self) :
        self.tempsReference += int(time.time() * 10000)/10000 - self.tempsStoppe

    def tempsEcoule(self) :
        tempsNouveau = int(time.time() * 10000)/10000
        return int((tempsNouveau - self.tempsReference)*10000)/10000

    def setTempsRefence(self, temps) :
        self.tempsReference = int(time.time() * 10000)/10000 - temps
        self.tempsStoppe = int(time.time() * 10000)/10000

class Texte : 

    def __init__(self, texteAAfficher, couleur, taillePolice, position) :
        self.texte = pygame.font.Font("ArchitectsDaughter.ttf", taillePolice)
        self.texteRendu = self.texte.render(texteAAfficher, True, couleur)
        self.position = position
        # posX et posY correspondent au milieu de l'image !

    def afficherTexte(self, fenetre) :
        fenetre.getWindow().blit(self.texteRendu, self.position)

    def centrerProsition(self) :
        self.position[0] -= (self.hitbox()[2] - self.hitbox()[0]) / 2
        self.position[1] -= (self.hitbox()[3] - self.hitbox()[1]) / 2

    def hitbox(self) :
        self.hautGaucheX = self.position[0]
        self.hautGaucheY = self.position[1]
        self.basDroitX = self.position[0] + self.texteRendu.get_rect()[2]
        self.basDroitY = self.position[1] + self.texteRendu.get_rect()[3]
        return (self.hautGaucheX, self.hautGaucheY, self.basDroitX, self.basDroitY)

    def afficherHitbox(self, fenetre) :
        pygame.draw.line(fenetre.getWindow(), (0,0,255), (self.hitbox()[0], self.hitbox()[1]), (self.hitbox()[0], self.hitbox()[3]))
        pygame.draw.line(fenetre.getWindow(), (0,0,255), (self.hitbox()[2], self.hitbox()[1]), (self.hitbox()[2], self.hitbox()[3]))
        pygame.draw.line(fenetre.getWindow(), (0,0,255), (self.hitbox()[0], self.hitbox()[1]), (self.hitbox()[2], self.hitbox()[1]))
        pygame.draw.line(fenetre.getWindow(), (0,0,255), (self.hitbox()[0], self.hitbox()[3]), (self.hitbox()[2], self.hitbox()[3]))
