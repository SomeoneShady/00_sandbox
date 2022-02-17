

total_cost = 0.00
sugar_tax = 0.50

bread_type = input("Sandwich or wrap? ").lower()

filling_type = input("Meat, vegetarian or vegan? ").lower()

pudding = input("Cookie, chips, fruit or none ").lower()

drink = input("Fizzy drink, water or none? ").lower()

extra_sauce = input("Would you like extra sauce? ").lower()

extra_salad = input("Do you want extra salad? ").lower()

if bread_type != "sandwich":
    total_cost = 2.00
else:
    total_cost = 3.00

if filling_type == "vegetarian" or filling_type == "vegan":
    total_cost = total_cost + 1.00
else:
    total_cost = total_cost + 1.50

if pudding == "cookie" and drink == "fizzy drink":
    total_cost = total_cost + sugar_tax

if pudding == "none" or drink == "none":
    total_cost = total_cost - 0.50

if extra_salad == "yes" and extra_sauce == "yes":
    total_cost = total_cost + 1.00

print("Your total cost is: ${}".format(total_cost))
print("Have a good day!")
