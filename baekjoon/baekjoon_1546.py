import numpy

N = int(input("N <= 1000 : "))

list=[]
for i in range(N):
    subject = int(input("0 <= subject{} <= 100 : ".format(i)))
    list.append(subject)

list.sort()

M = list[N-1]

for i in range(N):
    change = list[i]/M*100
    list[i] = round(change, 2)

average = numpy.mean(list)
print(average)