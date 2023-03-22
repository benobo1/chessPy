from chessboard import Board

b = Board()
b.populate()


def check_board():
  for x in range(len(b.matrix)):
    for i in range(len(b.matrix[x])):
      if not b.matrix[x][i] == None:
        print(
          f"r: {x}, c: {i} / color: {b.matrix[x][i].color} / name: {b.matrix[x][i].name} / type: {b.matrix[x][i].type}"
        )
      else:
        print(None)


def visualize_board():
  for x in range(len(b.matrix)):
    print("\n")
    for i in range(len(b.matrix[x])):
      if not b.matrix[x][i] == None:
        print(b.matrix[x][i].symbol, end=" ")
      else:
        print("-", end=" ")


###

#check_board()
#visualize_board()

visualize_board()

b.move(b.matrix[6][1], [5, 1])
visualize_board()
print(f"\nCurrent turn: {b.current_turn}")
print(f"Currently playing color: {b.playing_color}")

b.move(b.matrix[1][4], [3, 4])
visualize_board()
print(f"\nCurrent turn: {b.current_turn}")
print(f"Currently playing color: {b.playing_color}")