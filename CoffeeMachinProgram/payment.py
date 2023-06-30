from resorces import requirementsForCoffee, availableresources


def payment(coffeeType):
    price = int(requirementsForCoffee[coffeeType]["price"])
    print("Please insert coines.")
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quarters = float(input("How many quarters?"))
    dimes = float(input("How many dimes?"))
    nickles = float(input("How many nickles?"))
    pennies = float(input("How many pennies?"))

    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if price > total:
        print("sorry that's not sufficient money. money refunded")
    elif total > price:
        remaining = round(total-price,2)
        print(f"Here is ${remaining} in change")
        print(f"Here is your {coffeeType} Enjoy!")
        for key in availableresources:
            availableresources[key] -= requirementsForCoffee[coffeeType][key]