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
print(fibonacci(12))  # Output: 144

#Iterative Implementation
def fibonacci_loop(n):
    """
    Returns the nth Fibonacci number using a loop (no recursion).
    The Fibonacci sequence starts as: 0, 1, 1, 2, 3, 5, 8, ...
    Each number is the sum of the two numbers before it.
    """

    # Handle case when input is 0 or negative
    if n <= 0:
        return 0  # The 0th Fibonacci number is 0

    # Handle case when input is 1
    elif n == 1:
        return 1  # The 1st Fibonacci number is 1

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1  # a = F(0), b = F(1)

    # Loop starts from 2 up to n (inclusive)
    for _ in range(2, n + 1):
        # Calculate next Fibonacci number by summing the previous two
        # Then update a and b for the next iteration
        a, b = b, a + b

    # After the loop, b holds the nth Fibonacci number
    return b

# Example usage:
print(fibonacci_loop(12))  # Output: 144

