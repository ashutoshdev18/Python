print('In implicit the physical new line token is ignored by the python interpreter and treats the whole line as single line')

#examples

list = [1,
        2,
        3]

print(list) # doesn't print the values in line instead prints in single line

dict = {'a': 97
        ,'b': 98,
        'c': 99}

print(dict)

def func_example(a,
                 b,
                 c):
    print(a, b, c)

func_example(1, 2, 3)


a = 100
b = 200
c = 300

if a >= 100 and b >= 200 and c >= 300:
    print(True)
else:
    print(False)


if a >= 100 \
and b >= 200 \
and c >= 300:
    print(True)