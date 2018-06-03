import random
plansza = [1,2,3,
           4,5,6,
           7,8,9]
def NarysujPole():
    print ('  |  |')
    print (' '+board[1]+ ' | ' + board[2] + ' | ' +board[3])
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
           
           if plansza[input] != 'X' and plansza[input] !='O':
                      plansza[input] = 'X'
                      random.seed() # Randomowe liczby
           else:
                      print "To miejsce jest już zajęte"
     
         

        
        
