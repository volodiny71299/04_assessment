# Component three, GENERATE RANDOM numbers with .00 decimal points

import random

secret_one = float(random.uniform(100, 10000))
print("Number (1): {:.2f}".format(secret_one))
secret_two = float(random.uniform(100, 10000))
print("Number (2): {:.2f}".format(secret_two))

if secret_one > secret_two:
    print("{:.2f} - {:.2f} = {:.2f}".format(secret_one, secret_two, secret_one - secret_two))
else:
    print("{:.2f} + {:.2f} = {:.2f}".format(secret_one, secret_two, secret_one + secret_two))
