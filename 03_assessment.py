# Component three, choose what game to play

game_multi_choice = "multi-choice"
game_other = "other"
error = "please enter 1 or 2"


keep_going = ""
while keep_going == "":
    choose = input("Multi-choice(1) or other(2)? ").lower()

    if choose == "1":
        print()
        print("you chose", game_multi_choice)
        print()

    elif choose == "2":
        print()
        print("you chose", game_other)
        print()

    else:
        print()
        print(error)
        print()

keep_going = input("<enter>")
