def computer_turn(character):
    computer_move = 0
    return computer_move

def computer_character(character):
    if character == 'x' or 'X':
        computer_character = 'O'
    else:
        computer_character
    return computer_character


def update_board(board,player_move,character):
    new_board = list(map(lambda st: str.replace(st, str(player_move), character), board)) 
    return new_board

def get_player_character():
    character = input('\nWould you like to be X or O ? ')
    while character:
        if character.upper() in ('X', 'O'):
            return character
        else:
            print('Please enter X or O')
            character = input('\nWould you like to be X or O ? ')
        

def player_turn():
    while True:
        try:
            player_move = int(input('\nYour turn! Enter a number to choose your position: '))
        except ValueError: 
            print('INVALID - not a number! ')
        else:     
            if 1 <= player_move < 10 :
                #computer turn here 
                return player_move
            else:
                print('INVALID - please enter a number 1-9')




#looked up how to bold letters on stack overflow(for easier viewing)
print('\033[1m' +'LETS PLAY TIC TAC TOE!')
character = get_player_character()
board = ['1 | 2 | 3 ','__________', '4 | 5 | 6','__________', '7 | 8 | 9']
for b in board:
        print(b)


while character:
    player_move = player_turn()
    board = update_board(board,player_move,character)
    for b in board:
        print(b)


