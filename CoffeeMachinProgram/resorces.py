availableresources = {
    "coffee": 100,
    "milk": 800,
    "water": 1000
}

print(availableresources["coffee"])

requirementsForCoffee = {
    "espresso": {"coffee": 18,
                 "milk": 0,
                 "water": 50,
                 "price": 1.50},

    "latte": {"coffee": 24,
              "milk": 150,
              "water": 200,
              "price": 2.50},

    "cappuccino": {"coffee": 24,
                   "milk": 100,
                   "water": 250,
                   "price": 3.00}
}
print(requirementsForCoffee)


def Availability(coffeeType):
    print(coffeeType)
    for key in availableresources:
        if requirementsForCoffee[coffeeType][key] > availableresources[key]:
            print( f"Sorry! sufficient '{key}' is not present so cant make it '{coffeeType}'")
            return "block"

    return "next"
