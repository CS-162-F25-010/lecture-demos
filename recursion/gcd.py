# Given two integers, a and b, compute the greatest common divisor between
# them
def gcd(a: int, b: int) -> int:
    if a <= 0 or b <= 0:
        raise ValueError('a and b must both be positive!')

    if a < b:
        tmp = a
        a = b
        b = tmp

    # We're certain that a and b are both positive, AND a >= b
    # We're going to implement Euclid's Algorithm
    if a % b == 0:
        return b

    else:
        # You can prove that a - c is actually equal to a % b
        return gcd(b, a % b)

def main() -> None:
    print(f'The greatest common divisor between 56 and 24 is: {gcd(72, 24)}')

if __name__ == '__main__':
    main()
