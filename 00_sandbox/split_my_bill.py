print("Welcome to Split My Pizza!")
print("Each slice of pizza is $1!")

while True:
    try:
        number_of_slices = int(input("How many slices do you want?"))
        if number_of_slices > 0:
            break
    except:
        print("We cannot make that amount of pizza, please choose again")


while True:
    try:
        customers = int(input("How many people are sharing?"))
        if customers > 0:
            break
    except:
        print("What's the point of ordering if you can't bring a suitable amount of people?")


while True:
    try:
        tip_percentage = int(input("How much money would you like to leave as a tip?"))
        if tip_percentage >= 0:
            break
    except:
        print("We're not going to pay you for ordering our food!")

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


