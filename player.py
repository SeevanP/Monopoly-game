class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def take_turn(self, dice,board):
        roll = dice.roll()
        self.token.move(roll)
        new_position = self.token.move(roll)
        board.move_token(self.token, new_position)