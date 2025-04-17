'''
'''

def wrap(string, max_width):
    bite = ''
    count = 0
    i = 0
    j = 0
    
    while count < len(string):
        while (j < max_width) and (count < len(string)):
            bite += string[count]
            count += 1
            j = j+1
        j = 0
        bite += '\n'

    return bite

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

# not solved