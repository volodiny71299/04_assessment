# Component one, NUMBER CHECKER


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


# chose_answer = num_checker("1) {}\n2) {}\n3) {}\nAnswer: ".format(yellow, pink, blue), 1, 3)
chose_answer = num_checker("1, 2 or 3? ", 1, 3)
print()
print("Your answer is {}".format(chose_answer))
