from collections import defaultdict


class Knight:
    possible_positions = set()

    def __init__(self, row, col):
        self.moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

        self.position = (row, col)

    def get_possible_moves(self, board: list) -> dict:
        possible_moves = defaultdict(int)
        row, col = self.position
        nb_rows = len(board)
        nb_cols = len(board[0])
        for move_row, move_col in self.moves:
            new_move_row, new_move_col = move_row + row, move_col + col
            if (-nb_rows <= new_move_row < 0) and (0 <= new_move_col < nb_cols):
                for row_, col_ in self.moves:
                    if (-nb_rows <= new_move_row + row_ < 0) and (0 <= new_move_col + col_ < nb_cols) and "*" not in \
                            board[new_move_row + row_][new_move_col + col_]:
                        possible_moves[(new_move_row, new_move_col)] = possible_moves[(new_move_row, new_move_col)] + 1

                    else:
                        possible_moves[(new_move_row, new_move_col)] = possible_moves[(new_move_row, new_move_col)]
        return possible_moves


class Grid:
    def __init__(self, col: int, row: int) -> None:
        self.ROW = row
        self.COL = col
        self.placeholder = len(str(row * col))
        self.BOARD_BORDER_LEN = self.COL * (self.placeholder + 1) + 3
        self.board = [[self.placeholder * "_" for _ in range(self.COL)] for _ in range(self.ROW)]

    def __str__(self) -> str:
        print_string = f'{"  " if self.ROW >= 10 else " "}{"-" * self.BOARD_BORDER_LEN}\n'
        for i in range(len(self.board)):
            print_string += f'{" " if len(self.board) - i < 10 <= self.COL else ""}{len(self.board) - i}| ' + " ".join(
                self.board[i]) + ' |\n'
        print_string += f' {"-" * self.BOARD_BORDER_LEN}\n'
        print_string += f'{" " if len(self.board) - 1 < 10 <= self.COL else ""}{"  " if self.COL < 10 else "  "} ' + \
                        " ".join(
                            [(self.placeholder - len(str(i + 1))) * " " + str(i + 1) for i in range(self.COL)]) + '  '
        return print_string

    def write_on_board(self, x: int, y: int, symbol: str) -> None:
        tmp = list(self.board[x][y])
        tmp[-1] = symbol
        self.board[x][y] = "".join(tmp).replace("_", " ") if "*" not in self.board[x][y] else self.board[x][y]

    def reset_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].strip().isdigit():
                    self.board[i][j] = self.placeholder * "_"


def setup_grid() -> (int, int):
    invalid_dimension_msg = "Invalid dimensions!"

    while True:
        try:
            col, row = input("Enter your board dimensions:").split(" ")
            assert (col is not None and row is not None)
            assert (row.isdigit() and col.isdigit())
            assert (len(row) <= 2 and len(col) <= 2)
            assert (1 <= int(row) and 1 <= int(col))
        except Exception:
            print(invalid_dimension_msg)
        else:
            break
    return int(row), int(col)


def move_knight(input_msg: str) -> bool:
    global VISIT
    invalid_position_msg = "Invalid position!" if input_msg == start_msg else "Invalid move!"

    while True:
        try:
            k_col, k_row = input(input_msg).split(" ")
            assert (k_col is not None and k_row is not None)
            assert (k_row.isdigit() and k_col.isdigit())
            assert (len(k_row) <= 2 and len(k_col) <= 2)
            k_row, k_col = int(k_row), int(k_col)
            assert (1 <= k_row <= grid.ROW and 1 <= k_col <= grid.COL)
            if Knight.possible_positions and input_msg == next_move_msg:
                assert ((k_col, k_row) in Knight.possible_positions)
        except Exception:
            print(invalid_position_msg)
        else:
            k_row *= -1
            k_col -= 1
            break
    knight = Knight(k_row, k_col)
    VISIT += 1
    grid.write_on_board(k_row, k_col, "X")
    knight.possible_positions.clear()

    knight_moves = knight.get_possible_moves(grid.board)
    for row, col in knight_moves:
        if knight_moves[(row, col)] >= 0:
            grid.write_on_board(row, col, symbol=str(knight_moves[(row, col)] - 1))
            if "*" not in grid.board[row][col]:
                Knight.possible_positions.add((col + 1, row * -1))
    print(grid)
    grid.write_on_board(k_row, k_col, "*")
    grid.reset_board()
    print()

    return len(Knight.possible_positions) == 0


if __name__ == '__main__':

    grid_col, grid_row = setup_grid()
    grid = Grid(grid_row, grid_col)
    start_msg = "Enter the knight's starting position:"
    VISIT = 0
    move_knight(start_msg)

    next_move_msg = "Enter your next move:"

    while True:
        if move_knight(next_move_msg):
            if VISIT < grid_col * grid_row:
                print("No more possible moves!")
                print(f"Your knight visited {VISIT} squares!")
            else:
                print("What a great tour! Congratulations!")
            break
