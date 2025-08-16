'''Task : Your task is to print an array of size nXm with its main diagonal elements as 1's and 0's everywhere else.
Note - In order to get alignment correct, please insert the line  below the numpy import.

Input Format -
A single line containing the space separated values of n and m.
n denotes the rows.
m denotes the columns.

Output Format - Print the desired nXm array.

Sample Input - 3 3
Sample Output - [[1. 0. 0.]
                 [0. 1. 0.]
                 [0. 0. 1.]]
'''

import numpy as np
np.set_printoptions(legacy='1.13')

n,m = [int(x) for x in input().split(" ")]

arr = np.eye(n,m)

print(arr)