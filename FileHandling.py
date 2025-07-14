with open("f1.txt", "r") as f1, open("f2.txt", "r") as f2, open("f3.txt", "w") as f3:
    f3.write(f1.read() + f2.read())
