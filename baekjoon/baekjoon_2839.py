sugar = int(input("3<=N<=5000 : "))

bag_weight_5kg = 0
bag_weight_3kg = 0

if sugar%5 == 0:
    bag_weight_5kg = sugar//5

else:
    if (sugar%5)%3 == 0:
        bag_weight_3kg = (sugar%5)//3
        bag_weight_5kg = sugar//5
    else:
        if sugar%3 == 0:
            bag_weight_3kg = sugar//3
        else:
            bag_weight_3kg = -1

print(bag_weight_3kg + bag_weight_5kg)

        