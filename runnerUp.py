''' Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
Input Format:
5
2 3 6 6 5
Sample Output : 5
'''

n = int(input("How many elements in array"))
arr = map(int, input("Enter elements (comma seperated) ").split(','))
arr = list(arr)

lst = []
first = max(arr)
for i in range(n):
    if arr[i] != first:
        lst.append(arr[i])

lst.sort()
print(lst[-1])