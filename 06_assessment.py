# Rounds
import random
# Number checker for rounds, valid in between 1 and 20 (inclusive)


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
# function that allows float numbers (decimal point)


def qst_statement(question):
    valid = False
    while not valid:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print("Invalid input, try again")


# Start of loop to the game
keep_going = ""
while keep_going == "":

    # Sets round info to 0 rounds
    round_counter = 0
    rounds_won = 0

    # Amount of rounds input (in range of 1 and 20)
    rounds = int_check("How many question would you like?\n(20 questions max)\n>>> ", 1, 20)

    # Start of round counter, keeps going until *round_counter* reaches rounds
    while round_counter < rounds:

        # Generates 2 random numbers in range of one (1) and one-hundred (100) with two (2) decimal points
        a = round(random.uniform(1, 100), 2)
        b = round(random.uniform(1, 100), 2)

        # Sums up (a) and (b) to find the total, answer to the question
        total = round(a + b, 2)

        # Prints (a), (b) and (answer) for test purposes
        print("\na = {}".format(a))
        print("b = {}".format(b))
        print(total, "\n")

        # Adds +1 round counter at the start of each round
        round_counter += 1

        # Prints number of current number
        print("Round ({})".format(round_counter))

        # compares your answer to actual answer
        answer = qst_statement("What's {:.2f} + {:.2f} = ".format(a, b))

        # When your answer is correct, print win statement and add a +1 win counter
        if answer == total:
            print("Correct")
            rounds_won += 1

        # You lose, prints lose statement
        else:
            print("You lose, answer was: {:.2f}".format(a + b))

        # kekw
    # End of loop, gives user option to continue or stop playing
    keep_going = input("Press <enter> to play again or any key to exit")
print("\nGood bye!")
