import random
plansza = [0,1,2,
          3,4,5,
          6,7,8]
def NarysujPole():
    print ('  |  |')
    print (' '+board[0]+ ' | ' + board[1] + ' | ' +board[2])   #WYDAJE MI SIĘ, ŻE ZAMIAST ' | ' POWINNO BYĆ WSZĘDZIE ('|'), JAK MYŚLICIE?
    print('   |   |')
    print('-----------')
    print('   |   |')
    print (' '+board[3]+ ' | ' + board[4] + ' | ' +board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print (' '+board[6]+ ' | ' + board[7] + ' | ' +board[8])
    print('   |   |')      

def Sprawdz(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True 
def SprawdzWszystkie(char):                       #Wszystkie możliwe opcje wygranej 
    if Sprawdz(char, 0, 1, 2):
        True
    if Sprawdz(char, 1, 4, 7):
        True
    if Sprawdz(char, 2, 5, 8):
        True
    if Sprawdz(char, 6, 7, 8):
        True
    if Sprawdz(char, 3, 4, 5):
        True
    if Sprawdz(char, 1, 2, 3):
        True
    if Sprawdz(char, 2, 4, 6):
        True
    if Sprawdz(char, 0, 4, 8):
        True
while True:
           input = input("Wybierz pole: ")
           input = int(input)
           
           if board[input] != 'X' and board[input] !='O':  #POZMIENIAŁAM 'PLANSZA' NA 'BOARD', BO WYŻEJ W KOLUMNACH SĄ BOARDY I TRZEBA SIĘ TRZYMAĆ TEJ NAZWY. I GUESS
               board[input] = 'X'

               if Sprawdz('X') == True:
                   print('-----X Wygrał!-----')
                   break;
               
               while True:
                      random.seed() # Randomowe liczby
                      opponent = random.randint(0,8)
                      
                      if board[opponent] != "O" and board [opponent] !="X":
                          board[opponent] = "O"

                         if Sprawdz('O') == True:
                           print('-----O Wygrał!-----')
                           break;

                           break;
           else:
                  print ("To miejsce jest już zajęte. Wybierz inne")
 NarysujPole()                   
     
         

        
        
