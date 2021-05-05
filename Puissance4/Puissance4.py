import numpy as np

nb_lignes = 6
nb_colonnes = 12
l=0
col=0
compteur=1
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


def test2():
    align4_2 = checkForStreak(2,4)
    align3_2 = checkForStreak(2,3)
    align2_2 = checkForStreak(2,2)
    align4_1 = checkForStreak(1,4)
    align3_1 = checkForStreak(1,3)
    align2_1 = checkForStreak(1,2)
    return (align4_2 * 10 + align3_2 * 5 + align2_2 * 2) - (align4_1 * 10 + align3_1 * 5 + align2_1 * 2)    

def checkForStreak(joueur, streak):
    count = 0
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            if theBoard[i][j] == 0:
                count += parcoursHeur2(i, j, 1,0, streak,joueur) + parcoursHeur2(i, j,-1,0, streak,joueur)
                count += parcoursHeur2(i, j, 0,1, streak,joueur)+ parcoursHeur2(i, j,0,-1, streak,joueur)
                count += parcoursHeur2(i, j, 1,1, streak,joueur) + parcoursHeur2(i, j,-1,-1, streak,joueur)
                count += parcoursHeur2(i, j, -1,1, streak,joueur) + parcoursHeur2(i, j, 1,-1, streak,joueur)

    return count
def parcoursHeur2(ligne,colonne,Vx,Vy,streak,joueur):
    cpt = 0
    while True:
        if((ligne > nb_lignes-1 or ligne < 0) or (colonne > nb_colonnes-1 or colonne < 0)):
            cpt = 0
            break
        else:
            if(theBoard[ligne][colonne] == joueur):
                cpt+=1
            else:
                break
        ligne+=Vy
        colonne+=Vx
    if(cpt < streak):
        cpt= 0
    return cpt 
   
def test():
    valeur = 0

    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):         
            # Ligne - 
            valeur += parcoursHeur(ligne,colonne,1,0) + parcoursHeur(ligne,colonne,-1,0)            
            # Colonne |
            valeur += parcoursHeur(ligne,colonne,0,1) + parcoursHeur(ligne,colonne,0,-1)                 
            # Diagonale ascendante /
            valeur += parcoursHeur(ligne,colonne,1,1) + parcoursHeur(ligne,colonne,-1,-1)                   
            # Diagonale descendante \
            valeur += parcoursHeur(ligne,colonne,-1,1) + parcoursHeur(ligne,colonne,1,-1)  
        
    return valeur
    
def parcoursHeur(ligne,colonne,Vx,Vy):
    cpt = 1
    alignement = 4
    while alignement != 0 and cpt != 0:

        if((ligne > nb_lignes-1 or ligne < 0) or (colonne > nb_colonnes-1 or colonne < 0)):
            cpt = 0
        else:
            if(theBoard[ligne][colonne] == 2):
                cpt*=1
            elif(theBoard[ligne][colonne] == 0):
                cpt*=0.5
            else:
                cpt*=0
        ligne+=Vy
        colonne+=Vx
        alignement-=1
    return cpt    

def heuristique():
    heur = 0
    #teste toutes les possibilités en lignes
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

def heuristiquebis():
        '''Heuristique un peu plus complexe'''
        somme = 0
        # colonnes
        for j in range(12):  #colonnes
            for i in range(3):  #lignes
                zone =[theBoard[i][j], theBoard[i+1][j], theBoard[i+2][j], theBoard[i+3][j]]
                if not(1 in zone) :
                    if zone.count(2) == 4:
                        somme += (1000)
                    else :
                        somme += zone.count(2)
                if not (2 in zone) :
                    if zone.count(1) == 4:
                        somme -= (1000)
                    else :
                        somme -= zone.count(1)
        # lignes
        for i in range(6):     #lignes
            for j in range(9):  #colonnes
                zone = [theBoard[i][j], theBoard[i][j+1], theBoard[i][j+2], theBoard[i][j+3]]
                if not(1 in zone) :
                    if zone.count(2) == 4:
                        somme += (1000)
                    else :
                        somme += zone.count(2)
                if not (2 in zone) :
                    if zone.count(1) == 4:
                        somme -= (1000)
                    else :
                        somme -= zone.count(1)
        # diagonales haut-droites
        for i in range(3):
            for j in range(9):
                zone = [theBoard[i][j+3], theBoard[i+1][j+2], theBoard[i+2][j+1], theBoard[i+3][j]]
                if not(1 in zone) :
                    if zone.count(2) == 4:
                        somme += (1000)
                    else :
                        somme += zone.count(2)
                if not (2 in zone) :
                    if zone.count(1) == 4:
                        somme -= (1000)
                    else :
                        somme -= zone.count(1)
        # diagonales haut-gauches
        for i in range(3):
            for j in range(4):
                zone = [theBoard[i+3][j+3], theBoard[i+2][j+2], theBoard[i+1][j+1], theBoard[i][j]]
                if not(1 in zone) :
                    if zone.count(2) == 4:
                        somme += (1000)
                    else :
                        somme += zone.count(2)
                if not (2 in zone) :
                    if zone.count(1) == 4:
                        somme -= (1000)
                    else :
                        somme -= zone.count(1)

        return somme

def minmax(board,alpha,beta, profondeur, isMaximazing,ligne,colonne,joueur):
    global compteur
    if(profondeur == 0 or checkWinningConditions(ligne,colonne,compteur,joueur)):
        return heuristiquebis()
    
    if(isMaximazing): # Max
        maxEvaluate = np.NINF
        for colonne in np.arange(0,12):
            if canPlay(colonne):
                ligne = getLastFreeCase(colonne)
                theBoard[ligne][colonne] = joueur
                evaluate = minmax(theBoard,alpha,beta, profondeur-1 ,False,ligne,colonne,1)
                theBoard[ligne][colonne] = 0
                maxEvaluate = max(maxEvaluate,evaluate)
                alpha = max(alpha,evaluate)
                if beta <= alpha:
                    break
        return maxEvaluate
    else: # Min
        minEvaluate = np.Inf
        for colonne in np.arange(0,12):
            if canPlay(colonne):
                ligne = getLastFreeCase(colonne)
                theBoard[ligne][colonne] = joueur
                evaluate = minmax(theBoard,alpha,beta, profondeur-1 ,True,ligne,colonne,2)
                theBoard[ligne][colonne] = 0
                minEvaluate = min(minEvaluate,evaluate)
                beta = min(beta,evaluate)
                if beta <= alpha:
                    break            
        return minEvaluate



def turnAI():
	#AI to make its turn
    global l,col
    move = (0,0)
    bestScore = np.NINF
    for colonne in np.arange(0,12):
        if canPlay(colonne):
            ligne = getLastFreeCase(colonne)
            theBoard[ligne][colonne] = 2
            score = alphabetasearch(theBoard,ligne,colonne)
            #score = minmax(theBoard,np.NINF,np.Inf, 2 ,False,ligne,colonne,1)
            theBoard[ligne][colonne] = 0
            if score > bestScore:
                bestScore = score
                move = (ligne,colonne)
    theBoard[move[0]][move[1]] = 2
    l=move[0]
    col=move[1]

def terminalState(board):
    terminal = False
    #teste toutes les possibilités en lignes
    for i in range(6):
        for j in range(9):
            if theBoard[i][j] == 1 and theBoard[i][j+1] == 1 and theBoard[i][j+2] == 1 and theBoard[i][j+3] == 1:
                terminal = True
            if theBoard[i][j] == 2 and theBoard[i][j+1] == 2 and theBoard[i][j+2] == 2 and theBoard[i][j+3] == 2:
                terminal = True


    #teste toutes les possibilités en colonnes
    for j in range(12):
        for i in range(3):
            if theBoard[i][j] == 1 and theBoard[i+1][j] == 1 and theBoard[i+2][j] == 1 and theBoard[i+3][j] == 1:
                terminal = True
            if theBoard[i][j] == 2 and theBoard[i+1][j] == 2 and theBoard[i+2][j] == 2 and theBoard[i+3][j] == 2:
                terminal = True

    #teste toutes les possibilités en diagonales montantes / et descendantes \
    for i in range(3):
        for j in range(9):
            if theBoard[i][j] == 1 and theBoard[i+1][j+1] == 1 and theBoard[i+2][j+2] == 1 and theBoard[i+3][j+3] == 1:
                terminal = True
            if theBoard[i+3][j] == 1 and theBoard[i+2][j+1] == 1 and theBoard[i+1][j+2] == 1 and theBoard[i][j+3] == 1:
                terminal = True
            if theBoard[i][j] == 2 and theBoard[i+1][j+1] == 2 and theBoard[i+2][j+2] == 2 and theBoard[i+3][j+3] == 2:
                terminal = True
            if theBoard[i+3][j] == 2 and theBoard[i+2][j+1] == 2 and theBoard[i+1][j+2] == 2 and theBoard[i][j+3] == 2:
                terminal = True
    return terminal  


def maxvalue(board,alpha,beta,profondeur,ligne,colonne,joueur):
    global compteur
    if(profondeur == 0 or checkWinningConditions(ligne,colonne,compteur,joueur)):
        return test2()
    evaluate = np.NINF
    for colonne in np.arange(0,12):
        if canPlay(colonne):
            ligne = getLastFreeCase(colonne)
            theBoard[ligne][colonne] = joueur
            evaluate = max(evaluate,minvalue(theBoard,alpha,beta, profondeur-1,ligne,colonne,1))
            theBoard[ligne][colonne] = 0
            if(evaluate>=beta):
                return evaluate
            alpha = max(alpha,evaluate)
    return evaluate
    
def minvalue(board,alpha,beta,profondeur,ligne,colonne,joueur):
    if(profondeur == 0 or checkWinningConditions(ligne,colonne,compteur,joueur)):
        return test2()
    evaluate = np.Inf
    for colonne in np.arange(0,12):
        if canPlay(colonne):
            ligne = getLastFreeCase(colonne)
            theBoard[ligne][colonne] = joueur
            evaluate = min(evaluate,maxvalue(theBoard,alpha,beta, profondeur-1,ligne,colonne,2))
            theBoard[ligne][colonne] = 0
            if(evaluate <= alpha):
                return evaluate
            beta = min(beta,evaluate)          
    return evaluate
   

def alphabetasearch(board,ligne,colonne):
    v = minvalue(board,np.NINF,np.Inf,4,ligne,colonne,2)
    return v


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
def checkWinningConditions(ligne,colonne,joueur):
    winning = False
    if(compteur==42):
        print("__TIE__")
        winning = None
    victory = 4
    
    # Ligne -
    valeur = parcours(ligne,colonne,1,0,joueur) + parcours(ligne,colonne,-1,0,joueur) + 1 
    if(valeur >= victory):
        #print("Ligne -")
        winning = True
    
    # Colonne |
    valeur = parcours(ligne,colonne,0,1,joueur) + parcours(ligne,colonne,0,-1,joueur) + 1
    if(valeur >= victory):
        #print("Colonne |")
        winning = True
    
    # Diagonale ascendante /
    valeur = parcours(ligne,colonne,1,1,joueur) + parcours(ligne,colonne,-1,-1,joueur) + 1
    if(valeur >= victory):
        #print("Diagonale ascendante /")
        winning = True
    
    # Diagonale descendante \
    valeur = parcours(ligne,colonne,-1,1,joueur) + parcours(ligne,colonne,1,-1,joueur) + 1
    if(valeur >= victory):
        #print("Diagonale descendante \"")
        winning = True  
       
    return winning

<<<<<<< HEAD
=======
    
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


>>>>>>> origin/develop
def PvP():
    joueur = 1
    compteur =1
    gameNotFinished = False
    while not gameNotFinished:
        isPositionNotOkay = True
        print("Tour: "+ str(compteur)+f" Joueur: {joueur}")
        printBoard()
        while isPositionNotOkay:
            userInput = input("Veuillez selectionner une colonne entre 1 et 12 pour valider votre tour:\n")
            colonne = int(userInput) - 1
            if colonne in np.arange(0,12):
                if canPlay(colonne):
                    ligne = getLastFreeCase(colonne)
                    theBoard[ligne][colonne] = joueur
                    compteur += 1
                    gameNotFinished = checkWinningConditions(ligne, colonne,joueur)
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
    global compteur,l,col
    playingFirst = False
    gameChoiceIA = None
    while not playingFirst:
        gameChoiceIA = input("Qui commence ? (1 : Moi, 2 : IA):\n")
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
                        gameNotFinished = checkWinningConditions(ligne, colonne,joueur)
                        isPositionNotOkay = False
                    else:
                        print("Il n'est pas possible de jouer là !")
                else:
                    print("Case hors du plateau !")
        else:
            # printBoard()
            turnAI()
            compteur += 1
            gameNotFinished = checkWinningConditions(l, col, compteur,joueur)


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
        gameChoice = input("Sélectionnez le mode de jeu : \n 1) Player versus Player \n 2) Player versus IA \n\n")
        if gameChoice in ["1","2"]:
            hasChosen = True
        else:
            print("Choix inconnu")  
    if(gameChoice == "1"):
        print("Choix 1 : Joueur contre Joueur")
        PvP()
    elif(gameChoice == "2"):
        print("Choix 2 : Joueur contre IA")
        PvIA()
  

if __name__ == "__main__":
    gameLoop()
