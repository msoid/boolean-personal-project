#tells the user what kind of accessories, clothing, or action they need to wear or do today based on the weather (i did not have time to do every posisble combination, sorry)

usersun = str(input("Is it sunny today?: "))
userrain = str(input("Is it raining today?: "))
usersnow = str(input("Is it snowing today?: "))
userheat = str(input("Is it hot today?: "))
usercold = str(input("Is it cold today?: "))

# userhealth = bool(input("True or False: I am on Earth: "))

while True:
    if usersun == "Yes" and userrain == "No" and usersnow == "No" and userheat == "No" and usercold == "No":
        print("You need sunglasses.")
    if usersun == "Yes" and userrain == "Yes":
        print("You need to look for a rainbow.")
    if usersun == "Yes" and usercold == "Yes":
        print("That's a bit strange...")
    if usersun == "Yes" and userheat == "Yes":
        print("Wear sunglasses and shorts.")
    if usersun == "Yes" and usersnow == "Yes":
        print("I think you're lying.")
    if usersun == "Yes" and userrain == "Yes" and usersnow == "Yes" and userheat == "Yes" and usercold == "Yes":
        print("Don't lie.")
    if usersun == "No" and userheat == "No":
        print("You need to wear a jacket.")
    if userrain == "Yes":
        print("You need to get an umbrella.")
    if userrain == "Yes" and usercold == "Yes":
        print("Don't drive, there might be ice on the roads.")
    if usersnow == "Yes" or usercold == "Yes":
        print("You need a hat and gloves.")
    """
    elif userhealth == "False":
        print("Aliens suck. Try again when you're human.")
        """