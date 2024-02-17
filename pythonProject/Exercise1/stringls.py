''' Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
Return the string unchanged if the given string already begins with "Is".'''

string = input("Enter a string: ")
stringlower = string.lower()
if stringlower.startswith('is'):
    print(f'no change required in string {string}' )
else:
    print(f'Is{string}')
# -------------------------------------------------------------------------------------
def new_string(text):
    if len(text) >= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text
print(new_string("Array"))
print(new_string("IsEmpty"))

# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

count = int(input("Enter the repetition count: "))
print(f'{string} ' * count)





