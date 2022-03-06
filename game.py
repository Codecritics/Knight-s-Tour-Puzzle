class Grid:

    def __init__(self, col: int, row: int) -> None:
        self.ROW = row
        self.COL = col
        self.placeholder = len(str(row * col))
        self.knight_position = (0, 0)
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
        self.knight_position = (x, y)

    def set_knight_possible_moves(self) -> None:
        row, col = self.knight_position

        move_left_up = (row - 1, col - 2)
        move_left_down = (row + 1, col - 2)
        move_up_left = (row - 2, col - 1)
        move_up_right = (row - 2, col + 1)
        move_right_up = (row - 1, col + 2)
        move_right_down = (row + 1, col + 2)
        move_down_left = (row + 2, col - 1)
        move_down_right = (row + 2, col + 1)

        print(self.warnsdorff_rule(row - 1, col - 2))

        possibilities = [move_left_up, move_left_down, move_up_left, move_up_right, move_right_up, move_right_down,
                         move_down_left, move_down_right]
        for row_possibility, col_possibility in possibilities:
            if 1 <= abs(row_possibility) <= self.ROW and 0 <= col_possibility < self.COL:
                self.write_on_board(row_possibility, col_possibility,
                                    str(self.warnsdorff_rule(row_possibility, col_possibility)))

    def warnsdorff_rule(self, row, col):
        counter = -1
        move_left_up = (row - 1, col - 2)
        move_left_down = (row + 1, col - 2)
        move_up_left = (row - 2, col - 1)
        move_up_right = (row - 2, col + 1)
        move_right_up = (row - 1, col + 2)
        move_right_down = (row + 1, col + 2)
        move_down_left = (row + 2, col - 1)
        move_down_right = (row + 2, col + 1)
        possibilities = [move_left_up, move_left_down, move_up_left, move_up_right, move_right_up, move_right_down,
                         move_down_left, move_down_right]
        for row_possibility, col_possibility in possibilities:
            if (-self.ROW <= row_possibility < 0) and 0 <= col_possibility < self.COL:
                counter += 1

        return counter


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

    grid.write_on_board(knight_row, knight_col, "X")
    grid.set_knight_possible_moves()
    print(grid)
