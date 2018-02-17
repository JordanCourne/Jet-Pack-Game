### - menu.py - ###
"""
Date de la création du fichier : 14/07/2017
Date de la dernière édition du fichier : 19/07/2017
"""

### import ###
import pygame
from pygame.locals import *
from game import Texte, Collision, Event

class Menu() :

    def __init__(self, tailleFenetreLargeur, fenetre) :
        self.fondMenu = pygame.image.load("Fond ADN eclairage.png").convert()

        self.hauteurFond = self.fondMenu.get_height()
        self.largeurFond = self.fondMenu.get_width()
        self.fondMenu = pygame.transform.scale(self.fondMenu, (tailleFenetreLargeur, int(tailleFenetreLargeur * self.hauteurFond / self.largeurFond)))

        self.start = Texte("Jouer", (255,255,255), int(fenetre.getTailleFenetreL()/25), (int(fenetre.getTailleFenetreL()/9),int(fenetre.getTailleFenetreH()/3)))
        self.options = Texte("Options",(255,255,255), int(fenetre.getTailleFenetreL()/25), (int(fenetre.getTailleFenetreL()/9),int(fenetre.getTailleFenetreH()/1.9)))
        self.exit = Texte("Quitter",(255,255,255), int(fenetre.getTailleFenetreL()/25), (int(fenetre.getTailleFenetreL()/9),int(fenetre.getTailleFenetreH()/1.4)))
        
        
    def afficherMenu(self, fenetre) :
        fenetre.getWindow().blit(self.fondMenu, (0,0))
        self.start.afficherTexte(fenetre)
        self.options.afficherTexte(fenetre)
        self.exit.afficherTexte(fenetre)
        """
        self.start.afficherHitbox(fenetre)
        self.options.afficherHitbox(fenetre)
        self.exit.afficherHitbox(fenetre)"""

    def selection(self, fenetre) :
        choix = 0
        click = True
        hiboxSouris = None
        while click :
            hiboxSouris = Event.obsevateurEvenement(fenetre)
            #hiboxSouris = Event.hiboxSourisClick()
            if hiboxSouris[0] == True :
                if Collision.collision((hiboxSouris[1],hiboxSouris[2],hiboxSouris[3],hiboxSouris[4]), self.start.hitbox()) :
                    click = False
                    choix = 1
                elif Collision.collision((hiboxSouris[1],hiboxSouris[2],hiboxSouris[3],hiboxSouris[4]), self.options.hitbox()) :
                    click = False
                    choix = 2
                elif Collision.collision((hiboxSouris[1],hiboxSouris[2],hiboxSouris[3],hiboxSouris[4]), self.exit.hitbox()) :
                    click = False
                    choix = 3
            #hiboxSouris = Event.hiboxSourisMouvement()
            if hiboxSouris[0] == False :
                if Collision.collision((hiboxSouris[1],hiboxSouris[2],hiboxSouris[3],hiboxSouris[4]), self.start.hitbox()) :
                    self.start = Texte("Jouer", (170,255,255), int(fenetre.getTailleFenetreL()/25), (int(fenetre.getTailleFenetreL()/9),int(fenetre.getTailleFenetreH()/3)))
                elif Collision.collision((hiboxSouris[1],hiboxSouris[2],hiboxSouris[3],hiboxSouris[4]), self.options.hitbox()) :
                    self.options = Texte("Options",(170,255,255), int(fenetre.getTailleFenetreL()/25), (int(fenetre.getTailleFenetreL()/9),int(fenetre.getTailleFenetreH()/1.9)))
                elif Collision.collision((hiboxSouris[1],hiboxSouris[2],hiboxSouris[3],hiboxSouris[4]), self.exit.hitbox()) :
                    self.exit = Texte("Quitter",(170,255,255), int(fenetre.getTailleFenetreL()/25), (int(fenetre.getTailleFenetreL()/9),int(fenetre.getTailleFenetreH()/1.4)))
                else :
                    self.start = Texte("Jouer", (255,255,255), int(fenetre.getTailleFenetreL()/25), (int(fenetre.getTailleFenetreL()/9),int(fenetre.getTailleFenetreH()/3)))
                    self.options = Texte("Options",(255,255,255), int(fenetre.getTailleFenetreL()/25), (int(fenetre.getTailleFenetreL()/9),int(fenetre.getTailleFenetreH()/1.9)))
                    self.exit = Texte("Quitter",(255,255,255), int(fenetre.getTailleFenetreL()/25), (int(fenetre.getTailleFenetreL()/9),int(fenetre.getTailleFenetreH()/1.4)))
                self.afficherMenu(fenetre)
                fenetre.actualiser()
                    
        return choix

    def afficherJeu(self, fenetre) :
        pass

    def jeu(self, fenetre) :
        pass

    def afficherOptions(self, fenetre) :
        pass

    def options(self) :
        pass
