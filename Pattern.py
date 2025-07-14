# square pattern

# n = int(input("Please enter length"))

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i, end=" ")
#     print()

n = int(input("Please enter length"))

for i in range(1, n + 1):
    for j in range(i):
        print(5 - i + 1, end=" ")
    print()
