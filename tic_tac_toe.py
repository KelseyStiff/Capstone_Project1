import random

def computer_turn(possible_moves):
    computer_move = random.choice(possible_moves)
    return computer_move

def player_turn(possible_moves):
    while True:
        try:
            player_move = int(input('\nYour turn! Enter a number to choose your position: '))
        except ValueError: 
            print('INVALID - not a number! ')
        else: 
            if 1 <= player_move < 10 and player_move in possible_moves:
                possible_moves.remove(player_move)
                return player_move
            else:
                print('INVALID - please enter a number 1-9 that has not already been taken')

def assign_computer_character(player_character):
    if player_character == 'x' or player_character == 'X':
        computer_character = 'O'
    
    elif player_character == 'o' or player_character == 'O':
        computer_character = 'X'

    return computer_character

def assign_player_character():
    player_character = input('\nWould you like to be X or O ? ')
    while player_character:
        if player_character.upper() in ('X', 'O'):
            return player_character
        else:
            print('Please enter X or O')
            player_character = input('\nWould you like to be X or O ? ')

def update_board(board,move,character):
    new_board = [place.replace(str(move), character) for place in board]
    return new_board

def play_again(player_character):
    play_again = input('Would you like to play again? (Y/N)').upper
    if play_again == 'Y':
        player_character = ''
        main()
    elif play_again == 'N':
        quit()


        while True:
            try:
                play_again = input('Would you like to play again? (Y/N)').upper
            except: 
                print('PLEASE ENTER Y or Yes N for No')
            else: 
                if play_again == 'Y':
                    main()

def check_winner(board,moves):
    #possible wins
    row1 = [1,2,3]
    row2 = [4,5,6]
    row3 = [7,8,9]

    col1 = [1,4,7]
    col2 = [2,5,8]
    col3 = [3,6,9]

    diagonal1 = [1,5,9]
    diagonal2 = [3,5,7]

    #check rows
    if all(m in moves  for m in row1):
        winner = True
    elif all(m in moves  for m in row2):
        winner = True
    elif all(m in moves  for m in row3):
        winner = True
    #check columns
    elif all(m in moves  for m in col1):
        winner = True
    elif all(m in moves  for m in col2):
        winner = True
    elif all(m in moves  for m in col3):
        winner = True
    #check diagonals
    elif all(m in moves  for m in diagonal1):
        winner = True
    elif all(m in moves  for m in diagonal2):
        winner = True
    else:
        winner =  False
    return winner


def main():
   
    print('LETS PLAY TIC TAC TOE!')
    possible_moves = [1,2,3,4,5,6,7,8,9]
    
    player_character = assign_player_character()
    computer_character = assign_computer_character(player_character)
    player_moves = []
    computer_moves = []
    board = ['1 | 2 | 3 ','__________', '4 | 5 | 6','__________', '7 | 8 | 9']
    for b in board:
            print(b)

    while player_character:

        player_move = player_turn(possible_moves)
        player_moves.append(player_move)
        board = update_board(board,player_move,player_character)

        winner = check_winner(board,player_moves)

        computer_move = computer_turn(possible_moves)
        computer_moves.append(computer_move)
        possible_moves.remove(computer_move)
        board = update_board(board,computer_move,computer_character)


        for b in board:
            print(b)

        if winner:
            print('YOU WON!')
            play_again(player_character)
        else:
            'ITS A TIE!'
    else:
        print('YOU LOSE')
        #print('YOU LOSE! OR TIE?')

main()
