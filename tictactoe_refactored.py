# Constants
X = "X"
O = "O"

# Global variables
current_grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Using numbers for initial visualization
straight_lines = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]]
occupied_pos = []


def display_grid():
    print("\n********************************\nCurrent Grid:\n")
    print(current_grid[0], current_grid[1], current_grid[2], "\n")
    print(current_grid[3], current_grid[4], current_grid[5], "\n")
    print(current_grid[6], current_grid[7], current_grid[8], "\n")


def take_input(player):
    while True:
        try:
            pos = int(input(f"\nEnter the location on which you want {player}:\n1 2 3\n4 5 6\n7 8 9\n: "))
            if pos in occupied_pos:
                print("Location already occupied! Please select a different location:")
            elif pos < 1 or pos > 9:
                print("Invalid input! Please enter a number between 1 and 9.")
            else:
                occupied_pos.append(pos)
                return pos
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def check_for_winner(player):
    for line in straight_lines:
        if all(current_grid[pos - 1] == player for pos in line):
            return True
    return False


def check_for_draw():
    return len(occupied_pos) == 9


while True:
    display_grid()
    X_pos = take_input(X)
    current_grid[X_pos - 1] = X
    if check_for_winner(X):
        display_grid()
        print("X wins the game!")
        break
    if check_for_draw():
        display_grid()
        print("It's a draw!")
        break

    display_grid()
    O_pos = take_input(O)
    current_grid[O_pos - 1] = O
    if check_for_winner(O):
        display_grid()
        print("O wins the game!")
        break
    if check_for_draw():
        display_grid()
        print("It's a draw!")
        break

