theBoard = [
	['-', '-', '-'],
	['-', '-', '-'],
	['-', '-', '-']
]

boardStates = []
scores = {
	'X': -1,
	'O': 1,
	'Tie': 0
}
def reset():
	for i in range(3):
		for j in range(3):
			theBoard[i][j] = "-"

def printBoard():
	affichage = "  ─   ─   ─\n"
	affichage += f"| {theBoard[0][0]} | {theBoard[0][1]} | {theBoard[0][2]} |\n"
	affichage += f"| {theBoard[1][0]} | {theBoard[1][1]} | {theBoard[1][2]} |\n"
	affichage += f"| {theBoard[2][0]} | {theBoard[2][1]} | {theBoard[2][2]} |\n"
	affichage += "  ─   ─   ─\n"
	print(affichage)

def canPlay():
	emptySlots = False
	for i in range(0,3):
		for j in range(0,3):
			if theBoard[i][j] == '-':
				emptySlots = True
	return emptySlots

def gameState(theBoard, joueur):
	gameNotFinished = False
	if theBoard[0][0] == theBoard[0][1] == theBoard[0][2] != '-':
		printBoard()
		print(f"Game Over ! \nLe joueur {joueur} a gagné !")
		gameNotFinished = True
	elif theBoard[1][0] == theBoard[1][1] == theBoard[1][2] != '-':
		printBoard()
		print(f"Game Over ! \nLe joueur {joueur} a gagné !")
		gameNotFinished = True
	elif theBoard[2][0] == theBoard[2][1] == theBoard[2][2] != '-':
		printBoard()
		print(f"Game Over ! \nLe joueur {joueur} a gagné !")
		gameNotFinished = True
	elif theBoard[0][0] == theBoard[1][0] == theBoard[2][0] != '-':
		printBoard()
		print(f"Game Over ! \nLe joueur {joueur} a gagné !")
		gameNotFinished = True
	elif theBoard[0][1] == theBoard[1][1] == theBoard[2][1] != '-':
		printBoard()
		print(f"Game Over ! \nLe joueur {joueur} a gagné !")
		gameNotFinished = True
	elif theBoard[0][2] == theBoard[1][2] == theBoard[2][2] != '-':
		printBoard()
		print(f"Game Over ! \nLe joueur {joueur} a gagné !")
		gameNotFinished = True
	elif theBoard[0][0] == theBoard[1][1] == theBoard[2][2] != '-':
		printBoard()
		print(f"Game Over ! \nLe joueur {joueur} a gagné !")
		gameNotFinished = True
	elif theBoard[2][0] == theBoard[1][1] == theBoard[0][2] != '-':
		printBoard()
		print(f"Game Over ! \nLe joueur {joueur} a gagné !")
		gameNotFinished = True
	elif not canPlay():
		printBoard()
		print(f"Game Over ! \nEgalité, personne a gagné !")
		gameNotFinished = True
	return gameNotFinished

def minimax(board, isMaximazing):
	result = checkWinner()
	if result != None:
		return scores[result]

	if isMaximazing:
		bestScore = -999999
		for i in range(0,3):
			for j in range(0,3):
				#Is the spot available?
				if board[i][j] == '-':
					board[i][j] = 'O'
					score = minimax(board, False)
					board[i][j] = '-'
					bestScore = max(score, bestScore)
		return bestScore
    
	else:
		bestScore = 999999
		for i in range(0,3):
			for j in range(0,3):
				#Is the spot available?
				if board[i][j] == '-':
					board[i][j] = 'X'
					score = minimax(board, True)
					board[i][j] = '-'
					bestScore = min(score, bestScore)
		return bestScore

def bestMove():
	#AI to make its turn
	move = (0,0)
	bestScore = -999999
	for i in range(0,3):
		for j in range(0,3):
		#Is the spot available?
			if theBoard[i][j] == '-':
				theBoard[i][j] = 'O'
				score = minimax(theBoard, False)
				theBoard[i][j] = '-'
				if score > bestScore:
					bestScore = score
					move = (i,j)
	theBoard[move[0]][move[1]] = 'O'





def equals3(a, b, c):
    return a == b and b == c and a != '-'

def checkWinner(): # Utility, pas d'état en paramètres car état est une variable globale
	winner = None

	# Ligne
	for i in range(3):
		if (equals3(theBoard[i][0], theBoard[i][1], theBoard[i][2])):
			winner = theBoard[i][0]
	# Colonne
	for i in range(3):
		if (equals3(theBoard[0][i], theBoard[1][i], theBoard[2][i])): 
			winner = theBoard[0][i]

	# Diagonale /
	if (equals3(theBoard[0][0], theBoard[1][1], theBoard[2][2])):
		winner = theBoard[0][0] 

	# Diagonale \
	if (equals3(theBoard[2][0], theBoard[1][1], theBoard[0][2])):
		winner = theBoard[2][0]

	emptySlots = 0
	for i in range(0,3):
		for j in range(0,3):
			if theBoard[i][j] == '-':
				emptySlots+=1

	# Debug
	if winner == "X":
		pass
		#print("Joueur gagne")
	elif winner == "O":
		pass
		#print("IA gagne")
	elif(not canPlay() and winner == None):
		winner = "Tie"
		#print("Tie")

	return winner



def TicTacToe():
	wannaPlay = True
	while wannaPlay:
		joueur = 'X'
		compteur = 1
		gameFinished = False

		while not gameFinished:
			print(f"Tour {compteur} Joueur: {joueur}")
			#printBoard()

			isPositionOkay = True

			if(joueur == 'X'): # Joueur
				while isPositionOkay:
					printBoard()
					userInput = input("Veuillez selectionner une position i,j (entre 1 et 3) pour valider votre tour !\n")
					if ',' in userInput:
						moveI = int(userInput.split(',')[0])
						moveJ = int(userInput.split(',')[1])
						if moveI in [1,2,3] and moveJ in [1,2,3]:
							moveI, moveJ = moveI -1, moveJ -1
							if theBoard[moveI][moveJ] == '-':
								isPositionOkay = False
						if(not isPositionOkay):
							theBoard[moveI][moveJ] = joueur
							compteur += 1
							gameFinished = gameState(theBoard,joueur)
						else:
							print("Position déjà prise")
			else: # IA
				printBoard()
				bestMove()
				gameFinished = gameState(theBoard,joueur)

			if joueur == 'X':
				joueur = 'O'
			else:
				joueur = 'X'
		goodInput = True
		while goodInput:
			restart = input("Voulez-vous rejouer ? [O/N]\n")
			if restart.upper() in ['O','N']:
				if restart == 'O':
					goodInput = False
					reset()
				else:
					goodInput = False
					wannaPlay = False


TicTacToe()
