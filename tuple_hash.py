''' Task
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t.

Output Format

Print the result of hash(t).
'''

n = int(input())
lst = []

# for num in range(n):
#     lst.append(input().split(" "))
# tup = tuple(lst)
# print(tup)

t = tuple(input().split(" "))
print(t)

print(hash(t))