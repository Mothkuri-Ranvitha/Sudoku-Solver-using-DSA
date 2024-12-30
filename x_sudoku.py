import random

def is_valid_x(board, row, col, num):

    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    if row == col:
        for i in range(9):
            if board[i][i] == num:
                return False

    if row + col == 8:
        for i in range(9):
            if board[i][8 - i] == num:
                return False

    return True

def solve_x_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  
                for num in range(1, 10):  
                    if is_valid_x(board, row, col, num):
                        board[row][col] = num
                        if solve_x_sudoku(board):  
                            return True
                        board[row][col] = 0  
                return False 
    return True

def generate_full_x_solution():
    board = [[0] * 9 for _ in range(9)]
    solve_x_sudoku(board)
    return board

def create_x_puzzle(solution, clues=30):
    puzzle = [row[:] for row in solution]
    attempts = 81 - clues
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            attempts -= 1
    return puzzle 

def print_sudoku(sudoku):
    size = len(sudoku)
    box_size = int(size ** 0.5)
    for i in range(size):
        if i % box_size == 0 and i != 0:
            print("- " * (size + box_size - 1))
        for j in range(size):
            if j % box_size == 0 and j != 0:
                print("| ", end="")
            print(sudoku[i][j] if sudoku[i][j] != 0 else ".", end=" ")
        print()
    print()  

def play_x_sudoku():
    solution = generate_full_x_solution()
    puzzle = create_x_puzzle(solution, clues=30)
    print("\nRULE: X-Sudoku adds two diagonal lines to the standard Sudoku rules.\n\nThese diagonal lines, from top-left to bottom-right and top-right to bottom-left, must also contain unique digits 1-9.")
    print("\n\nGenerated X-Sudoku Puzzle:")
    print_sudoku(puzzle)
    
    while True:
        user_input = input("Enter 'row col num' (1-9) to fill in a cell, 'solve' to see the solution, or 'exit' to quit: ").strip().lower()
        
        if user_input == 'solve':
            print("Solution to the X-Sudoku Puzzle:")
            print_sudoku(solution)
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
                    if puzzle[row][col] == 0 and is_valid_x(puzzle, row, col, num):
                        puzzle[row][col] = num
                        print("Updated X-Sudoku Puzzle:")
                        print_sudoku(puzzle)
                    else:
                        if puzzle[row][col] != 0:
                            print(f"Invalid move: Cell ({row + 1}, {col + 1}) is already filled with {puzzle[row][col]}.")
                        else:
                            print(f"Invalid move: Number {num} is not valid for cell ({row + 1}, {col + 1}).")
                else:
                    print("Invalid input. Please enter values in the format 'row col num' with row and col between 1-9 and num between 1-9.")
            except ValueError:
                print("Invalid input format. Please enter values in the format 'row col num'.")
