import numpy as np

nb_lignes = 6
nb_colonnes = 12

values = {0:'Vide', 1:'Bleu', 2: 'Rouge'}
theBoard = np.zeros((nb_lignes,nb_colonnes),dtype=int)

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

# Le principe est qu'on vérifie le conformité de la pièce du joueur avec celle suivante
# suivant l'axe, si on trouve une pièce adverse on s'arrete, sinon on incrémente le compteur
def checkWinningConditions(ligne,colonne,compteur,joueur):
    if(compteur==42):
        print("__TIE__")
        return None
    victory = 4
    
    # Ligne -
    cpt_ligne = 1
    for i in range(ligne+1,nb_colonnes): # out of range
        print("ligne:",i,"colonne:",colonne)
        if theBoard[i][colonne] == joueur:
            cpt_ligne+=1
        else:
            break
    for i in range(ligne-1,0,-1):
        if theBoard[i][colonne] == joueur:
            cpt_ligne+=1
        else:
            break
    
    # Colonne |
    cpt_colonne = 1
    for i in range(colonne+1,nb_lignes):
        if theBoard[ligne][i] == joueur:
            cpt_colonne+=1
        else:
            break
    for i in range(colonne-1,0,-1):
        if theBoard[ligne][i] == joueur:
            cpt_colonne+=1
        else:
            break   
        
    # Diagonale ascendante /
    cpt_diagAsc = 1
    cptLoopAsc_1 = 1
    cptLoopAsc_2 = 1
    for i in range(colonne+1,nb_colonnes):
        # On dépasse le board (supérieur)
        if(ligne-cptLoopAsc_1 < 0):
            break
        if theBoard[ligne-cptLoopAsc_1][i] == joueur:
            cpt_diagAsc+=1
        else:
            break
        cptLoopAsc_1+=1
        
    for i in range(colonne-1,0,-1):
        # On dépasse le board (inférieur)
        if(ligne+cptLoopAsc_2 > nb_lignes-1):
            break
        if theBoard[ligne+cptLoopAsc_2][i] == joueur:
            cpt_diagAsc+=1
        else:
            break   
        cptLoopAsc_2+=1
    
    #diagonale descendante \ 
    cpt_diagDesc = 1
    cptLoopDesc_1 = 1
    cptLoopDesc_2 = 1
    for i in range(colonne+1,nb_colonnes):
        # On dépasse le board (supérieur)
        if(ligne-cptLoopDesc_1 < 0):
            break
        if theBoard[ligne-cptLoopDesc_1][i] == joueur:
            cpt_colonne+=1
        else:
            break
        cptLoopDesc_1+=1
    for i in range(0,colonne):
        # On dépasse le board (inférieur)
        if(ligne+cptLoopDesc_2 > nb_lignes-1):
            break
        if theBoard[ligne+cptLoopDesc_2][i] == joueur:
            cpt_colonne+=1
        else:
            break  
        cptLoopDesc_1+=1
        
    if cpt_colonne >= victory or cpt_ligne >= victory or cpt_diagAsc >= victory or cpt_diagDesc >= victory:
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
                    gameNotFinished = checkWinningConditions(ligne, colonne, compteur,joueur)
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
