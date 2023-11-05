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

friends = ['John', 'Terry', 'Eric', 'Michael', 'George']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
msg = 'You are invited to the party on saturday.'
friends += friends1

for index in range(2):
    friends.append(input('Enter a new friend: '))

for num, name in enumerate(friends, 1):
    print(f"{num}.{name.title()}! {msg}")

friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
friends1 = ['John1', 'Terry2', 'Eric3', 'Michael4', 'George5']
