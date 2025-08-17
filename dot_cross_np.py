''' Task - You are given two arrays a and b. Both have dimensions of nXn. Your task is to compute their matrix product.

Input Format : The first line contains the integer n.
               The next n lines contains n space separated integers of array a.
               The following n lines contains n space separated integers of array b.

Output Format : Print the matrix multiplication of a and b.

Sample Input : 2
               1 2
               3 4
               1 2
               3 4
Sample Output : [[ 7 10]
                [15 22]]
'''
import numpy

n = int(input())
arr_a = []
arr_b = []

for i in range(n):
    arr_a.append([int(x) for x in input().split(" ")])    

for i in range(n):
    arr_b.append([int(x) for x in input().split(" ")])    

npA = numpy.array(arr_a)
npB = numpy.array(arr_b)

print(numpy.dot(npA, npB))