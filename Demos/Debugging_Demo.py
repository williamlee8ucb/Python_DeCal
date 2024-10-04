# DEBUGGING

# compilation error: forgetting syntax that makes computer unable to read code
# logical error: when the code tries to do something that doesn't make sense
# runtime error: nothing inherently wrong with syntax, but results in error ex. divide by 0

# Docstrings
# letting yourself and others know what a function does
# enclosed in triple quotes
# nothing outputted if function works
# shows failures if error in function

def add(x, y):
    """
    >>> add(3, 5) #add space after 3 characters
    8
    >>> add(4, 10)
    14
    """
    return x + y

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Print Statements

def factLoop(n):
    """
    >>> factLoop(3)
    6
    >>> factLoop(4)
    24
    """
    total = 1
    for i in range(1, n+1):
        # delete print statement when debugging is done
        total *= i
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Common Errors

# Syntax Error
# cause: typo/syntax mistake
# Ex. missing parentheses, missing colon

# Type Error
# cause: invalid operand types for operation, wrong number of args passed into function, non_function object in function call
# Ex. add(1, "n") -> adding string and int; add(1) -> wrong number of args

# Name Error
# cause: variable is not defined
# Ex. a = 3 + x -> x is not defined

# Index Error
# cause: indexing into a sequence (list, tuple, string, dict, etc.) with a number greater than the length
# Ex. str = "hello" 
#     str(6) -> greater index than length of errors

# Mitigating Bugs
# make sure spelling is correct
# close parentheses andn qhotes
# = vs. ==
# check for infinite loops
# off by one errors
# use comments
# give appropriate variable names 

# Unexpected Outputs

