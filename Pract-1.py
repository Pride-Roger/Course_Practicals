def Sum(n):
    num=str(n)
    total=0
    for i in num:
        total+=int(i)
    return total
n=int(input('Enter the number:'))
print('Sum of Digits:', Sum(n))