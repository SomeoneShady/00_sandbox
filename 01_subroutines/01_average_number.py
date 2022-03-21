def average_value (a, b, c):
    average = (a + b + c) / 3
    print("({} + {} + {}) / 3 = {}".format(a, b, c, average))
    print("The average value is {}".format(average))


num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
num3 = int(input("Enter one final number"))

average_value(num1, num2, num3)
