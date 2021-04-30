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


def heuristique(ligne,colonne,joueur):
    '''exemple d'heuristique : calcule le nombre d'endroit où le joueur peut gagner moins le nombre d'endroits où l'adversaire peut gagner '''
    heur = 0
    #teste toutes les possibilités en lignes
    i = ligne
    j = colonne
    if((ligne > nb_lignes-1 or ligne < 0) or (colonne > nb_colonnes-1 or colonne < 0)):
        return 
    else:
        for i in range(6):
            for j in range(9):
                if theBoard[i][j] != 1 and theBoard[i][j+1] != 1 and theBoard[i][j+2] != 1 and theBoard[i][j+3] != 1:
                    heur +=1
                if theBoard[i][j] != 2 and theBoard[i][j+1] != 2 and theBoard[i][j+2] != 2 and theBoard[i][j+3] != 2:
                    heur -=1
    
    
        #teste toutes les possibilités en colonnes
        for j in range(12):
            for i in range(3):
                if theBoard[i][j] != 1 and theBoard[i+1][j] != 1 and theBoard[i+2][j] != 1 and theBoard[i+3][j] != 1:
                    heur +=1
                if theBoard[i][j] != 2 and theBoard[i+1][j] != 2 and theBoard[i+2][j] != 2 and theBoard[i+3][j] != 2:
                    heur -=1
    
        #teste toutes les possibilités en diagonales montantes / et descendantes \
        for i in range(3):
            for j in range(9):
                if theBoard[i][j] != 1 and theBoard[i+1][j+1] != 1 and theBoard[i+2][j+2] != 1 and theBoard[i+3][j+3] != 1:
                    heur +=1
                if theBoard[i+3][j] != 1 and theBoard[i+2][j+1] != 1 and theBoard[i+1][j+2] != 1 and theBoard[i][j+3] != 1:
                    heur +=1
                if theBoard[i][j] != 2 and theBoard[i+1][j+1] != 2 and theBoard[i+2][j+2] != 2 and theBoard[i+3][j+3] != 2:
                    heur -=1
                if theBoard[i+3][j] != 2 and theBoard[i+2][j+1] != 2 and theBoard[i+1][j+2] != 2 and theBoard[i][j+3] != 2:
                    heur -=1

    return heur

def minmax(board,alpha,beta, profondeur, isMaximazing,joueur):
    gameNotFinished = checkWinningConditions(ligne, colonne, compteur,joueur)
    if (profondeur == 0):
        return scores[result]

    if isMaximazing:       
        bestScore = 999999
        for colonne in np.arange(0,12):
            if canPlay(colonne):
                ligne = getLastFreeCase(colonne)
                theBoard[ligne][colonne] = joueur
                score = minmax(theBoard,np.NINF,np.Inf, 4 ,False)
                theBoard[ligne][colonne] = 0
                if score > bestScore:
                    bestScore = score
                    move = (ligne,colonne)
        return bestScore
    
    else:
        bestScore = 999999
        for colonne in np.arange(0,12):
            if canPlay(colonne):
                ligne = getLastFreeCase(colonne)
                theBoard[ligne][colonne] = joueur
                score = minmax(theBoard,np.NINF,np.Inf, 4 ,False)
                theBoard[ligne][colonne] = 0
                if score > bestScore:
                    bestScore = score
                    move = (ligne,colonne)
        return bestScore

def bestMove(joueur):
	#AI to make its turn
    move = (0,0)
    bestScore = np.NINF
    for colonne in np.arange(0,12):
        if canPlay(colonne):
            ligne = getLastFreeCase(colonne)
            theBoard[ligne][colonne] = joueur
            score = minmax(theBoard,np.NINF,np.Inf, 4 ,False)
            theBoard[ligne][colonne] = 0
            if score > bestScore:
                bestScore = score
                move = (ligne,colonne)
    theBoard[move[0]][move[1]] = joueur

def parcours(ligne,colonne,Vx,Vy,joueur):
    cpt = 0   
    while True:
        ligne+=Vy
        colonne+=Vx
        if((ligne > nb_lignes-1 or ligne < 0) or (colonne > nb_colonnes-1 or colonne < 0)):
            break
        else:
            if(theBoard[ligne][colonne] == joueur):
                cpt+=1
            else:
                break
    return cpt

# Le principe est qu'on vérifie le conformité de la pièce du joueur avec celle suivante
# suivant l'axe, si on trouve une pièce adverse on s'arrete et on passe à l'autre axe, sinon on incrémente le compteur
def checkWinningConditions(ligne,colonne,compteur,joueur):
    winning = False
    if(compteur==72):
        print("__TIE__")
        winning = None
    victory = 4
    
    # Ligne -
    valeur = parcours(ligne,colonne,1,0,joueur) + parcours(ligne,colonne,-1,0,joueur) + 1 
    if(valeur >= victory):
        print("Ligne -")
        winning = True
    
    # Colonne |
    valeur = parcours(ligne,colonne,0,1,joueur) + parcours(ligne,colonne,0,-1,joueur) + 1
    if(valeur >= victory):
        print("Colonne |")
        winning = True
    
    # Diagonale ascendante /
    valeur = parcours(ligne,colonne,1,1,joueur) + parcours(ligne,colonne,-1,-1,joueur) + 1
    if(valeur >= victory):
        print("Diagonale ascendante /")
        winning = True
    
    # Diagonale descendante \
    valeur = parcours(ligne,colonne,-1,1,joueur) + parcours(ligne,colonne,1,-1,joueur) + 1
    if(valeur >= victory):
        print("Diagonale descendante \"")
        winning = True  
       
    return winning

    """
    # A améliorer, utiliser une seule fonction
    # Ligne -
    cpt_ligne = 1
    for i in range(colonne+1,nb_colonnes): # out of range
        if theBoard[ligne][i] == joueur:
            cpt_ligne+=1
        else:
            break
    for i in range(colonne-1,-1,-1):
        if theBoard[ligne][i] == joueur:
            cpt_ligne+=1
        else:
            break
    
    # Colonne |
    cpt_colonne = 1
    for i in range(ligne+1,nb_lignes):
        if theBoard[i][colonne] == joueur:
            cpt_colonne+=1
        else:
            break
    for i in range(ligne-1,-1,-1):
        if theBoard[i][colonne] == joueur:
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
        
    for i in range(colonne-1,-1,-1):
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
        if(ligne+cptLoopDesc_1 > nb_lignes-1):
            break
        if theBoard[ligne+cptLoopDesc_1][i] == joueur:
            cpt_diagDesc+=1
        else:
            break
        cptLoopDesc_1+=1
    for i in range(colonne-1,-1,-1):
        # On dépasse le board (inférieur)
        print(ligne+cptLoopDesc_2 )
        if(ligne+cptLoopDesc_2 < 0):
            break
        if theBoard[ligne-cptLoopDesc_2][i] == joueur:
            cpt_diagDesc+=1
        else:
            break  
        cptLoopDesc_2+=1
    #print("cpt_colonne:",cpt_colonne, "cpt_ligne:",cpt_ligne,"cpt_diagDesc:",cpt_diagDesc,'cpt_diagAsc:',cpt_diagAsc)
    if cpt_colonne >= victory or cpt_ligne >= victory or cpt_diagAsc >= victory or cpt_diagDesc >= victory:
        return True
    else:
        return False
    """


def PvP():
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


        if gameNotFinished is True:
            printBoard()
            print(f"Le joueur {joueur} gagne !")
            break
        elif gameNotFinished is None:
            print("Egalité")
            break
        # Afin de stopper le jeu après que les 42 pièces soit posés
        elif compteur>42:
            printBoard()
            print("Egalité")
            break
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1
def PvIA():
    # print("Qui commence ? (1 : Moi, 2 : IA)")
    playingFirst = False
    gameChoiceIA = None
    while not playingFirst:
        gameChoiceIA = input("Qui commence ? (1 : Moi, 2 : IA)")
        if gameChoiceIA in ["1","2"]:
            playingFirst = True
        else:
            print("Choix inconnu")  
    compteur = 1
    joueur = int(gameChoiceIA)
    gameNotFinished = False
    while not gameNotFinished:
        isPositionNotOkay = True
        print(f"Tour: {compteur} Joueur: {joueur}")
        printBoard()
        if(joueur == 1):
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
                        print("Il n'est pas possible de jouer là !")
                else:
                    print("Case hors du plateau !")
        else:
            printBoard()
            bestMove(joueur)
            compteur += 1
            gameNotFinished = checkWinningConditions(ligne, colonne, compteur,joueur)


        if gameNotFinished is True:
            printBoard()
            print(f"Le joueur {joueur} gagne !")
            break
        elif gameNotFinished is None:
            print("Egalité...")
            break
        # Afin de stopper le jeu après que les 42 pièces soit posés
        elif compteur>42:
            printBoard()
            print("Egalité")
            break
        
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1
    pass
    
def gameLoop():
    hasChosen = False
    gameChoice = None
    while not hasChosen:
        gameChoice = input("Sélectionnez le mode de jeu : \n 1) Player versus Player \n 2) Player versus IA \n")
        if gameChoice in ["1","2"]:
            hasChosen = True
        else:
            print("Choix inconnu")  
    if(gameChoice == "1"):
        print("Choix 1 : Joueur contre Joueur")
        PvP()
    elif(gameChoice == "2"):
        print("Choix 3 : Joueur contre IA")
        PvIA()
  

if __name__ == "__main__":
    gameLoop()
