from re import A


num = int(input("num : "))
a=0
b=0


for i in range(1,10000000):
    a = num-i
    num = a
    if a <= 0:
        break

a = a + i
b = i+1-a

if i%2 == 0:
    print("{}/{}".format(a,b))
else:
    print("{}/{}".format(b,a))