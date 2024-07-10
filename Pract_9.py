try:
    Dict={'Key_1': 'Value_1', 'Key_2': 'Value_2', 'Key_3': 'Value_3'}
    Input=input('Enter a key to retrieve corresponding value from the dictionary:')
    print(Dict[Input.capitalize()])

except KeyError:
    print('The key does not exist.')

finally:
    print('The code executed successfully!')