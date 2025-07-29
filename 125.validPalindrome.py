''' A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

def isPalindrome(sentence:str):
    cnt = 0
    char_arr = []

    for ch in sentence:
        if (ord(ch.lower()) in range(97,123)) or (ord(ch) in range(48,58)):                             # appending char in array if alphaneumeric
            char_arr.append(ch.lower())
    print(char_arr)

    # new_str = ""                                                                                      # alternate way : without creating array/list
    #     for ch in s:  
    #         if (ord(ch.lower()) in range(97,123)) or (ord(ch) in range(48,58)):
    #             new_str += ch.lower()

    fwd = 0                                                                                             # pointers to start & end of array
    bkwd = len(char_arr)-1

    while fwd < bkwd:                                                                                   # loop to check that pointers dont crossover
        front = char_arr[fwd]
        rear = char_arr[bkwd]

        if front != rear:                                                                               # comparing values at both pointers
            print("Not a palindrome")
            return

        fwd += 1
        bkwd -= 1

    print("Palindrome")

isPalindrome("A man, a plan, a canal: Panama")
isPalindrome("race a car")
isPalindrome(" ")
isPalindrome("0P")


'''
OUTPUT :
['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']
Palindrome
['r', 'a', 'c', 'e', 'a', 'c', 'a', 'r']
Not a palindrome
[]
Palindrome
['0', 'p']
Not a palindrome
'''