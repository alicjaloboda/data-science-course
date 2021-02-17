#python --version

print('You\'re \nwelcome')

statement = '''
This
Is
Very
Important
'''
print(statement)

first_name = 'Ala'
last_name = 'Loboda'
#hello_text = 'Hello, {} {}'.format(first_name,last_name)
hello_text = 'Hello, {first} {last}'.format(first=first_name,last=last_name)
print(hello_text)

my_name = 'ala'
my_age = 25
hello_statement = f'{my_name} is {my_age} years old'
print(hello_statement)
print(hello_statement.upper())
print(hello_statement.lower())
print(hello_statement.capitalize())
print(hello_statement.count('a'))
print(hello_statement.endswith('a'))
print(hello_statement.isdigit())

name = input('Enter your name: ')
age = input('Enter the year you were born: ')
print(f'{name} was born on {age}')