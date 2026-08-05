# Week 5 oplossing: Casino de Gouden Driehoek met meerdere spelersprofielen

from games.blackjack import play_blackjack
from games.fruitmachine import play_fruitmachine
from games.roulette import play_roulette
from profiles import (
    create_account,
    get_current_balance,
    initialize_player,
    register_played_game,
    remove_account,
    show_account,
    show_all_players,
    switch_account,
    update_current_balance,
)

TICKET_PRICE = 10.00
CONSUMPTION_PRICE = 4.50
GAMBLING_TAX = 2.00
DIVIDER_LENGTH = 35
TOTAL_COST = TICKET_PRICE + CONSUMPTION_PRICE + GAMBLING_TAX


def show_main_menu():
    """
    Show the casino's main menu.
    :return:
    """
    print("\nCasino de Gouden Driehoek - hoofdmenu")
    print("-" * DIVIDER_LENGTH)
    print("1. Spellen")
    print("2. Saldo")
    print("3. Account")
    print("0. Stop")
    print()


def show_games_menu():
    """
    Show the game menu.
    :return:
    """
    print("\nCasino de Gouden Driehoek - spellen")
    print("-" * DIVIDER_LENGTH)
    print("1. Fruitmachine")
    print("2. Roulette")
    print("3. Blackjack")
    print("0. Terug")
    print()


def show_account_menu():
    """
    Show the account menu.
    :return:
    """
    print("\nCasino de Gouden Driehoek - accountmenu")
    print("-" * DIVIDER_LENGTH)
    print("1. Toon alle accounts")
    print("2. Nieuw account")
    print("3. Wissel account")
    print("4. Verwijder account")
    print("0. Terug")
    print()


def show_balance(balance):
    """
    Show the player's current balance.
    :param balance:
    :return:
    """
    print("\nCasino de Gouden Driehoek - saldo")
    print("-" * DIVIDER_LENGTH)
    print(f"Huidig saldo: € {balance:.2f}")


def main():
    initialize_player(TOTAL_COST)

    while True:
        show_main_menu()
        choice = int(input("Kies een optie: "))

        match choice:
            case 0:  # stop
                break
            case 1:  # spellen
                show_games_menu()
                game_choice = int(input("Kies een spel: "))

                match game_choice:
                    case 0:  # terug
                        pass
                    case 1:  # fruitmachine
                        balance = play_fruitmachine(get_current_balance())
                        update_current_balance(balance)
                        register_played_game("fruitmachine")
                    case 2:  # roulette
                        balance = play_roulette(get_current_balance())
                        update_current_balance(balance)
                        register_played_game("roulette")
                    case 3:  # blackjack
                        balance = play_blackjack(get_current_balance())
                        update_current_balance(balance)
                        register_played_game("blackjack")
                    case _:  # ongeldig
                        print("Ongeldige spelkeuze, probeer opnieuw.")
            case 2:  # saldo
                show_balance(get_current_balance())
            case 3:  # account
                show_account()
                show_account_menu()
                account_choice = int(input("Kies een accountoptie: "))

                match account_choice:
                    case 0:  # terug
                        pass
                    case 1:  # tonen
                        show_all_players()
                    case 2:  # nieuw
                        create_account(TOTAL_COST)
                    case 3:  # wisselen
                        switch_account()
                    case 4:  # verwijderen
                        remove_account()
                    case _:  # ongeldig
                        print("Ongeldige accountkeuze.")
            case _:  # ongeldig
                print("Ongeldige keuze, probeer opnieuw.")

    print(f"Eindsaldo: € {get_current_balance():.2f}")



main()
