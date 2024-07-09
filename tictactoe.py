current_grid = [1, 1, 1, 1, 1, 1, 1, 1, 1]
straight_lines = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]]
occupied_pos = []
is_game_over = False


def display_grid():
    print("\n********************************\nCurrent Grid:\n")
    print(current_grid[0], current_grid[1], current_grid[2], "\n")
    print(current_grid[3], current_grid[4], current_grid[5], "\n")
    print(current_grid[6], current_grid[7], current_grid[8], "\n")


def take_input_X():
    while True:
        X = int(input("\nEnter the location on which you want X:\n1 2 3\n4 5 6\n7 8 9\n: "))

        if X not in occupied_pos:
            occupied_pos.append(X)
            break
        else:
            print("Location already occupied! Please select a different location:")
    
    current_grid[X - 1] = "X"


def take_input_O():
    while True:
        O = int(input("\nEnter the location on which you want O:\n1 2 3\n4 5 6\n7 8 9\n: "))

        if O not in occupied_pos:
            occupied_pos.append(O)
            break
        else:
            print("Location already occupied! Please select a different location:")
    
    current_grid[O - 1] = "O"


def check_for_straight_line():
    global is_game_over
    for i in straight_lines:
        if current_grid[i[0] - 1] == current_grid[i[1] - 1] == current_grid[i[2] - 1] == "X":
            print("X wins the game!")
            is_game_over = True
            
        elif current_grid[i[0] - 1] == current_grid[i[1] - 1] == current_grid[i[2] - 1] == "O":
            print("O wins the game!")
            is_game_over = True


while True:
    display_grid()
    take_input_X()
    display_grid()
    check_for_straight_line()
    if is_game_over:
        break

    display_grid()
    take_input_O()
    display_grid()
    check_for_straight_line()
    if is_game_over:
        break
