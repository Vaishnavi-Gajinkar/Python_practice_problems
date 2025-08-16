''' Task - You are given two integer arrays, a and b of dimensions nXm. Your task is to perform the following operations:
Add ( a+b )
Subtract ( a-b )
Multiply ( a*b )
Integer Division ( a/b )
Mod ( a%b )
Power ( a**b )

Note - There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

Input Format - The first line contains two space separated integers, n and m.
               The next n lines contains m space separated integers of array a.
               The following n lines contains m space separated integers of array b.

Output Format : Print the result of each operation in the given order under Task.

Sample Input
1 4
1 2 3 4
5 6 7 8

Sample Output
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 
'''

import numpy as np

n, m = [int(x) for x in input().split(" ")]
arr_a = []
arr_b = []

for i in range(n):
    arr_a.append([int(x) for x in input().split(" ")])
for j in range(n):
    arr_b.append([int(x) for x in input().split(" ")])

np_a = np.array(arr_a)
np_b = np.array(arr_b)

print(np.add(np_a,np_b))
print(np.subtract(np_a,np_b))
print(np.multiply(np_a,np_b))
print(np.floor_divide(np_a,np_b))
print(np.mod(np_a,np_b))
print(np.power(np_a,np_b))