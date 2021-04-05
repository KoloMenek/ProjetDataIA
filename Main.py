theBoard = [
	['-', '-', '-'],
	['-', '-', '-'],
	['-', '-', '-']
]

boardStates = []

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

def minimax(theBoard, isMaximisingPlayer, joueur):
	isGameFinished = gameState(theBoard, joueur)
	if isGameFinished:
		return True







def TicTacToe():
	wannaPlay = True
	while wannaPlay:
		joueur = 'X'
		compteur = 1
		gameFinished = False

		while not gameFinished:
			print(f"Tour {compteur} Joueur: {joueur}")
			printBoard()

			isPositionOkay = True
			if joueur == 'X':
				while isPositionOkay:
					#Joueur choisi sa position
					userInput = input("Veuillez selectionner une position i,j (entre 1 et 3) pour valider votre tour !\n")
					if ',' in userInput:
						moveI = int(userInput.split(',')[0])
						moveJ = int(userInput.split(',')[1])
						if moveI in [1,2,3] and moveJ in [1,2,3]:
							moveI, moveJ = moveI -1, moveJ -1
							if theBoard[moveI][moveJ] == '-':
								isPositionOkay = False
				theBoard[moveI][moveJ] = joueur
				compteur += 1
				gameFinished = gameState(theBoard,joueur)

			else:
				gameFinished = minimax(theBoard, True, joueur)

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
				else:
					goodInput = False
					wannaPlay = False


TicTacToe()
