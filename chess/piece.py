# Generic piece
class Piece:
    type = ""

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.captured = False

    def move(x, y):
        self.x = x
        self.y = y

    def availableMoves(boardState):
        pass

    def capture():
        self.captured = True

# Pawn
class Pawn(Piece):
    type = "Pawn"
