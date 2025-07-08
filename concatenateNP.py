''' Task :
You are given two integer arrays of size nXp and mXp (n & m are rows, and p is the column). Your task is to concatenate the arrays along axis 0.

Input Format: The first line contains space separated integers n,m and p.
The next n lines contains the space separated elements of the p columns.
After that, the next m lines contains the space separated elements of the p columns.

Output Format : Print the concatenated array of size (n+m)Xp.
Sample Input: 4 3 2
              1 2
              1 2 
              1 2
              1 2
              3 4
              3 4
              3 4 
'''

import numpy

n, m, p = [int(x) for x in input().split(" ")]
np = []
mp = []

for i in range(n):
    np.append([int(x) for x in input().split(" ")])

for j in range(m):
    mp.append([int(x) for x in input().split(" ")])
    
np_arr = numpy.array(np)
mp_arr = numpy.array(mp)

np_concat_mp = numpy.concatenate((np_arr,mp_arr),axis=0)
print(np_concat_mp)