a = 10
def print_a():
    print(f'Local a: {a}')

print_a()
print(f'Global a: {a}')

count = 0
def increment():
    global count
    count += 1
    print(f'count: {count}')

increment()
increment()
print(f'Final count : {count}')

def outer():
    x = 'outer'
    
    def inner():
        nonlocal x
        x = 'inner'
        print(f'Inner x: {x}')
        
    inner()
    print(f'outer x: {x}')

outer()