import random
plansza = [1,2,3,
           4,5,6,
           7,8,9]
def NarysujPole():
    print ('  |  |')
    print (' '+board[1]+ ' | ' + board[2] + ' | ' +board[3])   #WYDAJE MI SIĘ, ŻE ZAMIAST ' | ' POWINNO BYĆ WSZĘDZIE ('|'), JAK MYŚLICIE?
    print('   |   |')
    print('-----------')
    print('   |   |')
    print (' '+board[4]+ ' | ' + board[5] + ' | ' +board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print (' '+board[7]+ ' | ' + board[8] + ' | ' +board[9])
    print('   |   |')      
        
while True:
           input = input("Wybierz pole: ")
           input = int(input)
           
           if board[input] != 'X' and board[input] !='O':  #POZMIENIAŁAM 'PLANSZA' NA 'BOARD', BO WYŻEJ W KOLUMNACH SĄ BOARDY I TRZEBA SIĘ TRZYMAĆ TEJ NAZWY. I GUESS
                      board[input] = 'X'
                      random.seed() # Randomowe liczby
                      opponent = random.randint(0,8)
                      
                      if board(opponent) != "o" and board (opponent) !="x":
                                 board(opponent) = "o"
           else:
                      print ("To miejsce jest już zajęte. Wybierz inne")
                      
     
         

        
        
