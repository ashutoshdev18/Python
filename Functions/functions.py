#Let's learn about functions

s = [1, 2, 3]
print(len(s))

from math import sqrt
print(round(sqrt(98), 2))

import math
print(math.pi)

def print_name(name):
    print(name)

print_name('Ashutosh Pandey')


def multiply(a, b):
    return a * b

print(multiply('Ashutosh ', 5))
print(multiply([1, 2, 3], 10))


def my_func(a, b, c=10):
    print(a, b, c)

my_func(1, 2)
my_func(1, 2, 3)
my_func(a=10, b=20, c=30)