# Component two, allows numbers with decimals


def statement_qestion(question):
    valid = False
    while not valid:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print("Please enter a number as answers are numbers only!")

answer = statement_qestion("What is 3 + 3 = ")
