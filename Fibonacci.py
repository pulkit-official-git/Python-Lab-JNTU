n = int(input("Please enter range"))
a = 0
b = 1
if n == 1:
    print(a)
else:
    print(a, b, end=" ")
    count = 2
    while count < n:
        sum = a + b
        a = b
        b = sum
        count += 1
        print(sum, end=" ")
