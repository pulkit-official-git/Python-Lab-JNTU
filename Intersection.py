import numpy as np

l1 = [1, 2, 3, 3, 4, 5]
l2 = [8, 9, 3, 4, 1]

# way1
ans = []

for i in l1:
    if i in l2 and i not in ans:
        ans.append(i)
print(ans, "****************")

# way2

al1 = np.array(l1)
al2 = np.array(l2)

way2Ans = np.intersect1d(al1, al2)
print(way2Ans, "#############")
