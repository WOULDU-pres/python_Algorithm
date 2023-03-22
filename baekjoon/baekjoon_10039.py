import numpy as np

students = []
for i in range(1,6):
    score = int(input("점수 {} : ".format(i)))
    students.append(score)


for i in range(len(students)):
    if students[i] <= 40:
        students[i] = 40
    

print(np.mean(students))