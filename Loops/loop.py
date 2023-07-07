#Learning about loops

#1) While loop
i = 1

while i <= 5:
    print(i)
    i += 1


i = 5

while True:

    if i >= 10:
        print('Reached the end')
        break
    i += 1

# min_length_of_name = 2
# name = input("Please enter your name: ")

# while not (len(name) >= min_length_of_name and name.isprintable() and name.isalpha()):
#     print("Please Enter the Name again: ")
#     name = input()

# print('The name you have entered is: ', name)

# To take the name input just once

min_length_of_name = 3
while True:
    name = input("Please enter your name: ")

    if len(name) >= min_length_of_name and name.isprintable() and name.isalpha():
        break

print(name)


#continue
a = 0
while a < 10:
    a += 1

    if a % 2 == 0:
        continue

    print(a)

l = [1, 2, 3]
val = 5
idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)

print(l)


#2) try...except...finally
a = 20
b = 0
try:
    print(a/b)
except ZeroDivisionError:
    b = 1
    print('Zero Division Error')
finally:
    print(a/b)
    print('Always execute with or without exception')


print("---- Iterables ----")
print("In python, an iterable is an object capable of returning values one at a time.")


#3) for loop
print("range(num) always starts from 0")
for i in range(5):
    print(i)

for i in [1,2,3,4,5]:
    print(i)


for x in [(1, 2), (3, 4), (5, 6)]:
    print(x)

for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)


for i in range(1, 100):

    if i % 7 == 0:
        print("Multiple of 7 found")
        break
else:
    print("Please try to increase the range")


for i in range(1, 6):
    print('-------------------------')
    try:
        print(10 / (i - 2))
    except ZeroDivisionError:
        print('Zero Division')
        continue
    finally:
        print("Always run")

name = 'Ashutosh Pandey'

for c in name:
    print(c, end=" ")

for i, c in enumerate(name):
    print(i, c)

l = [101, 102, 103, 104, 105]

for i, num in enumerate(l):
    print(i, num)

