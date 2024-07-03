import random as rd

while True:
    V=input('Do you want to roll the dice? (Yes/No):')
    if V=='Yes':
        V_1=rd.randint(1,6)
        print('You\'ve rolled a dice.')
        Var=int(input('Guess a int between 1 to 6:'))
        if Var==V_1:
            print('You\'ve guessed it right!!!')
        else:
            print('Better luck next time.')
    elif V=='No':
        print('Goodbye')
        break
    else:
        print('Enter a valid input.')