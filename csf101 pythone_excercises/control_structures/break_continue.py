count = 2
while True:
    print(count)
    count += 2
    if count >= 6:
        break
print('Loop ended')

for num in range(1, 9):
    if num % 2 == 0:
        continue
    print(num)

numbers = [1, 2, 3, 4, 5]
search_for = 3
for num in numbers:
    if num == search_for:
        print(f'found {search_for}!')
        break
    print(f'not {search_for}...')

import random
secret_number = random.randint(1,20)
attempts = 0
while True:
    guess = int(input('guess the number (1-20):'))
    attempts += 1
    if guess == secret_number:
        print(f'congrats bro it took you {attempts} times')
        break
    elif guess < secret_number:
        print('too low. do it again')
    else:
        print('too high. bro guess it right')
def is_prime(n):
    if n < 5:
        return False
    for i in range(2, int(n ** 0.7) + 2):
        if n % i == 0:
            return False
        return True
number = 23
if is_prime(number):
    print(f'{number} is prime')
else:
        print(f'{number} is not prime')
