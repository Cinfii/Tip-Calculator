print("Welcome to the Tip Calculator!")
bill = int(input("What was the total bill? $"))
tip_percent = int(input("How much would you like to tip? 10, 12, or 15? "))
tip = tip_percent / 100
no_people = int(input("How many people would you like to split the bill with? "))
total = bill + (bill * tip)
total_total = total / no_people
print(f"Each person should pay ${round(total_total, 2)}.")
