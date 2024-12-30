import random

def is_valid_hyper(grid, row, col, num):

    if num in grid[row]:
        return False

    if num in [grid[i][col] for i in range(9)]:
        return False

    box_row, box_col = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if grid[box_row + i][box_col + j] == num:
                return False


    if (0 <= row < 3 and 0 <= col < 3) or \
       (0 <= row < 3 and 6 <= col < 9) or \
       (6 <= row < 9 and 0 <= col < 3) or \
       (6 <= row < 9 and 6 <= col < 9):
        for i in range(3):
            for j in range(3):
                if grid[i + (row // 6) * 6][j + (col // 6) * 6] == num:
                    return False

    return True

def solve_hyper(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_hyper(grid, row, col, num):
                        grid[row][col] = num
                        if solve_hyper(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def generate_full_hyper_solution():
    grid = [[0] * 9 for _ in range(9)]
    solve_hyper(grid)
    return grid

def create_hyper_puzzle(solution, clues=30):
    puzzle = [row[:] for row in solution]
    attempts = 81 - clues
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            attempts -= 1
    return puzzle

def print_grid(grid):
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("-" * 21) 
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  
            print(num if num != 0 else '.', end=" ")
        print()
    print() 

def play_hyper_sudoku():
    solution = generate_full_hyper_solution()
    puzzle = create_hyper_puzzle(solution, clues=30)
    print("\nHyper Sudoku introduces a new constraint:\nHyperboxes: The 9x9 grid is divided into four 3x3 hyperboxes.\n\nEach hyperbox must contain all the digits from 1 to 9.")
    print("\n\nGenerated HyperSudoku Puzzle:")
    print_grid(puzzle)
    
    while True:
        user_input = input("\nEnter 'row col num' (1-9) to fill in a cell, 'solve' to see the solution, or 'exit' to quit: ").strip().lower()
        
        if user_input == 'solve':
            print("Solution to the HyperSudoku Puzzle:")
            print_grid(solution)
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
                    if puzzle[row][col] == 0 and is_valid_hyper(puzzle, row, col, num):
                        puzzle[row][col] = num
                        print("Updated HyperSudoku Puzzle:")
                        print_grid(puzzle)
                    else:
                        if puzzle[row][col] != 0:
                            print(f"Invalid move: Cell ({row + 1}, {col + 1}) is already filled with {puzzle[row][col]}.")
                        else:
                            print(f"Invalid move: Number {num} is not valid for cell ({row + 1}, {col + 1}).")
                else:
                    print("Invalid input.")
                    print("Invalid input. Please enter values in the format 'row col num' with row and col between 1 and 9, and num between 1 and 9.")
            except ValueError:
                print("Invalid input format. Please enter values in the format 'row col num'.")
