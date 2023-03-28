class Piece:

    def __init__(self, pos):
        self.pos = pos  # [rowNumber, colNumber]

    def set_color(self):
        # 1st or 2nd line (top -> bottom)
        if self.pos[0] == 0 or self.pos[0] == 1:
            return "b"  # BLACK
        elif self.pos[0] == 7 or self.pos[
                0] == 6:  # 8th ou 7th line (top -> bottom)
            return "w"  # WHITE


class Pawn(Piece):

    def __init__(self, pos):
        super().__init__(pos)
        self.name = 'pawn'
        self.type = 1
        self.color = self.set_color()
        if self.color == "b":
            self.symbol = "♟"
        elif self.color == "w":
            self.symbol = "♙"
        else:
            print("Error: wrong (color) value.")


class Knight(Piece):

    def __init__(self, pos):
        super().__init__(pos)
        self.name = 'knight'
        self.type = 2
        self.color = self.set_color()
        if self.color == "b":
            self.symbol = "♞"
        elif self.color == "w":
            self.symbol = "♘"
        else:
            print("Error: wrong (color) value.")


class Bishop(Piece):

    def __init__(self, pos):
        super().__init__(pos)
        self.name = 'bishop'
        self.type = 3
        self.color = self.set_color()
        if self.color == "b":
            self.symbol = "♝"
        elif self.color == "w":
            self.symbol = "♗"
        else:
            print("Error: wrong (color) value.")


class Rook(Piece):

    def __init__(self, pos):
        super().__init__(pos)
        self.name = "rook"
        self.type = 4
        self.color = self.set_color()
        if self.color == "b":
            self.symbol = "♜"
        elif self.color == "w":
            self.symbol = "♖"
        else:
            print("Error: wrong (color) value.")


class King(Piece):

    def __init__(self, pos):
        super().__init__(pos)
        self.name = "king"
        self.type = 5
        self.color = self.set_color()
        self.on_check = False
        if self.color == "b":
            self.symbol = "♚"
        elif self.color == "w":
            self.symbol = "♔"
        else:
            print("Error: wrong (color) value.")

    def get_valid_moves(self):
        return [[self.pos[0]+1, self.pos[1]], [self.pos[0]-1, self.pos[1]], [self.pos[0], self.pos[1]+1], [self.pos[0], self.pos[1]-1], [
            self.pos[0]+1, self.pos[1]+1], [self.pos[0]-1, self.pos[1]-1], [self.pos[0]+1, self.pos[1]-1], [self.pos[0]-1, self.pos[1]+1]]


class Queen(Piece):

    def __init__(self, pos):
        super().__init__(pos)
        self.name = "queen"
        self.type = 6
        self.color = self.set_color()
        if self.color == "b":
            self.symbol = "♛"
        elif self.color == "w":
            self.symbol = "♕"
        else:
            print("Error: wrong (color) value.")
