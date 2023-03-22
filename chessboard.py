from pieces import Pawn, Knight, Bishop, Rook, King, Queen

class Board:
  def __init__(self):
    self.matrix = [
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None]
    ]
  def populate_board(self):
    for x in range(len(self.matrix)):
      if x==0 or x==7: # Pour la première rangée des noirs & blancs
          self.matrix[x][0] = Rook({r:x, c:0}) # r: row, c: column
          self.matrix[x][1] = Knight({r:x, c:1})
          self.matrix[x][2] = Bishop({r:x, c:2})
          self.matrix[x][3] = Queen({r:x, c:3})
          self.matrix[x][4] = King({r:x, c:4})
          self.matrix[x][5] = Bishop({r:x, c:5})
          self.matrix[x][6] = Knight({r:x, c:6})
          self.matrix[x][7] = Rook({r:x, c:7})
      elif x==1 or x==6: # Pour la seconde rangée des noir & blancs
        for i in range(len(self.matrix[x])):
          self.matrix[x][i] = Pawn({r:x, c:i})