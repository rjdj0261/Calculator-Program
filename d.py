import math
q = True
def remainder(x, y):
    remainder(x, y)
def absolute(x):
    return abs(x)
def power(x, y):
    return x ** y
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x/y
while q == True:
    choice = input("""
    Select operation.
    1.Add      | 5.Power
    2.Subtract | 6.Absolute Value
    3.Multiply | 7.Remainder
    4.Divide   | 8.Quit
    Enter choice(1/2/3/4/5/6/7/8): """)
    if choice == '1':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1, " + ", num2, " = ", add(num1, num2))
    elif choice == '2':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1, " - ", num2, " = ", subtract(num1, num2))
    elif choice == '3':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1, " * ", num2, " = ", multiply(num1, num2))
    elif choice == '4':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1, "/", num2, " = ", divide(num1, num2))
    elif choice == '5':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1, " ** ", num2, " = ", power(num1, num2))
    elif choice == '6':
        num1 = int(input("Enter first number: "))
        print(num1, " = ", absolute(num1))
    elif choice == '7':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1, "//", num2, " = ", (num1 // num2))
    elif choice == '8':
        print("Thanks For trying The Basic Calculator!!!")
        q = False
    else:
        print("Invalid Input!!!")