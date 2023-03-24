from pieces import Pawn, Knight, Bishop, Rook, King, Queen


class Board:

  def __init__(self):
    self.current_turn = 1
    self.playing_color = "w"
    self.white_on_check = False
    self.black_on_check = False
    self.matrix = [[None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None]]

  def is_on_check(self):
    if self.white_on_check or self.black_on_check:
      return True
    else:
      return False

  def is_valid_pawn_move(self, Piece, new_pos):
    if Piece.color == "b":
      if self.matrix[Piece.pos[0] + 1][
          Piece.pos[1]] == None and new_pos[0] == Piece.pos[0] + 1 and new_pos[
            1] == Piece.pos[1]:  # moving straight 1 case logic
        return True
      elif Piece.pos[0] == 1 and new_pos[0] == 3 and Piece.pos[1] == new_pos[
          1]:  # Moving straight 2 cases logic
        return True
      elif self.matrix[new_pos[0]][new_pos[1]] != None and self.matrix[
          new_pos[0]][new_pos[1]].color == "w":
        if Piece.pos[0] + 1 == new_pos[0] and Piece.pos[1] + 1 == new_pos[
            1]:  # Take Piece logic
          return True
        elif Piece.pos[0] + 1 == new_pos[0] and Piece.pos[1] - 1 == new_pos[
            1]:  # Take Piece logic
          return True
        else:
          return False
      else:
        return False
    elif Piece.color == "w":
      if self.matrix[Piece.pos[0] - 1][
          Piece.pos[1]] == None and new_pos[0] == Piece.pos[0] - 1 and new_pos[
            1] == Piece.pos[1]:  # moving straight logic
        return True
      elif Piece.pos[0] == 6 and new_pos[0] == 4 and Piece.pos[1] == new_pos[
          1]:  # Moving straight 2 cases logic
        return True
      elif self.matrix[new_pos[0]][new_pos[1]] != None and self.matrix[
          new_pos[0]][new_pos[1]].color == "b":
        if Piece.pos[0] - 1 == new_pos[0] and Piece.pos[1] + 1 == new_pos[
            1]:  # Take Piece logic
          return True
        elif Piece.pos[0] - 1 == new_pos[0] and Piece.pos[1] - 1 == new_pos[
            1]:  # Take Piece logic
          return True
        else:
          return False
      else:
        return False
    else:
      print("Error: wrong Piece.color value.")

  def is_valid_knight_move(self, Piece, new_pos):
    if Piece.color == "b":
      if self.matrix[new_pos[0]][new_pos[1]] == None or self.matrix[
          new_pos[0]][new_pos[
            1]].color == "w":  # Only moves on empty cases or those with opponent's pieces.
        if (new_pos[0] == Piece.pos[0] + 1 and
            (new_pos[1] == Piece.pos[1] + 2 or new_pos[1] == Piece.pos[1] - 2)
            ) or (new_pos[0] == Piece.pos[0] + 2 and
                  (new_pos[1] == Piece.pos[1] + 1
                   or new_pos[1] == Piece.pos[1] - 1)) or (
                     new_pos[0] == Piece.pos[0] - 1 and
                     (new_pos[1] == Piece.pos[1] + 2
                      or new_pos[1] == Piece.pos[1] - 2)) or (
                        new_pos[0] == Piece.pos[0] - 2 and
                        (new_pos[1] == Piece.pos[1] + 1 or new_pos[1]
                         == Piece.pos[1] - 1)):  # Knight movement logic
          return True
    elif Piece.color == "w":
      if self.matrix[new_pos[0]][new_pos[1]] == None or self.matrix[
          new_pos[0]][new_pos[
            1]].color == "b":  # Only moves on empty cases or those with opponent's pieces.
        if (new_pos[0] == Piece.pos[0] + 1 and
            (new_pos[1] == Piece.pos[1] + 2 or new_pos[1] == Piece.pos[1] - 2)
            ) or (new_pos[0] == Piece.pos[0] + 2 and
                  (new_pos[1] == Piece.pos[1] + 1
                   or new_pos[1] == Piece.pos[1] - 1)) or (
                     new_pos[0] == Piece.pos[0] - 1 and
                     (new_pos[1] == Piece.pos[1] + 2
                      or new_pos[1] == Piece.pos[1] - 2)) or (
                        new_pos[0] == Piece.pos[0] - 2 and
                        (new_pos[1] == Piece.pos[1] + 1 or new_pos[1]
                         == Piece.pos[1] - 1)):  # Knight movement logic
          return True
    else:
      return False

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
          return self.is_valid_pawn_move(Piece, new_pos)
        elif Piece.type == 2:  # Knight
          return self.is_valid_knight_move(Piece, new_pos)
        elif Piece.type == 3:  # Bishop
          return True
        elif Piece.type == 4:  # Rook
          return True
        elif Piece.type == 6:  # Queen
          return True
        elif Piece.type == 5:  # King
          return True
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
      Piece.pos = new_pos
      if self.playing_color == "w":
        self.playing_color = "b"
      elif self.playing_color == "b":
        self.current_turn += 1
        self.playing_color = "w"
