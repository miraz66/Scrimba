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

'''
i = 0
while i < 5:
    i += 1
    print(f'{i}.' + '*' * i + 'while loop are awesome' + '*' * i)

'''
'''
num = 12
guess = 0
guess_limit = 3
guess_number = 0

while guess_number < guess_limit:
    guess = int(
        input(f'Guess # {guess_number + 1} a number 1-20: last guess:{guess} '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    else:
        print(f'No, not {guess}!')
        guess_number += 1
if guess != num:
    print(f'Sorry you lose! It was {num}')
'''

num = 12
guess = 0
guess_limit = 3
guess_number = 1

while guess_number <= guess_limit:
    guess = int(
        input(f'Guess # {guess_number } a number 1-20: last guess:{guess} '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    else:
        print(f'No, not {guess}!')
        guess_number += 1
if guess != num:
    print(f'Sorry you lose! It was {num}')
4
