s = "Anuj Arcane"

# name [0] = "R" # This will raise an error because strings are immutable

a = len(s)
# print
# print(s.upper(), s)
# print(s.lower())
# print(s.capitalize())
# print(s.title)


# text =" \nhello world  "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip())# Output: "hello world  "
# print(text.rstrip())# Output: "  hello world"

# text ="Python is fun"
# print(text.find("is")) # Output: 7
# print(text.replace("fun","awesome")) # Output: "Python is awesome

# text = "Apples,Bananas,Cherries"
# print(text.split(","))
# print(",".join(["Apples", "Bananas", "Cherries"]))  1

text ="Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False