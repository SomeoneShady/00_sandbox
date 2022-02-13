name = input("What is your name? ").lower()

if name == "anakin":
    print("How do you do, anakin!")
elif name == "leia":
    print("May the force be with you")
else:
    print("Nice name, {}".format(name))

weather = input("So {}, is it hot or cold where you are today? ".format(name)).upper()
if weather == "COLD":
    print("You must be freezing!")
elif weather == "HOT":
    print("Drink plenty of water")
else:
    print("I can't advise you on that type of weather")

likes_blue = input("do you like the colour blue? ").upper()
if likes_blue == "YES":
    print("I like blue too!")
else:
    print("That’s a shame, because I really like blue")

print("Have a good day, bye")
