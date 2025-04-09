''' You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2 
'''

def swap_case(s):
    modified_word = ''
    for ch in s:
        if ord(ch)>64 and ord(ch)<91:
            modified_word += ch.lower()
        elif ord(ch)>96 and ord(ch)<123:
            modified_word += ch.upper()
        else:
            modified_word += str(ch)
    return modified_word

s = input()
result = swap_case(s)
print(result)