from chessboard import Board

b = Board()

for x in range(len(b.matrix)):
  for i in range(len(b.matrix[x])):
    if not None:
      print(b.matrix[x][i].color)
    else:
      print("None")