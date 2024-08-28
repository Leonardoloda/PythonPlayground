from constants import EMPTY, X, O
from square import Square

grid = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]

for index_row, row in enumerate(grid):
    for index_col, col in enumerate(grid):
        grid[index_row][index_col] = Square(index_row, index_col, EMPTY)

has_winner = False


def get_next_turn(current_turn):
    return O if current_turn == X else X


def pretty_print(grid):
    for row in grid:
        print(" | ".join(map(str, row)))


def check_winner(grid):
    if grid[0][0].value == grid[0][1].value == grid[0][2].value and grid[0][0].value != EMPTY and grid[0][
        1].value != EMPTY and grid[0][2].value != EMPTY:
        return True

    if grid[1][0].value == grid[1][1].value == grid[1][2].value and grid[1][0].value != EMPTY and grid[1][
        0].value != EMPTY and grid[1][2].value != EMPTY and grid[1][2].value != EMPTY:
        print("Won middle column")
        return True

    if grid[2][0].value == grid[2][1].value == grid[2][2].value and grid[2][0].value != EMPTY and grid[2][
        0].value != EMPTY and grid[2][2].value != EMPTY and grid[2][2].value != EMPTY:
        print("Won bottom row")
        return True

    if grid[0][0].value == grid[1][1].value == grid[2][2].value and grid[0][0].value != EMPTY and grid[0][
        0].value != EMPTY and grid[1][1].value != EMPTY:
        print("Won left diagonal")
        return True

    if grid[0][2].value == grid[1][1].value == grid[2][0].value and grid[0][0].value != EMPTY and grid[0][
        2].value != EMPTY and grid[0][2].value != EMPTY and grid[0][2].value != EMPTY:
        print("Won right diagonal")
        return True


current_turn = X

while not has_winner:
    print(f"It's your turn {current_turn}")

    target_row = int(input("What's the row you wanna target?\n"))
    target_col = int(input("What's the column you wanna target?\n"))

    if grid[target_row][target_col].value == EMPTY:
        grid[target_row][target_col].value = current_turn
    else:
        print("Row already there, F")

    has_winner = check_winner(grid)

    current_turn = get_next_turn(current_turn)

    pretty_print(grid)

print(f"Congrats {current_turn}! you've won")
