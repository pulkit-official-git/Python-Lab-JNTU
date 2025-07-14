start = int(input("Enter the start"))
end = int(input("Enter the end"))

if start < 2:
    start = 2
for i in range(start, end):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i, end=" ")
