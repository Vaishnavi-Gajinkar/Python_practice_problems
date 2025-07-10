'''
Task : You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Input Format : A single line containing the space-separated integers.
Constraints
Output Format

Sample Input : 3 3 3
First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.
'''

import numpy

l, m, n = [int(x) for x in input().split(' ')]

# print(l,m,n)
print(numpy.zeros((l,m,n),dtype=int))

print(numpy.ones((l,m,n),dtype=int))

'''
OUTPUT : 
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
'''