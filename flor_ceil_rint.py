''' Task - You are given a 1-D array, a. Your task is to print the floor, ceil and rint of all the elements of a.
Note - In order to get the correct output format, add the line numpy.set_printoptions(legacy='1.13') below the numpy import.

Input Format - A single line of input containing the space separated elements of array a.
Output Format - On the first line, print the floor of A.
                On the second line, print the ceil of A.
                On the third line, print the rint of A.

Sample Input
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Sample Output
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
'''

import numpy
numpy.set_printoptions(legacy='1.13')

arr = [int(x) for x in input().split(" ")]
np_arr = numpy.array(arr)

print(numpy.floor(np_arr))
print(numpy.ceil(np_arr))
print(numpy.rint(np_arr))