''' Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x
'''

n = int(input("Enter a number "))
num = n
power = 0
while num > 1:
    if num % 2 == 0:
        num /= 2
        power += 1
    else:
        print(f'{n} is not a power of 2')
        break
else:
    print(f'{n} is the {power} power of 2 ')


# OUTPUT
'''
Enter a number 1024
1024 is the 10 power of 2 
'''