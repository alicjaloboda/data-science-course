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

# Dictionaries

user_dict = {
    'first_name': 'John',
    'last_name': 'Doe',
    'birth_year': 1998
}

print(user_dict['birth_year'])
print(user_dict.get('last_name'))
user_dict['major'] = 'Math'
print(user_dict)

#Lenth
print(len(user_dict))
#remove
user_dict.pop('major')
print(user_dict)
del user_dict['birth_year']
user_dict.clear() #clear the dictionary
print(user_dict)

vehicle = {
    'model': 'Opel',
    'make': 'Volkswagen',
    'year': 2013,
    'mileage': 100000
}
print(vehicle['year'])
vehicle['year'] = 2008
vehicle['type'] = 'car'
vehicle.pop('make')
print(vehicle)

user_dict = {
    'first_name': 'John',
    'last_name': 'Doe',
    'birth_year': 1990
}

#Loops
for x,y in user_dict.items():
    print(x,y)

if 'birth_year' in user_dict:
    print('yes birth_year exists')

dict2 = user_dict
dict2.popitem() # usuwa zmienną również w user_dict
print(f'user dict {user_dict}')
print(f'dict2 {dict2}')

#Copy
dict3 = user_dict.copy()
dict3.popitem()
print(f'user_dict {user_dict}')
print(f'dict3 {dict3}')

#Nested dictionary
family = {
    'child1': {
        'first_name': 'John',
        'last_name': 'Doe',
        'birth_year': 1998
    },
    'child2': {
        'first_name': 'Mary',
        'last_name': 'Doe',
        'birth_year': 1993
    },
        'first_name': 'Peter',
        'last_name': 'Doe',
        'birth_year': 1995
}
print(family)

vehicle = {
    'model': 'Opel',
    'make': 'Volkswagen',
    'year': 2013,
    'mileage': 100000
}
for x,y in vehicle.items():
    print(x,y)

vehicle2 = vehicle.copy()
vehicle2['number of tires'] = 4

print(f'vehicle {vehicle}')
print(f'vehicle2 {vehicle2}')

#Key = word,Value = number of times the word appears
sentence = 'I am so happy to learn Python which makes my wife happy and interested in Python Python Python Python'

sentence_dict = {}
for each_word in sentence.split(' '):
    sentence_dict[each_word] = sentence_dict.get(each_word, 0) + 1
print(sentence_dict)
'''
'''
# tuples - krotki - wartości nie mogą być zmieniane
my_tuple = (1,2,3,4,5)
print(my_tuple[1:4])

for x in my_tuple:
    print(x)
print(len(my_tuple))

'''
'''
# Sets - typ struktury danych, podobnie jak listy. 
# Listy są odrobinę szybsze, gdy chcesz przechodzić przez kolejne elementy
# Sets są o wiele szybsze, gdy chcesz sprawdzić, czy dany element znajduje się w nim
# Najczęściej używane do usuwania duplikatów - mogą zawierać jedynie unikalne wartości

my_set = {'jabłka', 'banany', 'melony','ananasy','itd...'}
print(my_set) #za każdym razem set wyświetla się w innej kolejności, ponieważ jest to zbiór nieuporządkowany
print('jabłka' in my_set) #sprawdza, czy dany element znajduje się w secie

for x in my_set:
    print(x)

# nie można indeksować set - na przykład print(my_set[3])

my_set.remove('ananasy')
print(my_set)
# my_set.remove('pomarańcze') - będzie błąd
my_set.discard('pomarańcze') # nie będzie błędu! remove jest bezpieczniejszą opcją
#my_set.clear() - możemy wyczyścić set

set_one = {1,2,3,4,5}
set_two = {6,7,8,9,10}

set_three = set_one.union(set_two) #union łączy zbiory

my_set.add('pomarańcze')
my_set.update(['śliwki', 'wiśnie'])
print(my_set)
print(len(my_set))
'''
# IMPORTOWANIE MODUŁÓW I BIBLIOTEK - pliki homework.py + grade_average_service.py

# Odczytywanie i zapis do pliku tekstowego
'''
f = open('text.txt', 'r')
print(f.read()) #odczyt całego pliku
#musi się zakończyć funkcją CLOSE, bo inaczej może dojść do memory leak 
f.close()
'''
#Context Manger automatycznie otworzy i zamknie odczytywany plik
'''
with open('text.txt', 'r') as f:
    #print(f.readline()) #zczytuje pierwszą linię, READLINES() zczytuje wszystkie linie jako listę
    #for line in f:
        #print(line, end='')
    print(f.read(10))
    print(f.read(20))
    print(f.read(10))
    print(f.tell) #podaje, na którym znaku się zatrzymaliśmy czytając plik (czyli tu będzie 30)

with open('text2.txt', 'w') as f:
    f.write('this is a new file and some text')
#jeżeli plik już istniał, to go nadpisze nowym tekstem

#Data i Czas
import datetime

today = datetime.date.today()
print(today)
print(today.weekday())
# weekday = Poniedziałek = 0, Niedziela = 6
# isoweekday = Poniedziałek = 1, Niedziela = 7
print(today.isoweekday())
create_day = datetime.date(2020,6,9)
print(create_day)
date_string = '2020-06-19'
date_object = datetime.date.fromisoformat(date_string)
time_delta = datetime.timedelta(days=5)
print(date_object + time_delta)

# Try & Catch 
try:
    # x = 10 * (1/0)
    x = '2' + 2
    print(x)

except ZeroDivisionError as e:
    print(f'{e} : Nie można dzielić przez zero!')
except TypeError as e:
    print(f'{e} : Błędny typ danych')
except Exception as e:
    print(f'ERROR! : {e}' )
finally:
    print('Pokaż to, nieważne co było wcześniej')

try:
    x = None
    if x is None:
        raise Exception

except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(f'x to nic, nie można znaleźć odpowiedzi')

'''