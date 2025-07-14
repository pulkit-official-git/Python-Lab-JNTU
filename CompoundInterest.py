principle = int(input("PLease enter the principle"))
rate = float(input("Please enter the rate"))
time = int(input("please enter time in years"))

amount = principle * (1 + (rate / 100)) ** time
# print(amount)
ci = amount - principle
print("Compount Interest is", ci)
