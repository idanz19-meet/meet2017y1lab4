speed = input("What was the speed you were going in?")
is_birthday = False

if int(speed) < 31:
    print("no ticket for you, sir")
elif int(speed) < 51 and speed > 30:
    print("Small ticket for you, sir")
else:
    print("Big ticket for you, sir")
