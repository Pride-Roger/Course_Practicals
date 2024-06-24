def Sum(V):
    Num=str(V)
    Total=0
    for z in Num:
        Total+=int(z)
    return Total
V=int(input('Enter a digit:'))
print(Sum(V))