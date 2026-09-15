
# W02 Project: Meal Price Calculator
# This program calculates the meal subtotal, sales tax, total amount,
# and the change returned to the customer. It also displays the
# restaurant name to make the calculator more personalized.

child_price = float(input("What is the price of the child meal? "))
adult_price = float(input("What is the price of the adult meal? "))

number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

tax_rate = float(input("What is the sales tax rate (%)? "))

# Calculate subtotal
subtotal = (child_price * number_of_children) + (adult_price * number_of_adults)

# Calculate sales tax
sales_tax = subtotal * (tax_rate / 100)

# Calculate total
total = subtotal + sales_tax

# Ask for payment
payment = float(input("What is the payment amount? "))

# Calculate change
change = payment - total

# Ask for restaurant name
restaurant_name = input("What is the name of the restaurant? ")

# Display results
print("\n--- Meal Price Calculator ---")
print("Restaurant:", restaurant_name)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total Amount: ${total:.2f}")
print(f"Payment Amount: ${payment:.2f}")
print(f"Change: ${change:.2f}")
