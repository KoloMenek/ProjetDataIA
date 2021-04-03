theBoard = [
	['-', '-', '-'],
	['-', '-', '-'],
	['-', '-', '-']
]

def printBoard():
	affichage = "  _   _   _\n"
	affichage += f"| {theBoard[0][0]} | {theBoard[0][1]} | {theBoard[0][2]} |\n"
	affichage += f"| {theBoard[1][0]} | {theBoard[1][1]} | {theBoard[1][2]} |\n"
	affichage += f"| {theBoard[2][0]} | {theBoard[2][1]} | {theBoard[2][2]} |\n"
	affichage += "  _   _   _\n"
	print(affichage)

printBoard() 