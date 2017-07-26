weather = input("is it raining?")
train = input("are there delays on the train?")

if train == "yes" and weather == "yes":
    print("I think we should take a taxi...")
elif weather == "yes":
    print("It will be better to take a train")
else:
    print("Let us walk home")
