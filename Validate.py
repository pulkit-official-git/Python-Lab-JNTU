phone = input("Please enter the phone number")

if len(phone) == 10 and phone.isdigit():
    print("phone is valid")
else:
    print("phone is invalid")

email = input("Please enter the email")

if "@" in email and "." in email:
    print("email is valid")
else:
    print("email is invalid")
