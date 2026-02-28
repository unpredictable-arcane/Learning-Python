s = {3, 33, 2, 11}

print(s)

s.add(32)
print(s)

s.remove(11)
print(s)
s.discard(39) # This will not raise an error even if 39 is not present

s.remove(39)  # This will raise an error because 39 is not present in the set