def removeDuplicates(a):
    b = []
    for i in a:
        if i in b:
            continue
        b.append(i)
    return b


a = [1, 2, 3, 5, 2, 3, 7, 4]
# b=[1, 2, 3, 5, 7, 4]
print(removeDuplicates(a))
