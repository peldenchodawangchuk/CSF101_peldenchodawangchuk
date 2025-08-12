def greet_with_default(name='Guest'):
    print(f'hey, {name}')

greet_with_default()
greet_with_default('bbg')

def calculate_rectangle_area(width, height):
    return width * height

area = calculate_rectangle_area(5, 6)
print(f'The area of the rectangle is: {area}')

def print__info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
print__info(name='pogi', age=18, city='thimphu')

def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([6, 9 , 8, 5, 3])
print(f'Min: {result[0]}, Max: {result[1]}')

def safe_divide(x, u):
    if u == 0:
        return 'cannot divide by zero'
    return x/u

print(safe_divide(10,2))
print(safe_divide(5,0))