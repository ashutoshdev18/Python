print("Declaring tuple with 1 element")

t = (1, )

tup = (1) # declared as int
print("{0} is of type {1}".format(t, type(t)))
print("{0} is of type {1}".format(tup, type(tup)))


a = 100
b = 200

print(a, b)
print("After swapping")
a, b = b, a
print(a, b)

d = {"key1" : 1, "key2": 2, "key3": 3}

for e in d:
    print(e)


s = {1, 2, 3, 4, 1, 6, 5, 1, 4}

for c in s:
    print(c)
print()
a = [1, 2, 3]

for l in a:
    print(l)