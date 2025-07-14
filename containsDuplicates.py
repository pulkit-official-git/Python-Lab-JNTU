def containsDuplicates(a):
    b = []
    for i in a:
        if i in b:
            return True
        b.append(i)
    return False


a = [1, 2, 3, 5, 7, 4]
print(containsDuplicates(a))
