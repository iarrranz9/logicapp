import data

def app():
    print("Hi! Welcome to the best fitness app!!! ")
    save = input("Do you want to register to train??? Type 'y' for yes 'n' for no")
    f = False
    while not f:
        if save == "y":
            state = input("Are you a new user, a current user or just a visitor?")
            if state == "new":
                print("ENTER DATA!!!\n---------------------------------------------------------------------")
                input("ID machine")
                input("Name")
                input("Sensor activity")
                input("Value pression")
                input("Date and time?")
                trainment = input("Do you want to work with a therapist, without assist or with app guidance?")
                if trainment == "guidance":
                    body_part = input("What do you want to train today?")
                    print(f"This is your guide for {body_part}:")
                    f = True
            elif state == "current":
                user = input("Select your user")
                password = input("Enter your password")
                if user == data.data["name"] and password == data.data["password"]:
                    trainment = input("Do you want to work with a terapist, without assist or with app guidance?")
                    if trainment == "guidance":
                        body_part = input("What do you want to train today?")
                        print(f"This is your guide for {body_part}:")
                        f = True
                    else:
                        f = True
                else:
                    print("Invalid user or password")
            elif state == "visitor":
                input("Type your name(voluntary)")
                trainment = input("Do you want to work with a therapist, without assist or with app guidance?")
                if trainment == "guidance":
                    body_part = input("What do you want to train today?")
                    print(f"This is your guide for {body_part}:")
                    f = True
                else:
                    f = True
        elif save == "n":
            trainment = input("Do you want to work with a therapist, without assist or with app guidance?")
            if trainment == "guidance":
                body_part = input("What do you want to train today?")
                print(f"This is your guide for {body_part}:")
                f = True
            else:
                f = True
        else:
            print("Enter a valid option!!!")
            save = input("Do you want to register to train??? Type 'y' for yes 'n' for no")

app()




