'''msg = 'welcome to Python 101: Strings'
msg1 = msg[18] + " " + msg[:8] + msg[8:10] + msg[10:17]


print(msg1)
print(msg.replace("Strings", "Release"))'''

# -----input creacor`python-----`

'''name = input("What is your name? : ")
age = input("What is your age? : ")

print("Hello " + name + "! You are " + age + " years old.")

name = input("Enter your name: ")
distance_km = input("Enter your distance_km: ")
distance_mi = int(distance_km) / 1.609

print(f"Hi {name.title()}! {distance_km} Km is equivalent to {round(distance_mi,1)} miles.")'''

# -----Array of distances -----
'''friends = ["Inzam", "Al-amin", "Al-amin-E",
           "Monju", "Monju-E", "Tuhin", "Tuhin-E",]

cars = [911, 471, 158, 177, 28, 228, 255,]


print(friends)
print(sum(cars))'''

'''
# sales_w1 = [7, 3, 42, 19, 15, 35, 9]
# sales_w2 = [12, 4, 26, 10, 7, 28]
# sales = []
# new_day = input('Enter #of lemonades for new day: ')
# sales_w2.append(int(new_day))
# sales.extend(sales_w1)
# sales.extend(sales_w2)
# sales.sort()

# print(sales)

# worst_day_prof = min(sales) * 1.5
# best_day_prof = max(sales) * 1.5
# print(f'Worst day profit:$ {worst_day_prof}')
# print(f'Best day profit:$ {best_day_prof}')
# print(f'Combined profit:$ {worst_day_prof + best_day_prof}')'''


'''# msg = 'Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham']
# print('Welcome to Python 101: Split and Join')

# print(" ".join(friends_list))
# print(" ".join(msg.split()))

# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = (','.join(','.join(csv.split(';')).split(':')).split(','))
# print(friends_list)
# print(csv.replace(";", ",").replace(":", ",").split(','))'''

'''
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')  # Tuples Array
friends_set = {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Eric'}
my_friends_set = {'Reg', 'Loretta', 'Colin', 'Eric', 'Graham', 'Terry'}

print(friends)
print(friends_tuple)
print(friends_set.union(my_friends_set))
'''

'''
friends = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
my_friends = {'Reg', 'Loretta', 'Colin', 'John', 'Graham'}
cars = ['900', '420', 'V70', '911', '996',
        'V90', '911', '911', 'S', '328', '900']

print("Eric" in friends and "John" in friends and "Terry" in friends)
print(friends.union(my_friends))
print(friends | my_friends)
print(friends.intersection(my_friends))
print(friends & my_friends)
print(friends.difference(my_friends))
print(friends - my_friends)
print(friends.symmetric_difference(my_friends))
print(friends ^ my_friends)
cars_no_dupl = list(set(tuple(cars)))
print(cars_no_dupl)
'''

cars = [911, 471, 158, 177, 28, 228, 255,]
cars = [911, 471, 158, 177, 28, 228, 255,]
cars = [911, 471, 158, 177, 28, 228, 255,]
