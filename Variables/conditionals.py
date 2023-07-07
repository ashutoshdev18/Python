a = -100

if a < 5:
    print(a)
else:
    print('a is $gt than 5')


a = 20

if a < 5:
    print('a < 5')
elif a < 10:
    print('5 <= a < 10')
elif a < 15:
    print('10 <= a < 15')
elif a < 20:
    print('15 <= a < 20')
else:
    print('a >= 20')


#TERNARY CONDITIONALS

a = 5

if a <= 5:
    b = 'a <= 5'
else:
    b = 'a > 5'

print(b)

print('In the above if else loop it  is happening if a <= 5 is true then b is assigned a <= 5 else b is assigned a > 5')

print('we can do that in ternary operator')

b = 'a <= 5' if a <= 5 else 'a > 5' #-> ans if condition_satisfied else another_ans
print(b)