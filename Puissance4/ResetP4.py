"""

@author: VO Huu Toan Thierry
         MARUT Kamil
         PUKIVARAN Thanujan
"""
# Initialisation, imports
import numpy as np
import time 
nb_lignes = 6
nb_colonnes = 12
compteur = 0
negInfinity = np.NINF
posInfinity = np.Inf

theBoard = [[0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]]

# Reset du plateau
def reset():
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            theBoard[i][j] = 0

# Renvoie True si la colonne peut être jouée, False sinon
# Utilisée pour le choix du joueur
def canPlay(colonne):
    return theBoard[0][colonne] == 0

# Renvoie la derniere ligne, utilisée pour le choix du joueur
def getLastFreeCase(colonne):
    for i in range(5,-1,-1):
        if theBoard[i][colonne] == 0:
            return i
    return -1

# Affiche le plateau
def printBoard():
    affichage = "  1   2   3   4   5   6   7   8   9   10  11  12\n"
    affichage += "  ─   ─   ─   ─   ─   ─   ─   ─   ─   ─   ─   ─\n"
    for i in np.arange(nb_lignes):
        affichage += "| "
        for j in np.arange(nb_colonnes):
            affichage += f"{theBoard[i][j]} | "
        affichage += "\n"
    affichage += "  ─   ─   ─   ─   ─   ─   ─   ─   ─  ─  ─  ─  ─\n"
    print(affichage)

# Parcourt un axe en fonction de Vx (colonne) et Vy (ligne)
# Utilisé dans checkWinnerPlayer
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

# Parcourt les axes selon la position de la pièce posée pour voir si le joueur a gagné
# Utilisé dans le choix du joueur
def checkWinnerPlayer(ligne,colonne,joueur):
    winning = False
    victory = 4
    
    # Ligne -
    valeur = parcours(ligne,colonne,1,0,joueur) + parcours(ligne,colonne,-1,0,joueur) + 1 
    if(valeur >= victory):
        winning = True
    
    # Colonne |
    valeur = parcours(ligne,colonne,0,1,joueur) + parcours(ligne,colonne,0,-1,joueur) + 1
    if(valeur >= victory):
        winning = True
    
    # Diagonale ascendante /
    valeur = parcours(ligne,colonne,1,1,joueur) + parcours(ligne,colonne,-1,-1,joueur) + 1
    if(valeur >= victory):
        winning = True
    
    # Diagonale descendante \
    valeur = parcours(ligne,colonne,-1,1,joueur) + parcours(ligne,colonne,1,-1,joueur) + 1
    if(valeur >= victory):
        winning = True  
       
    return winning

# Parcourt tout le tableau pour voir si quelqu'un a gagné
# Utilisé dans l'algorithme minmax avec élagage alpha-beta
def checkWinnerIA():
    winner = 0
    for joueur in [2,1]: # Vérification pour les deux joueurs
        # Ligne -
        for i in range(6):
            for j in range(9):
                if theBoard[i][j] == joueur and theBoard[i][j+1] == joueur and theBoard[i][j+2] == joueur and theBoard[i][j+3] == joueur:
                    winner = joueur
 
        
        # Colonne |
        for j in range(12):
            for i in range(3):
                if theBoard[i][j] == joueur and theBoard[i+1][j] == joueur and theBoard[i+2][j] == joueur and theBoard[i+3][j] == joueur:
                    winner = joueur
                    

                    
        # Diagonale ascendante / et descendante \
        for i in range(3):
            for j in range(9):
                if theBoard[i][j] == joueur and theBoard[i+1][j+1] == joueur and theBoard[i+2][j+2] == joueur and theBoard[i+3][j+3] == joueur:
                    winner = joueur
                    
                if theBoard[i+3][j] == joueur and theBoard[i+2][j+1] == joueur and theBoard[i+1][j+2] == joueur and theBoard[i][j+3] == joueur:
                    winner = joueur
                    
        
    return winner

# Donne les cases possibles où l'on peut jouer
def choices():
    possibleChoices = []
    for ligne in range (nb_lignes): # On parcourt tout le plateau
        for colonne in range (nb_colonnes):
            if theBoard[ligne][colonne] == 0:
                if ligne == nb_lignes-1 : # Dernière ligne
                    possibleChoices.append([ligne,colonne])
                elif theBoard[ligne+1][colonne] !=0: # Autres lignes, si la ligne en dessous est "occupée"
                    possibleChoices.append([ligne,colonne])             
    return possibleChoices    
    
# Cette heuristique va renvoyer la différence entre :
    # La somme des possibilités d'alignement pour l'IA (maximisation du score)
    # La somme des possibilités d'alignement pour le joueur (minimisation du score)
# On aura une evaluation donc sur la case choisie
def heuristique():
    heur = 0
    # Teste toutes les possibilités en lignes
    for i in range(6):
        for j in range(9):
            if theBoard[i][j] != 1 and theBoard[i][j+1] != 1 and theBoard[i][j+2] != 1 and theBoard[i][j+3] != 1:
                heur +=1
            if theBoard[i][j] != 2 and theBoard[i][j+1] != 2 and theBoard[i][j+2] != 2 and theBoard[i][j+3] != 2:
                heur -=1


    # Teste toutes les possibilités en colonnes
    for j in range(12):
        for i in range(3):
            if theBoard[i][j] != 1 and theBoard[i+1][j] != 1 and theBoard[i+2][j] != 1 and theBoard[i+3][j] != 1:
                heur +=1
            if theBoard[i][j] != 2 and theBoard[i+1][j] != 2 and theBoard[i+2][j] != 2 and theBoard[i+3][j] != 2:
                heur -=1

    # Teste toutes les possibilités en diagonales ascendantes / et descendantes \
    for i in range(3):
        for j in range(4):
            if theBoard[i][j] != 1 and theBoard[i+1][j+1] != 1 and theBoard[i+2][j+2] != 1 and theBoard[i+3][j+3] != 1:
                heur +=1
            if theBoard[i+3][j] != 1 and theBoard[i+2][j+1] != 1 and theBoard[i+1][j+2] != 1 and theBoard[i][j+3] != 1:
                heur +=1
            if theBoard[i][j] != 2 and theBoard[i+1][j+1] != 2 and theBoard[i+2][j+2] != 2 and theBoard[i+3][j+3] != 2:
                heur -=1
            if theBoard[i+3][j] != 2 and theBoard[i+2][j+1] != 2 and theBoard[i+1][j+2] != 2 and theBoard[i][j+3] != 2:
                heur -=1
    return heur

# Cette heuristique va renvoyer la différence entre :
    # La somme des possibilités d'alignement pour l'IA (maximisation du score)
    # La somme des possibilités d'alignement pour le joueur (minimisation du score)   
    # Avec cela s'ajoute le fait que s'il ya déjà un alignement de 4, la valuation aura beaucoup plus de poids
    # Sinon on compte le nombre de pièces déjà présentes (pour un éventuel alignement)
# On aura une evaluation plus précise que l'heuristique 1
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

# Algorithme minmax avec élagage alpha-beta
def min_value(alpha,beta,profondeur):
    gameState = checkWinnerIA() # Vérification si partie gagnée
    if gameState == 1:
        return negInfinity
    elif gameState == 2:
        return posInfinity
    else:         
        if profondeur == 0 :
            return heuristique()
        evaluate= posInfinity
        for choice in choices():
                theBoard[choice[0]][choice[1]] = 1
                evaluate = min(evaluate,max_value(alpha,beta,profondeur-1))            
                theBoard[choice[0]][choice[1]] = 0
                if evaluate <= alpha: # On a trouvé une valeur plus petite que la valeur du noeud maximisant père (alpha), on élague
                    #print("Elagage type beta")
                    return evaluate
                beta = min(beta,evaluate) # On garde la plus petite des valeurs, qu'on transmets aux noeuds fils suivants
        return evaluate

def max_value(alpha,beta,profondeur):
    gameState = checkWinnerIA()
    if gameState == 1:
        return negInfinity
    elif gameState == 2:
        return posInfinity
    else:        
        if profondeur == 0:
            return heuristique()
        evaluate= negInfinity
        for choice in choices():
            theBoard[choice[0]][choice[1]] = 2
            evaluate = max(evaluate,min_value(alpha,beta,profondeur-1))            
            theBoard[choice[0]][choice[1]] = 0
            if evaluate >= beta: # On a trouvé une valeur plus grande que la valeur du noeud minimisant père (beta), on élague
                #print("Elagage type alpha")
                return evaluate
            alpha = max(alpha,evaluate) # On garde la plus grande des valeurs, qu'on transmets aux noeuds fils suivants
        return evaluate    

# Tour de l'IA 
def playAI():   
    bestEval = negInfinity # Pire score pour l'IA
    move = (0,0)
    for choice in choices():
        theBoard[choice[0]][choice[1]] = 2
        evaluate = min_value(negInfinity,posInfinity,6)
        #print("Choice :",choice," & Evaluate :",evaluate)
        theBoard[choice[0]][choice[1]] = 0
        if(evaluate > bestEval): # Si on a trouvé une meilleur evaluation, on change le mouvement 
            bestEval = evaluate
            move = (choice[0],choice[1])
    if move == (0,0): # En cas de défaite...
        print("L'IA s'avoue vaincu...")
        return False
    print("L'IA a joué à la colonne :",move[1] + 1 )
    theBoard[move[0]][move[1]] = 2
    return True


# Boucle de jeu
def gameLoop():
    global compteur
    reset()
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
            print("Tour du joueur \n")   
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
                        print("Il n'est pas possible de jouer là")
                else:
                    print("Case hors du plateau")
        else:
            print("Tour de l'IA \n")   
            start_time = time.time()
            turnAI = playAI()
            if(not turnAI):
                break
            compteur +=1
            gameNotFinished = True if checkWinnerIA() == 2 else False
            print("=== Temps de calcul : %s secondes ===" % (time.time() - start_time))


        if gameNotFinished is True:
            printBoard()
            print(f"Le joueur {joueur} gagne !")
            break
        elif compteur == 42:
            print("Limite de pièces atteinte, égalité...")
            break   
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1
    
        
if __name__ == "__main__":
    print("GL HF :)")
    while True:
        gameLoop()
        playAgain = input("Merci d'avoir joué, voulez vous réessayer ? (O/N)")
        if playAgain == "N":
            break
