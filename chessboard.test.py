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
    print("  0 1 2 3 4 5 6 7", end="")
    for x in range(len(b.matrix)):
        print("\n")
        print(x, end=" ")
        for i in range(len(b.matrix[x])):
            if not b.matrix[x][i] == None:
                print(b.matrix[x][i].symbol, end=" ")
            else:
                print("-", end=" ")


###

# check_board()
# visualize_board()

# b.move(b.matrix[6][1], [5, 1])

b.move(b.matrix[6][4], [4, 4])
b.move(b.matrix[1][0], [3, 0])
b.move(b.matrix[7][4], [6, 4])

visualize_board()
