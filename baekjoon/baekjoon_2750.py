N = int(input("1 <= N <= 1000: "))

list= []
count = 0

while count < N:
    num = int(input("num {} : ".format(count+1)))
    if num in list:
        print("Do again")
        continue
    list.append(num)
    count = count +1

list.sort()

for i in range(N):
    print(list[i])