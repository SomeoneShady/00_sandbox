user_input = input("Welcome! See if you can guess what letters are in my word!").lower()
word = "sheep"
letters_number = 0

for letter in word:
    if letter == user_input:
        letters_number += 1


print("Hmm, it appears the letter you have chosen: {}, appears {} times".format(user_input, letters_number))

if user_input == "sheep":
    print("Hold on a second! How'd you guess the word? Are you cheating? Or is this not the first time you've done this...?")
