from functools import reduce

numbers = [1, 2, 3, 4, 5]
# [n1+n2, n3, n4] and then n3 goes for addition
# [3, 3, 4, 5]
# [6, 4, 5]
# [10, 5]
# [15]


def sum(x, y):
    return x + y

c = reduce(sum, numbers)
print(c)