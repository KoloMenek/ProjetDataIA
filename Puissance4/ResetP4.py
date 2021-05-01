
import numpy as np
import time 
nb_lignes = 6
nb_colonnes = 7
compteur = 0
negInfinity = np.NINF
posInfinity = np.Inf
# values = {0:'Vide', 1:'Bleu', 2: 'Rouge'}
theBoard = np.zeros((nb_lignes,nb_colonnes),dtype=int)

def printBoard():
    affichage = "  ─   ─   ─   ─   ─   ─   ─   ─   ─   ─   ─   ─\n"
    for i in np.arange(nb_lignes):
        affichage += "| "
        for j in np.arange(nb_colonnes):
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
def checkWinnerPlayer(ligne,colonne,joueur):
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

def checkWinnerIA():
    winner = 0
    for joueur in [2,1]:
        # Ligne -
        for i in range(6):
            for j in range(4): # 9
                if theBoard[i][j] == joueur and theBoard[i][j+1] == joueur and theBoard[i][j+2] == joueur and theBoard[i][j+3] == joueur:
                    winner = joueur

        # Colonne |
        for j in range(7): # 12
            for i in range(3):
                if theBoard[i][j] == joueur and theBoard[i+1][j] == joueur and theBoard[i+2][j] == joueur and theBoard[i+3][j] == joueur:
                    winner = joueur
            
        # Diagonale ascendante /et descendante \
        for i in range(3):
            for j in range(4): # 9
                if theBoard[i][j] == joueur and theBoard[i+1][j+1] == joueur and theBoard[i+2][j+2] == joueur and theBoard[i+3][j+3] == joueur:
                    winner = joueur
                if theBoard[i+3][j] == joueur and theBoard[i+2][j+1] == joueur and theBoard[i+1][j+2] == joueur and theBoard[i][j+3] == joueur:
                    winner = joueur
    return winner


def heuristique():
    heur = 0
    #teste toutes les possibilités en lignes
    for i in range(6):
        for j in range(4): # 9
            if theBoard[i][j] != 1 and theBoard[i][j+1] != 1 and theBoard[i][j+2] != 1 and theBoard[i][j+3] != 1:
                heur +=1
            if theBoard[i][j] != 2 and theBoard[i][j+1] != 2 and theBoard[i][j+2] != 2 and theBoard[i][j+3] != 2:
                heur -=1


    #teste toutes les possibilités en colonnes
    for j in range(7): # 12
        for i in range(3):
            if theBoard[i][j] != 1 and theBoard[i+1][j] != 1 and theBoard[i+2][j] != 1 and theBoard[i+3][j] != 1:
                heur +=1
            if theBoard[i][j] != 2 and theBoard[i+1][j] != 2 and theBoard[i+2][j] != 2 and theBoard[i+3][j] != 2:
                heur -=1

    #teste toutes les possibilités en diagonales montantes / et descendantes \
    for i in range(3):
        for j in range(4): # 9
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
        for j in range(7):  #colonnes
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
            for j in range(4):  #colonnes
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
            for j in range(4):
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


def min_value(alpha,beta,profondeur):
    gameState = checkWinnerIA()
    if gameState == 1:
        return -999999
    elif gameState == 2:
        return 999999
    else:         
        if profondeur == 0 :
            return heuristiquebis()
        evaluate= posInfinity
        for colonne in np.arange(nb_colonnes):
            if canPlay(colonne):
                ligne = getLastFreeCase(colonne)
                theBoard[ligne][colonne] = 1
                evaluate = min(evaluate,max_value(alpha,beta,profondeur-1))            
                theBoard[ligne][colonne] = 0
                if evaluate <= alpha:
                    #print("Beta pruning")
                    return evaluate
                beta = min(beta,evaluate)
        return evaluate

def max_value(alpha,beta,profondeur):
    gameState = checkWinnerIA()
    if gameState == 1:
        return -99999
    elif gameState == 2:
        return 99999
    else:        
        if profondeur == 0:
            return heuristiquebis()
        evaluate= negInfinity
        for colonne in np.arange(nb_colonnes):
            if canPlay(colonne):
                ligne = getLastFreeCase(colonne)
                theBoard[ligne][colonne] = 2
                evaluate = max(evaluate,min_value(alpha,beta,profondeur-1))            
                theBoard[ligne][colonne] = 0
                if evaluate >= beta:
                    #print("Alpha pruning")
                    return evaluate
                alpha = max(alpha,evaluate)
        return evaluate    


def playAI():   
    bestEval = negInfinity
    move = (0,0)
    for colonne in np.arange(nb_colonnes):
        if canPlay(colonne):
            ligne = getLastFreeCase(colonne)
            theBoard[ligne][colonne] = 2
            evaluate = min_value(negInfinity,posInfinity,5)
            print("Colonne :",colonne+1," & Evaluate :",evaluate)
            theBoard[ligne][colonne] = 0
            if(evaluate > bestEval):
                bestEval = evaluate
                move = (ligne,colonne)
    print("L'IA a joué à la colonne :",move[1] + 1 )
    theBoard[move[0]][move[1]] = 2
    
    
    
def gameLoop():
    global compteur
    joueur = None
    gameNotFinished = False
    choiceStart = False
    while not choiceStart:
        try:
            joueur = int(input("Qui commence ? (Moi : 1, IA : 2): \n"))
            if(joueur in [1,2]):
                choiceStart = True
            else:
                print("Choix inconnu")
        except ValueError:
            print("Value error, try again")
    while not gameNotFinished:
        printBoard()    
        if joueur == 1:
            print("Le joueur commence : \n")            
            hasPlayed = False
            while not hasPlayed:
                userInput = None
                choiceUser = False
                while not choiceUser:
                    try:
                        userInput = int(input("Veuillez selectionner une colonne entre 1 et 12 pour valider votre tour:\n"))
                        choiceUser = True
                    except ValueError:
                        print("Value error, try again")
                colonne = userInput - 1
                if colonne in np.arange(nb_colonnes):
                    if canPlay(colonne):
                        ligne = getLastFreeCase(colonne)
                        theBoard[ligne][colonne] = joueur
                        compteur += 1
                        gameNotFinished = checkWinnerPlayer(ligne,colonne,joueur)
                        hasPlayed = True
                    else:
                        print("Il n'est pas possible de jouer là !")
                else:
                    print("Case hors du plateau !")
        else:
            print("L'IA commence : \n")   
            start_time = time.time()
            playAI()
            compteur +=1
            gameNotFinished = True if checkWinnerIA() == 2 else False
            print("--- %s seconds ---" % (time.time() - start_time))


            
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1
    
        
if __name__ == "__main__":
    gameLoop()
