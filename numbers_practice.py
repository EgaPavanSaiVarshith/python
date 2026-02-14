# Python Numbers Practice

# Integer Operations
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

print("-------------")

# Float Operations
x = 5.5
y = 2.2

print("Float Addition:", x + y)
print("Float Multiplication:", x * y)

print("-------------")

# Type Checking
print("Type of a:", type(a))
print("Type of x:", type(x))

print("-------------")

# Type Conversion
num1 = "25"
num2 = 5
num1 = int(num1)

print("Converted Addition:", num1 + num2)

print("-------------")

# Even or Odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("-------------")

# Prime Number Check
n = int(input("Enter number to check Prime: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
else:
    print("Not Prime")
