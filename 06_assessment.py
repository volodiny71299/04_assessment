# Rounds
import random
# Number checker for rounds, 


def int_check(question, low, high):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                valid = True
                return response
            else:
                print("You did not enter a number between {} and {}".format(low, high))
        except ValueError:
            print("Invalid input")


round_counter = 0
rounds_won = 0

keep_going = ""
while keep_going == "":
    rounds = int_check("How long do you want your quiz to be?\n(20 questions max)\n>>> ", 1, 20)
    while round_counter < rounds:
        a = round(random.uniform(1, 100), 2)
        b = round(random.uniform(1, 100), 2)

        total = round(a + b, 2)
        print("a = {}".format(a))
        print("b = {}".format(b))
        print(total)
        round_counter += 1
        print("Round ({})".format(round_counter))
        answer = float(input("Whats {:.2f} + {:.2f} = ".format(a, b)))
        if answer == total:
            print("Correct")
            rounds_won += 1
        else:
            print("You lose answer was - {:.2f}".format(a + b))
