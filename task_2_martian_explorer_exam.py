rows = 6
cols = 6

matrix = []

water = 0
metal = 0
concrete = 0


def next_position(direction, row, col):
    if direction == 'down':
        if row == 5:
            next_row = 0
        else:
            next_row = row + 1
        return next_row, col
    if direction == 'up':
        if row == 0:
            next_row = 5
        else:
            next_row = row - 1
        return next_row, col
    if direction == 'left':
        if col == 0:
            next_col = 5
        else:
            next_col = col - 1
        return row, next_col
    if direction == 'right':
        if col == 5:
            next_col = 0
        else:
            next_col = col + 1
        return row, next_col


for row in range(rows):
    line = matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == "E":
            rover_row = row
            rover_col = col

commands = input().split(", ")
for command in commands:
    new_row, new_col = next_position(command, rover_row, rover_col)
    if matrix[new_row][new_col] == "-":
        rover_row = new_row
        rover_col = new_col
        continue

    elif matrix[new_row][new_col] == "W":
        print(f"Water deposit found at ({new_row}, {new_col})")
        water += 1
        # matrix[rover_row][rover_col] = "-"
        # matrix[new_row][new_col] = "-"
        rover_row = new_row
        rover_col = new_col

    elif matrix[new_row][new_col] == "C":
        print(f"Concrete deposit found at ({new_row}, {new_col})")
        concrete += 1
        # matrix[rover_row][rover_col] = "-"
        # matrix[new_row][new_col] = "-"
        rover_row = new_row
        rover_col = new_col

    elif matrix[new_row][new_col] == "M":
        print(f"Metal deposit found at ({new_row}, {new_col})")
        metal += 1
        # matrix[rover_row][rover_col] = "-"
        # matrix[new_row][new_col] = "-"
        rover_row = new_row
        rover_col = new_col

    elif matrix[new_row][new_col] == "R":
        print(f"Rover got broken at ({new_row}, {new_col})")
        break

if metal > 0 and concrete > 0 and water > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
