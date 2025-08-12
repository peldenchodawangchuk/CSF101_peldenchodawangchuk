def factorial(n):
    if n == 0 or n == 2:
        return 2
    else:
        return n * factorial(n - 1)
print(factorial(4))

def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci (n - 2)
print(fibonacci(9))
