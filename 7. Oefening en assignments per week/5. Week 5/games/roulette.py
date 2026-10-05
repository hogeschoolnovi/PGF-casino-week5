#Roulette.py

from profiles import players, register_played_game

import random

#Step 1: Show Roulette options.
#Step 2: Ask on what they would like to place the bet.
#Step 3: Ask How much the client would want to bet.
#Step 4: Check whether the bet is valid. (While loop)
#Step 5: Generate the roulette number.
#Step 6: Decide whether they won or lost.
#Step 7: Allow them if they would like to play another round.

#Step 1: Show Roulette options.
def show_roulette_options(balance, current_player):
    print(" Welcome to Roulette!! ")
    print("Your balance is:", balance)
    print(" Please choose one of the following options. ")
#Step 2: Ask on what they would like to place the bet.
    print("1. Single Number")
    print("2. Red ")
    print("3. Black ")
    print("4. Odd ")
    print("5. Even ")
    print("6. First 12")
    print("7. Second 12")
    print("8. Third 12")
    print("9. Return to games menu.")

    choice = input("What would you like to bet on?: ")

    if choice == "2":
        print("You chose Red ")

    if choice == "3":
        print("You chose Black ")

    if choice == "4":
        print("You chose Odd ")

    if choice == "5":
        print("You chose Even ")

    if choice == "6":
        print("You chose First 12")

    if choice == "7":
        print("You chose Second 12")

    if choice == "8":
        print("You chose Third 12")

    return choice

#Step 3: Ask How much the client would want to bet.
def ask_for_bet(balance):
    # Step 4: Check whether the bet is valid. (While loop)
    while True:
        stake = float(input("How much would you like to bet?: "))

        if stake <= balance:
            print("You have placed your bet! ")
            return stake

        else:
            print("Unfortunately you don't have sufficient funds... ")
            print("Please choose a different amount.")
#Step 5: Generate the roulette number.
def play_roulette(balance, current_player):
    balance = players[current_player]["balance"]

    round_number = 1

    while True:
        choice = show_roulette_options(balance, current_player)

        if choice == "9":
            return balance

        number = 0

        if choice == "1":
            print("You can now choose a single Number between 0 and 36.")
            number = int(input("Enter your single number: "))

        stake = ask_for_bet(balance)
        balance = balance - stake

        #Actual Spin
        roulette_number = random.randrange(0, 37)

        #Result
        print("The roulette number is:", roulette_number)

        #WDetermine result
        colour = determine_colour(roulette_number)
        odd_even = determine_odd_even(roulette_number)
        first_12 = determine_first_12(roulette_number)
        second_12 = determine_second_12(roulette_number)
        third_12 = determine_third_12(roulette_number)
        #Win Result
        win = determine_win(choice, number, roulette_number, colour, odd_even, first_12, second_12, third_12)

        if win == True:
            print("You've won!!")
            if choice == "1":
                balance = balance + stake * 36

            elif choice == "6" or choice == "7" or choice == "8":
                balance = balance + stake * 3

            elif choice == "2" or choice == "3" or choice == "4" or choice == "5":
                balance = balance + stake * 2

        else:
            print("You've lost!!")

        players[current_player]["balance"] = balance
        register_played_game("roulette")

        round_number = round_number + 1

def determine_colour(roulette_number):
    if roulette_number == 0:
        colour = "green"

    elif roulette_number == 1:
        colour = "red"

    elif roulette_number == 2:
        colour = "black"

    elif roulette_number == 3:
        colour = "red"

    elif roulette_number == 4:
        colour = "black"

    elif roulette_number == 5:
        colour = "red"

    elif roulette_number == 6:
        colour = "black"

    elif roulette_number == 7:
        colour = "red"

    elif roulette_number == 8:
        colour = "black"

    elif roulette_number == 9:
        colour = "red"

    elif roulette_number == 10:
        colour = "black"

    elif roulette_number == 11:
        colour = "black"

    elif roulette_number == 12:
        colour = "red"

    elif roulette_number == 13:
        colour = "black"

    elif roulette_number == 14:
        colour = "red"

    elif roulette_number == 15:
        colour = "black"

    elif roulette_number == 16:
        colour = "red"

    elif roulette_number == 17:
        colour = "black"

    elif roulette_number == 18:
        colour = "red"

    elif roulette_number == 19:
        colour = "red"

    elif roulette_number == 20:
        colour = "black"

    elif roulette_number == 21:
        colour = "red"

    elif roulette_number == 22:
        colour = "black"

    elif roulette_number == 23:
        colour = "red"

    elif roulette_number == 24:
        colour = "black"

    elif roulette_number == 25:
        colour = "red"

    elif roulette_number == 26:
        colour = "black"

    elif roulette_number == 27:
        colour = "red"

    elif roulette_number == 28:
        colour = "black"

    elif roulette_number == 29:
        colour = "black"

    elif roulette_number == 30:
        colour = "red"

    elif roulette_number == 31:
        colour = "black"

    elif roulette_number == 32:
        colour = "red"

    elif roulette_number == 33:
        colour = "black"

    elif roulette_number == 34:
        colour = "red"

    elif roulette_number == 35:
        colour = "black"

    elif roulette_number == 36:
        colour = "red"

    return colour
#determine odd_even
def determine_odd_even(roulette_number):
    if roulette_number == 0:
        odd_even = "zero"

    elif roulette_number % 2 == 0:
        odd_even = "even"

    else:
        odd_even = "odd"

    return odd_even

def determine_first_12(roulette_number):
    if roulette_number >= 1 and roulette_number <= 12:
        first_12 = True

    else:
        first_12 = False

    return first_12

def determine_second_12(roulette_number):
    if roulette_number >= 13 and roulette_number <=24:
        second_12 = True

    else:
        second_12 = False

    return second_12

def determine_third_12(roulette_number):
    if roulette_number >= 25 and roulette_number <=36:
        third_12 = True

    else:
        third_12 = False

    return third_12
#Step 6: Decide whether they won or lost.
def determine_win(choice, number, roulette_number,  colour, odd_even, first_12, second_12, third_12):

    if choice == "1":

        if number == roulette_number:
            win = True
            print("You have won!")
        else:
            win = False
            print("Unfortunately you have lost!")

    elif choice == "2" and colour =="red":
        win = True

    elif choice == "3" and colour =="black":
        win = True

    elif choice == "4" and odd_even =="odd":
        win = True

    elif choice == "5" and odd_even =="even":
        win = True

    elif choice == "6" and first_12 == True:
        win = True

    elif choice == "7" and second_12 == True:
        win = True

    elif choice == "8" and third_12 == True:
        win = True

    else:
        win = False
    # Step 7: Allow them, if they would like to, play another round.
    return win















