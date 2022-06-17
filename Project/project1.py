# This function will assign the marker sign to players to fill the board with.
def assign_marker_sign_to_player():
    mark = " "
    # It will keep asking for either "X" or "O" until player1 entered "X" or "O".
    # And will return markers in the form of (player1_marker,player2_marker)
    while not (mark == "X" or mark == "O"):
        mark = input("Player1 want to be X or O: ").upper()
    if mark == "X":
        return ("X", "O")
    else:
        return ("O", "X")


# This function will decide the player's turn randomly (At start of the game).
def player_turn():
    import random
    if random.randint(0,1) == 0:
        return "player1"
    else:
        return "player2"


# This function will display the board.
def display_board(board):
    print("   |     |   ")
    print(board[1] + "  |  " + board[2] + "  |  " + board[3])
    print("   |     |   ")
    print("--------------")
    print("   |     |   ")
    print(board[4] + "  |  " + board[5] + "  |  " + board[6])
    print("   |     |   ")
    print("--------------")
    print("   |     |   ")
    print(board[7] + "  |  " + board[8] + "  |  " + board[9])
    print("   |     |   ")


# This function will make sure that player's choice is in range of 1 to 9, and not a string.
# And entered number's position is still empty or not.
# And will return availabe position in the board.
def players_choice_a_position_to_mark(board):
    while True:
        user_input = input("Please enter the position number 1-9: ")
        if user_input.isdigit():
            position = int(user_input)
            if position in range(1,10):
                if not check_empty_position(board,position):
                    print("Entered position has been filled: ")
                    continue
                else:
                    return position
            else:
                print("Entered number is not from 1 to 9: ")
                continue
        else:
            print("Entered is not a number, It's a string: ")
            continue


# This function will check the empty position in the board.
def check_empty_position(board,position):
    if board[position] == " ":
        return True

# This function will make sure that the board is not full with marked.
def board_is_full(board):
    for i in range(1,10):
        if check_empty_position(board,i):
            return False
    return True


# This function will mark player's sign to the position in the board.
def mark_players_sign_at_position(board,mark,position):
    board[position] = mark


# This function will check winning pattern.
def check_win_pattern(board,mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark))


# This function will make sure that players wnats to play again or not.
def play_again():
    play = input("Do you want to play again ? yes or no: ")
    if play.lower()[0] == 'y':
        return True
    else:
        return False





# Tic_Tac_Toe
print("Tic_Tac_Toe: ")

while True:
    board = [" "]*10
    display_board(board)
    mark1,mark2 = assign_marker_sign_to_player()
    turn = player_turn()
    print( turn + " is going first")

    game_start = input("Are you ready to play? y or n: ")

    if game_start.lower()[0] == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "player1":
            display_board(board)
            position = players_choice_a_position_to_mark(board)
            mark_players_sign_at_position(board,mark1,position)

            if check_win_pattern(board,mark1):
                display_board(board)
                print("Congrats, player1 has won....!! ")
                game_on = False
            elif board_is_full(board):
                display_board(board)
                print("The game is draw....!! ")
                game_on = False
            else:
                turn = "player2"
        else:
            display_board(board)
            position = players_choice_a_position_to_mark(board)
            mark_players_sign_at_position(board,mark2,position)

            if check_win_pattern(board,mark2):
                display_board(board)
                print("Congrats, player2 has won....!! ")
                game_on = False
            elif board_is_full(board):
                display_board(board)
                print("The game is draw....!! ")
                game_on = False
            else:
                turn = "player1"

    if not play_again():
        break
