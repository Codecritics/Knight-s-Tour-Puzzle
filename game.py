if __name__ == '__main__':
    GRID_SIZE = 8
    grid = [['_' for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

    try:
        knight_starting_position = input("Enter the knight's starting position:")
        message = "Invalid dimensions!"
        assert (len(knight_starting_position.split(" ")) == 2 and 1 <= int(
            knight_starting_position.split(" ")[0]) <= GRID_SIZE and
                1 <= int(knight_starting_position.split(" ")[1]) <= GRID_SIZE), message
    except Exception as err:
        print(err)
    else:
        y_coordinate, x_coordinate = knight_starting_position.split(" ")
        x_coordinate = len(grid) - int(x_coordinate)
        y_coordinate = int(y_coordinate) - 1

        grid[x_coordinate][y_coordinate] = "X"

        print("", "-" * 19)
        line_grid = " ".join(["_"] * GRID_SIZE)
        for i in range(len(grid)):
            print(f'{len(grid) - i}|', " ".join(grid[i]), '|')
        print("", "-" * 19)
        print("   ", " ".join([f'{i}' for i in range(1, GRID_SIZE + 1)]))
