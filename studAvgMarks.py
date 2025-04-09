'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
Example: marks key:val pairs are 
'alpha':[20,30,40]
'beta':[30,50,70]
query_name = 'beta'
'beta's avg score is (30+50+70)/3=50.00
'''

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

for key, val in student_marks.items():
    if key == query_name:
        summ = 0
        count = 0
        for num in val:
            summ += num
            count += 1
        res = summ/count
        print(f'{res:.2f}')
        break