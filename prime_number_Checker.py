prime=int(input("Enter a number to check prime or not: "))
p=0
for i in range(1,prime+1):
    if prime%i==0:
       p+=1
if p==2:
    print("It is a prime number")
else:
    print("It is not a prime number")