try:
    a = 10 / 0

except Exception as e:
    print(e)

#Getting executed when there is no error
else:
    print("Hey I am good")