def isPalindrome(x):
    reverseX = x[::-1]
    if x == reverseX:
        return True
    else:
        return False


x = input("Please enter the string")
print(isPalindrome(x))
