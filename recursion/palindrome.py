def is_palindrome(s: str) -> bool:
    # Goal: Return True if s is a palindrome, False otherwise
    # Palindrome: String spelled the same forward and backwards

    # Recursion is good for solving problems that can be broken down into
    # smaller versions of themselves

    # Suppose you have a string s with 5 characters.
    # Suppose that you are capable of determining whether some smaller string
    # s2 with 3 characters is a palindrome. How might we use that capability
    # to determine wither s is a palindrome?

    # A string is a palindrome if and only if:
    # 1. The first and last characters of the string are the same
    # 2. All the characters in between must also make up a palindrome

    if s == '':
        return True

    if len(s) == 1:
        return True

    if s[0] != s[-1]:
        return False

    middle_substring = s[1:len(s) - 1]
    if not is_palindrome(middle_substring):
        return False

    return True

def main() -> None:
    print(is_palindrome('racecar'))
    print(is_palindrome('raceecar'))
    print(is_palindrome('raceecafdsjafjdsajfdsar'))
    

if __name__ == '__main__':
    main()
