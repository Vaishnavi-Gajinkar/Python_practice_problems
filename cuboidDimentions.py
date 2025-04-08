'''You are given three integers x,y,z representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by  on a 3D grid where the sum of dimentions is not equal to n.
Here, Please use list comprehensions rather than multiple loops, as a learning exercise.
Sample Input 
x = 1
y = 1
z = 1
n = 2
Sample Output [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
n = int(input("n = "))

lst_comp = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if (i+j+k)!= n]

print(lst_comp)
