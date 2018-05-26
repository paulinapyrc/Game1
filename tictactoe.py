import random #zeby komputer mogl zajac przypadkowe pole
#rysowanie pola gry
def narysujPole(board):
    print ('  |  |')
    print (' '+board[7]+ ' | ' + board[8] + ' | ' +board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print (' '+board[4]+ ' | ' + board[5] + ' | ' +board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print (' '+board[1]+ ' | ' + board[2] + ' | ' +board[3])
    print('   |   |')   

def wybierzZnak():
    znak= ' '
    while not (znak =='X' or znak == '0'):
        print ('Wybierz 0 lub X')
        znak = input().upper()

        if lznak =='X':
            return['X','0']
        else:
            return['0','X']
def ktoPierwszy():
    if random.randint(0,1) ==0:
        return 'komputer'
    else:
        return 'gracz'

    
