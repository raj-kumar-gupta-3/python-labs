print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

n = int(input("Enter a number for its table: "))
print("Table of", n)
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
