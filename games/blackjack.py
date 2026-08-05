# Blackjack voor Casino de Gouden Driehoek
import random

from games.helpers import ask_for_bet


SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def create_deck():
    """
    Create a deck as a shuffled list of cards.
    :return:
    """
    deck = [f"{suit}{rank}" for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck


def determine_card_value(card):
    """
    Determine the value of one card.
    :param card:
    :return:
    """
    rank = card[1:] # Gebruik hier `1:` in plaats van `1`, omdat 10 anders 1 wordt.
    if rank in ["J", "Q", "K"]:
        return 10
    if rank == "A":
        return 11
    return int(rank)


def calculate_hand_value(hand):
    """
    Calculate the value of a hand and adjust aces when necessary.
    :param hand:
    :return:
    """
    total = sum(determine_card_value(card) for card in hand) # Tel alle kaartwaardes bij elkaar op met behulp van de helper functie
    number_of_aces = sum(1 for card in hand if card[1] == "A") # Tel alle azen in de hand. Hiervoor gebruik je 'card[1:]', omdat een kaart altijd 2 tekens heeft (b.v. "♠A"), waarvan het eerste teken de kaartwaarde geeft.
    while total > 21 and number_of_aces > 0: # Als de hand waarde van de speler boven de 21 komt EN de speler heeft 1 of meer aasen in de hand, dan ga je per aas de waarde aanpassen van "11" naar "1". Net zo lang tot de hand waarde weer onder de 21 komt. Zijn er geen aasen van 11 over, dan is het "bust" voor de speler.
        total -= 10
        number_of_aces -= 1
    return total


def show_hand(label, hand, dealer_hide_card=False):
    """
    Show a player's or dealer's hand.
    :param label:
    :param hand:
    :param dealer_hide_card:
    :return:
    """
    if dealer_hide_card and len(hand) > 1:
        visible_cards = [hand[0], "??"] # De situatie waar de speler aan de beurt is en de dealer één kaart laat zien en de tweede kaart geheim houdt. We vervangen hier de hand van de dealer met eeen nieuwe lijst waarin de eerste kaart van de dealer zit en de tweede kaart "??" is.
    else:
        visible_cards = hand # Dit is de situatie waar alle kaarten getoond worden (speler en dealer).

    print(f"{label}: {' | '.join(visible_cards)}")


def draw_card(deck, hand):
    """
    Move one card from the deck to a hand.
    :param deck:
    :param hand:
    :return:
    """
    card = deck.pop(0)
    hand.append(card)
    return card


def play_blackjack(balance):
    """
    Play one round of blackjack and return the updated balance.
    :param balance:
    :return:
    """

    print("\nCasino de Gouden Driehoek - blackjack")
    print("-" * 38)
    print(f"Huidig saldo: € {balance:.2f}")

    bet = ask_for_bet(balance)
    balance -= bet

    # Initialiseer als eerst de benodigde lijsten.
    deck = create_deck()
    player_hand = []
    dealer_hand = []


    # De eerste kaarten worden verdeeld over beide handen.
    draw_card(deck, player_hand)
    draw_card(deck, dealer_hand)
    draw_card(deck, player_hand)
    draw_card(deck, dealer_hand)

    print()
    show_hand("Jouw hand", player_hand)
    show_hand("Dealer hand", dealer_hand, dealer_hide_card=True)
    print(f"Jouw totaal: {calculate_hand_value(player_hand)}")


    # De speler kiest hit of stand.
    while calculate_hand_value(player_hand) < 21:
        print()
        action = input("Kies hit of stand: ").strip().lower()
        if action == "stand":
            break
        if action != "hit":
            print("Typ hit of stand.")
            continue

        card = draw_card(deck, player_hand)
        print(f"Je trekt: {card}")
        show_hand("Jouw hand", player_hand)
        print(f"Jouw totaal: {calculate_hand_value(player_hand)}")


        if calculate_hand_value(player_hand) > 21:
            print("Je bent bust gegaan.")
            print(f"Nieuw saldo: € {balance:.2f}")
            return balance

    # De dealer trekt kaarten totdat de waarde minimaal 17 is.
    print()
    show_hand("Dealer hand", dealer_hand)
    while calculate_hand_value(dealer_hand) < 17:
        card = draw_card(deck, dealer_hand)
        print(f"Dealer trekt: {card}")
        show_hand("Dealer hand", dealer_hand)

    # Laat de totale waardes zien van zowel de speler als de dealer
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)
    print(f"Jouw totaal: {player_total}")
    print(f"Dealer totaal: {dealer_total}")

    # De uitbetaling wordt bepaald door de totale waarden van beide handen.
    if dealer_total > 21:
        print("Dealer bust gegaan. Je wint!")
        balance += bet * 2
    elif player_total > dealer_total:
        print("Je wint van de dealer!")
        balance += bet * 1.5
    elif player_total == dealer_total:
        print("Gelijkspel. Je krijgt je inzet terug.")
        balance += bet
    else:
        print("Dealer wint deze ronde.")

    print(f"Nieuw saldo: € {balance:.2f}")
    return balance

