numbers = [5, 2, 5, 2, 2]
for i in numbers:
    print('*' * i)
print('Letter E ')
m = 0
for n in range(1,6):
    if n % 2 == 0:
        print('*')
    else:
        print('*****')
print('Letter F ')
for a in numbers:
    output = ''
    for b in range(a):
        output += '*'
    print(output)

print('Letter L ')
l = [1,1,1,1,5]
for c in l:
    output = ''
    for d in range(c):
        output += '* '
    print(output)
