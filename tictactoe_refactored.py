# Constants
X = "X"
O = "O"
EMPTY = "_"

# Global variables
current_grid = [EMPTY] * 9
straight_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Zero-indexed for consistency
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6]]
occupied_positions = []

def display_grid():
    """Display the current grid state."""
    print("\n********************************\nCurrent Grid:\n")
    print(current_grid[0], current_grid[1], current_grid[2], "  1 2 3")
    print(current_grid[3], current_grid[4], current_grid[5], "  4 5 6")
    print(current_grid[6], current_grid[7], current_grid[8], "  7 8 9")

def take_input():
    """Take input from the player for their move."""
    while True:
        try:
            pos = int(input(f"\nEnter the location on which you want to place your marker (1-9): "))
            if pos < 1 or pos > 9:
                print("Invalid input! Please enter a number between 1 and 9.")
            elif pos - 1 in occupied_positions:
                print("Location already occupied! Please select a different location.")
            else:
                return pos - 1
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def update_grid(pos, player):
    """Update the grid with the player's move."""
    current_grid[pos] = player
    occupied_positions.append(pos)

def check_for_winner(player):
    """Check if the given player has won the game."""
    for line in straight_lines:
        if all(current_grid[pos] == player for pos in line):
            return True
    return False

def check_for_draw():
    """Check if the game is a draw."""
    return len(occupied_positions) == 9

# Main game loop
def play_game():
    while True:
        display_grid()
        update_grid(take_input(), X)
        if check_for_winner(X):
            display_grid()
            print("X wins the game!")
            break
        if check_for_draw():
            display_grid()
            print("It's a draw!")
            break

        display_grid()
        update_grid(take_input(), O)
        if check_for_winner(O):
            display_grid()
            print("O wins the game!")
            break
        if check_for_draw():
            display_grid()
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
