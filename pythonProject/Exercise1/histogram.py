# Write a Python program to create a histogram from a given list of integers.

count = int(input("enter how many values exist in histogram: "))
print("Enter the values")
lizt = []
for i in range(count):
    lizt.append(int(input()))
for j in lizt:
    print('@'*j)