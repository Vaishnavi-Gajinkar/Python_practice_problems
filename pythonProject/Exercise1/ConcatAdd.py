'''Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615 '''

num = input("Enter the value for n ")
rep = int(input("Enter the value of repetitions "))
output = ""
i = sum = 0

while (i < rep):
    output = output+num
    print(f'{num} is appended {i+1} times now ie {output}')
    sum = sum + int(output)
    i += 1

print(f'sum of {num} appended {rep} times is {sum} \n')

#static code logic
n1 = int("%s" % num)                # Convert 'a' to an integer
n2 = int("%s%s" % (num, num))          # Concatenate 'a' with itself and convert to an integer
n3 = int("%s%s%s" % (num, num, num))      # Concatenate 'a' with itself twice and convert to an integer
print(n1 + n2 + n3)