import numpy as np


myList = [1, 2, 3, 4, 5]
myTuple = (1, 2, 3, 4, 5)
# mySet = {1, 2, 3, 4, 5}. #how to create a set

ListToArray = np.array(myList)
TupleToArray = np.array(myTuple)

print(type(ListToArray))
print(type(TupleToArray))
