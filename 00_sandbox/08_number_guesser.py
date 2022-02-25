lives = 3
tries_attempted = 1
print("Hello, I have a challenge for you! Can you guess the number I am currently thinking of?")

while True:
    try:
        user_input = input("Now, guess the number! (Hint: It's between 1-10)")
        if user_input == "6":
            print("Wow! You guess the number! I know you could do it!")
            break
        elif user_input != "6":
            lives -= 1
            tries_attempted += 1
            print("Incorrect, try again! You have {} lives remaining".format(lives))
            if lives == 0:
                print("You have run out of lives! What a shame...")
                break
    except:
        print("Come on, just guess a number, I believe in you!")

print("Interesting, you ended the game with {} tries!".format(tries_attempted))
