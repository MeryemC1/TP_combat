import random
import time
from classe_TP import *
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
 
if guerier.pv ==0 or sorciere.pv ==0 :

    coefficient=random.randint(0.1,1)
    def DegatInfligésGuerier (PointAttaqueGuerier*coefficient)
    def DegatInfligésSorciere (PointAttaqueSorciere*coefficient)
    time.sleep(1)


class Game :
    def __init__(personnage, guerier, sorciere ):
        personnage.guerier = guerier
        personnage.sorciere = sorciere
        
    
    def print(personnage)
            "guerier =", personnage.PointAttaqueGuerier, "\n" \
            "sorciere =", personnage.PointAttaqueSorciere"\n" \


def __init__ (game) : 
    return personnage.hp
def setHP(personnage = newHp)
     personnage.hp = newHp

def attack(personnage, target):
    print ("Le personnage attaque !")
    target.setHp(target.getHp()self.pa)
    print("La cible a maintenant" target.getHP(),"HP")

game = Game()
game.launch()

while (pa!= 0) and (pc!=O):
    pa= pa+1
    pv = pv+1
    else:
        print(guerier,sorciere)
        print("Gagné !")
