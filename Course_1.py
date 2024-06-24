def celsius_to_fahrenheit(C):
    F=(9/5)*C+32
    return F
C=int(input('Enter temperature in degree celsius'))
print(celsius_to_fahrenheit(C))