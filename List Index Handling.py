try:
    V=[1,2,3,4,5,6,7,8,9,0]
    Input=int(input('Enter an index of an element:'))
    print(V[Input])

except ValueError:
    print('Enter a numeric value.')
except IndexError:
    print('You\'ve entered an index that is out of the range.')

finally:
    print('The code executed successfully!')