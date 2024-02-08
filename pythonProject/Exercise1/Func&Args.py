def cust_info(fname,lname,disc,ship,cost):
    print(f'Hey {fname} {lname}')
    print(f'Your order details are as beloww')
    print(f'''
Item Cost:{cost}
Shipping: {ship}
Discount: {disc}
''')


print("Start")
cust_info("John","Smith",cost=100, ship=40, disc=5)
print("Stop")