import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINNING_SCORE = 5
WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5, 7]
]

def prompt(message):
    print(f"=> {message}")

def display_board(board):
    os.system('clear')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    square = None

    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, COMPUTER_MARKER)
            if square:
                break
                
    for line in WINNING_LINES:
        square = find_at_risk_square(line, board, HUMAN_MARKER)
        if square:
            break

    if not square:
        if board[5] == INITIAL_MARKER:
            board[5] = COMPUTER_MARKER
        else:
            square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
               and board[sq2] == HUMAN_MARKER
               and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                  and board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def find_at_risk_square(line,board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None

def alternate_player(current_player):
    if current_player == "player":
        current_player = "computer"
    else:
        current_player = "player"

def choose_square(board, current_player):
    if current_player == "player":
        player_chooses_square(board)
    else:
        computer_chooses_square(board)

def play_tic_tac_toe():
    player_score = 0
    computer_score = 0
    current_player = "player"
    while True:
        board = initialize_board()

        while True:
            display_board(board)

            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                player_score += 1
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                computer_score += 1
                break

        display_board(board)

        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
            if player_score > 2:
                prompt("Player is the overall winner!")
                exit()
            elif computer_score > 2:
                prompt("Computer is the overall winner!")
                exit()
        else:
            prompt("It's a tie!")

        prompt("Play again? (y or n)")
        answer = input().lower()

        while answer[0] != 'y' or answer[0] != 'n':
            prompt("Play again? (y or n) Please enter y or n.")
            answer = input().lower()
            if answer[0] == 'y':
                break
            if answer[0] == 'n':
                prompt("Thanks for playing Tic Tac Toe!")
                exit()

def join_or(lst, separator = ", ", conjunction = "or"):
    if lst == []:
        return ""
    elif len(lst) == 1:
        return lst[0]

    lst_str = [str(number) for number in lst]
    first = separator.join(lst_str[0:-1])
    return f"{first} {conjunction} {lst_str[-1]}"

play_tic_tac_toe()