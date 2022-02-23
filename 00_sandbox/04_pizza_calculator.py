total_cost = 0.00

crust_type = input("Would you like a thick or thin crust? ").lower()

size_type = input("Would you like your pizza to be 8/10 inches, or 12/14/18 inches? ").lower()

cheese_type = input("What type of cheese would you like?"
                    "We have margarita, vegetarian, vegan, hawaiian, and meat feast! ").lower()

if crust_type != "thin":
    total_cost = 8.00
else:
    total_cost = 10.00

if size_type == "12" or "14" or "18":
    total_cost = total_cost + 2.00
else:
    total_cost = total_cost + 0.00

if cheese_type == "vegetable" or "vegan":
    total_cost = total_cost + 1.00

elif cheese_type == "hawaiian" or "meat feast":
    total_cost = total_cost + 2.00

voucher_discount = input("If you have a voucher code, please use it now")

if voucher_discount == "FunFriday":
    total_cost = total_cost - 2.00


print("Your total cost is: ${}".format(total_cost))
print("Have a good day!")
