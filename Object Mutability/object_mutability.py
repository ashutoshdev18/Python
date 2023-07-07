print("Changing data inside object is called modifying the internal state of the object")

print("AN OBJECT WHOSE INTERNAL STATE CAN BE CHANGED IS CALLED ****MUTABLE****")

print("AN OBJECT WHOSE INTERNAL STATE CANNOT BE CHANGED IS CALLED ****IMMUTABLE****")

print("Immutable objects are::::: ")
print("numbers, strings, tuples, frozen sets, user-defined class")


print("Mutable Objects are::::: ")
print("lists, sets, dictionaries, user-defined class")

print("FOR LISTS")
a = [1, 2, 4]
print(hex(id(a)))
a.append(5)
print("After appending elements: {0}".format(hex(id(a))))


my_dict = {"a": 65, "b": 66}
print(hex(id(my_dict)))
my_dict["c"] = 67
print(hex(id(my_dict)))

print('IMMUTABLE OBJECTS ARE SAFE FROM UNINTENDED SIDE EFFECTS')

def process(s):
    s + ' world!'
    return s # s points to hello world and return the value

my_var =  'hello'
print(hex(id(my_var)))
process(my_var)
print(hex(id(my_var)))
print(my_var)

#VARIABLE EQUALITY

print("we can compare with the help of memory address and object state(data)")

print("{0} is used to compare memory address and {1} is used to compare object state".format("is", "=="))

a = 10
b = a
b = 10
print(a is b) #compares memory
print(a == b) #compares object state

a = "hello"
b = "hello"

print(a is b)
print(a == b)

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
print(a == b)

a = 10
b = 10.0

print(a is b)
print(a == b)


#STRING INTERNING

a = "hello"
b = "hello"

print(id(a), id(b))

a = "hello world"
b  =  "hello world"
print(a is b)
print(a == b)

import sys

a = sys.intern('hello world')
b = sys.intern('hello world')
c = 'hello world'
print(id((a)), id(b), id(c))

print(a is not c)


for i in range(len(a)):
    if(a[i] != b[i]):
        print("Not equals!!")
        break
else:
    print("Equals")
    