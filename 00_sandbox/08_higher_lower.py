import random

number = random.randint(1,10)
player_guess = 0
player_guesses = 0
lives = 3

print(number)

while player_guess != number and player_guesses != lives:
    try:
        player_guess = int(input("Try and guess a number between 1 and 10! "))
    except:
        print("Please enter a number!")

    if player_guess == number:
        print("Fantastic! You guessed the right number!")
    else:
        player_guesses = player_guesses + 1
        print("Incorrect, you have {} lives remaining!".format(lives - player_guesses))
        if player_guess < number:
            print("Here's a hint: The number is higher than what you guessed!")
        else:
            print("Here's a hint: The number is lower than what you guessed!")


if player_guesses == lives:
    print("You ran out of lives, what a shame!")
