num1 = int(input("num1 : "))     #(1)
num2 = int(input("num2 : "))     #(2)

num3 = num1 * int(str(num2)[0])
num4 = num1 * int(str(num2)[1])
num5 = num1 * int(str(num2)[2])
num6 = num1 * num2

num3 = str(num3)
num4 = str(num4) + " "
num5 = str(num5) + "  "

print("\n(세 자리 수)x(세 자리 수)")
print('{:10d}'.format(num1))     #(1)
print('{:10d}'.format(num2))     #(2)
print('{:10.10}'.format("-------------------"))  
print('{:>10}'.format(num3))     #(3)
print('{:>10}'.format(num4))     #(4)
print('{:>10}'.format(num5))     #(5)
print('{:10.10}'.format("-------------------"))   
print('{:10d}'.format(num6))     #(6)