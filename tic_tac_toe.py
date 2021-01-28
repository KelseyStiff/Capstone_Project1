import random

def assign_player_character():
    #users choice input of X or O - making it Uppercase
    player_character = input('\nWould you like to be X or O ? ')
    while player_character:
        if player_character.upper() in ('X', 'O'):
            return player_character
        else:
            print('Please enter X or O')
            player_character = input('\nWould you like to be X or O ? ')

def assign_computer_character(player_character):
    #assigns computer opposite character of user
    if player_character == 'x' or player_character == 'X':
        computer_character = 'O'
    
    elif player_character == 'o' or player_character == 'O':
        computer_character = 'X'

    return computer_character

def player_turn(possible_moves):
    while True:
        #try for users move input
        try:
            player_move = int(input('\nYour turn! Enter a number to choose your position: '))
        #validates if input is a number
        except ValueError: 
            print('INVALID - not a number! ')
        else: 
            #validating the input is 1-9 and is not already taken
            if 1 <= player_move < 10 and player_move in possible_moves:
                possible_moves.remove(player_move)
                return player_move
            else:
                #prints error message if input isn't an available number 1-9
                print('INVALID - please enter a number 1-9 that has not already been taken')

def computer_turn(possible_moves):
    #used random to choose computers move out of possible moves available
    computer_move = random.choice(possible_moves)
    return computer_move

def update_board(board,move,character):
    #updates the board by replacing chosen number/move with X or O
    new_board = [place.replace(str(move), character) for place in board]
    return new_board

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

    #checks board for wins of every combo
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
    while True:
        print('LETS PLAY TIC TAC TOE!')

        #count for number of turns
        count = 0

        #all possible moves available on the board
        possible_moves = [1,2,3,4,5,6,7,8,9]

        #assign users character (X or O)
        player_character = assign_player_character()

        #assigns computer character (X or O)
        computer_character = assign_computer_character(player_character)

        #lists to hold players and computers moves played
        player_moves = []
        computer_moves = []

        #board creation
        board = ['1 | 2 | 3 ','__________', '4 | 5 | 6','__________', '7 | 8 | 9']

        #printing the board
        for b in board:
                print(b)

        #looping user and computer moves to stop once board is filled
        for i in range(10):
        
            #gets users move
            player_move = player_turn(possible_moves)

            #adds users move to moves list
            player_moves.append(player_move)

            #updates board with users move
            board = update_board(board,player_move,player_character)

            #counts users turns
            count += 1

            #if any moves are available
            if possible_moves:

                #computers move
                computer_move = computer_turn(possible_moves)

                #add computers move to list of moves
                computer_moves.append(computer_move)

                #remove computer move from possible moves available
                possible_moves.remove(computer_move)

                #update board with computers move
                board = update_board(board,computer_move,computer_character)

                #counts computers move 
                count += 1

                #print the updated board
                for b in board:
                    print(b)

                #check winner
                # if user wins - player_won = TRUE 
                player_won = check_winner(board,player_moves)
                # if computer wins - computer_won = TRUE
                computer_won = check_winner(board,computer_moves)

                #prints message if win or lose and closes program
                if player_won:
                    print('YOU WON!')
                    exit()
                elif computer_won:
                    print('YOU LOSE')
                    exit()

            #if no more moves are available, the board is full and its a tie, program closes
            if not possible_moves:             
                print("It's a Tie!!")
                exit()
                
main()
    