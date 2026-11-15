def greet(name):
    print("Hello,", name)

def square(number):
    return number * number

def bigger(a, b):
    if a > b:
        return a
    else:
        return b

greet("Raj")

n = int(input("Enter a number: "))
print("Square:", square(n))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Bigger number:", bigger(x, y))
