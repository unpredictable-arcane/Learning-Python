def marks(**kwargs):
    # kwargs is a dictionary with all key 
    # value pairs which were passed to marks

    for item in kwargs.keys():
        print(f"The marks of {item} are {kwargs[item]}")

marks(hitesh=34, piyush=66, harry=60, Mannu=97)