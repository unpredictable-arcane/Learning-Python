#string formatting

template = "Dear {}, You are awesome! Take this {} rupees as a token of appreciation."
a = "john"
a1 = 1000
b = "jack"
b1 = 2000
c = "jill"
c2 = 3000

s1 = template.format(a, a1)
print(s1)

print(f"{a} is a good person and he has {a1} rupees.")