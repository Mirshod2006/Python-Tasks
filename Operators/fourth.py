angle = int(input("Enter the value of angle:"))
if angle>0 and angle<90:
    print("The angle is acute")
elif angle==90:
    print("The angle is right")
elif angle>90 and angle<180:
    print("The angle is obtuse")
elif angle==180:
    print("The angle is curse")