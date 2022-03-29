def highest(a, b):
    if num1 > num2:
        print("{} is higher than {}".format(num1, num2))
    elif num1 < num2:
        print("{} is higher than {}".format(num2, num1))


num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

highest(num1, num2)
