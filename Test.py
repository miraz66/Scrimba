msg = 'welcome to Python 101: Strings'
msg1 = msg[18] + " " + msg[:8] + msg[8:10] + msg[10:17]


print(msg1)
print(msg.replace("Strings", "Release"))

# input creacor`python`
# name = input("What is your name? : ")
# age = input("What is your age? : ")

# print("Hello " + name + "! You are " + age + " years old.")

name = input("Enter your name: ")
distance_km = input("Enter your distance_km: ")
distance_mi = float(distance_km) / 1.609

print(f"Hi {name.title()}! {distance_km} Km is equivalent to {distance_mi} miles.")
