try:
    V=int(input('Enter the first number:'))
    V_1=int(input('Enter the second number:'))
    V_2=V/V_1
except ValueError as VE:
    print(f'Your input caused a {VE}')
except ZeroDivisionError as ZDE:
    print(f'Your inout caused a {ZDE}')
else:
    print(V_2)
finally:
    print('The code has executed successfully!')