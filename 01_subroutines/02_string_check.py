def int_check(question):
    while True:
        try:
            response = int(input(question))
            break
        except ValueError:
            print("That's not a real age! Be honest!")
    return response

def check_input(letter_age):
    while True:
        digi_check = input(letter_age)
        if digi_check.isdigit():
            print("Those are not letters! I demand letters!")
        else:
            break
    return digi_check





question = int_check("How old are you?")
letter_age = check_input("Now write your age using letters!")
user_age = question
if user_age <= 5:
    print("You're far too young! Begone!")
elif user_age >= 70 and user_age != 420:
    print("A true computer veteran! What an honour!")
elif user_age == 69 or user_age == 420:
    print("nice")
else:
    print("Ah, {}, a fine age indeed.".format(user_age))
