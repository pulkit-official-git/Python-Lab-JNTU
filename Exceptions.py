# IndexError
# ZeroDivisionError


try:
    a = [1, 2, 3, 4, 5]
    print(a[8])
except IndexError:
    print("Index out of bound")
except ZeroDivisionError:
    print("division by zero not possible")
