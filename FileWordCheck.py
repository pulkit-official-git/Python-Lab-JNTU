def checkWord(filename, word):
    with open(filename, "r") as f:
        # print(f.read().split())
        return word in f.read().split()


filename = "f3.txt"
word = input("Please enter the word")

print(checkWord(filename, word))
