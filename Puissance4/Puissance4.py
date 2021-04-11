import numpy as np

values = {0:'Vide', 1:'Bleu', 2: 'Rouge'}
theBoard = np.zeros((6,12),dtype=int)
compteur = 42

def printBoard():
    affichage = "  ─   ─   ─   ─   ─   ─   ─   ─   ─   ─   ─   ─\n"
    for i in range(0, 6):
        affichage += "| "
        for j in range(0, 12):
            affichage += f"{theBoard[i][j]} | "
        affichage += "\n"
    affichage += "  ─   ─   ─   ─   ─   ─   ─   ─   ─  ─  ─  ─  ─\n"
    print(affichage)

def canPlay(colonne):
    return theBoard[0][colonne] == 0

def getLastFreeCase(colonne):
    for i in range(5,-1,-1):
        if theBoard[i][colonne] == 0:
            return i
    return -1

def play(colonne, joueur):
    if canPlay(colonne):
        ligne = getLastFreeCase(colonne)
        theBoard[ligne][colonne] = joueur
        return True
    else:
        return False

def checkWinningConditions(ligne, colonne):
    if compteur == 0:
        return "Tie"

def gameLoop():
    joueur = 1
    gameNotFinished = False
    while not gameNotFinished:
        print(f"Joueur: {joueur}")
        printBoard()
        isPositionNotOkay = True
        while isPositionNotOkay:
            userInput = input("Veuillez selectionner une colonne entre 1 et 12 pour valider votre tour")
            move = int(userInput) -1
            if play(move, joueur):
                isPositionNotOkay = False
                
