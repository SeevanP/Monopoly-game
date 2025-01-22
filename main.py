import tkinter as tk
from board import Board
from dice import Dice
from game_token import GameToken
from player import Player

# Initialize the main window
root = tk.Tk()
root.title("My_Monopoly_Game")
root.geometry("500x500")

# Initialize game components
board = Board(root)
dice = Dice()
players = [Player("Player 1", GameToken("Car")), Player("Player 2", GameToken("Hat"))]

for player in players:
    board.add_token(player.token)

# Start the Tkinter event loop
root.mainloop()