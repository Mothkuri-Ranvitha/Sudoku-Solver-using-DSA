import random
import pickle
import hyper
import x_sudoku
import gt_sudoku

def generate_sudoku(size, difficulty):
    if size == 3:
        if difficulty == 1:  
            return random.choice([
                [[1, 0, 2], [0, 2, 0], [0, 0, 0]],
                [[0, 0, 0], [1, 2, 3], [0, 0, 0]]
            ])
        elif difficulty == 2:  
            return random.choice([
                [[0, 0, 1], [0, 3, 0], [0, 0, 0]],
                [[3, 0, 0], [0, 2, 0], [0, 0, 1]]
            ])
        elif difficulty == 3:  
            return random.choice([
                [[0, 0, 0], [2, 0, 0], [0, 2, 1]],
                [[1, 0, 0], [0, 0, 3], [0, 2, 0]],
                [[0, 0, 2], [0, 1, 0], [3, 0, 0]]
            ])
    elif size == 6:
        if difficulty == 1:  
            return random.choice([
                [[0, 0, 3, 0, 6, 0], [5, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [4, 0, 0, 0, 0, 2], [0, 1, 0, 5, 0, 0]],
                [[1, 0, 0, 0, 0, 2], [0, 2, 0, 3, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 4, 0, 1, 0], [2, 0, 0, 0, 0, 3]]
            ])
        elif difficulty == 2:  
            return random.choice([
                [[0, 0, 0, 0, 5, 0], [6, 0, 3, 0, 0, 0], [0, 0, 1, 0, 0, 0],[0, 0, 0, 3, 0, 0], [0, 0, 0, 6, 0, 2], [0, 0, 5, 0, 0, 0]],          
            ])
        elif difficulty == 3: 
            return random.choice([
                [[0, 0, 0, 2, 0, 0], [0, 4, 0, 0, 0, 1], [0, 0, 0, 0, 3, 0], [0, 1, 0, 0, 0, 0], [5, 0, 0, 0, 2, 0], [0, 0, 6, 0, 0, 0]],
                [[0, 0, 4, 0, 0, 0], [0, 5, 0, 0, 0, 0], [0, 0, 0, 1, 0, 2], [2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 5, 0], [0, 0, 1, 0, 0, 0]]
            ])
    elif size==9:
        if difficulty==1:  
            return random.choice([
                [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]],
                [[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0], [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0], [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]]
            ])
        elif difficulty==2:  
            return random.choice([
                [[0, 2, 0, 6, 0, 8, 0, 0, 0], [5, 8, 0, 0, 0, 9, 7, 0, 0], [0, 0, 0, 0, 4, 0, 0, 0, 0], [3, 7, 0, 0, 0, 0, 5, 0, 0], [6, 0, 0, 0, 0, 0, 0, 0, 4], [0, 0, 8, 0, 0, 0, 0, 1, 3], [0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 9, 8, 0, 0, 0, 3, 6], [0, 0, 0, 3, 0, 6, 0, 9, 0]]
                            ])
        elif difficulty==3:  
            return random.choice([
                [[0, 0, 0, 6, 0, 0, 4, 0, 0], [7, 0, 0, 0, 0, 3, 6, 0, 0], [0, 0, 0, 0, 9, 1, 0, 8, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 5, 0, 1, 8, 0, 0, 0, 3], [0, 0, 0, 3, 0, 6, 0, 4, 5], [0, 4, 0, 2, 0, 0, 0, 6, 0], [9, 0, 3, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 1, 0, 0]],
                [[2, 0, 0, 0, 0, 0, 0, 0, 0], [8, 0, 4, 0, 0, 7, 0, 0, 0], [0, 1, 3, 0, 0, 8, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 6, 0], [0, 6, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2, 8], [0, 0, 0, 5, 0, 0, 7, 0, 0], [7, 0, 0, 0, 0, 9, 0, 1, 3], [0, 2, 0, 0, 0, 0, 0, 0, 0]]
            ])
    return []

def is_valid_entry(grid, num, row, col):
    size = len(grid)
    box_size = int(size ** 0.5)
    if num in grid[row]:  
        return False
    if num in (grid[i][col] for i in range(size)): 
        return False
    start_row = (row // box_size) * box_size
    start_col = (col // box_size) * box_size
    for i in range(start_row, start_row + box_size):
        for j in range(start_col, start_col + box_size):
            if grid[i][j] == num:
                return False
    return True

def save_puzzle(sudoku, size):
    with open('sudoku_save.pkl', 'wb') as f:
        pickle.dump((sudoku, size), f)  
    print("Puzzle saved successfully!")
    
def load_puzzle():
    try:
        with open('sudoku_save.pkl', 'rb') as f:
            loaded_data = pickle.load(f)  
            loaded_sudoku, size = loaded_data  
            return loaded_sudoku, size
    except FileNotFoundError:
        print("No saved puzzle found.")
        return None, None
    
def solve(grid):
    size = len(grid)
    empty_pos = find_empty(grid)
    if not empty_pos:
        return True  
    row, col = empty_pos
    for num in range(1, size + 1):  
        if is_valid_entry(grid, num, row, col):
            grid[row][col] = num 

            if solve(grid): 
                return True
            grid[row][col] = 0 
    return False

def solve_step_by_step(grid):
    size = len(grid)
    empty_pos = find_empty(grid)

    if not empty_pos:
        return True  

    row, col = empty_pos

    for num in range(1, size + 1):
        if is_valid_entry(grid, num, row, col):
            grid[row][col] = num  

            print(f"Placing {num} at row {row + 1}, column {col + 1}.")
            print_sudoku(grid)          
            action = input("Enter 'n' for next step, 'e' to exit, or 'c' to complete solving: ").lower()
            if action == 'e':
                print("Exiting the solving process.")
                return False  
            elif action == 'c':
                if solve(grid):  
                    print("Puzzle solved completely!")
                    return True
                else:
                    print("This puzzle is unsolvable.")
                    return False

            if solve_step_by_step(grid):  
                return True
            
            grid[row][col] = 0  
            print(f"Backtracking from row {row + 1}, column {col + 1}.")

    return False 

def find_empty(grid):
    size = len(grid)
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                return (i, j)  
    return None  

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
        
def get_hint(sudoku):
    size = len(sudoku)
    empty_cells = [(r, c) for r in range(size) for c in range(size) if sudoku[r][c] == 0]

    if not empty_cells:
        print("No empty cells left!")
        return None, None, None

    row, col = random.choice(empty_cells)
    for num in range(1, size + 1):
        if is_valid_entry(sudoku, num, row, col):
            return row, col, num
    return None, None, None

def play():
    choice = input("Enter 'n'to start a new game or 'l' to load a saved game: ").lower()
    
    if choice == "l":
        sudoku,size =load_puzzle()
        if sudoku is None:
            print("No saved game ")
        print("Loaded saved game:")

    elif choice=="n":
    
        ip = int(input("\n1. 3*3 \n2. 6*6\n3. 9*9\nEnter Your Choice:"))
        ip2 = int(input("\n1. Easy\n2. Medium\n3. Hard\nEnter Your Choice:"))

        if ip == 1:
            size = 3
        elif ip == 2:
            size = 6
        elif ip == 3:
            size = 9
        else:
            print("Invalid size choice.")
            return

        if ip2 in [1, 2, 3]:
            difficulty = ip2
        else:
            print("Invalid difficulty choice.")
            return

        sudoku = generate_sudoku(size, difficulty)
    else:
        print("Invalid input format.")
      
    move_stack = []
    redo_stack = []
    print("Here is your Sudoku puzzle:")
    print_sudoku(sudoku)
    print("Keyboard shortcuts\nh: Get a hint for the next move.\ns: Solve the current Sudoku puzzle.\nu: Undo the last move.\nr: Redo the last undone move.\nk: save the puzzle.\n")
       
    while True:
        move_input = input("Enter your move (row col num) or use keyboard shortcuts (h, s, u, r,k): ").lower()

        if not move_input:
            print("Please enter a valid move or use a keyboard shortcut.")
            continue
        if move_input in ['h', 's', 'u', 'r','k']:
            if move_input == 'h':
                 row, col, num = get_hint(sudoku)
                 if row is not None:
                     print(f"Hint: Place {num} at row {row + 1}, column {col + 1}.")
                 else:
                    print("No hints available.")
            elif move_input == 's':
                if solve_step_by_step(sudoku):
                    print("Solved Sudoku puzzle:")
                    print_sudoku(sudoku)
                    print("Thanks for playing!")
                    break
                else:
                    print("This puzzle is unsolvable.")
            elif move_input == 'u':
                if move_stack:
                    last_move = move_stack.pop()
                    sudoku[last_move[0]][last_move[1]] = 0
                    redo_stack.append(last_move)
                    print("Last move undone.")
                    print_sudoku(sudoku)
                else:
                    print("No moves to undo.")
            elif move_input == 'r':
                if redo_stack:
                    last_undone = redo_stack.pop()
                    row, col, num = last_undone
                    sudoku[row][col] = num
                    move_stack.append(last_undone)
                    print("Last move redone.")
                    print_sudoku(sudoku)
                else:
                    print("No moves to redo.")
            elif move_input=='k':
                save_puzzle(sudoku,size)
                break
        else:
            try:
                row, col, num = map(int, move_input.split())
                row -= 1
                col -= 1
                if 0 <= row < size and 0 <= col < size and 1 <= num <= size:
                    if is_valid_entry(sudoku, num, row, col):
                        move_stack.append((row, col, num))
                        redo_stack.clear()
                        sudoku[row][col] = num
                        print_sudoku(sudoku)
                    else:
                        print("Invalid move. Try again.")
                else:
                    print(f"Invalid input. Please enter row and column between 1 and {size}, and number between 1 and {size}.")
            except ValueError:
                print("Invalid input format. Please enter row, column, and number.")

def Customize():
    print("Select puzzle size:\n1. 3x3\n2. 6x6\n3. 9x9\n")
    size_choice = int(input("Enter choice: "))
    if size_choice == 1:
        size = 3
    elif size_choice == 2:
        size = 6
    elif size_choice == 3:
        size = 9
    elif size_choice == 4:
        size = 16
    else:
        print("Invalid choice. Exiting customization.")
        return None  
    sudoku_grid = [[0] * size for _ in range(size)]
    print("Custom Puzzle: Use numbers to fill cells, enter 'done' when finished.")

    while True:
        print_sudoku(sudoku_grid)
        move = input("Enter 'row col num' to place a number, or 'done' to save: ").lower().split()

        if move[0] == "done":
            print("Custom puzzle saved. You can now play or solve it.")
            break
        try:
            row = int(move[0]) - 1
            col = int(move[1]) - 1
            num = int(move[2])
            if not (0 <= row < size and 0 <= col < size and 1 <= num <= size):
                print("Invalid entry: Row, column, or number is out of range.") 
                continue
            if is_valid_entry(sudoku_grid, num, row, col):
                sudoku_grid[row][col] = num
            else:
                print("Invalid move: Violates Sudoku rules. Try a different position or number.")
        except ValueError:
            print("Invalid input format. Please enter row, column, and number.")
    solve_choice = input("Would you like to solve your custom puzzle automatically now? (yes/no): ")
    if solve_choice.lower() == "yes":
        if solve(sudoku_grid):  
            print("Solved Custom Puzzle:")
            print_sudoku(sudoku_grid)
        else:
            print("Unable to solve the puzzle; it may be invalid.")

    return sudoku_grid
def fun_quiz():
    question = [
        {
            "question": "Q1) If each number was a character in a story, which number would be the hero?",
            "options": ["6", "7", "9", "5"],
        },
        {
            "question": "Q2) Do you want to play by yourself or with your friends?",
            "options": ["By myself", "With friends"],
        },
        {
            "question": "Q3) When you're stuck on a Sudoku puzzle, do you try to eliminate possibilities first, or do you guess a number and see if it fits?",
            "options": ["Eliminate possibilities", "Guess a number"],
        },
        {
            "question": "Q4) How many times have you almost thrown your pencil at a particularly stubborn puzzle?",
            "options": ["Once", "A few times", "Never", "Too many times to count"],
        },
        {
            "question": "Q5) If Sudoku solving styles were like personalities, what type would you be?",
            "options": [
                "1. The fast guesser: Always guesses but often wrong",
                "2. A question bank: Double checks each step",
                "3. Pattern seeker: Looks for symmetry or shortcuts first",
                "4. The detective: Looks for clues for each cell"
            ],
        }
    ]
    answers = []  
    current_question = 0  
    
    while current_question < len(question):
        q = question[current_question]
        print(f"\n{q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"{idx}. {option}")
        
        while True:
            user_input = input("Select an option (1-4), 'Next' to continue, or 'Exit' to quit: ").strip().lower()

            if user_input == 'next':
                current_question += 1
                break
            elif user_input == 'exit':
                print(f"\nYou exited the quiz. Your total answers were:\n{answers}")
                return
            else:
                try:
                    ans = int(user_input) - 1
                    if ans in range(len(q['options'])):
                        answers.append(q['options'][ans])
                        print(f"Your answer: {q['options'][ans]}\n")
                        current_question += 1  
                        break
                    else:
                        print("Invalid choice. Please select a valid option between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 4 or type 'Next' or 'Exit'.")
    
    print("\n--- Your Quiz Summary ---")
    for idx, ans in enumerate(answers, 1):
        print(f"Q{idx}: {ans}")
    print("\nThanks for taking the quiz!")

def logic_quiz():
    logical_questions = [
        {
            "question": "Q1) In Sudoku, each row must contain which of the following?",
            "options": ["The same number", "Unique numbers 1-9", "All even numbers", "All odd numbers"],
            "answer": "Unique numbers 1-9"
        },
        {
            "question": "Q2) In sudoku ,what does the term grid refers to?",
            "options": ["The set of all possible numbers", "The overall layout of the puzzle,including rows,coloumns,and boxes", "The final solution", "The techniques used to solve the puzzle"],
            "answer": "The overall layout of the puzzle,including rows,columns,and boxes"
        },
        {
            "question": "Q3) What is the minimum number of clues needed for a Sudoku puzzle to have a unique solution?",
            "options": ["21", "17", "19", "15"],
            "answer": "17"
        },
        {
            "question": "Q4) If every row, column, and box must have one of each number 1-9, what is the maximum number of times each number can appear in the whole puzzle?",
            "options": ["5", "4", "7", "9"],
            "answer": "9"
        },
        {
            "question": "Q5) If the number 6 appears in the middle row of a Sudoku puzzle, where can't it appear?",
            "options": ["In the middle column", "In the next row", "In the same 3*3 box", "In the middle row"],
            "answer": "In the same 3*3 box"
        },
    ]
    
    score = 0
    current_question = 0
    while current_question < len(logical_questions):
        ques = logical_questions[current_question]
        print(f"\n{ques['question']}")
        options = random.sample(ques['options'], len(ques['options']))
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        while True:
            user_input = input("Select the correct option (1-4) or type 'Next' to continue or 'Exit' to quit: ").strip().lower()
            
            if user_input == 'next':
                current_question += 1
                break
            elif user_input == 'exit':
                print(f"\nYou exited the quiz. Your total score: {score}/{len(logical_questions)}")
                return
            else:
                try:
                    answer_idx = int(user_input) - 1
                    if answer_idx in range(len(options)):
                        if options[answer_idx] == ques['answer']:
                            print("Correct!")
                            score += 1
                        else:
                            print(f"Wrong! The correct answer was: {ques['answer']}")
                        current_question += 1
                        break
                    else:
                        print("Invalid choice. Please choose a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a valid number or type 'Next' or 'Exit'.")

    print(f"\nYour total score: {score}/{len(logical_questions)}")

custom_puzzles = []
while True:
    ip = int(input("\n1. Play\n2. Customize\n3. Quiz\n4. Play Variations\n5. Exit\nEnter Your Choice:"))
    print()
    if ip == 1:
        play()
    elif ip == 2:
        custom_puzzle = Customize()
        if custom_puzzle:
            custom_puzzles.append(custom_puzzle)
    elif ip == 3:
        print("Welcome to the Sudoku solver Quiz")
        choice=input("\n1.Fun related Questions \n2.Logical related questions\nEnter your choice:").lower()
        if choice=="1":
            fun_quiz()
        elif choice=="2":
            logic_quiz()
    elif ip==4:
        ch=int(input("\n1. X-Sudoku\n2. Greater-Than Sudoku\n3. Hyper Sudoku\nEnter Your Choice:"))
        if ch==1:
            x_sudoku.play_x_sudoku()
        elif ch==2:
            gt_sudoku.play_gt_sudoku()
        elif ch==3:
            hyper.play_hyper_sudoku()
    elif ip==5:
        break                      
