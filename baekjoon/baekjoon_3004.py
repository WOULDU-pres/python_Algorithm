cut = int(input("How many times will you cut the board? : "))
print("I will cut {} times".format(cut))

if cut % 2 == 1: # 홀수 번 자를 때
    answer = (cut//2 + 1) * (cut//2 +2)
else:            # 짝수 번 자를 때
    answer = (cut//2 + 1) ** 2

print(answer)