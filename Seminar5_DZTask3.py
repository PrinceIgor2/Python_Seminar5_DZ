# 3-Создайте программу для игры в ""Крестики-нолики""

print('Cыграем в крестики нолики!')

board = list(range(1,10))

def play_board(board):
    print('-'*12)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*12)


def place_choice(krestik_nolik):
    valid = False
    while not valid:
        player_index = input('Ваш ход, выберите ячейку для ' + krestik_nolik + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Что то не то нажали')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index-1]) not in 'XO'):
                board[player_index-1] = krestik_nolik
                valid = True
            else:
                print('Занято')
        else:
            print('Еще раз попробуй')

def winner_determination(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def process_game(board):
    counter =0
    vic = False
    while not vic:
        play_board(board)
        if counter % 2 == 0:
            place_choice('X')
        else:
            place_choice('0')
        counter +=1
        if counter > 4:
            tt_win = winner_determination(board)
            if tt_win:
                print(tt_win,'Победа')
                vic = True
                break
            if counter == 9:
                print('Победила, ДРУЖБА)')
        play_board(board)
process_game(board)
