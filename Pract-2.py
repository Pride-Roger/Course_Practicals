def Reverse(V):
    Rev=V[::-1]
    if V==Rev:
        print('Palindrome.')
    else:
        print('Not Palindrome.')
V=input('Enter a string value:')
Reverse(V.lower())