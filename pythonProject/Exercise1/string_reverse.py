# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

fname = input("enter first name ")
lname = input("enter last name ")
lizt = []
rev = []
fullname = fname +" "+ lname
output = fullname[::-1]
print(output)

#  Write a Python program that accepts a filename from the user and prints the extension of the file.
naem = input("Enter name of your file along with extension")
extn = naem.split(".")
for word in extn:
    lizt.append(word)
print(lizt)
print("extension of your file is ", extn[-1])
