# def is_greater_than_10(x):
#     if x > 10:
#         return True
#     else:
#         return False
    
a = [1, 2, 3, 44, 95, 66, 7, 8, 9]

new = list(filter(lambda x: x>10, a))
print(new)
