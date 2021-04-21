import random as ra
p = 1
while(p):
    roll=input("Press r to roll the die or e to exit\t")
    if roll == "r":
        x=ra.randint(1,6)
        if x==1:
            print(" -----")
            print("|     |\n|  0  |\n|     |")
            print(" -----")
        elif x==2:
            print(" -----")
            print("|     |\n| 0 0 |\n|     |")
            print(" -----")
        elif x==3:
            print(" -----")
            print("|  0  |\n|  0  |\n|  0  |")
            print(" -----")
        elif x==5:
            print(" -----")
            print("| 0 0 |\n|  0  |\n| 0 0 |")
            print(" -----")
        elif x==4:
            print(" -----")
            print("| 0 0 |\n|     |\n| 0 0 |")
            print(" -----")
        elif x==6:
            print(" -----")
            print("| 0 0 |\n| 0 0 |\n| 0 0 |")
            print(" -----")
    elif roll == "e":
        p = 0
        
