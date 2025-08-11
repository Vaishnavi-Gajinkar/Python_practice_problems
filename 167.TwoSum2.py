'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
'''

nums = [2,7,11,15]
target = 9

arr = []
strt = 1
end = len(nums)

while strt < end:
    if(nums[strt-1] + nums[end-1] == target):
        arr.append(strt)
        arr.append(end)
        strt += 1
        end -= 1
    elif (nums[strt-1] + nums[end-1]) > target:
        end -= 1
    elif (nums[strt-1] + nums[end-1]) < target:
        strt += 1

print(arr)


'''
OUTPUT:
nums = [2,7,11,15]
target = 9 
output = [1,2]

nums = [2,3,4]
target = 6
output = [1,3]

nums = [-1,0]
target = -1 
output = [1,2]
'''
