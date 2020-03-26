from mcpi.minecraft import Minecraft
from mcpi import block
from random import randint
from time import sleep
import time
mc = Minecraft.create()

murX = 0
murY = 0
murZ = 0
dureePartie = 30
tempsDebutPartie = 0
tempsFinPartie = 0
nbPointsJoueur = 0
nbPointsPartie = 0


def afficherMessage(message) :
    mc.postToChat(message)

def initialiserMur() :
    x, y, z = mc.player.getPos()
    mc.setBlocks(x + 1, y, z , x + 1, y + 2 , z + 2, 1)
    global murX
    murX = x + 1
    global murY
    murY = y
    global murZ
    murZ = z

def renitialiserMur() :
    global murX
    global murY
    global murZ
    mc.setBlocks(murX, murY, murZ , murX, murY + 2 , murZ + 2, 1)

def placerBlockMur(x,y,blockId) :
    mc.setBlock(murX,murY + y,murZ + x, blockId)

def placerBlockAleatoireMur(blockId):
    global nbPointsPartie
    nbPointsPartie+=1
    x = randint(0,2)
    y = randint(0,2)
    placerBlockMur(x,y,blockId)

def verifierFinPartie():
    global tempsDebutPartie
    global tempsFinPartie
    global dureePartie
    tempsFinPartie = time.time()
    if tempsFinPartie - tempsDebutPartie > dureePartie :
        return True
    else :
        return False

def frapperEtVerifierTaupe():
    global nbPointsJoueur
    for bh in mc.events.pollBlockHits() :
        if mc.getBlock(bh.pos.x,bh.pos.y,bh.pos.z) == 2:
            mc.setBlock(bh.pos.x,bh.pos.y,bh.pos.z,1)
            nbPointsJoueur+=1

initialiserMur()
afficherMessage("Bienvenue sur whack a mole!")
afficherMessage("Debut de la partie dans")
afficherMessage("3")
sleep(1)
afficherMessage("2")
sleep(1)
afficherMessage("1")
sleep(1)
afficherMessage("GO!")
tempsDebutPartie = time.time()

while True:
    sleep(2.0)
    renitialiserMur()
    if verifierFinPartie() == True:
        break
    placerBlockAleatoireMur(2)
    frapperEtVerifierTaupe()

afficherMessage("Partie termine")
afficherMessage("Resultat: " + str(nbPointsJoueur) + "/" + str(nbPointsPartie))
   