# Component three, round counter

import random

rounds_won = 0

round_counter = 0

a = round(random.uniform(1, 100), 2)
b = round(random.uniform(1, 100), 2)

total = a + b

print(total)
answer = float(input("Whats {:.2f} + {:.2f} = ".format(a, b)))
if answer == total:
    print("Correct")
    round_counter += 1
else:
    print("You lose answer was - {:.2f}".format(a + b))
