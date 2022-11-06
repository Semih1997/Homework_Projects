import random
shot_number = 0
pointlist = []
for _ in range(10):
    cordinates = []
    num1 = (random.uniform(0,20))
    num2 = (random.uniform(0,20))
    shots = (round(num1,1),round(num2,1))
    shot_number += 1
    distance = ((num1**2)+(num2**2))**0.5
    if distance < 3:
        point = 10
        pointlist.append(point)
    elif distance >= 3 and distance < 6:
        point = 5
        pointlist.append(point)
    elif distance >= 6 and distance < 9:
        point = 3
        pointlist.append(point)
    elif distance >= 9 and distance < 12:
        point = 2
        pointlist.append(point)
    elif distance >= 12 and distance < 15:
        point = 1
        pointlist.append(point)
    else :
        point = 0
        pointlist.append(point)
    print("Your {}. shoots:" .format(shot_number), ' - '.join(str(x) for x in shots) , "==>" , point , "points!")
print("Your Total Score is: ", sum(pointlist))