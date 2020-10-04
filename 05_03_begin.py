def wash_car(amount_paid):
    if (amount_paid == "12"):
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    if (amount_paid == "6"):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 


user_input = input ("How much would you like to pay?")

wash_car(user_input)