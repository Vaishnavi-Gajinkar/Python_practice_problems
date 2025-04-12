''' You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
The one line contains a string consisting of space separated words.
Eg. input - this is a string
    output - this-is-a-string
'''

def split_and_join(line):
    lst_of_strings = (line.strip()).split(" ")
    new_line = "-".join(lst_of_strings)
    return new_line

line = input()
result = split_and_join(line)
print(result)