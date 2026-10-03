"""
Program: Shopping Cart
Author: Delcio Eduardo
I added a cleaner display with numbered items and a safer remove check, so the cart is easier to use and closer to the assignment requirements.
"""

print("Welcome to the Shopping Cart Program!\n")

item_names = []
item_prices = []

while True:
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    try:
        action = int(input("Please enter an action: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue

    print()

    if action == 1:
        item_name = input("What item would you like to add? ")

        try:
            item_price = float(input(f"What is the price of '{item_name}'? "))
        except ValueError:
            print("Invalid price. Please enter a valid number.\n")
            continue

        item_names.append(item_name)
        item_prices.append(item_price)
        print(f"'{item_name}' has been added to the cart.\n")

    elif action == 2:
        if not item_names:
            print("The cart is empty.\n")
        else:
            print("The contents of the shopping cart are:")
            for i, (name, price) in enumerate(zip(item_names, item_prices), start=1):
                print(f"{i}. {name} - ${price:.2f}")
            print()

    elif action == 3:
        if not item_names:
            print("Your cart is empty. Nothing to remove.\n")
            continue

        print("The contents of the shopping cart are:")
        for i, (name, price) in enumerate(zip(item_names, item_prices), start=1):
            print(f"{i}. {name} - ${price:.2f}")

        try:
            remove_choice = int(input("Which item would you like to remove? "))
        except ValueError:
            print("Sorry, that is not a valid item number.\n")
            continue

        if 1 <= remove_choice <= len(item_names):
            item_names.pop(remove_choice - 1)
            item_prices.pop(remove_choice - 1)
            print("Item removed.\n")
        else:
            print("Sorry, that is not a valid item number.\n")

    elif action == 4:
        total = sum(item_prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}\n")

    elif action == 5:
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid choice, try again.\n")