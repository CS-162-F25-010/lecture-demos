# Scope is a region of code in which a named thing is accessible
# In python, scopes are dictated by functions.

# When you create a named thing, it belongs to the scope in which
# you created it.

# This first line is referred to as a "function header". Tells you
# the function's "interface", meaning what it does.

# The parameter list is a comma-separated list of parameter declarations
def volume_of_sphere(radius: float) -> float:
    # Function's body goes here. The body tells you "how" the function does it.
    # Function's body must be indented

    x = 5 # x is "scoped to" the volume_of_sphere function
    # x is only accessible within this function

    return 4 / 3 * 3.141592 * radius ** 3

# print(x) # x does not exist in this scope. Syntax error.

def main() -> None:
    # "Calling" a function means using it
    print(volume_of_sphere(3.0))
    print(volume_of_sphere(5.0))
    # print(x) # x does not exist in this scope. Syntax error.
    
    x = 5
    print(x) # Now I can print x.

if __name__ == '__main__':
    main()
