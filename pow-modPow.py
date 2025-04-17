''' You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

Input
3
4
5
Output
81
1
'''

def paw(a, b):
    res = pow(a,b)
    return res

def calc(a, b, m=1):
    res = pow(a,b,m)
    return res

a = input()
b = input()
m = int(input())

if '.' in a:                # convert type of a to float if decimal is present
    a = float(a)
else:
    a = int(a)              # else converts type of a to integer

if '.' in b:                # convert type of b to float if decimal is present
    b = float(b)
else:
    b = int(b)              # else converts type of a to integer
    
print(paw(a,b))
if m is None:
    print(calc(a,b,m))
else:
    print(calc(a,abs(b),m))     # if 3rd param is present, b cannot be negative
