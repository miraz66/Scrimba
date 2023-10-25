def greetings(name, age):
    print(f"Hello {name}, you are {age}!")


greetings("Miraz", 27)

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


'''num1 = float(input('Enter first number: '))
mode = input('Enter math operation(+,-,*,/): ')
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
    print('Input error!')'''

mode = input("Enter your Calculation: ")


print(mode)
