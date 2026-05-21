import os 

a = os.listdir("dir1")
print(a) #to get the list of files and directories nothing magical.
# print(os.getcwd())

print(os.path.exists("dir1"))
# os.remove("sample.txt")
# os.rmdir("dir1")   #but the catch is it can only delete the empty directories