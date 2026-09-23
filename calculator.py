import json

def add(a, b):
    return a + b


def subtract(a, b):
    if a > b:
        return a - b
    return b - a


def multiply(a,b):
    return a * b


def divide(a,b):
    if b == 0:
        return "divide by zero error"
    return a / b

while True:
    try:
        a = float(input("Enter a"))
        break
    except ValueError:
        print("Invalid i/p , please eneter valid number")



while True:
    try:
        b = float(input("Enter b"))
        break
    except ValueError:
        print("Invalid i/p , please eneter valid number")


c=input("Enter operation")


if c=="+":
    add(a,b)

elif c=="-":
    subtract(a,b)

elif c=="*":
    multiply(a,b)

elif c=="/":
    divide(a,b)

else:
    print("Invalid operation")
