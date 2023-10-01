grid= []
for i in range(5):
    row = []
    for j in range(5):
        row.append(" ")
    grid.append(row)

for i in range(9):
    if i in [0,2,4,6,8]:
        print("Plater 1 turn: ")
        row = int(input("enter row(0 to 2): "))
        col = int(input("enter column(0 to 2): "))

        if grid[row*2][col*2] == " ":
            grid[row*2][col*2] = "X"
        else:
            print("slot taken, try other box")
            continue

        for i in range(5):
            for j in range(5):
                if i%2 == 0:
                    if j%2 == 0:
                        print(grid[i][j], end=" ")
                    else:
                        print("|", end=" ")
                else:
                    print("-", end=" ")
            print()

    else:
        print("Player 2 turn: ")
        row = int(input("enter row(0 to 2): "))
        col = int(input("enter column(0 to 2): "))

        if grid[row*2][col*2] == " ":
            grid[row*2][col*2] = "O"
        else:
            print("slot taken, try other box")
            continue

        for i in range(5):
            for j in range(5):
                if i%2 == 0:
                    if j%2 == 0:
                        print(grid[i][j], end=" ")
                    else:
                        print("|", end=" ")
                else:
                    print("-", end=" ")
            print()