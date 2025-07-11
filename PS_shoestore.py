'''
Task - Raghu is a shoe shop owner. His shop has x number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are n number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains x, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains n, the number of customers.
The next n lines contain the space separated values of the shoesize desired by the customer and xi, the price of the shoe.

Constraints

Output Format : Print the amount of money earned by Raghu.

Sample Input: 10
              2,3,4,5,6,8,7,6,5,18
              6 
              6 55
              6 45
              6 55
              4 40
             18 60
             10 50
Sample Output : 200

Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned =  55 + 45 + 40 + 60 = 200

'''
try: 
    x = int(input("Enter count of shoes in shop "))
    shoe_sizes = None
    total = 0

    shoe_sizes = [int(x) for x in input("Enter available sizes").split(" ")]
    print(f'Available shoe sizes are {shoe_sizes}')
    if len(shoe_sizes) != x:
        raise Exception("invalid number of sizes entered ")

    n = int(input("Enter number of customers "))
    temp = n
    for val in range(n):
        size, price = [int(num) for num in input("enter size seperated by price").split(" ")]
        if size in shoe_sizes:
            shoe_sizes.remove(size)
            total += price
        print(shoe_sizes, total)

    print(total)

except Exception as e:
    print("Some error occured")




























