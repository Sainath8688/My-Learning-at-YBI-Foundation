marks = int(input("Enter a number:"))
if marks < 35:
    print("you are failed in exam")
elif marks>35:
    print("You are passed in exam!")
    if marks >= 50 and marks >= 60:
        print("you got Average marks")
    elif marks >= 61 and marks <=70:
        print("you got above average marks")
    elif marks >=71 and marks <= 90:
        print("you got a Good marks")
    elif marks >= 91 and marks <=100:
        print("You got a excellent marks")
else:
    print(" ")

