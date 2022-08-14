answer = 0

while True:
    try:
        times_table = int(input("What times table do you want us to solve?"))
        maximum_value = int(input("Now, what is the maximum value you want me to go up too?"))
        break
    except:
        print("Please enter a number!")

print("Here is the {} times tables you have requested:".format(times_table))
for x in range(1,maximum_value):
    answer = x * times_table
    user_answer = int(input("It's now your turn, {} times {} equals?".format(x, times_table)))
    if user_answer == answer:
        print("Correct! Now, for the next question!")
    else:
        print("Incorrect!, the correct answer is {}!".format(answer))
