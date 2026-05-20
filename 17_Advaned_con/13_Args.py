def sum(*args): #args
    #args will be tuple of all the values passed to sum

    total = 0
    for item in args:
        total += item
    return total


print(sum(342, 1, 7, 87))