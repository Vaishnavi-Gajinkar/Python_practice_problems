'''Write a Python program to calculate the difference between a given number and 17.
If the number is greater than 17, return twice the absolute difference.'''

val = int(input("Enter a 2 digit number "))
calc = 17 - val
if calc > 0:
    print("difference is ",calc)
else:
    print(2 * abs(calc))

'''Write a Python program to get the volume of a sphere with radius six.'''
rad = 6; pi = 3.14
print("Vol of sphere having radius 6 is ", 4/3*pi*rad**3)

''' Write a Python program to test whether a number is within 100 of 1000 or 2000 '''
def near_val(num):
    return ((abs(1000-num)<100) or (abs(2000-num)<100))

print(near_val(1500))
print(near_val(1950))

#code to calculate the sum of three given numbers. If the values are equal, return three times their sum.
def check_nums(a,b,c):
    if a == b and b == c:
        return 3*a*3
    else:
        return a+b+c

print(check_nums(3,3,3))
print(check_nums(1,2,3))








