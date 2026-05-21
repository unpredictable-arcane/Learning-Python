# Append to a existing file called JohnDoe.txt
# It should contain data about John Doe's Hometown

f = open("John Doe.txt", "a")

string = '''
John Doe initially lived in Phoenix, Arizona. He is a very nice guy 
'''
f.write(string)

f.close()