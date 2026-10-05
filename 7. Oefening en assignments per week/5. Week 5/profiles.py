from datetime import datetime



players = {
    "JohnSmith": {
        "name": "John",
        "surname": "Smith",
        "birthdate": "01-01-1990",
        "gender": "m",
        "greeting": "Mr",
        "balance": 0,
        "played_games": {}
    },
    "SarahJones": {
        "name": "Sarah",
        "surname": "Jones",
        "birthdate": "15-05-1992",
        "gender": "f",
        "greeting": "Miss",
        "balance": 0,
        "played_games": {}
    },
    "MikeBrown": {
        "name": "Mike",
        "surname": "Brown",
        "birthdate": "20-08-1988",
        "gender": "m",
        "greeting": "Mr",
        "balance": 0,
        "played_games": {}
    }
}
current_player = ""
#Step 1: Profile Check
def initialize_player(total_cost):
    global current_player

    name = input("What is your name? ")
    surname = input("What is your surname? ")

    current_player = name + surname

    if name + surname in players:
        profile = players[current_player]
        print("Welcome Back", name, surname, "!")
        print("Your balance is €", profile["balance"])

    else:
        create_account(total_cost, name, surname)

        profile = players[current_player]
        balance = profile["balance"]
        start_budget = balance + total_cost

        print("Welcome to De Gouden Driehoek Casino!")
        print("Start budget:", start_budget)
        print("Fixed costs:", total_cost)
        print("Your balance is €", balance)

    return current_player

#Step 2: Create Account
def create_account(total_cost, name, surname):
    budget = float(input("What is your starting budget? €: "))

    balance = budget - total_cost

    if balance < 0:
        print("Unfortunately you dont have sufficient funds to enter the Casino!")
        return

    create_profile(name, surname)

    players[name + surname]["balance"] = balance

#Step 3: Start Menu
def create_profile(name, surname):
    birthdate = input("Whats your birthdate? (dd-mm-yyyy) ")
    #Step 2: Calculate Age
    if calculate_age(birthdate):
        print("Welcome to De Goude Driehoek Casino!")
    else:
        print("Unfortunately you are not old enough to enter the Casino.")
        exit()
    # Step 4: Gender
    gender = input("What is your gender? m/f/x ")

    if gender == "m":
        greeting = "Mr"
    elif gender == "f":
        greeting = "Miss"
    else:  # Anything apart from M/F
        greeting = "X"

    players[name + surname] = {"name":name,"surname":surname,"birthdate":birthdate,
                     "gender":gender, "greeting":greeting, "balance":0, "played_games":{} }

# Step 5: Add Profile
def add_profile():
    name = input("What is your name? ")
    surname = input("What is your surname? ")

    if name + surname in players:
        print("This profile already exists!")
        return

    create_profile(name, surname)

    budget = float(input("What is your budget? €:"))

    entrance_fee = 10
    parking_fee = 10.50
    drinks_fee = 10
    balance = budget - entrance_fee - parking_fee - drinks_fee

    if balance < 0:
        print("Unfortunately, you don't have sufficient funds to enter the Casino!")
        return

    players[name + surname]["balance"] = balance

    print("Profile created successfully!")
#Step 6: Switch Profile
def switch_profile():
    global current_player

    print("Available Profiles:")

    for player in players.keys():
        print(player)

    choice = input("Choose a profile from the list: ")

    if choice in players:
        current_player = choice
        print("Profile switched successfully!")
        print("Current Profile:", current_player)
    else:
        print("Unfortunately, you don't have a active profile.")

    return current_player

#Step 7: Show All Profiles
def show_all_profiles():
    print("All Available Profiles:")
    for player in players:
        profile = players[player]
        print("-", player, "Balance:", profile["balance"])

#Step 8: Delete Profile
def delete_profile():
    global current_player

    if len(players) == 1:
        print("You cannot delete the last profile!")
        return current_player

    print("Available Profiles:")

    for player in players.keys():
        print(player)

    choice = input("Which profile would you like to delete? : ")

    if choice not in players:
        print("Profile not found!")
        return current_player

    del players[choice]
    print("Profile deleted successfully!")

    if choice == current_player:
        for player in players:
            current_player = player
            break

    print("Current Profile:", current_player)


    return current_player

#Step 9: Add Games amount played
def register_played_game(game_name):
    profile = players[current_player]

    if game_name in profile["played_games"]:
        profile["played_games"][game_name] += 1
    else:
        profile["played_games"][game_name] = 1

#Step 10: Get Current Balance
def get_current_balance():
    profile = players[current_player]
    return profile["balance"]

#Step 11: Update Current Balance
def update_current_balance(balance):
    profile = players[current_player]
    profile["balance"] = balance


#Step 12: Calculate Age
def calculate_age(birthdate):
    date_of_birth = datetime.strptime(birthdate, "%d-%m-%Y")
    today = datetime.today()
    age = today.year - date_of_birth.year
    print(age)
    if age >= 18:
        return True
    else:
        return False








