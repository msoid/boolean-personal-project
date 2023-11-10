# tells the user what kind of accessories, clothing, or action they need to wear or do today based on the weather 

# variables used
usertf = bool(input("(True/or leave blank) I am on Earth: "))

# defines function used if users answers match
def usertcomp():
    userrain = str(input("Is it raining today?: "))
    userheat = str(input("Is it hot today?: "))
    usercold = str(input("Is it cold today?: "))
    if userrain == "yes" and userheat == "yes" and usercold == "yes":
        print("Seems like an oddball day, maybe aliens are coming?")
    elif userrain == "yes" and userheat == "no" and usercold == "no":
        print("You need an umbrella.")
    elif userrain == "yes" and userheat == "yes" and usercold == "no":
        print("You should wear light clothes and bring an umbrella.")
    elif userrain == "yes" and userheat == "no" and usercold == "yes":
        print("You might need to watch out for hail, and bring an umbrella regardless.")
    elif userrain == "no" and userheat == "no" and usercold == "no":
        print("It's probably a pretty nice day out...")
    elif userrain == "no" and userheat == "yes" and usercold == "yes":
        print("You're lying, it can't be hot and cold at the same time.")
    elif userrain == "no" and userheat == "no" and usercold == "yes":
        print("You should bring a hat and gloves, maybe even a jacket..")
    elif userrain == "no" and userheat == "yes" and usercold == "no":
        print("You need to wear light clothing and drink water.")
    else:
        print("Cannot help you today. try again later.")

# executes code based on users response
if usertf == True:
    usertcomp()
else:
    print("You must be on Earth to ask about the weather.")


