msg = 'welcome to Python 101: Strings'
msg1 = msg[18] + " " + msg[:8] + msg[8:10] + msg[10:17]


print(msg1)
print(msg.replace("Strings", "Release"))

# -----input creacor`python-----`

# name = input("What is your name? : ")
# age = input("What is your age? : ")

# print("Hello " + name + "! You are " + age + " years old.")

# name = input("Enter your name: ")
# distance_km = input("Enter your distance_km: ")
# distance_mi = int(distance_km) / 1.609

# print(f"Hi {name.title()}! {distance_km} Km is equivalent to {round(distance_mi,1)} miles.")

# -----Array of distances -----
# friends = ["Inzam", "Al-amin", "Al-amin-E",
#            "Monju", "Monju-E", "Tuhin", "Tuhin-E",]

# cars = [911, 471, 158, 177, 28, 228, 255,]


# print(friends)
# print(sum(cars))

sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
# sales.extend(sales_w1)
# sales.extend(sales_w2)
sales = sales_w1 + sales_w2
sales.sort()
print(sales)
worst_day_prof = sales[0] * 1.5
print(worst_day_prof)
