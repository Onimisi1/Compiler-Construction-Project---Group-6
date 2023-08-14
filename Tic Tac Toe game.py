import random


def display(board):
    print('\n'*10)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-' * 5)
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-' * 5)
    print(board[7] + '|' + board[8] + '|' + board[9])


def playmark():
    marker = None

    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Please choose X or O ').upper()
        if marker != 'X' and marker != 'O':
            print('\nYou didn\'t choose X or O')
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def choosefirst():
    first = random.choice([1, 2])

    if first == 1:
        return ('Player1')
    else:
        return ('Player2')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def space_check(board, position):
    return board[position] == ' '


def full_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def play_again():
    choice = input('Do you want to play again ? Yes/No ')
    return choice.upper().startswith('Y')


def player_position(board):
    position = ' '
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input('Please choose a position from 1-9 '))
        except:
            continue
    return position


# function for computer

def getBoardCopy(board):
    dupboard = []
    for i in board:
        dupboard.append(i)
    return dupboard


def chooseRandomMove(board, Moves_List):
    possibleMoves = []
    for i in Moves_List:
        if space_check(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def ComputerMove(board, player2):
    if player2 == 'X':
        player1 = 'O'
    else:
        player1 = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if space_check(copy, i):
            place_marker(copy, player2, i)
            if win_check(copy, player2):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if space_check(copy, i):
            place_marker(copy, player1, i)
            if win_check(copy, player1):
                return i

    move = chooseRandomMove(board, [1, 3, 7, 9])
    if move != None:
        return move

    if space_check(board, 5):
        return 5

    return chooseRandomMove(board, [2, 4, 6, 8])


print("Welcome to Onimisi Tic Tac Toe Game")

while True:
    board = [' '] * 10
    player1, player2 = playmark()
    turn = choosefirst()
    print(turn + ' will go first')
    gameOn = True

    while gameOn:
        if turn == 'player1':
            display(board)
            move = player_position(board)
            place_marker(board, player1, move)

            if win_check(board, player1):
                display(board)
                print('Nice! You have won the game.')
                gameOn = False

            else:
                if full_check(board):
                    display(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player2'

        else:
            turn == 'player2'
            move = ComputerMove(board, player2)
            place_marker(board, player2, move)

            if win_check(board, player2):
                display(board)
                print('player2 has won the game!')
                gameOn = False

            else:
                if full_check(board):
                    display(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'

    if not play_again():
        break











