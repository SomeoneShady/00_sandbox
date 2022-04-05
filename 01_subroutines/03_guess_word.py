guesses = 5
stored_password = "password"
password = "Greatest"
pass_mismatch = stored_password != password
password_length = len(password)
print("This password contains {} letters.".format(password_length))
first_letter = password[0]
second_letter = password[1]
third_letter = password[2]
fourth_letter = password[3]
while pass_mismatch:
    print("Enter your password:")
    password = input()
    pass_mismatch = stored_password != password
    if password == "Greatest":
        break
    elif password == "greatest":
        print("Close, but you're missing a capital letter.")
    else:
        guesses -= 1
        print("Incorrect, you have {} guesses remaining".format(guesses))
    if guesses == 4:
        print("I shall provide you with a hint, the first letter is {}.".format(first_letter))
    elif guesses == 3:
        print("I see you are having trouble, here's another hint. The second letter is {}.".format(second_letter))
    elif guesses == 1:
        print("You shall be granted one final hint: The third and forth letters are {}, and {}".format(third_letter, fourth_letter))
    elif guesses == 0:
        break


if guesses != 0:
    print("Correct, you have been granted access.")
else:
    print("Guesses depleted. Locking computer until further notice.")
