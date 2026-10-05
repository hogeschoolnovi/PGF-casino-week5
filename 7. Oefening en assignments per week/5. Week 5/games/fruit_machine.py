#Fruit_Machine

import random

from profiles import players, register_played_game

# Fruit Machine

#Step 1: Ask for bet
def ask_for_bet(balance):

    while True:
        stake = float(input("How much would you like to bet? "))

        if stake <= balance:
            return stake
        else:
            print("You don't have enough money.")
            print("Please choose a different amount.")

#Step 2: Determine Roll/Result
def determine_rolls(round_number):

    option = round_number % 5

    if option == 0:
        return "kers", "citroen", "ster"

    elif option == 1:
        return "kers", "kers", "kers"

    elif option == 2:
        return "ster", "ster", "citroen"

    elif option == 3:
        return "citroen", "kers", "ster"

    else:
        return "ster", "ster", "ster"

#Step 3: Determine Payout
def determine_payout(roll1, roll2, roll3, stake):

    if roll1 == roll2 and roll2 == roll3:
        return stake * 3

    elif roll1 == roll2 or roll1 == roll3 or roll2 == roll3:
        return stake * 2

    else:
        return 0

#Step 4: Run of Fruit Machine
def fruit_machine(balance, current_player):

    round_number = 1

    while True:

        print()
        print("Welcome to the Fruit Machine!")
        print("Your balance is:", balance)
        print("1. Play")
        print("2. Return to games menu")

        choice = input("Choose an option: ")

        if choice == "2":
            return choice

        elif choice == "1":
            #Get_bet/stake
            stake = ask_for_bet(balance)

            #Remove_bet_from_the_balance
            balance = balance - stake
            #Determine_roll
            roll1, roll2, roll3 = determine_rolls(round_number)
            #Print_Roll_results
            print()
            print("Roll 1:", roll1)
            print("Roll 2:", roll2)
            print("Roll 3:", roll3)

            #Determine_payout
            payout = determine_payout(
                roll1,
                roll2,
                roll3,
                stake)
            #Add_payout_to_balance
            if payout > 0:

                balance = balance + payout

                print("You've won!")
                print("Your payout is:", payout)

            else:

                print("You've lost!")

            #Show_balance
            print("Your balance is:", balance)

            players[current_player]["balance"] = balance
            register_played_game("fruit_machine")
            #Games Played
            round_number = round_number + 1

        else:
            print("Please choose 1 or 2.")

