print("Reducing functions are: combine iterables recursively ending up returning a single value")

#function to find the max element.
def max_ele(l):
    result = l[0]
    print(result)
    for e in l[1:]:
        if result < e:
            result = e
    return result
l = [1, 4, 100, 7, 3, 102, 67, 55]
print(max_ele(l))

from functools import reduce

ans = reduce(lambda a, b: a if a > b else b, l)
print(ans)

ans = reduce(lambda a, b: a + b, l)
print(ans)

ans = reduce(lambda a, b: a + " " + b, ("ashutosh", "is", "learning", "python"))
print(ans)

ans = reduce(lambda a, b: a * b, l)
print(ans)

ans = reduce(lambda a, b: a * b, range(1, 6))
print(ans)
