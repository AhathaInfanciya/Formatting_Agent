
import json
def add(a,b):
    return a + b


def subtract(a,b):
    if a > b:
        return a - b
    else:
        return b - a


def multipy(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "divide by zero error"
    return a / b


a = int(input("Enter a"))
b = int(input("Enter b"))
