import random
import string

length=int(input("Enter the length of your password: "))
chars=string.ascii_letters + string.digits + "@#$%^&*()"
password=""
for i in range(length):
    password+=random.choice(chars)
print("Password is:",password)