### - niveau.py - ###
"""
Date de la création du fichier : 27/07/2017
Date de la dernière édition du fichier : 16/08/2017
"""

### import ###
import pygame
from pygame.locals import *

from character import Character
from game import Event, Collision, Texte
from generateur import Generateur
from score import Score

class Niveau() :

    def __init__(self, fenetre) :
        self.hauteurPersonnage = int(fenetre.getTailleFenetreL() / 32.5) # égal à 40 quand tailleFenetreLargeur = 1300
        self.hauteurAsteroide = int(fenetre.getTailleFenetreL() / 4.3333) # environ égal à 300 quand tailleFenetreLargeur = 1300  
        self.vitessePerso = fenetre.getTailleFenetreL() / 2.1666 # environ égal à 600 quand tailleFenetreLargeur = 1300
        self.vitesseObjet = self.vitessePerso / 1.6666 # environ égal à 360 quand tailleFenetreLargeur = 1300 et vitessePerso environ égal à 600

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.character = Character(self.hauteurPersonnage, self.vitessePerso, fenetre)
        self.generateur = Generateur(self.hauteurAsteroide, self.vitesseObjet)
        self.score = Score()

    def lancerJeu(self, fenetre) :
        self.score.startTempsJeu()
        self.niveau1(fenetre)
        self.finJeu(fenetre)

    def niveau1(self, fenetre) :
        self.clock.tick(self.fps)
        repeat = True
        while repeat == True :
            self.dt = self.clock.tick(self.fps) / 1000

            fenetre.afficherFond(1)
            self.character.actualiserPerso(fenetre, self.dt)
            
            self.generateur.genererAsteroide(fenetre)
            self.generateur.regulerAsteroide(fenetre)
            self.generateur.actualiserAsteroide(fenetre, self.dt)
    
            #Affichage Hitbox
            #self.generateur.afficherHitboxAsteroide(fenetre)
            #self.character.afficherHitbox(fenetre)

            ### pour les collisions, il faut que je modifie la fonction collision pour gerer la collision x sur y et y sur x (en gros supprimer if/elif ci dessous)
            # + Voir pour transferer la gestion des collisions dans le generateur : je pense que c'est mieux et plus simple
            for asteroide in self.generateur.getListAsteroide() :
                if Collision.collision(self.character.hitbox(), asteroide.hitbox()) :
                    repeat = False
                    pass
                elif Collision.collision(asteroide.hitbox(), self.character.hitbox()) :
                    repeat = False
                    pass
            #
            
            fenetre.actualiser()

            #A etudier pour modification (mettre ca dans une classe
            if Event.evenementPause(fenetre) :
                self.score.stopTempsJeu()
                self.generateur.stopGeneration()
                pause = Texte("Pause",(100,200,200), int(fenetre.getTailleFenetreL()/7),(int(fenetre.getTailleFenetreL()/3.2),int(fenetre.getTailleFenetreH()/3.2))) 
                pause.afficherTexte(fenetre)
                fenetre.actualiser()
                while not Event.evenementUnPause(fenetre) :
                    pass
                self.score.reprendreTempsJeu()
                self.generateur.reprendreGeneration()
                self.dt = self.clock.tick(self.fps) / 1000
            #

            if self.score.score() >= 20 :
                self.niveau2(fenetre)
                repeat = False
                
    def niveau2(self, fenetre) :
        repeat = True
        while repeat == True :
            self.dt = self.clock.tick(self.fps) / 1000

            fenetre.afficherFond(2)
            self.character.actualiserPerso(fenetre, self.dt)
            
            self.generateur.genererAsteroide(fenetre)
            self.generateur.regulerAsteroide(fenetre)
            self.generateur.actualiserAsteroide(fenetre, self.dt)
    
            #Affichage Hitbox
            #self.generateur.afficherHitboxAsteroide(fenetre)
            #self.character.afficherHitbox(fenetre)

            ### pour les collisions, il faut que je modifie la fonction collision pour gerer la collision x sur y et y sur x (en gros supprimer if/elif ci dessous)
            # + Voir pour transferer la gestion des collisions dans le generateur : je pense que c'est mieux et plus simple
            for asteroide in self.generateur.getListAsteroide() :
                if Collision.collision(self.character.hitbox(), asteroide.hitbox()) :
                    repeat = False
                    pass
                elif Collision.collision(asteroide.hitbox(), self.character.hitbox()) :
                    repeat = False
                    pass
            #
            
            fenetre.actualiser()

            #A etudier pour modification (mettre ca dans une classe
            if Event.evenementPause(fenetre) :
                self.score.stopTempsJeu()
                self.generateur.stopGeneration()
                pause = Texte("Pause",(100,200,200), int(fenetre.getTailleFenetreL()/7),(int(fenetre.getTailleFenetreL()/3.2),int(fenetre.getTailleFenetreH()/3.2))) 
                pause.afficherTexte(fenetre)
                fenetre.actualiser()
                while not Event.evenementUnPause(fenetre) :
                    pass
                self.score.reprendreTempsJeu()
                self.generateur.reprendreGeneration()
                self.dt = self.clock.tick(self.fps) / 1000
            #

            if self.score.score() >= 140 :
                self.niveau2(fenetre)
                repeat = False

    def finJeu(self, fenetre) :
        scoreT = Texte("Score Joueur : " + str(int(self.score.score())),(255,100,100), int(fenetre.getTailleFenetreL()/25),(int(fenetre.getTailleFenetreL()/3),int(fenetre.getTailleFenetreH()/3))) 
        scoreT.afficherTexte(fenetre)
        messageGO = Texte("Game Over",(100,100,255), int(fenetre.getTailleFenetreL()/25),(int(fenetre.getTailleFenetreL()/3),int(fenetre.getTailleFenetreH()/2)))
        messageGO.afficherTexte(fenetre)
        retour = Texte("Retour", (100,255,100), int(fenetre.getTailleFenetreL()/30), (int(fenetre.getTailleFenetreL()/1.15), int(fenetre.getTailleFenetreH()/1.1)))
        retour.afficherTexte(fenetre)
        fenetre.actualiser()

        repeat = True
        while repeat :
            hiboxSouris = Event.obsevateurEvenement(fenetre)
            if hiboxSouris[0] == True :
                if Collision.collision((hiboxSouris[1],hiboxSouris[2],hiboxSouris[3],hiboxSouris[4]), retour.hitbox()) :
                    repeat = False
                    
            if hiboxSouris[0] == False :
                if Collision.collision((hiboxSouris[1],hiboxSouris[2],hiboxSouris[3],hiboxSouris[4]), retour.hitbox()) :
                    retour = Texte("Retour", (50,200,50), int(fenetre.getTailleFenetreL()/30), (int(fenetre.getTailleFenetreL()/1.15), int(fenetre.getTailleFenetreH()/1.1)))
                else :
                    retour = Texte("Retour", (100,255,100), int(fenetre.getTailleFenetreL()/30), (int(fenetre.getTailleFenetreL()/1.15), int(fenetre.getTailleFenetreH()/1.1)))
                retour.afficherTexte(fenetre)
                fenetre.actualiser()
