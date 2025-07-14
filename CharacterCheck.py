ch = input("Please enter the character")

if ch >= "0" and ch <= "9":
    print(" Its a digit ")
elif ch.islower():
    print("Its a lowercase")
elif ch.isupper():
    print("Its an uppercase")
else:
    print("Its a special character")
