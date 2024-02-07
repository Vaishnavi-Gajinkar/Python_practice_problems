import random

naem = input("enter name")
flag = False
while (flag == False):
    if len(naem) < 3:
        print("Name too short.Enter valid name")
        naem = input("enter name")
        flag = False
    elif len(naem) > 20:
        print("Name too long.Enter valid name")
        naem = input("enter name")
        flag = False
    else:
        print("Name looks good")
        flag = True

guess = 0
numb = random.randint(1,9)
print(numb)
while guess != numb:
    guess = int(input("guess the number"))
print("Correct guess")
