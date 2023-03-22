class Piece:
    def __init__(self, coor):
        self.coor = coor
        self.color = color
    def set_color(self):
        if self.coor.r == 0 or self.coor.r == 1: # 1e ou 2e ligne (haut->bas)
            self.color = "n" # NOIR
        elif self.coor.r == 7 or self.coor.r == 6: # 8e ou 7e ligne (haut->bas)
            self.color = "b" # BLANC
        
class Pawn(Piece):
    def __init__(self, coor):
        super().__init__(coor)
        self.name = 'pawn'
        self.type=1

class Knight(Piece):
    def __init__(self, coor):
        super().__init__(coor)
        self.name = 'knight'
        self.type=2
        

class Bishop(Piece):
    def __init__(self, coor):
        super().__init__(coor)
        self.name = 'bishop'
        self.type=3
        

class Rook(Piece):
    def __init__(self, coor):
        super().__init__(coor)
        self.name = "rook"
        self.type=4

class King(Piece):
    def __init__(self, coor, color):
        super().__init__(coor)
        self.name = "king"
        self.type=5

class Queen(Piece):
    def __init__(self, coor, color):
        super().__init__(coor)
        self.name = "queen"
        self.type=6