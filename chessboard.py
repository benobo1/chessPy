from pieces import Pawn, Knight, Bishop, Rook, King, Queen


class Board:

  def __init__(self):
    self.current_turn = 1
    self.playing_color = "w"
    self.matrix = [[None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None]]

  def populate(self):
    for x in range(len(self.matrix)):
      if x == 0 or x == 7:  # For the first line of both W&B
        self.matrix[x][0] = Rook([x, 0])  # 0: row, 1: column
        self.matrix[x][1] = Knight([x, 1])
        self.matrix[x][2] = Bishop([x, 2])
        self.matrix[x][3] = Queen([x, 3])
        self.matrix[x][4] = King([x, 4])
        self.matrix[x][5] = Bishop([x, 5])
        self.matrix[x][6] = Knight([x, 6])
        self.matrix[x][7] = Rook([x, 7])
      elif x == 1 or x == 6:  # For the second line of both W&B
        for i in range(len(self.matrix[x])):
          self.matrix[x][i] = Pawn([x, i])

  def is_valid_move(self, Piece, new_pos):
    if new_pos[0] >= 0 and new_pos[0] <= 7 and new_pos[1] >= 0 and new_pos[
        1] <= 7:  # avoid board overflow
      if Piece != None and Piece.color == self.playing_color:
        if Piece.type == 1:  # Pawn
          if Piece.color == "b":
            if self.matrix[Piece.pos[0] + 1][Piece.pos[1]] == None and new_pos[
                0] == Piece.pos[0] + 1 and new_pos[1] == Piece.pos[
                  1]:  # moving straight logic
              return True
            else:
              return False
          elif Piece.color == "w":
            if self.matrix[Piece.pos[0] - 1][Piece.pos[1]] == None and new_pos[
                0] == Piece.pos[0] - 1 and new_pos[1] == Piece.pos[
                  1]:  # moving straight logic
              return True
            else:
              return False
        else:
          return False
      else:
        return False
    else:
      return False

  def move(self, Piece, new_pos):  # new_pos (list): [row, col]
    if self.is_valid_move(Piece, new_pos):
      self.matrix[new_pos[0]][new_pos[1]] = Piece
      self.matrix[Piece.pos[0]][Piece.pos[1]] = None
      if self.playing_color == "w":
        self.playing_color = "b"
      elif self.playing_color == "b":
        self.current_turn += 1
        self.playing_color = "w"
