''' You are given a string s.
Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format : A single line containing a string .
Output :
True
True
True
True
True
'''

s = input()

for ch in s:
    if ch.isalnum():
        print(True)
        break
else:
    print(False)
        
for ch in s:        
    if ch.isalpha():
        print(True)
        break
else:
    print(False)
        
for ch in s:
    if ch.isdigit():
        print(True)
        break
else:
    print(False)
        
for ch in s:
    if ch.islower():
        print(True)
        break
else:
    print(False)
        
for ch in s:
    if ch.isupper():
        print(True)
        break
else:
    print(False)