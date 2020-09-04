def start():
    yes = "yes"
    no = "no"
    #its a water bottle intake calculator
    print("Hi, this is a Water Intake Calculator")
    #ask if you have drank water today out of a water bottle
    drank = input("have you drank water today out of a water bottle? \n")
    #if you say yes it runs the if statement and if something else the funcntion restarts
    if drank == yes:
        Bottles = int(input("Please Type how ever Many Water Bottles you Drank: "))
        #A regualar water bottle is 16.9 oz and then also multiply by how many times you drank water
        TodayIntake = Bottles * 16.9
        print("You Drank " + str(TodayIntake) + " oz of Water")
    else:
        start()
start()