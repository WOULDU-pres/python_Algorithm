N = int(input("0 <= N <= 99 : "))

count = 1
list = [N]
print(list)
new_num = -1

while N != new_num:
    num = (N//10) + (N%10)
    num = ((N%10)*10) + (num%10)
    if N == num:
        break
    list.append(num)
    print(list)

    while True:
        new_num = (list[count-1]%10) + (list[count]%10)
        new_num = ((list[count]%10)*10) + (new_num%10)
        if N == new_num:
            break
        list.append(new_num)
        count = count + 1
        print(list)

print(len(list))