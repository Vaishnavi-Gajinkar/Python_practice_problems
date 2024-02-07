phone = input("Phone: ")
pair = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '0': 'Zero'}
count = 0
for c in phone:
    count += 1
str = orGet = ""
for i in phone:
    str += pair[i] + " "
    orGet += pair.get(i, 'invalid') + " "
print(str)
print(orGet)