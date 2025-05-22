def add(num1,num2):
    add=num1+num2
    return add
def subtract(num1,num2):
    subtract=num1-num2
    return subtract
def multiply(num1,num2):
    multiply=num1*num2
    return multiply
def divide(num1,num2):
    try:
        divide=num1/num2
        return divide
    except ZeroDivisionError:
        print("Division by zero is not possible")
def power(num1,num2):
    power=num1**num2
    return power

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. square root")

choice=int(input("Enter your choice:"))

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if choice==1:
    print("Add:",add(num1,num2))
elif choice==2:
    print("Subtract:",subtract(num1,num2))
elif choice==3:
    print("Multiply:",multiply(num1,num2))
elif choice==4:
    print("Divide:",divide(num1,num2))
elif choice==5:
    print("square root:",power(num1,num2))
else:
    print("Invalid choice")