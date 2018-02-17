### - setup.py - ###
"""
Date de la création du fichier : 11/07/2017
Date de la dernière édition du fichier : 11/07/2017
"""

### import ###
from cx_Freeze import setup, Executable

setup(
    name = "Jet Pack Game",
    version = "0.1",
    description = "Eviter les asteroides",
    executables = [Executable("main.py")],
)
