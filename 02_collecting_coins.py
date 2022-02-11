"""
2.	Collecting Coins

You are playing a game, and your goal is to collect 100 coins.
On the first line, you will be given a number representing the size of the field with a square shape. On the following few lines, you will be given the field with:
•	One player - randomly placed in it and marked with the symbol "P"
•	Numbers for coins placed at different positions of the field
•	Walls marked with "X"
After the field state, you will be given commands for the player's movement. Commands can be: "up", "down", "left", "right".
The player moves in the given direction with one step for each command and collects all the coins that come across. If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.
Note: He can go through the same path many times, but he can collect the coins just once (the first time).
There are only two possible outcomes of the game:
•	The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest integer number.
•	The player collects at least 100 coins and wins the game.
For more clarifications, see the examples below.
Input
•	A number representing the size of the field (matrix NxN)
•	A matrix representing the field (each position separated by a single space)
•	On each of the following lines, you will get a move command
•	The input will always be in the correct format
Output
•	If the player won the game, print: "You won! You've collected {total_coins} coins."
•	If the player loses the game, print: "Game over! You've collected {total_coins} coins."
•	Collected coins have to be rounded down to the next-lowest number.
•	The player's path as cooridnates in lists on separate lines:
"Your path:
[{row_position1}, {column_position1}]
[{row_position2}, {column_position2}]
…
[{row_positionN}, {column_positionN}]"
Constrains
•	There will be no case in which less than 100 coins will be in the field
•	All given numbers will be valid integers in the range [0, 100]
"""


def calculate_position(ma, row, col):
    if row < 0:
        row = len(ma) - 1
    if col < 0:
        col = len(ma) - 1
    if row >= len(ma):
        row = 0
    if col >= len(ma):
        col = 0
    return row, col


n = int(input())

matrix = []
player_position = []

for row_index in range(n):
    row_data = input().split()
    if 'P' in row_data:
        player_position = [row_index, row_data.index('P')]
    matrix.append(row_data)

player_path = []
coins = 0
is_winner = True

player_path.append(player_position)
while coins < 100:
    command = input()
    current_row, current_col = player_position
    if command == "up":
        row, col = calculate_position(matrix, current_row - 1, current_col)
    elif command == "down":
        row, col = calculate_position(matrix, current_row + 1, current_col)
    elif command == "right":
        row, col = calculate_position(matrix, current_row, current_col + 1)
    elif command == "left":
        row, col = calculate_position(matrix, current_row, current_col - 1)

    # TODO refactor repetitive code
    matrix[current_row][current_col] = '0'
    if matrix[row][col] == "X":
        player_path.append([row, col])
        is_winner = False
        coins //= 2
        print(f"Game over! You've collected {coins} coins.")
        break
    coins += int(matrix[row][col])
    matrix[row][col] = 'P'
    player_position = [row, col]
    player_path.append(player_position)

if is_winner:
    print(f"You won! You've collected {coins} coins.")

print("Your path:")
[print(step) for step in player_path]
