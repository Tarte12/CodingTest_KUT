n = int(input())
students = []

for _ in range(n):
    students.append(input())

length = len(students[0]) #길이 체크

for k in range(1, length+1):
    lst = set() #중복 안 되게 담아서 학생수랑 같은지 체크

    for student in students:
        lst.add(student[-k:])

    if len(lst) == n:
        print(k)
        break