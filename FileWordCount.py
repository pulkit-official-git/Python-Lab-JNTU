with open("f3.txt", "r") as f3:
    data = f3.read()
words = data.split()
# print(words)

d = {}
for i in words:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
# print(d)

maxCount = 0
maxWord = ""
for i in d:
    if d[i] > maxCount:
        maxCount = d[i]
        maxWord = i
print(maxCount)
print(maxWord)
