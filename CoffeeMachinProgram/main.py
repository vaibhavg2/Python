from resorces import Availability, availableresources
from payment import payment

while True:
    coffee_type = input("Please choose what type of coffee you want ('espresso/latte/cappuccino'): ").lower()
    if coffee_type == "resources":
        print(availableresources)
    elif coffee_type == "fill":
        for key in availableresources:
            availableresources[key] += int(input(f"fill {key}: "))
    elif coffee_type in ["espresso", "latte", "cappuccino"]:
        AvailabilityPermissions = Availability(coffee_type)
        if AvailabilityPermissions == "next":
            payment(coffee_type)
    else:
        print("Please enter a proper input.")