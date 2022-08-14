# Function that constantly loops until the user provides a proper answer
def age_checker(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            break
        except ValueError:
            print("That's not a real age! Be honest!")
    return response

# Ask the user how old they are
age = age_checker("Now, can you tell me how old you are?")

