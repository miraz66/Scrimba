'''def greetings(name, age):
    print(f"Hello {name}, you are {age}!")


greetings("Miraz", 27)'''

'''
a = 7
b = 3
print('a == b is', a == b)
print('a != b is', a != b)
print('a > b is', a > b)
print('a < b is', a < b)
print('a >= b is', a >= b)
print('a <= b is', a <= b)
print('o in John is ', 'o' in 'John')  # membership
print('o in John is ', 'o' not in 'John')  # non membership
print('John is John ', 'John' is 'John')  # identity
print('John is not John is ', 'John' is not 'John')  # negative identity
'''
'''
is_raining = False
is_cold = False
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and jacket")
elif is_raining and not (is_cold):
    print("Bring Umbrella")
elif not (is_raining) and is_cold:
    print("Bring Jacket")
else:
    print("Shirt is fine!")
'''

'''
mode = input(
    'Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if mode.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif mode == '*':
        print(f'Answer is: {num1 * num2}')
    elif mode == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error!')
'''

# ----------------While Loop----------------
'''
i = 0
while i < 5:
    i += 1
    print(f'{i}.' + '*' * i + 'while loop are awesome' + '*' * i)

'''

'''num = 12
guess = 0
guess_limit = 3
guess_number = 1
guess = int(input(f'Guess a number 1-100: '))

while guess_number <= guess_limit:

    if guess != num:
        guess_number += 1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 1-100: '))
        else:
            guess = int(input(f'{guess} too low - Guess again 1-100: '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break

if guess != num:
    print(f'Sorry you lose! It was {num}')'''


# -----------------For Loop -----------------
'''friends = {'John', 'Terry', 'Eric', 'Michael', 'George'}

for friend in friends:
    if friend == "Terry":
        print("Found " + friend + "!")
        break
    print(friend)

print("For Loops")'''

'''friends = ['John', 'Terry', 'Eric', 'Michael', 'George']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
msg = 'You are invited to the party on saturday.'
friends += friends1

for index in range(2):
    friends.append(input('Enter a new friend: '))

for num, name in enumerate(friends, 1):
    print(f"{num}.{name.title()}! {msg}")'''

'''friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
efriends = [(51, 'Brian'), (52, 'Judith'), (53, 'Reg'),
            (54, 'Loretta'), (55, 'Colin')]

for num, friend in enumerate(friends, 2):
    print(num, friend)

print(type(enumerate(friends)))
print(list(enumerate(friends, 100)))'''


'''for num, letter in enumerate("Md.Mirajul islam", start=1):
    print(num, letter)'''

'''my_list = [1, 5, 3, 7, 2]
my_dict = {'car': 4, 'dog': 2, 'add': 3, 'bee': 1}
my_tuple = ('d', 'c', 'e', 'a', 'b')
my_string = 'python'

print(sorted(my_dict.items()))
print(my_list[::-1])
print(list(reversed(my_list)))'''


'''my_list = [1, -4,  5, 0, -3, 7, -2, -5]
my_llist = [['car', 4, 65, 100], ['dog', 2, 30, 500],
            ['add', 3, 10, 200], ['bee', 1, 24, 400]]


print(sorted(my_list, key=abs))
print(sorted(my_llist, key=lambda item: item[3]))'''

'''movie = {
    'title': 'Life of Brian',
    'year': 1979,
    'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']
}
print(movie.get('', "Not Fount!",))
for key, value in movie.items():
    print(key, value)'''

python = {'John': 35, 'Eric': 36, 'Michael': 35,
          'Terry': 38, 'Graham': 37, 'TerryG': 34}
holy_grail = {'Arthur': 40, 'Galahad': 35,
              'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17}
life_of_brian = {'Brian': 33, 'Reg': 35,
                 'Stan/Loretta': 32, 'Biccus Diccus': 45}


print('Arthur' in holy_grail)
if 'Arthur' not in python:
    print('He\'s not here!')
people = {}
people1 = {}
people2 = {}
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(sorted(people))

for groups in (python, holy_grail, life_of_brian):
    people1.update(groups)
print(sorted(people1))

people2 = {**python, **holy_grail, **life_of_brian}
print(sorted(people2))

print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print('The sum of the ages: ', sum(people.values()))
print(people.values())
