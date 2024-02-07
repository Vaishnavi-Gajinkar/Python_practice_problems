cost = 0
for price in range(10, 100, 10):
    cost = cost + price
print(cost)

# code to draw an F shape pattern
i = 0; j=0
count = [5,2,5,2,2]
#count = [1,1,1,1,5]
for i in count:
    output = ""
    for j in range(i):
        output += "*"
    print(output)