import numpy as np

values = {0:'Vide', 1:'Bleu', 2: 'Rouge'}
theBoard = np.zeros((6,12),dtype=int)

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

def checkWinningConditions(ligne, colonne, compteur):
    if compteur == 42:
        print("---TIE---")
        return True
    else:
        return False

def gameLoop():
    compteur = 1
    joueur = 1
    gameNotFinished = False
    while not gameNotFinished:
        isPositionNotOkay = True
        print(f"Tour: {compteur} Joueur: {joueur}")
        printBoard()
        while isPositionNotOkay:
            userInput = input("Veuillez selectionner une colonne entre 1 et 12 pour valider votre tour:\n")
            colonne = int(userInput) - 1
            if colonne in np.arange(0,12):
                if canPlay(colonne):
                    ligne = getLastFreeCase(colonne)
                    theBoard[ligne][colonne] = joueur
                    compteur += 1
                    gameNotFinished = checkWinningConditions(ligne, colonne, compteur)
                    isPositionNotOkay = False
                else:
                    print("La case choisi n'est pas valide !")
            else:
                print("La case choisi n'est pas valide !")

        if joueur == 1:
            joueur = 2
        else:
            joueur = 1

if __name__ == "__main__":
    gameLoop()
