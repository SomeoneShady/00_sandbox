print("Welcome to Split My Pizza!")
print("Each slice of pizza is $1!")

number_of_slices = int(input("How many slices do you want?"))

customers = int(input("How many people are sharing?"))

tip_percentage = int(input("How much money would you like to leave as a tip?"))

slices_per_customer = number_of_slices//customers
remaining_pizza = number_of_slices % customers
percentage_decimal = tip_percentage / 100
tip_total = number_of_slices * percentage_decimal
bill_total = number_of_slices + tip_total

cost_per_customer = bill_total / customers
print("To make things fair, each person will get {} slices of pizza"
      " and there will be {} spare pieces left for anyone to grab!".format(slices_per_customer, remaining_pizza))

print("Total bill including your lovely tip is ${}".format(bill_total))

print("Total cost per person will be ${}".format(cost_per_customer))

print("Thank you for coming to Split My Pizza! We hope to see you again soon!")


