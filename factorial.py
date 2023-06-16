def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
number = int(input("Enter a number:"))
result = factorial(number)
print("Factorial of number:",result)
