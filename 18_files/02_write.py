# Write to a file called JohnDoe.txt
# It should contain data about John Doe

f = open("John Doe.txt", "w")

string = '''
John Doe is a nice guy. He lives in nyc and he works with python, his fav package is Pandas 
''' 
f.write(string)

f.close()