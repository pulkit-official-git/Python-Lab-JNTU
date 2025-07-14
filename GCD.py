def GCD(a, b):
    while b > 0:
        t = a % b
        a = b
        b = t
    return a


a = int(input("Enter first number"))
b = int(input("Enter the second number"))
print(GCD(a, b))
