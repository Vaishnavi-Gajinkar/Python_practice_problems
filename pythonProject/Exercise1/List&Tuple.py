''' Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23') '''

seq = input("Enter some comma seperated numbers ")
discreet = seq.split(",")
lizt = []
tapal = ()
for l in discreet:
    lizt.append(l)
tapal = tuple(lizt)
print(f"List : ",lizt)
print(f"Tuple : ",tapal)

# Write a Python program to display the first and last colors from the following list. color_list = ["Red","Green","White" ,"Black"]

calar = ["Red","Green","White","Black"]
print(calar[0]+calar[-1])

# Write a Python program to count the number 4 in a given list.

def count_4(lizt):
    counter = 0
    for num in lizt:
        if num==4:
            counter+=1
    print(counter)
    return (lizt.count(4))

print(count_4([1,4,2,5,5,8,4]))