#python --version
'''
print('You\'re \nwelcome')

statement = 
This
Is
Very
Important

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

#name = input('Enter your name: ')
#age = input('Enter the year you were born: ')
#print(f'{name} was born on {age}')

my_list = [6,7,8,9,8,10]
my_list[1] = 13
print(my_list[0])
print(my_list[-1])
print(len(my_list))
print(my_list[0:2])
print(my_list[1:4])
print(my_list[0:4:2])

new_list = my_list[1:3]

#dodawanie nowych elementów do listy
my_list.append(11)
my_list.insert(3, 12)
my_list.remove(8) # usuwa daną wartość (pierwsze wystąpienie) z tablicy
my_list.pop(2) # usuwa wartość z danego indeksu
my_list.reverse() # odwraca kolejność listy
my_list.sort() # trzeba najpierw posortować przed wyświetleniem, nie zadziała sortowanie w poleceniu print
print(my_list)

#listy zagnieżdżone
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print(nested_list)
print(len(nested_list))
print(nested_list[1])
print(nested_list[1][2])

#warunek if
hour = 18
if hour < 15:
    message = 'Good morning'
elif hour < 20:
    message = 'Good afternoon'
else:
    message = 'Good night'
print(message)

#pętle
number_list = [1, 2, 3, 4, 5]
for x in number_list:
    print(x)
for x in range(3,6):
    print(x)

sum_of_loop = 0
for x in range(3,6):
    sum_of_loop += x
    print(sum_of_loop)
    
co_workers = ['Ala','Marek','Łukasz']
for x in co_workers:
    if x == 'Ala':
        print('Hello Ala')
    elif x == 'Marek':
        print('Hello Marek')
    else:
        print('Hello Łukasz')

for x in co_workers:
    print(f'Hello {x}!')

for x in co_workers:
    if x == 'Marek':
        print('hello Marek')
        break
Pętle WHILE:

while x < 10:
    x += 1
    if x == 6:
        continue
    print(x)

while x < 10:
    print(x)
    x += 1
else:
    print('x jest równe lub większe niż 10')

tablica = [1,2,3,4,5,6,7,8]

for x in tablica:
    if x == 3 or x== 7:
        continue
    print(x)

liczba = 5
while liczba > 0:
    print(liczba)
    liczba -= 1
else liczba == 0:
        print('GO!')

for number in range(1,50):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

#Functions

print('Hello from outside the function')

def my_function():
    print('Hello from within the function!')

my_function()

def print_name(first_name, last_name):
    print(f'Hello {first_name} {last_name}')

print_name('Ala', 'Lala')

def remove_elements(lista):
    lista.pop(0)
    lista.pop(-1)
    return lista

moja_lista = [0,1,2,3,4,5,6]
nowa_lista = remove_elements(moja_lista)
print(nowa_lista)

# Funkcje rekursywne
# 5*4*3*2*1

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

factorial_number = factorial(5)
print(factorial_number)

#Fibonacci - funkcja rekursywna

def fib_seq(amount):
    if amount == 0:
        return 0
    elif amount == 1:
        return 1
    else:
        return fib_seq(amount-2) + fib_seq(amount - 1)

print(fib_seq(13))

for x in range(13):
    print(fib_seq(x))
'''

pozdrowienia = 'Witaj, w świecie Pythona!'
#Indexing
#print(pozdrowienia[0])

#Slicing
#print(pozdrowienia[0:7])
#print(pozdrowienia[0:10:2])

#length
#print(len(pozdrowienia))

#zwraca listę oddzieloną znakiem podanym w nawiasie
#print(pozdrowienia.split(','))

#znajduje i zwraca index
#print(pozdrowienia.find('Python'))

#Joins
#print(pozdrowienia, ':'.join('abcdefg'))
#print(pozdrowienia, ':'.join(('10','23','15','10000000023')))
'''
haslo = ' abc123      !

if haslo.strip() == 'abc123!':
    print('Hasło poprawne')
else:
    print('Hasło niepoprawne!')
'''

#nowe_pozdrowienia = pozdrowienia.replace('Witaj','Cześć')
#print(nowe_pozdrowienia)

success = 'Do or do not there is no try'
print(success[0:12])

success_quote = 'you win some and you lose some'
new_success_quote = success_quote.replace('lose','learn')
print(new_success_quote)

string_list = 'lets make this a list'
list_variable = string_list.split()
print(list_variable)
print(string_list[2])