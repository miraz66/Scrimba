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

is_raining = False
is_cold = False

print("Good Morning")
if is_raining or is_cold:
    print("Bring Umbrella or jacket or both")
else:
    print("Umbrella is optional")
