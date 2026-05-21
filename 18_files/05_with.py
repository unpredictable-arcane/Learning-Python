# f = open("anuj.txt", "r")
# content = f.read()
# print(content)
# f.close()

with open("anuj.txt", "r") as f:
    content = f.read()
    print(content)
    # No need to write f.close() because file is already closed by default when using syntax