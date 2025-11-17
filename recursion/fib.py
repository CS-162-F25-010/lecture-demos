# Fibonacci sequence: 0 1 1 2 3 5 8 13 21

# Hint: The nth number in the fibonacci sequence is the sum of the previous
# two numbers in the fibonacci sequence

# Recursion is when a function calls itself

def fib(n: int) -> int:
    if n <= 0:
        raise ValueError('n must be positive!')

    # If I could compute the n-1st number in the fibonacci sequence, AND
    # the n-2nd number in the fibonacci sequence, I can simply add them up
    # to get the nth number

    # These if statements are referred to as "base cases".
    # Every recursive function needs at least one base case.
    # Base cases are cases where the arguments to your recursive function
    # are "small enough" that the final answer to be computed is "obvious."
    if n == 1:
        return 0

    if n == 2:
        return 1



    return fib(n-1) + fib(n-2)

    # If n == 1, return 0
    # If n == 2, return 1
    # If n == 3, return 1

# How to think about recursion:
# Recursion is good whenever you have a problem where, in order to solve
# that problem, you need to break it down into smaller versions of the
# same problem. You keep breaking it down smaller and smaller until the
# problems that you're dealing with are so small that the answers are "obvious".
# Those are your base cases, which are handled with if statements.

def main() -> None:
    print(fib(4))

if __name__ == '__main__':
    main()
