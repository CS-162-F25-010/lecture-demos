# Recursion: Self-dependency

# In programming, we often say that recursion is when a function calls itself

# It could also be a function a, that calls another function b, that in turn
# calls a again

def hello_world(n: int) -> None:
    print('Hello, World!')

    if n > 1:
        hello_world(n - 1) # This is referred to as a "recursive call"

def main() -> None:
    hello_world(10)

if __name__ == '__main__':
    main()
