'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

parenth = [pr for pr in input("Enter parenthesis in pairs ").strip().split(" ")]
lst = []
dnary = {'}':'{',']':'[',')':'('}
print(f'input received {parenth}')
flag = 0

if len(parenth) % 2 != 0:                                           # checking for pairs
    print("Missing some pair of parenthesis")
else:
    for bract in parenth:
        if bract == '(' or bract =='{' or bract == '[':             
            lst.append(bract)                                       # push if opening brace
        elif (bract == ')' or bract == '}' or bract == ']') and len(lst) != 0:          
                lifo = lst.pop()                                    # pop if closing brace
                print(f'lst {lst} \nLIFO element {lifo}')
                if lifo == dnary[bract]:                            # continue if matching brace found
                    continue
                else:
                    print('Invalid parenthesis sequence')
                    break
        else:
            print("Invalid inputs")
            flag = 1
            break

    if len(lst) != 0 or flag == 1:                                    # iterate till lst is empty
        print('Invalid parenthesis sequence')
    else:
        print("Parenthesis sequence is correct")