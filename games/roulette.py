# Roulette voor Casino de Gouden Driehoek

from games.helpers import ask_for_bet


def show_roulette_options():
    """
    Show the options for the roulette table.
    :return:
    """
    print("Kies één van de volgende opties:")
    print()
    print("1. Rood")
    print("2. Zwart")
    print("3. Even")
    print("4. Oneven")
    print("0. Stop")
    print()


def determine_win(choice, color, odd_even):
    """
    Determine whether the player has won the roulette round.
    :param choice:
    :param color:
    :param odd_even:
    :return:
    """
    win = False
    if choice == 1 and color == "rood":
        win = True
    elif choice == 2 and color == "zwart":
        win = True
    elif choice == 3 and odd_even == "even":
        win = True
    elif choice == 4 and odd_even == "oneven":
        win = True
    return win


def play_roulette(balance):
    """
    Play multiple rounds of roulette.
    :param balance:
    :return:
    """
    round_number = 1

    while True:
        show_roulette_options()
        choice = int(input("Kies je gok (0 om te stoppen): "))

        if choice == 0:
            break

        if choice < 1 or choice > 4:
            print("Ongeldige keuze, probeer opnieuw.\n")
            continue

        bet = ask_for_bet(balance)
        balance -= bet

        spin = (round_number * 7) % 37
        if spin == 0:
            color = "groen"
            odd_even = "geen"
        elif spin <= 18:
            if spin % 2 == 0:
                color = "zwart"
                odd_even = "even"
            else:
                color = "rood"
                odd_even = "oneven"
        else:
            if spin % 2 == 0:
                color = "rood"
                odd_even = "even"
            else:
                color = "zwart"
                odd_even = "oneven"
        win = determine_win(choice, color, odd_even)

        print(f"De bal valt op {color} ({spin}).")
        if win:
            balance += bet * 2
            print(f"Je wint € {bet:.2f}")
        else:
            print(f"Je verliest € {bet:.2f}")

        print(f"Nieuw saldo: € {balance:.2f}\n")
        round_number += 1

    return balance
