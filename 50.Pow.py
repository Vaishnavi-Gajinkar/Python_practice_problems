''' Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Eg. Input: x = 2.00000, n = 10 Output: 1024.00000 '''

x = float(input("Enter base value "))
n = int(input("Enter power "))
res = 1

while n != 0:
    if n > 0:
        res *= x
        n -= 1
    else:
        res /= x
        n += 1

print(f'Result when {x} is raised to power {n} is {res}')