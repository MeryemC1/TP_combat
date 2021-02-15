import random
import time

class personnage :
    pa = 10
    pv = 100


class guerier(personnage):
    "Début du tour de jeu du guerier !" 
    pv = personnage.pv + 20
    pa=personnage.pa + 10

class sorciere(personnage):
    "Début du tour de jeu de la sorciere"
    def boirePotion() : 
        personnage.pv+15

class Game :
    def __init__(personnage, guerier, sorciere ):
        personnage.guerier = guerier
        personnage.sorciere = sorciere
        
    
    def print(personnage)
            "guerier =", personnage.PointAttaqueGuerier, "\n" \
            "sorciere =", personnage.PointAttaqueSorciere"\n" \