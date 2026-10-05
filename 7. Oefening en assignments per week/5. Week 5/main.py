#Step 1, 2 and 3 is in profiles.py

from games.roulette import play_roulette
from games.fruit_machine import fruit_machine
from games.blackjack import blackjack

from profiles import initialize_player, create_profile, add_profile, switch_profile, show_all_profiles, delete_profile, players

#Fixed cost
entrance_fee = 10
parking_fee = 10.50
drinks_fee = 10

total_cost = entrance_fee + parking_fee + drinks_fee

# Steps 1, 2 and 3: Are in Profile check/add/switch/delete with profiles.py
current_player = initialize_player(total_cost)

balance = players[current_player]["balance"]

print("Your balance is €:",balance)

#step 5: Main menu
def main_menu(balance, current_player):
    profile = players[current_player]

    print("             Main Menu              ")
    print("------------------------------------")
    print("Welcome", profile["greeting"], profile["name"], profile["surname"] , "to De Goude Driehoek Casino!")
    print("------------------------------------")
    print("1. Games")
    print("2. Account Information")
    print("3. Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        balance = games_menu(balance, current_player)

    elif choice == "2":
        account_information(balance, current_player)

    elif choice == "3":
        balance_menu(balance, current_player)

    elif choice == "4":
        current_player = initialize_player

#step 6: Games Menu
def games_menu(balance, current_player):
    #Games menu
    while True:
        print("Games Menu")
        print("1. Roulette")
        print("2. Fruit machine")
        print("3. Blackjack")
        print("4. Return to the main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            balance = play_roulette(balance, current_player)
        elif choice == "2":
            balance = fruit_machine(balance, current_player)
        elif choice == "3":
            balance = blackjack(balance, current_player)
        elif choice == "4":
            main_menu(balance, current_player)

            return
#Step 7: Account Info
def account_information(balance, current_player):
    profile = players[current_player]

    print("Account Information")
    print("1. View Profile")
    print("2. Add Profile")
    print("3. Switch Profile")
    print("4. Show All Profiles")
    print("5. Delete Profile")
    print("6. Main Menu ")

    choice = input("Choose an option: ")

    if choice == "1":
        print(profile["greeting"], profile["name"], profile["surname"])
        print("Birthdate:", profile["birthdate"])
        print("Gender: ", profile["gender"])
        print("Balance:", profile["balance"])
        print("Played Games:", profile["played_games"])

        account_information(balance, current_player)

    elif choice == "2":
        add_profile()
        account_information(balance, current_player)

    elif choice == "3":
        current_player = switch_profile()
        main_menu(balance, current_player)

    elif choice == "4":
        show_all_profiles()
        account_information(balance, current_player)

    elif choice == "5":
        current_player = delete_profile()
        account_information(balance, current_player)

    elif choice == "6":
        main_menu(balance, current_player)
    else:
        account_information(balance, current_player)
#Step 8: Balance Menu
def balance_menu(balance, current_player):
    profile = players[current_player]
    print("1. ", profile["balance"])
    print("0. Main Menu")

    choice = input("Choose an option: ")
    if choice == "1":
        print("Your balance is", profile["balance"])
    elif choice == "0":
        main_menu(balance, current_player)
    else:
        balance_menu(balance, current_player)

#Step 9: Return to Main menu
main_menu(balance, current_player)





