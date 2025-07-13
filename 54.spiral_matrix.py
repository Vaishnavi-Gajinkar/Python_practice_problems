''' Task: Given an mXn matrix, print the elements of matrix in a spiral fashion.
Sample Input: 1 2 3
              4 5 6
              7 8 9
Sample Output: 1 2 3 6 9 8 7 4 5
'''

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrx = []
tot_elemts = rows * cols

for arr in range(rows):
    matrx.append([int(x) for x in input(f"Enter elements of row {arr} (space sep) ").split(" ")])

left = 0
right = cols
top = 0
bottm = rows
val = 0

while val < tot_elemts:
    i = left
    j = top+1
    k = right-2
    l = bottm-2

    while i < right:                            # prints top row
        print(matrx[top][i], end=" ")
        i += 1
        val += 1
    top += 1

    while j < bottm:                            # prints right edge
        print(matrx[j][right-1], end=" ")
        j += 1
        val += 1
    right -= 1

    while k >= left:                             # prints bottom row
        print(matrx[bottm-1][k], end=" ")
        k -= 1
        val += 1
    bottm -= 1

    while l >= top:                              # prints left edge
        print(matrx[l][left], end=" ")
        l -= 1
        val += 1
    left += 1


'''
OUTPUT 1:
Enter number of rows: 4
Enter number of columns: 4
Enter elements of row 0 (space sep) 1 2 3 4
Enter elements of row 1 (space sep) 5 6 7 8
Enter elements of row 2 (space sep) 9 10 11 12
Enter elements of row 3 (space sep) 13 14 15 16
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
--------------------------------------------------------------------------
OUTPUT 2:
Enter number of rows: 2
Enter number of columns: 3
Enter elements of row 0 (space sep) 1 2 3
Enter elements of row 1 (space sep) 4 5 6
1 2 3 6 5 4 
--------------------------------------------------------------------------
OUTPUT 3:
Enter number of rows: 4
Enter number of columns: 5
Enter elements of row 0 (space sep) 1 2 3 4 5
Enter elements of row 1 (space sep) 6 7 8 9 0
Enter elements of row 2 (space sep) 1 2 3 4 5
Enter elements of row 3 (space sep) 8 5 2 1 6
1 2 3 4 5 0 5 6 1 2 5 8 1 6 7 8 9 4 3 2 
--------------------------------------------------------------------------
OUTPUT 4:
Enter number of rows: 3
Enter number of columns: 3
Enter elements of row 0 (space sep) 1 2 3
Enter elements of row 1 (space sep) 4 5 6
Enter elements of row 2 (space sep) 7 8 9
1 2 3 6 9 8 7 4 5 

'''