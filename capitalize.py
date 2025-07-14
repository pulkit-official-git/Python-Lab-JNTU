a = "hELLO wOrLd"
# Hello World
listOfStr = a.split(" ")
finalList = []
for word in listOfStr:
    newWord = word[0].upper() + word[1:].lower()
    finalList.append(newWord)
ans = " ".join(finalList)
print(ans)
