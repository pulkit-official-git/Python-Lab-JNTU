def isSorted(a):
    temp = a[0]
    for i in range(1, len(a)):
        if temp > a[i]:
            return False
        temp = a[i]
    return True


a = [1, 2, 3, 4, 5, 1]
print(isSorted(a))
