class Piece:
    def __init__(self, coor, color):
        self.coor = coor
        self.color = color
        
class Pawn(Piece):
    def __init__(self, coor, color):
        super().__init__(coor, color)
        self.name = 'pawn'
        self.type=1
        if color == 'b':
            self.symbol = '♙';
        elif color == 'n':
            self.symbol = '♟';
        else:
            print('Erreur: color doit etre "b" ou "n".')

class Knight(Piece):
    def __init__(self, coor, color):
        super().__init__(coor, color)
        self.name = 'knight'
        self.type=2
        if color == 'b':
            self.symbol = '♘';
        elif color == 'n':
            self.symbol = '♞';
        else:
            print('Erreur: color doit etre "b" ou "n".')