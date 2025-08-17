''' Task - You are given a 2-D array with dimensions nXm. Your task is to perform the min function over axis 1 and then find the max of that.

Input Format - The first line of input contains the space separated values of n and m.
               The next n lines contains m space separated integers.

Output Format - Compute the min along axis 1 and then print the max of that result.

Sample Input - 4 2
               2 5
               3 7
               1 3
               4 0
Sample Output - 3

Explanation - The min along axis 1 = [2,3,1,0]
              The max of[2,3,1,0]  = 3
'''

import numpy as np

n,m = [int(x) for x in input().split(" ")]
arr = []

for i in range(n):
    arr.append([int(x) for x in input().split(" ")])

np_arr = np.array(arr)

min_arr = np.min(np_arr, axis=1)
print(min_arr)

print(np.max(min_arr))