#Blackjack_game
from profiles import players, register_played_game

import random


# Step 1: Constants
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


# Step 2: Create the deck
def create_deck():
    deck = [(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


# Step 3: Draw a card
def draw_card(deck, hand):
    card = deck.pop()
    hand.append(card)
    return card


# Step 4: Show a hand
def show_hand(label, hand, hide_card=False):
    visible_cards = hand[:]

    if hide_card:
        visible_cards[1] = ("?")

    print(f"{label}: {visible_cards}")


# Step 5: Calculate the value of one card
def calculate_card_value(card):
    rank = card[1]

    if rank in ["J", "Q", "K"]:
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)


# Step 6: Calculate the value of a hand
def calculate_hand_value(hand):
    total = sum(calculate_card_value(card) for card in hand)

    number_of_aces = sum(1 for card in hand if card[1] == "A")

    while total > 21 and number_of_aces > 0:
        total -= 10
        number_of_aces -= 1

    return total


# Step 7: Work out who won
def result(balance, stake, player_total, dealer_total):

    if dealer_total > 21:
        print("Dealer Bust!")
        print("You win!")
        balance = balance + stake * 2

    elif player_total > dealer_total:
        print("Your total is:", player_total)
        print("Dealer total is:", dealer_total)
        print("You win!")
        balance = balance + stake * 2

    elif player_total == dealer_total:
        print("Your total is:", player_total)
        print("Dealer total is:", dealer_total)
        print("Draw!")
        balance = balance + stake

    else:
        print("Your total is:", player_total)
        print("Dealer total is:", dealer_total)
        print("You lose!")

    print("Your balance is:", balance)

    return balance


# Step 8: Blackjack game
def play_blackjack(balance, current_player):
    balance = players[current_player]["balance"]

    print("Welcome to the Blackjack Game!")
    print("Your balance is", balance)

    while True:

        stake = float(input(
            "Please place your bet (or press 0 to return to Games Menu): "
        ))

        if stake == 0:
            return balance

        if stake < 0 or stake > balance:
            print("Invalid bet.")
            continue

        print("You have placed your bet!")

        balance = balance - stake

        print("Your remaining balance is:", balance)

        # Create a new deck
        deck = create_deck()

        # Empty hands
        player_hand = []
        dealer_hand = []

        # Deal two cards to each player
        draw_card(deck, player_hand)
        draw_card(deck, player_hand)

        draw_card(deck, dealer_hand)
        draw_card(deck, dealer_hand)

        # Show starting hands
        show_hand("Your hand", player_hand)
        show_hand("Dealer hand", dealer_hand, True)

        player_total = calculate_hand_value(player_hand)

        print("Your total is:", player_total)

        # Player turn
        while player_total < 21:

            choice = input("Would you like to hit or stand?: ").lower()

            if choice == "stand":
                print("You chose to stand!")
                break

            elif choice == "hit":

                card = draw_card(deck, player_hand)

                print(f"You draw: {card}")

                show_hand("Your hand", player_hand)

                player_total = calculate_hand_value(player_hand)

                print("Your total is:", player_total)

                # Player Bust
                if player_total > 21:
                    print("Bust!")
                    print("You lose.")
                    print("Your balance is:", balance)

                    players[current_player]["balance"] = balance
                    register_played_game("blackjack")

                    return balance

        # Dealer turn
        show_hand("Dealer hand", dealer_hand)

        dealer_total = calculate_hand_value(dealer_hand)

        print("Dealer total:", dealer_total)

        while dealer_total < 17:

            card = draw_card(deck, dealer_hand)

            print(f"Dealer draws: {card}")

            show_hand("Dealer hand", dealer_hand)

            dealer_total = calculate_hand_value(dealer_hand)

            print("Dealer total:", dealer_total)

        print("Dealer finished!")

        # Calculate result
        balance = result(balance, stake, player_total, dealer_total)

        print("After result:", balance)

        players[current_player]["balance"] = balance
        register_played_game("blackjack")

        return balance


# Step 9: Compatibility with the current main.py
def blackjack(balance, current_player):
    return play_blackjack(balance, current_player)


