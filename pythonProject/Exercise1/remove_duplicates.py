count = int(input("how many numbers in your list? "))
print(f"Enter the {count} numbers")
lizt = []
for i in range(count):
    lizt.append(int(input()))
print(lizt)
for j in lizt:
    check_ripit = lizt.count(j)
    if check_ripit > 1:
        lizt.remove(j)
        print(f"Duplicate item {j} removed from list")
print(lizt)