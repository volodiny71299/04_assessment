# Component three, PRINT ANSWER options

import random


def num_checker(question, low, high):
    valid = False
    while not valid:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print("You did not enter 1, 2 or 3")
        except ValueError:
            print("You did not enter a number, try again")

secret_one = float(random.uniform(100, 10000))
print("Number (1): {:.2f}".format(secret_one))

secret_two = float(random.uniform(100, 10000))
print("Number (2): {:.2f}".format(secret_two))

if secret_one > secret_two:
    print("{:.2f} - {:.2f} = {:.2f}".format(secret_one, secret_two, secret_one - secret_two))
else:
    print("{:.2f} + {:.2f} = {:.2f}".format(secret_one, secret_two, secret_one + secret_two))


chosen_answer = num_checker("1)\n2)\n3)\n", 1, 3)

print()
print("Your answer is {}".format(chosen_answer))
