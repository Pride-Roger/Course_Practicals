Var=int(input('Enter your weight:'))
Var_1=int(input('Enter your height:'))
BMI=Var/(Var_1*Var_1)

if BMI<18.5:
    print('You are underweight.')
elif 18.5<=BMI<24.9:
    print('You are normal weight.')
elif 25<=BMI<29.9:
    print('You are Overwight.')
elif BMI >=30:
    print('You are obese.')