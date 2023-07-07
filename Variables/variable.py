#case sensitive
#start with _ or letter
#followed by any number of underscores, letters, numbers
#cannot use reserve keyworkds


print("_my_var starts with _ is private objects")

print("__my_var starts with __ is used to mangle class attributes useful in inheritance")

print("__my_var__ ends with double __ used for system defined names")

my_num = 10

print(my_num)

my_str = "Hello!!! This is Ashutosh."
print(my_str)

my_dec_num = 100.90
print(type (my_dec_num))

print("Hello world")

my_var = 10
ref1_var = my_var
ref2_var = ref1_var

import sys
print(hex(id(my_var)))
cnt = sys.getrefcount(my_var)
print(cnt)


print("Python is dynamically typed")
a = "hello"

print("a type is: {0}".format(type(a)))

a = 10
print("Now a type is: {0}".format(type(a)))


a = 100
print(hex(id(a)))

a = a + 1
print(hex(id(a)))

