from collections import defaultdict


class Knight:
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
            possible_moves[(new_move_row, new_move_col)] = 0
            if (-nb_rows <= new_move_row < 0) and (0 <= new_move_col < nb_cols):
                for row_, col_ in self.moves:
                    possible_moves[(new_move_row, new_move_col)] = possible_moves[(new_move_row, new_move_col)] + 1 \
                        if (-nb_rows <= new_move_row + row_ < 0) and (0 <= new_move_col + col_ < nb_cols) \
                        else possible_moves[(new_move_row, new_move_col)]
        return possible_moves


class Grid:
    def __init__(self, col: int, row: int) -> None:
        self.ROW = row
        self.COL = col
        self.placeholder = len(str(row * col))
        self.BOARD_BORDER_LEN = self.COL * (self.placeholder + 1) + 3
        self.board = [[self.placeholder * "_" for _ in range(self.COL)] for _ in range(self.ROW)]

    def __str__(self) -> str:
        print_string = "\nHere are the possible moves:\n"
        print_string += f'{"  " if self.ROW >= 10 else " "}{"-" * self.BOARD_BORDER_LEN}\n'
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
        self.board[x][y] = "".join(tmp).replace("_", " ")


def setup_grid() -> (int, int):
    invalid_dimension_msg = "Invalid dimensions!"

    while True:
        try:
            col, row = input("Enter your board dimensions:").split(" ")
            assert (col is not None and row is not None)
            assert (row.isdigit() and col.isdigit())
            assert (len(row) <= 2 and len(col) <= 2)
        except Exception:
            print(invalid_dimension_msg)
        else:
            break
    return int(row), int(col)


if __name__ == '__main__':

    grid_col, grid_row = setup_grid()
    grid = Grid(grid_row, grid_col)
    invalid_position_msg = "Invalid position!"

    while True:
        try:
            knight_col, knight_row = input("Enter the knight's starting position:").split(" ")
            assert (knight_col is not None and knight_row is not None)
            assert (knight_row.isdigit() and knight_col.isdigit())
            assert (len(knight_row) <= 2 and len(knight_col) <= 2)
            knight_row, knight_col = int(knight_row), int(knight_col)
            assert (1 <= knight_row <= grid.ROW and 1 <= knight_col <= grid.COL)
        except Exception:
            print(invalid_position_msg)
        else:
            knight_row *= -1
            knight_col -= 1
            break

    knight = Knight(knight_row, knight_col)
    grid.write_on_board(knight_row, knight_col, "X")
    knight_moves = knight.get_possible_moves(grid.board)
    for knight_move in knight_moves:
        if knight_moves[knight_move] > 0:
            grid.write_on_board(*knight_move, symbol=str(knight_moves[knight_move] - 1))
    print(grid)
