"""The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal."""

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
if query_name in student_marks.keys():
    a = student_marks[query_name]
    sum_m = 0
    for i in a:
        sum_m = sum_m + i
    
    print(format(sum_m/3,".2f"))