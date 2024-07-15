Correct='1234'

user_input=''

while user_input!=Correct:
    user_input=input('Enter the password:')
    if user_input==Correct:
        print('Access Granted!!!')
    else:
        print('Incorrect password, please try again.')
print('You have successfully entered your account!!!')