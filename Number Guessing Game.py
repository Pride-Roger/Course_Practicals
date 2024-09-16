import random as rd

def play_game():
    print('Choose the difficulty level:')
    print('1. Easy (1-10, 3 lives)')
    print('2. Medium (1-50, 5 lives)')
    print('3. Hard (1-100, 7 lives)')
    
    choice=int(input('Enter your choice:'))
    
    if choice==1:
        max_number=10
        lives=3
    elif choice==2:
        max_number=50
        lives=5
    elif choice==3:
        max_number=100
        lives=7
    else:
        print('Invalid choice, selecting easy level automatically.')
        max_number=10
        lives=3
        
    secret_number=rd.randint(1, max_number)
    chances=0
    
    print(f'Guess the number between 1 and {max_number}. You have {lives} chances.')
    
    while chances<lives:
        num=int(input('Guess the number:'))
        chances+=1
        
        if (num==secret_number):
            print('Congratulations you have guessed it right!')
            break
        elif (num<secret_number):
            print('Too low, guess higher.')
        else:
                print('Too high, guess lower.')
        print(f'{chances} chance is over!')
    if num !=secret_number:
        print(f'Better luck next time! The correct number was {secret_number}')
        
def main():
    print('Welcome to nuumber guessing game!')
    
    while True:
        play_game()
        
        playgame=input('Do you want to play the game again (yes/no):')
        
        if playgame=='no':
            print('Thanks for playing!')
            break

main()