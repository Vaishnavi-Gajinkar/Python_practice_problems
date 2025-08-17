''' Task - You are given a 2-D array of size nXm. Your task is to find:
The mean along axis 1
The var along axis 0
The std along axis None

Input Format:
The first line contains the space separated values of n and m.
The next n lines contains m space separated integers.

Output Format:
First, print the mean.
Second, print the var.
Third, print the std.

Sample Input : 2 2
               1 2
               3 4
Sample Output : [ 1.5  3.5]
                [ 1.  1.]
                1.11803398875
'''
import numpy as np

n,m = [int(x) for x in input().split(" ")]
arr = []

for i in range(n):
    arr.append([int(x) for x in input().split(" ")])

np_arr = np.array(arr)

print(np.mean(np_arr, axis=1))
print(np.var(np_arr, axis=0))
# print(np.std(np_arr, axis=None))
stdiv = "{:.11f}".format((np.std(np_arr, axis=None)),decimals=11)
print(stdiv)