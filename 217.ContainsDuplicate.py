'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false

Explanation:
All elements are distinct.
Example 3: Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

def containsDuplicate(nums):
    arr_set = set()

    for num in nums:
        if num in arr_set:
            break
        else:
            arr_set.add(num)
    else:
        print("Only Unique Elements")
        return
    print("Duplicates exist")

containsDuplicate([1,2,3,1])
containsDuplicate([1,2,3,4])
containsDuplicate([1,1,1,3,3,4,3,2,4,2])


"""OUTPUT:

Duplicates exist
Only Unique Elements
Duplicates exist
"""

#------------------------------------------------------------------------------------

def alternate_way(nums):
    list_size = len(nums)
    set_size = len(set(nums))

    if list_size == set_size:
        print("Uniques")
    else:
        print("Duplicates")


alternate_way([1,2,3,1])
alternate_way([1,2,3,4])
alternate_way([1,1,1,3,3,4,3,2,4,2])

'''
OUTPUT:
Duplicates
Uniques
Duplicates
'''
