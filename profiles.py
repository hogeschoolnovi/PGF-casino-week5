# Helperfuncties voor spelersprofielen in Casino de Gouden Driehoek

MIN_AGE = 18

players = {}
current_player = None

# ================
# Getters/updaters
# ================

def get_current_profile():
    """
    Return the profile of the current player.
    :return:
    """
    return players[current_player]


def get_current_balance():
    """
    Return the balance of the current player.
    :return:
    """
    return get_current_profile()["saldo"]


def update_current_balance(balance):
    """
    Update the balance of the current player.
    :param balance:
    :return:
    """
    get_current_profile()["saldo"] = balance



#================
# Helper functies (en de oude functies)
#================

def register_played_game(game_name):
    """
    Register a played game and increase its play count.
    :param game_name:
    :return:
    """
    played_games = get_current_profile()["gespeelde_spellen"]
    if game_name in played_games:
        played_games[game_name] += 1
    else:
        played_games[game_name] = 1


def determine_salutation(name, gender):
    """
    Determine the player's form of address.
    :param name:
    :param gender:
    :return:
    """
    if gender == "m":
        return f"meneer {name}"
    elif gender == "v":
        return f"mevrouw {name}"
    else:
        return f"speler {name}"


def calculate_age(birthdate):
    """
    Calculate someone's age based on their birth year.
    :param birthdate:
    :return:
    """
    birth_day, birth_month, birth_year = birthdate.split("-")
    return 2026 - int(birth_year)


def check_age(birthdate):
    """
    Check whether the player is at least 18 years old.
    :param birthdate:
    :return:
    """
    age = calculate_age(birthdate)
    if age < MIN_AGE:
        print("\nSorry, je moet 18 jaar of ouder zijn om deze applicatie te gebruiken.")
        exit(1)
    else:
        return birthdate

#================
# Account creatie
#================

def create_profile(name, birthdate, gender, balance):
    """
    Create a player profile as a dictionary.
    :param name:
    :param birthdate:
    :param gender:
    :param balance:
    :return:
    """
    return {
        "naam": name,
        "geboortedatum": birthdate,
        "gender": gender,
        "saldo": balance,
        "gespeelde_spellen": {},
    }


def create_start_players():
    """
    Create the initial collection of player profiles.
    :return:
    """
    return {
        "Banaan": create_profile("Banaan", "14-02-1998", "v", 50.0),
        "Appel": create_profile("Appel", "03-08-1997", "m", 30.0),
        "Kiwi": create_profile("Kiwi", "22-11-1999", "v", 40.0),
    }


def create_account(total_cost, name=None):
    """
    Create a new player account.
    :param total_cost:
    :param name:
    :return:
    """
    global current_player

    if name is None:
        name = input("Naam voor het nieuwe account: ").capitalize()
        if name in players:
            print("Dit account bestaat al. Gebruik wissel account om het te openen.")
            return

    birthdate = check_age(input("Wat is je geboortedatum? (dd-mm-yyyy) "))
    gender = input("Wat is je gender? (m/v/x) ").strip().lower()
    start_balance = float(input("Met hoeveel geld begin je in Casino de Gouden Driehoek? € "))
    balance = start_balance - total_cost
    players[name] = create_profile(name, birthdate, gender, balance)
    current_player = name
    return


def initialize_player(total_cost):
    """
    Initialize the player collection, select an existing account or create a new account and show the welcome message.
    :param total_cost:
    :return:
    """
    global players
    global current_player

    players = create_start_players()
    name = input("Wat is je naam? ").capitalize()
    current_player = name

    if name in players:
        profile = players[current_player]
        salutation = determine_salutation(current_player, profile["gender"])
        balance = profile["saldo"]
        print("\nCasino de Gouden Driehoek")
        print("-" * 35)
        print(f"Welkom terug, {salutation}")
        print()
        print(f"Saldo:          € {balance:.2f}")

    else:
        create_account(total_cost, name)

        profile = players[current_player]
        balance = profile["saldo"]
        start_balance = balance + total_cost  # Het startbudget wordt opnieuw berekend omdat create_account alleen het saldo na de vaste kosten opslaat.
        salutation = determine_salutation(current_player, profile["gender"])
        has_budget = total_cost <= start_balance
        conclusion = "Je hebt nog genoeg budget voor toegang tot het casino." \
            if has_budget \
            else "Je hebt niet voldoende budget voor toegang tot het casino."

        print("\nCasino de Gouden Driehoek")
        print("-" * 35)
        print(f"Welkom, {salutation}")
        print()
        print(f"Startbudget:    € {start_balance:.2f}")
        print(f"Vaste kosten:   € {total_cost:.2f}")
        print(f"Saldo:          € {balance:.2f}")
        print()
        print(conclusion)


def switch_account():
    """
    Select an existing account from the player collection.
    :return:
    """
    global current_player

    name = input("Welk account wil je gebruiken? ").capitalize()
    if name in players:
        current_player = name
        return True

    print("Dat account bestaat niet.")
    return False


def show_account():
    """
    Show the account menu and current player statistics.
    :return:
    """
    profile = get_current_profile()
    print("\nCasino de Gouden Driehoek - account")
    print("-" * 34)
    print(f"Huidige speler: {current_player}")
    print(f"Saldo: € {profile['saldo']:.2f}")
    print(f"Gespeelde spellen: {profile['gespeelde_spellen']}")
    print(f"Beschikbare spelers: {list(players.keys())}")


def remove_account():
    """
    Remove a player profile when it exists.
    :return:
    """
    global current_player

    player_to_remove = input("Welke speler wil je verwijderen? ").capitalize()

    if player_to_remove in players:
        if len(players) == 1: # Het laatst overgebleven profiel mag niet verwijderd worden.
            print("Het laatste account kan niet worden verwijderd.")
            return False
        del players[player_to_remove]
        if current_player == player_to_remove: # Zorg dat er altijd een actief profiel is, ook wanneer het actieve profiel zojuist verwijderd is.
            current_player = list(players.keys())[0]
        return True

    print("Dat account bestaat niet.")
    return False


def show_all_players():
    """
    Show all available player profiles.
    :return:
    """
    print("\nOverzicht spelers")
    print("-" * 17)
    for name, profile in players.items():
        print(f"{name}: saldo € {profile['saldo']:.2f}")


