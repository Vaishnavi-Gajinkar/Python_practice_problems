'''You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Eg. 
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
'''

number_arr = [int(num) for num in input("Enter int array (comma sepetated)").split(",")]
char_arr = ''
for i in range(len(number_arr)):
    char_arr += str(number_arr[i])

print(char_arr)
incrmnt = int(char_arr)+1

str_arr = str(incrmnt)

print([int(x) for x in str_arr])