#Recursive Implementation of Fibonacci Series
def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion.
    """
    #  Base case: The 0th Fibonacci number is 0.
    if n <= 0: 
        return 0
    # Base case: The 1st Fibonacci number is 1.
    elif n == 1:
        return 1
     # Recursive step: The nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers.
    else:
        return fibonacci(n-1) + fibonacci(n-2) 
print(fibonacci(12))  # Output: 8

#Iterative Implementation
def fibonacci_iterative(n):
    """
    Returns the nth Fibonacci number using an iterative approach (loops).
    """
    # Base case: If n is 0 or less, the Fibonacci number is 0.
    if n <= 0:
        return 0
    # Base case: If n is 1, the Fibonacci number is 1.
    elif n == 1:
        return 1
    
    # Initialize 'a' to the 0th Fibonacci number (0) and 'b' to the 1st Fibonacci number (1).
    # These two variables will hold the previous two Fibonacci numbers in the sequence.
    a, b = 0, 1
    
    # Iterate from the 2nd number up to n (inclusive).
    # The loop starts from 2 because the 0th and 1st numbers are already handled by the base cases.
    # The underscore '_' is used as a variable name when the loop counter itself isn't needed.
    for _ in range(2, n + 1):
        # In each iteration, calculate the next Fibonacci number.
        # The new 'a' becomes the old 'b' (the previous Fibonacci number).
        # The new 'b' becomes the sum of the old 'a' and old 'b' (the current Fibonacci number).
        # This simultaneously updates 'a' and 'b' to prepare for the next iteration.
        a, b = b, a + b
        
    # After the loop completes, 'b' will hold the nth Fibonacci number.
    return b

# This line calls the function with n=123 and prints the result.
print(fibonacci_iterative(123))
