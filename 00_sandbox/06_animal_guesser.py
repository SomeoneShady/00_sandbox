print("Pick either Ostrich, Lion, or Whale")
print("I will attempt to guess your choice!")

answer = input("Does your animal live in the water? Input either Y or N").lower()

if answer == "n":
    answer = input("Does your animal have wings? Y/N").lower()

    if answer == "y":
        print("It must be an Ostrich!")
    else:
        print("It must be a lion!")
else:
    print("It must be a whale!")
