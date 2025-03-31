'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Eg. Input: nums = [3,2,4], target = 6 Output: [1,2]
'''

nums = [int(x) for x in input("Enter elements of array seperated by comma ").split(',')]

target = int(input("Enter target sum to be achieved "))

arr = []

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            arr.append(i)
            arr.append(j)
            break
    else:
        continue                            # continue with the next iteration of outer for loop
    break                                   # break the outer for if inner for's break stmt was executed

print(arr)