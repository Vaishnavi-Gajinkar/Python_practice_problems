'''
Alice and Bob are playing a game. Initially, Alice has a string word = "a".
You are given a positive integer k.
Now Bob will ask Alice to perform the following operation forever:
Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.
Note that the character 'z' can be changed to 'a' in the operation.
'''

# print(ord('z'))

try:
    # ask = input("Enter chars (only btwn a-z) ")
    kthchr = int(input("Which position of the string would you want to access? "))
    word = 'a'

    while len(word) <= kthchr:
        for ch in word:
            assert ord(ch)>96 and ord(ch)<123
            pos = ord(ch)
            if ch == 'z':
                pos = 96
            pos += 1
            word += chr(pos)
    print(word)
    print(f'the {kthchr} character of new string {word} is {word[kthchr-1]}')

except AssertionError:
    print('Pls enter valid characters')
except Exception:
    print('Invalid position. Some error occured')

finally:
    print('This is awesome 😍')

