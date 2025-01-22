class GameToken:
    def __init__(self, type):
        self.type = type
        self.position = (0,0)
        self.button = None

    def move(self, steps):
        row,col = self.position
        new_position = (row+steps, col + steps)
        return new_position
    
    