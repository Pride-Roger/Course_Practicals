try:
    V=int(input('Enter a denominator value:'))
    D=10/V
except ZeroDivisionError:
    print('Please don\'t zero.')
else:
    print(D)
finally:
    print('The code is executed successfully!')