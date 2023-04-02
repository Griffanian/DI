def display_board(current_board:list) -> str:
    board_str='***************\n'
    for i,row in enumerate(current_board):
        board_str+='*  '+row[0]+' | '+row[1]+' | '+row[2]+'  *'+'\n'
        if i!=2:
            board_str+='* '+'---|'*2+'---'+' *'+'\n'
    board_str+='***************\n'
    print(board_str)


def player_input(player:str,current_board:list) -> list['row':int,'column':int]():
    check_list=['1','2','3']
    while True:
        position=input(f'player {player} please enter in which square you would like to place a piece in this form eg."1 3" would be the first row colunm three ')
        if len(position) == 3:
            if position[0] in check_list and position[2] in check_list:
                if position[1] == ' ':
                    if check_input(int(position[0]),int(position[2]),current_board) == True:
                        break
                    else:
                        print('That square already contains an item. Try again')
                else:
                    print('Second charecter must be a space. Try again.')
            else:
                print('First and last charecters must be a number between 1-3. Try again.')
        else:
            print('Your string is more then three charecters long. Try again.')
    
    return [int(position[0]),int(position[2])]
     
def check_input(row:int,column:int,current_board:list)-> list:
    if current_board[row-1][column-1] == ' ':
        return True
    else:
        return False
    
def update_board(row:int,column:int,players_turn:str,current_board:list)->list:
    current_board[row-1][column-1] = players_turn
    return current_board

def check_win(current_board:list) -> bool:
    players=['x','o']
    win=False
    for i,row in enumerate(current_board):
        if row[0] == row[1] == row[2] and row[0] in players:
            win = True
        elif current_board[0][i] == current_board[1][i] == current_board[2][i] and current_board[0][i] in players:
            win = True
        elif current_board[0][0] == current_board[1][1] == current_board[2][2] and current_board[0][0] in players:
            win = True
        elif current_board[0][2] == current_board[1][1] == current_board[2][0] and current_board[0][2] in players:
            win = True
    return win

def play():
    board_list=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    winner=False

    print('Welcome to tic tace toe\n')
    display_board(board_list)
    while True:
        player_str=input('Who is going first? ("x" or "o") ')
        if player_str in ['x','o']:
            break
        else:
            print("Pick one of the real choices!")

    while True:
        turn_row_column=player_input(player_str,board_list)
        board_list=update_board(turn_row_column[0],turn_row_column[1], player_str,board_list)
        display_board(board_list)
        winner=check_win(board_list
                         )
        if  winner == True:
            break
        elif player_str == 'x':
            player_str = 'o'
        else:
            player_str = 'x'
        print(f'It is now {player_str} turn.\n')
    print(f"player {player_str} wins \n Good Game")

play()
