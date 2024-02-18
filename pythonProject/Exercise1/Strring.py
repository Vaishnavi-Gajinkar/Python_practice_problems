# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
# Return n copies of the whole string if the length is less than 2.

stmt = input("Enter a string: ")
n = int(input("Enter a value for n: "))
counter = 0
#for word in stmt:
if len(stmt)>2:
    print(stmt[:2]*n)
else:
    print(stmt*n)

# Write a Python program to test whether a passed letter is a vowel or not.
def vowel(strring):
    scanning = strring.lower()
    for word in scanning:
        if word in ('a','e','i','o','u'):
            print('passed a vowel ',word)
        else:
            print("passed a consonant")
    all_vowels = 'aeiou'
    return strring in all_vowels
print(vowel(stmt))








