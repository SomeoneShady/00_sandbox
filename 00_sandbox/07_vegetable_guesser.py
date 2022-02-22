print("Pick either Carrot, Peas, Broccoli, or Sweetcorn ")
print("I will attempt to guess your chosen vegetable!")

answer = input("Is your vegetable green? Input either Y or N").lower()

if answer == "n":
    answer = input("Is your vegetable orange? Y/N").lower()

    if answer == "y":
        print("It must be a Carrot!")
    else:
        print("It must be Sweetcorn!")

if answer == "y":
    answer = input("Does the vegetable look like a tree? Y/N").lower()

    if answer == "y":
        print("It must be Broccoli!")
    else:
        print("It must be Peas!")
