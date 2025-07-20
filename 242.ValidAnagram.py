''' Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Eg1: Input: s = "anagram", t = "nagaram"
     Output: true
Eg2: Input: s = "rat", t = "car"
     Output: false
'''

def isAnagram(s:str, t:str):
    s_dict = {}
    t_dict = {}

    for i in s:                                             # adding values of string s with counter
        if i in s_dict:
            s_dict[i] += 1
        else:
            s_dict[i] = 1
            
    for j in t:                                             # adding values of string t with counter
        if j in t_dict:
            t_dict[j] += 1
        else:
            t_dict[j] = 1

    if len(s_dict) == len(t_dict):                          # comparing if both strings have same unique chars
        for key,val in s_dict.items():             
            if key in t_dict:                               # checking if counts of unique chars in s and t are same
                if t_dict[key] != val:
                    print("Not Aangram")
                    break
            else:
                print("Not anagram")
                break
        else:
            print("Anagram")
    else:
        print("Not Anagram")


isAnagram("tar","art")
isAnagram("qwerty","asdfg")
isAnagram("a","ab")

'''
OUTPUT :

Anagram
Not Anagram
Not Anagram
'''