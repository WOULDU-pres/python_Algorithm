A = int(input("hour (0 ≤ A ≤ 23) : "))
B = int(input("minute (0 ≤ B ≤ 59) : "))
C = int(input("finish (0 ≤ C ≤ 1,000) : "))

if B+C >= 60:
    A = A+((B+C)//60)
    if A >= 24:
        A = A%24

C = C%60
B = (B+C)%60

print(A, B)