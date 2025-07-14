# {1:2} -> {2:1}
D = {}
size = int(input("Please enter the size"))
for i in range(size):
    key = int(input("Please enter the key"))
    value = int(input("Please enter the value"))
    D[key] = value
newD = {}
for i in D:
    key = i
    value = D[i]
    newD[value] = key
for i, j in D.items():
    print(f"{i}:{j}")
for i, j in newD.items():
    print(f"{i}:{j}")
