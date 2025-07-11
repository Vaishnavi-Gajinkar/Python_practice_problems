'''
Task : You are given a 2-D array with dimensions nXm.
Your task is to perform the sum tool over axis 0 and then find the product of that result.

Input Format

The first line of input contains space separated values of n and m.
The next n lines contains m space separated integers.

Output Format

Compute the sum along axis 0. Then, print the product of that sum.

Sample Input : 2 2
               1 2
               3 4
Sample Output : 24
Explanation

The sum along axis 0 = [4 6]
The product of this sum = 24
'''
import numpy

n, m = [int(x) for x in input("Enter dimentions of array (space sep) ").split(" ")]
arr = []

for i in range(n):
    arr.append([int(x) for x in input("Enter elements of 1st row (space sep) ").split(" ")])

np_arr = numpy.array(arr)

np_sum = numpy.sum(np_arr, axis=0)

np_prod = numpy.prod(np_sum, axis=None)

print(np_prod)

