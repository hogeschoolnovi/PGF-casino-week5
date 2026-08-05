# Algemene hulpfuncties voor Casino de Gouden Driehoek


def ask_for_bet(balance):
    """
    Ask the player for a valid bet.
    :param balance:
    :return:
    """
    while True:
        bet = float(input("Je inzet: € "))
        if bet <= 0:
            print("De inzet moet groter zijn dan 0.")
            continue
        if bet > balance:
            print("Je hebt niet genoeg saldo voor deze inzet.")
            continue
        return bet
