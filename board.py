import tkinter as tk

class Board:
    def __init__(self, root):
        self.root = root
        self.create_board()

    def create_board(self):
        for col in range(10):
            self.root.grid_columnconfigure(col, weight=1)
        for row in range(10):
            self.root.grid_rowconfigure(row, weight=1)
            for col in range(10):
                if row in [0, 9] or col in [0, 9]:
                    tk.Button(self.root, text='R%s/C%s' % (row, col), width=20, height=10).grid(row=row, column=col)

    def add_token(self, token):
        token.button = tk.Button(self.root, text=token.type, width=10, height=5)
        token.button.grid(row=0, column=0)  # Initial position
        token.position = (0, 0)

    def move_token(self, token, new_position):
        token.button.grid(row=new_position[0], column=new_position[1])
        token.position = new_position