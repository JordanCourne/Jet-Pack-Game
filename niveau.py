### - niveau.py - ###
"""
Date de la création du fichier : 27/07/2017
Date de la dernière édition du fichier : 24/09/2017
"""

### import ###
import pygame
from pygame.locals import *

from character import Character
from game import Event, Collision, Texte, Temps
from generateur import Generateur
from score import Score

class Niveau() :

    def __init__(self, fenetre) :
        Texte("Chargement...", (255,240,220),int(fenetre.getTailleFenetreL()/13),(int(fenetre.getTailleFenetreL()/2.5), int(fenetre.getTailleFenetreH()/2.5))).afficherTexte(fenetre)
        fenetre.actualiser()
        
        self.hauteurPersonnage = int(fenetre.getTailleFenetreL() / 20) # égal à 65 quand tailleFenetreLargeur = 1300
        self.vitessePerso = fenetre.getTailleFenetreL() / 2.1666 # environ égal à 600 quand tailleFenetreLargeur = 1300

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.niveau = 0

        self.character = Character(self.hauteurPersonnage, self.vitessePerso, fenetre)
        self.generateur = Generateur("ASTEROIDE")
        self.score = Score()

    def lancerJeu(self, fenetre) :
        self.score.startTempsJeu()
        self.transition(fenetre)
        self.finJeu(fenetre)

    def transition(self, fenetre) :
        self.niveau += 1
        tempsTransition = Temps()
        tempsTransition.startChrono()
        while tempsTransition.tempsEcoule() < 3  :
            Event.observateurQuit(fenetre)
            self.dt = self.clock.tick(self.fps) / 1000
            texteTransition = None
            if self.niveau == 1 :
                fenetre.afficherFond(1)
                texteTransition = Texte("Terre",(100,100,255),int(fenetre.getTailleFenetreL()/(7-pow(tempsTransition.tempsEcoule(),1.7))),[int(fenetre.getTailleFenetreL()/2),int(fenetre.getTailleFenetreH()/2)])
            elif self.niveau == 2 :
                fenetre.afficherFond(2)
                texteTransition = Texte("Vénus",(255,255,100),int(fenetre.getTailleFenetreL()/(7-pow(tempsTransition.tempsEcoule(),1.7))),[int(fenetre.getTailleFenetreL()/2),int(fenetre.getTailleFenetreH()/2)])
            self.character.actualiserPerso(fenetre, self.dt)
            self.generateur.regulerObjet(fenetre)
            self.generateur.actualiserObjet(fenetre, self.dt)
            if texteTransition != None :
                texteTransition.centrerProsition()
                texteTransition.afficherTexte(fenetre)
            fenetre.actualiser()

        if self.niveau == 1 :
            self.niveau1(fenetre)
        elif self.niveau == 2 :
            self.niveau2(fenetre)
            

    def niveau1(self, fenetre) :
        self.clock.tick(self.fps)
        repeat = True
        while repeat == True :
            self.dt = self.clock.tick(self.fps) / 1000

            fenetre.afficherFond(1)
            self.character.actualiserPerso(fenetre, self.dt)
            
            if self.score.score() < 73 :
                self.generateur.genererObjet(fenetre)
            self.generateur.regulerObjet(fenetre)
            self.generateur.actualiserObjet(fenetre, self.dt)
    
            #Affichage Hitbox
            #self.generateur.afficherHitboxObjet(fenetre)
            #self.character.afficherHitbox(fenetre)

            ### pour les collisions, il faut que je modifie la fonction collision pour gerer la collision x sur y et y sur x (en gros supprimer if/elif ci dessous)
            # + Voir pour transferer la gestion des collisions dans le generateur : je pense que c'est mieux et plus simple
            for objets in self.generateur.getListObjet() :
                if Collision.collision(self.character.hitbox(), objets.hitbox()) :
                    repeat = False
                    pass
                elif Collision.collision(objets.hitbox(), self.character.hitbox()) :
                    repeat = False
                    pass
            #
            
            fenetre.actualiser()

            #A etudier pour modification (mettre ca dans une classe)
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

            if self.score.score() >= 77 :
                self.transition(fenetre)
                repeat = False
                
    def niveau2(self, fenetre) :
        self.generateur.changerTypeObjet("ACIDE")
        repeat = True
        while repeat == True :
            self.dt = self.clock.tick(self.fps) / 1000

            fenetre.afficherFond(2)
            self.character.actualiserPerso(fenetre, self.dt)
            
            if self.score.score() < 146 :
                self.generateur.genererObjet(fenetre)
            self.generateur.regulerObjet(fenetre)
            self.generateur.actualiserObjet(fenetre, self.dt)
    
            #Affichage Hitbox
            #self.generateur.afficherHitboxObjet(fenetre)
            #self.character.afficherHitbox(fenetre)

            ### pour les collisions, il faut que je modifie la fonction collision pour gerer la collision x sur y et y sur x (en gros supprimer if/elif ci dessous)
            # + Voir pour transferer la gestion des collisions dans le generateur : je pense que c'est mieux et plus simple
            for objets in self.generateur.getListObjet() :
                if Collision.collision(self.character.hitbox(), objets.hitbox()) :
                    repeat = False
                    pass
                elif Collision.collision(objets.hitbox(), self.character.hitbox()) :
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

            if self.score.score() >= 150 :
                self.transition(fenetre)
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
