"""
Nom : Jet Pack Game
Présentation du jeu (à venir)
Par Jordan Courné
Version : 0.3 (Pré Alpha)
"""
### - main.py - ###
"""
Date de la création du fichier : 03/07/2017
Date de la dernière édition du fichier : 27/07/2017
"""

### import ###
from window import Window
from menu import Menu

### Main ###
tailleFenetreLargeur = 1300
fenetre = Window(tailleFenetreLargeur)

menu = Menu(fenetre)

repeat = True
while repeat :
    menu.afficherMenu(fenetre)
    fenetre.actualiser()
    menu.selection(fenetre)
