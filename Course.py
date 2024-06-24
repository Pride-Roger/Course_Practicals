def Calculate_P(l,b):
    P=(l+b)*2
    return P
l=int(input('Enter the value for length:'))
b=int(input('Enter value for Breadth:'))
print('Perimeter of the rectangle is',
      Calculate_P(l,b),'cm')