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

# check_board()
# visualize_board()

# b.move(b.matrix[6][1], [5, 1])

b.move(b.matrix[6][3], [5, 3])
b.move(b.matrix[1][3], [2, 3])
b.move(b.matrix[7][2], [2, 7])
b.move(b.matrix[1][6], [2, 6])
b.move(b.matrix[2][7], [0, 5])
b.move(b.matrix[1][0], [2, 0])
b.move(b.matrix[0][5], [1, 4])
visualize_board()
