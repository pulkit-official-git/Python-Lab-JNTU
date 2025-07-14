def fileStats(filename):
    with open(filename, "r") as f:
        text = f.read()

    words = len(text.split())
    vowels = 0
    spaces = 0
    lowers = 0
    uppers = 0

    for i in text:
        if i.lower() in "aeiou":
            vowels += 1
        if i == " ":
            spaces += 1
        if i.islower():
            lowers += 1
        if i.isupper():
            uppers += 1

    print("word count : ", words)
    print("space count : ", spaces)
    print("vowel count : ", vowels)
    print("lowercase count : ", lowers)
    print("uppercase count : ", uppers)


fileStats("f3.txt")
