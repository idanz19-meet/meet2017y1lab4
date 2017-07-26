
for i in range(101):
    answer = input("what is " + str(i))
    if i % 3 == 0 and i % 5 == 0:
        if answer == "fizzbuzz":
            print("RIGHT")
        else:
            print("WRONG")
            break
    elif i % 3 == 0:
        if answer == "fizz":
            print("RIGHT")
        else:
            print("WRONG")
            break
    elif i % 5 == 0:
        if answer == "buzz":
            print("RIGHT")
        else:
            print("WRONG")
            break
    else:
       if int(answer) == i:
            print("RIGHT")
       else:
            print("WRONG")
            break
