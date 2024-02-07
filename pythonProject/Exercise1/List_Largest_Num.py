count = int(input("How many numbers are there in list? "))
lizt = []
print(f'Enter the {count} numbers of list ')
for i in range(count):
    number = int(input())
    lizt.append(number)

max = 0
for j in lizt:
    if max < j:
        max = j
print(f'Largest number in list is {max}')