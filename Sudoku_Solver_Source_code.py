# libraries included
from datetime import date
import json
name = input("Please Enter your name here -: ")
print("Welcome {0} to Sudoku Solver ".format(name))
print("How are you doing")
print("What you want to do ?")
grid = []
def help():
    print('''Sudoku is played on a grid of 9 x 9 spaces. Within the rows and columns are 9 “squares” (made up of 3 x 3 spaces).
Each row, column and square (9 spaces each) needs to be filled out with the numbers 1-9, without repeating any numbers within the row, column or square.
     ''')
    interface()


def writing_record(grid1):
    with open("record.txt", "a+") as file:
        day = date.today()  # gets  date of the day it was played
        file.writelines("Solved on -: {0} \n".format(day))  # writes the date into the file
        file.writelines("Solved by -: {0} \n".format(name))  # writes the name of the player into the file
        json.dump(grid1, file)   # writes the problem of that the user provided it to solve
        file.write("\n")  # appends a new line character each time as json does not append new line by itself


def record():
    file = open("record.txt", "r+")
    j = sum(1 for l in file)  # To count the total number of lines in the file
    file.close()
    with open("record.txt", "r+") as file1:
        for i in range(j // 4):  # integer dividing it with 4 as each info will contain 4 lines so we can get that how many times our loop will work
            for k in range(4):
                if k == 0 or k == 1:
                    print(file1.readline(), end='')  # Will get the name and date from the file and print it
                else:
                    print("_" * 20)  # when it will reach at the sudoku puzzles it will print 20 times '_'
                    a = eval(file1.readline())  # matrix will be stored as string in file to revert it back to list we use eval()
                    for b in range(9):
                        print("|", end='')
                        for c in range(9):
                            print(a[b][c], end=" ")  # prints b,c th element of the matrix
                        print("|")
                    print("-" * 20)


def taking_input():
    print("Enter the sudoku problem here ")
    print("Use '0' instead of empty spaces in the problem  ")
    global grid
    for i in range(9):  # the sudoku will be of 9 rows and nine columns
        a = list(map(int, input().split()))  # mapping each space separated input to the list
        grid.append(a)  # appending the roow int the matrix
    writing_record(grid)
    solve()
    return


# the more number of zeroes more and more solutions
def possible(row, column, number):
    # If the number comes in the row
    global grid
    for i in range(0, 9):
        if grid[row][i] == number:
            return False
            # if the number pre-exist in the row we return False
    # If the number comes in the column
    for i in range(0, 9):
        if grid[i][column] == number:
            return False
            # if the number pre-exist in the column we return False
    # If the number comes in the squares
    # we do integer division for finding the squares and multiply it with 3 to find the starting index of the square
    x0 = (column//3)*3
    y0 = (row//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            # These two loop will check each square of 3*3 with the start indices  x0 and y0
            if grid[y0+i][x0+j] == number:
                return False
    return True
    # set the grid global


def solve():
    global grid
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return
    print("_" * 20)
    for b in range(9):
        print("|", end='')
        for c in range(9):
            print(grid[b][c], end=" ")
        print("|")
    print("-" * 20)
    with open("record.txt", "a+") as file:
        json.dump(grid, file)
        file.write("\n")
    # input("Press Enter for more possible solution ") it is used to check all solution of problem


def interface():
    global grid
    print("Press 1 to Solve a Sudoku Puzzle  ")
    print("Press 2 to see previous records ")
    print("Press 3 to seek help ")
    ch = int(input("Enter your choice here -:  "))
    if ch == 1:
        grid = taking_input()
    elif ch == 2:
        record()
    elif ch==3:
        help()
    else:
        print("Enter a valid choice ")
        interface()


interface()


while True:  # this while loop will work till it is closed by the user
    print("Press 1 to continue ")
    print("Press 0 to end ")

    choice = int(input("Enter the choice here -: "))
    if choice == 1:
        interface()
    else:
        print("Thank You for playing ")
        break  # if user enters 0 it will break out of the while loop and will show the goodbye message


