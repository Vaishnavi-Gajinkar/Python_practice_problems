'''Given the names and grades for each student in a class of N students, store them in a nested list and 
print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example: records = [["Chi",20.0],["Beta",50.0],["Alpha",50.0]]

The ordered list of scores is [20.0,50.0], so the second lowest score is 50.0 There are two students with that score: ["Beta","Alpha"] 
Ordered alphabetically, the names are printed as:
alpha
beta
'''
lst = []
for n in range(1,int(input("How many student records ? "))+1):
    name = input(f"Enter name of student {n} ")
    score = float(input("Enter his marks "))
    lst.append([name,score])

names_lst = []

marks = []
for item in lst:
    marks.append(item[1])

lst_set = set(marks)
lst_set = list(lst_set)
lst_set.sort()
min_2 = lst_set[1]

for iter in lst:
    if iter[1] == min_2:
        names_lst.append(iter[0])

names_lst.sort()
for name in names_lst:
    print(name)