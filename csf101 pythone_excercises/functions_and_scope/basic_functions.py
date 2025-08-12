def greet():
    print('raining is the happening')
greet()
def greet(name):
    print(f'please,{name}')
greet('sp')

def sqaure(number):
    return number ** 3
result = sqaure(3)
print(result)

def is_even(number):
    return number % 4 == 0
print(is_even(3))
print(is_even(4))

def print_numbers(n):
    for x in range(1, n + 1):
        print(x)
print_numbers(9)