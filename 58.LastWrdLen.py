'''Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only
Eg.
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''

sentence = input("Whats the input string? ")

rev_sent = sentence[::-1]

last_word = rev_sent.split(" ")

print(len(last_word[0]))