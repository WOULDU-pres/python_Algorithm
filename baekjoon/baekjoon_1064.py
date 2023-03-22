import math

Xa, Ya, Xb, Yb, Xc, Yc = map(float, input("").split())
#Xa,Xb,Xc가 모두 같으면 -1
if Xa == Xb:
    if Xa == Xc:
        result = -1
    else:
        side_1 = ((Xa-Xb) ** 2) + ((Ya-Yb) ** 2)
        side_1 = math.sqrt(side_1)
        side_2 = ((Xb-Xc) ** 2) + ((Yb-Yc) ** 2)
        side_2 = math.sqrt(side_2)
        side_3 = ((Xc-Xa) ** 2) + ((Yc-Ya) ** 2)
        side_3 = math.sqrt(side_3)

        list = [side_1, side_2, side_3]
        list.sort()
        print(list)
        low = list[0]
        high = list[2]

        result = 2*(high - low)

else:
    # y = ax + b    
    a = (Ya - Yb) / (Xa - Xb)
    b = -(a*Xa) + Ya
    
    a = round(a,15)
    b = round(b,15)

    if Yc == (a*Xc)+b:
        result = -1
    else:
        side_1 = ((Xa-Xb) ** 2) + ((Ya-Yb) ** 2)
        side_1 = math.sqrt(side_1)
        side_2 = ((Xb-Xc) ** 2) + ((Yb-Yc) ** 2)
        side_2 = math.sqrt(side_2)
        side_3 = ((Xc-Xa) ** 2) + ((Yc-Ya) ** 2)
        side_3 = math.sqrt(side_3)

        list = [side_1, side_2, side_3]
        list.sort()
        low = list[0]
        high = list[2]

        result = 2*(high - low)

print(result)
