'''
Task : You are given a nXm integer array matrix with space separated elements (n = rows and m = columns).
Your task is to print the transpose and flatten results.

Input Format : The first line contains the space separated values of n and m. The next n lines contains the space separated elements of m columns.

Output Format : First, print the transpose array and then print the flatten.

Sample Input : 2 2
               1 2
               3 4
Sample Output : [[1 3]
                 [2 4]]
                [1 2 3 4] 
'''

import numpy

n, m = [int(x) for x in input().split(' ')]
arr = []

for i in range(n):
    arr.append([int(x) for x in input().split(' ')])
    
print(arr)
np_arr = numpy.array(arr)

print(np_arr)

transp_np = numpy.transpose(np_arr)
print(transp_np)

flat_np = np_arr.flatten()
print(flat_np)