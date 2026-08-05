# Fruitmachine voor Casino de Gouden Driehoek

from games.helpers import ask_for_bet


def determine_rolls(round_number):
    """
    Determine the three fruit machine rolls without lists or random.
    :param round_number:
    :return:
    """
    if round_number % 5 == 1:
        return "kers", "citroen", "ster"
    elif round_number % 5 == 2:
        return "kers", "kers", "kers"
    elif round_number % 5 == 3:
        return "ster", "ster", "citroen"
    elif round_number % 5 == 4:
        return "citroen", "kers", "ster"
    return "ster", "ster", "ster"


def determine_payout(rol1, rol2, rol3, bet):
    """
    Determine the payout for the three fruit machine rolls.
    :param rol1:
    :param rol2:
    :param rol3:
    :param bet:
    :return:
    """
    if rol1 == rol2 == rol3:
        return bet * 3
    if rol1 == rol2 or rol1 == rol3 or rol2 == rol3:
        return bet
    return 0.0


def play_fruitmachine(balance):
    """
    Play one or more rounds of the fruit machine.
    :param balance:
    :return:
    """
    round_number = 1
    while True:
        print(f"\nCasino de Gouden Driehoek - fruitmachine")
        print("-" * 35)
        print(f"Huidig saldo: € {balance:.2f}")

        action = input("Druk op enter om te spelen of typ stop om terug te gaan: ").strip().lower()
        if action == "stop":
            return balance

        bet = ask_for_bet(balance)
        balance -= bet
        rol1, rol2, rol3 = determine_rolls(round_number)
        print(f"Rollen: {rol1} | {rol2} | {rol3}")

        payout = determine_payout(rol1, rol2, rol3, bet)

        if payout > 0:
            balance += payout
            if rol1 == rol2 == rol3:
                print(f"Drie dezelfde! Je wint € {payout:.2f}")
            else:
                print(f"Twee dezelfde! Je wint € {payout:.2f}")
        else:
            print(f"Geen match. Je verliest € {bet:.2f}")

        print(f"Nieuw saldo: € {balance:.2f}")
        round_number += 1
