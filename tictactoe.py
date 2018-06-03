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

        if znak =='X':
            return['X','0']
        else:
            return['0','X']
def ktoPierwszy():
    if random.randint(0,1) ==0:
        return 'komputer'
    else:
        return 'gracz'
    #Funkcja, która drukuje True jeśli gracz chce grać jeszcze raz. Jeżeli nie chce - false
def ZagrajJeszczeRaz():
    print('Czy chcesz zagrać jeszcze raz? (Tak lub Nie)')
    return input().lower().startswith('y')

def zrobRuch(board, znak, ruch):
    board[ruch] = znak

    #Jeśli gracz wygra - True, jeśli przegra - False
def Wygral(board, znak):
return ((board[7] == znak and board[8] == znak and board[9] == znak)
(board[4] == znak and board[5] == znak and board[6] == znak) or    
(board[1] == znak and board[2] == znak and board[3] == znak) or    
(board[7] == znak and board[4] == znak and board[1] == znak) or     
(board[8] == znak and board[5] == znak and board[2] == znak) or    
(board[9] == znak and board[6] == znak and board[3] == znak) or    
(board[7] == znak and board[5] == znak and board[3] == znak) or 
(board[9] == znak and board[5] == znak and board[1] == znak) 
 def KopiaPlanszy(board):
 
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard
 def isSpaceFree(board, ruch):
    return board[move] == ' '
        
def RuchGracza(board):
    
    ruch = ' '
    while ruch not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(ruch)):
        print('What is your next move? (1-9)')
        ruch = input()
    return int(ruch)
        
