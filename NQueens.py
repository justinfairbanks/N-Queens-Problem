import sys
import os
import numpy as np

# N-Queens Problem with Recursive Solution
# Updated: 1.3.2023

print("\t\t\t\t=== Justin Fairbanks N-Queens Problem ===\n")


# CMD Args

if len(sys.argv) == 1:
    print("Syntax: NQueens.py <QueensNum>\n")
    Queens = 8 # If no specified Queen count

elif len(sys.argv) == 2:
    Queens = int(sys.argv[1]) # Number of Queens inputted

else: 
    print("Invalid Number of Command Line Args")
    print("Syntax: NQueens.py <QueensNum>\n")
    input("Press enter to close...")
    sys.exit()



# 8 by 8 Chess Board
Board = np.zeros((8,8), dtype= int)

 
# Recursive Function returns True or False
def CheckQueens(Board, queens, row, cols, diag1, diag2):
    if queens == 0:
        return True
    
    if row == 8:
        return False

    for col in range(8):
        if cols[col] or diag1[row-col] or diag2[row + col]:
            continue

        cols[col] = True
        diag1[row - col] = True
        diag2[row + col] = True
        Board[row][col] = 1
        queens -= 1


        if CheckQueens(Board, queens, row + 1, cols, diag1, diag2):
            return True

        cols[col] = False
        diag1[row - col] = False
        diag2[row + col] = False
        Board[row][col] = 0
        queens += 1

    return False



# Recursive Function returns True or False
def NQueens(Board, Queens):
    col = [False] * 8
    diag1 = [False] * (2 * 8 - 1)
    diag2 = [False] * (2 * 8 - 1)

    CheckQueens(Board, Queens, 0, col, diag1, diag2)

    return Board


Board = NQueens(Board, Queens) # Gets solution where 1s are Queens and 0s are Blank Spots

# First output of solution

if (Board == 0).all():
    print(f"There are no solutions for {Queens} Queens\n")

else: 
    print(f"Solution with {Queens} Queens")

    print("-" * 32)

    for row in Board: # Outputs 1s to '[Q]' and '[]' for blank spots
        for cell in row:            
            print('[Q]' if cell == 1 else '[ ]', end=' ')
        print()

    print("-" * 32)

os.system('pause')