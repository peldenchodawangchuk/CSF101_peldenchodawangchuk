number = 20
if number > 0:
    print('the number is positive')
else:
    print('the number is negative')

number = 0
if number > 0:
    print('the number is positive')
elif number < 0:
    print('the number is negative')
else:
    print('the number is zero')

score = 95
if score >= 90 :
    grade = 'A'
elif score >=80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >=60:
    grade = 'D'
else:
    grade = 'F'
print(f'Your grade is: {grade}')
number = 9
result = 'even' if number % 2 == 0 else 'odd'
print(f'the number is {result}')

num1 = 12
num2 = 5
operator = "+"
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 -num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2 if num2 != 0 else "error: division by zero"
else:
    result = "error:invalid operator"

print(f'Result: {result}')
