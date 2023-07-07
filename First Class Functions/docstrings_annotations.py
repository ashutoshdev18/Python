print("Docstrings -> we can document our functions")

print("help(str)")


print("if a string is first line of the function it will be treated as docstring")

def my_func(a):
    "this is my_func"
    return a

print(my_func(10))

print(help(my_func))

def fact(n):

    """"
    Calculates the factorial of a given integer.

    Input:
        n: a positive integer
    Output:
        x: the factorial of the given integer

    """
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

print(fact(5))

print(fact.__doc__)

def seq(a, b=1):
    return a * b

print(seq("ab", 5))