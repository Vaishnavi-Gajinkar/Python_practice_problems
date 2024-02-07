name = input("What's your name? ")

if len(name) < 3:
    print("Name must be atleast 3 chars long")
elif len(name) > 10:
    print("Name can be a max of 10 chars")
else:
    print("You have a great name!")