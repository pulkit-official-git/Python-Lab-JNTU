import math

x1 = int(input("please enter x1"))
x2 = int(input("please enter x2"))
y1 = int(input("please enter y1"))
y2 = int(input("please enter y2"))

xdiff = (x2 - x1) ** 2
ydiff = (y2 - y1) ** 2

sum = xdiff + ydiff

distance = math.sqrt(sum)
print(distance)
