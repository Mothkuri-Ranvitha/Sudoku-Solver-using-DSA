import random

def is_valid(grid, row, col, num):
    if num in grid[row]:
        return False

    if num in [grid[i][col] for i in range(9)]:
        return False

    box_row, box_col = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if grid[box_row + i][box_col + j] == num:
                return False
    return True

def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def generate_full_solution():
    grid = [[0] * 9 for _ in range(9)]
    solve(grid)
    return grid

def create_greater_than_marks(solution):
    horizontal_marks = [[None] * 8 for _ in range(9)]
    vertical_marks = [[None] * 9 for _ in range(8)]

    for i in range(9):
        for j in range(8):
            # Horizontal greater-than constraint
            if solution[i][j] > solution[i][j + 1]:
                horizontal_marks[i][j] = '>'
            elif solution[i][j] < solution[i][j + 1]:
                horizontal_marks[i][j] = '<'
            else:
                horizontal_marks[i][j] = ' ' 

    for i in range(8):
        for j in range(9):
            vertical_marks[i][j] = ' '

    return horizontal_marks, vertical_marks

def create_puzzle(solution, clues=30):
    puzzle = [row[:] for row in solution]
    attempts = 81 - clues
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            attempts -= 1
    return puzzle

def print_grid(grid, horizontal_marks=None, vertical_marks=None):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 29)  
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            cell = grid[i][j] if grid[i][j] != 0 else '.'
            print(cell, end=" ")

            if horizontal_marks and j < 8 and horizontal_marks[i][j]:
                print(horizontal_marks[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()

        if vertical_marks and i < 8:
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" ", end="  ")
                if vertical_marks[i][j]:
                    print(vertical_marks[i][j], end="  ")
                else:
                    print(" ", end="  ")
            print()

def play_gt_sudoku():
    solution = generate_full_solution()
    puzzle = create_puzzle(solution, clues=30)
    horizontal_marks, vertical_marks = create_greater_than_marks(solution)
    print("\n\nRULE:Greater-Than Sudoku adds inequality symbols between adjacent cells, making it a more challenging variant of Sudoku.")
    print("\n\nGenerated Greater-Than Sudoku Puzzle:")
    print_grid(puzzle, horizontal_marks, vertical_marks)

    while True:
        user_input = input("Enter 'row col num' (1-9) to fill in a cell, 'solve' to see the solution, or 'exit' to quit: ").strip().lower()

        if user_input == 'solve':
            print("Solution to the Greater-Than Sudoku Puzzle:")
            print_grid(solution, horizontal_marks, vertical_marks)
            break
        elif user_input == 'exit':
            print("Exiting the game.")
            break
        else:
            try:
                row, col, num = map(int, user_input.split())
                row -= 1  
                col -= 1  
                
                if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
                    if puzzle[row][col] == 0 and is_valid(puzzle, row, col, num):
                        puzzle[row][col] = num
                        print("Updated Greater-Than Sudoku Puzzle:")
                        print_grid(puzzle, horizontal_marks, vertical_marks)
                    else:
                        if puzzle[row][col] != 0:
                            print(f"Invalid move: Cell ({row + 1}, {col + 1}) is already filled with {puzzle[row][col]}.")
                        else:
                            print(f"Invalid move: Number {num} is not valid for cell ({row + 1}, {col + 1}).")
                else:
                    print("Invalid input. Please enter values in the format 'row col num' with row and col between 1-9 and num between 1-9.")
            except ValueError:
                print("Invalid input format. Please enter values in the format 'row col num'.")
