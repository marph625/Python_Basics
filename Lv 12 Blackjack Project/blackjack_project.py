import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
computer_cards = []

player = input("What's your name?\n")
print(f"Hello {player}! Let's play Blackjack!")

computer_won = False
player_won = False

print(player_cards, computer_cards)

# player and computer will be dealt two random values from cards
# this needs improvement

player_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))
player_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))

print(player_cards, computer_cards)

def check_blackjack(player_cards, computer_cards):

    # check if computer or player has blackjack
    # this needs improvement 

    if 11 in computer_cards and 10 in computer_cards:
        print("Computer has Blackjack")
        computer_won = True
    elif 11 in player_cards and 10 in player_cards:
        print("Player has Blackjack")
        player_won = True

def check_win(player_won, computer_won):
    if computer_won == True:
        print(f"{computer_cards} - Computer wins")
    else:
        print(f"{player_cards} | {computer_cards} - Player wins")

check_blackjack(player_cards, computer_cards)

