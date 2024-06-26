import random as rd
V=rd.randint(1,6)
Var=int(input('Enter an int between 1 to 6:'))
if Var==V:
    print('You\'ve guessed it correct.')
else:
    print('Better luck next time.')