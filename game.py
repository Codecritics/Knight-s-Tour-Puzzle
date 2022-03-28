def draw_board(board): #draw actual board state with formatting - not used in later stages

    dash_bar()
    for i in range(b):
        print("".join([str(b - i).rjust(cell - 1), "|"]), " ".join(
            [str(board[i][j]).rjust(len(str(a * b)), "_") if board[i][j] == "_" else str(board[i][j]).rjust(len(str(a * b)), " ")
             for j in range(a)]), "|")
    dash_bar()
    print(" " * (len(str(a)) + 1), " ".join([(str(r + 1).rjust(cell)) for r in range(a)]))

def check_moves(): #marks available moves on the board

    count = 0
    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]  #movement vectors  [x, y]
    for i in range(8):
        #for j in range(2):
        if y + moves[i][0] > b or y + moves[i][0] < 0 or x + moves[i][1] > a or x + moves[i][1] < 0:
            continue
        else:
            try:
                if board[y + moves[i][0]][x + moves[i][1]] == "_":
                    board[y + moves[i][0]][x + moves[i][1]] = str(count_moves(y + moves[i][0], x + moves[i][1]))
                    count += 1
                    print(f"ok  {moves[i]}")

            except:
                continue

    dash_bar()
    for i in range(b):
        print("".join([str(b - i).rjust(cell - 1), "|"]), " ".join([str(board[i][j]).rjust(len(str(a * b)), "_") if board[i][j] == "_" else str(board[i][j]).rjust(len(str(a * b)), " ")  for j in range(a)]), "|")
    dash_bar()
    print(" " * (len(str(a))), " ".join([(str(r).rjust(cell)) for r in range(a)]))

    return count

def count_moves(y, x): #subfunciton for check_moves(), counts available moves from tiles determined in master function
    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    count = 0
    #print("x:",x , "y:", y)
    for i in range(8):
        #for j in range(2):
        if y + moves[i][0] > b or y + moves[i][0] < 0 or x + moves[i][1] > a or x + moves[i][1] < 0:
            continue
        else:
            try:
                if board[y + moves[i][0]][x + moves[i][1]] == "_":
                    count += 1
            except:
                continue
    return count

def dash_bar(): #draw top and bottom --- line
    print(" " * (cell - 1), "-" * ((len(str(a * b)) + 1) * a), "---", sep="")

def ask_board(): #ask user for board dimensions
    while True:
        dim = input("Enter your board dimensions: ")
        try:
            a, b = dim.split(" ", 1)
        except ValueError:
            print(invalid_dim)
            continue

        if a.isnumeric() == False or b.isnumeric() == False:
            print(invalid_dim)
            continue
        elif len(dim.split(" ")) != 2:
            print(invalid_dim)
            continue
        elif int(a) < 1 or int(b) < 1:
            print(invalid_dim)
            continue
        else:
            return int(a), int(b)

def ask_pos(): #ask user about knight's starting position

    while True:
        pos = input("Enter the knight's starting position: ")
        try:
            x, y = pos.split(" ", 1)
        except ValueError:
            print(invalid_pos)
            continue

        if x.isnumeric() == False or y.isnumeric() == False:
            print(invalid_pos, "num")
            continue
        elif len(pos.split(" ")) != 2:
            print(invalid_pos, "split err")
            continue
        elif int(x) not in range(1, a + 1) or int(y) not in range(1, b + 1):
            print(invalid_pos, "range 1 - b")
            continue
        else:
            return int(x) - 1, b - int(y)

def ask_move(): #ask user about knight's next move

    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    pos = input("Enter your next move: ")
    while True:

        try:
            x_move, y_move = pos.split(" ", 1)
        except ValueError:
            print(invalid_pos)
            continue

        if x_move.isnumeric() == False or y_move.isnumeric() == False:
            print(invalid_pos, "num")
            pos = input("Invalid move! Enter your next move: ")
            continue
        elif len(pos.split(" ")) != 2:
            print(invalid_pos, "split err")
            pos = input("Invalid move! Enter your next move: ")
            continue
        elif int(x_move) not in range(1, a + 1) or int(y_move) not in range(1, b + 1):
            print(invalid_pos, "range 1 - b")
            pos = input("Invalid move! Enter your next move: ")
            continue
        else:
            x_move, y_move = int(x_move) - 1, b - int(y_move)
            for i in range(8):
                if y + moves[i][0] == y_move and x + moves[i][1] == x_move and y + moves[i][0] <= b and y + moves[i][0] >= 0 and x + moves[i][1] <= a and x + moves[i][1] >= 0 and board[y_move][x_move] != "X":
                    board[y_move][x_move] = "X"
                    print()
                    board[y][x] = "*"
                    return x_move, y_move

        pos = input("Invalid move! Enter your next move: ")

def solve():
    auto_board = [[-1 for i in range(a)] for j in range(b)]

    #first tile starts at #1
    auto_board[y][x] = 1
    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]  #movement vectors table [y, x]

    #next tile is #2
    steps = 2

    #checking if solution exists or not
    if (not next_move(auto_board, x, y, moves, steps)):
        print("No solution exists!")
        return False
    else:
        if choice == "n":
            print("Here's the solution!")
            draw_board(auto_board)

def next_move(board, x, y, moves, steps): #checking if valid route exists and passing it if it does
    if (steps == int(a) * int(b) + 1):
        return True


    for i in range(8):
        new_x = x + moves[i][1]
        new_y = y + moves[i][0]
        if y + moves[i][0] < b and y + moves[i][0] >= 0 and x + moves[i][1] < a and x + moves[i][1] >= 0 and board[new_y][new_x] == -1:
            board[new_y][new_x] = steps

            if (next_move(board, new_x, new_y, moves, steps + 1)):
                return True

            #backtracking
            board[new_y][new_x] = -1
    return False

def board_clean():
    for i in range(b):
        for j in range(a):
            if board[i][j] in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
                board[i][j] = "_"

def start():
    answer = input("Do you want to try the puzzle? (y/n): ")
    while answer != "y" and answer != "n":
        if answer != "y" and answer != "n":
            print(invalid_input)
        answer = input("Do you want to try the puzzle? (y/n): ")
    return answer

#starting setup

#errors
invalid_dim = "Invalid dimensions!"
invalid_pos = "Invalid position!"
no_solution = "No solution exists!"
invalid_input = "Invalid input!"

#getting board dimensions and knight's starting position

a, b = ask_board()

x, y = ask_pos()
cell = len(str(b)) + 1  # calculates cell width for drawing board

squares = 1
available_moves = 0

choice = start()

board = [["_" for _ in range(a)] for _ in range(b)]

if choice == "y": #manual gameplay
    board[y][x] = "X"

    if solve() == False:
        pass
    else:
        while True:
            board_clean()
            available_moves = check_moves()
            print(f"squares: {squares}")
            if available_moves == 0:
                if squares == a * b:
                    print("What a great tour! Congratulations!")
                    break
                else:
                    print("No more possible moves!")
                    print(f"Your knight visited {squares} squares!")
                    break
            else:
                squares += 1
            x, y = ask_move()
else: #automated solution
    solve()

