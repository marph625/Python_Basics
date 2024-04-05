import random
from blackjack_functions import *

ace = 11

cards = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
computer_cards = []

player_score = 0
computer_score = 0

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

def check_blackjack(player_cards, player_score, computer_cards, computer_score):

    # check if computer or player has blackjack
    # this needs improvement

    global ace, computer_won, player_won

    for card in computer_cards:
        computer_score += card
    for card in player_cards:
        player_score += card

    if computer_score == 21:
        print(computer_cards,"Computer has Blackjack")
        computer_won = True
    elif player_score == 21:
        print(player_cards,"Player has Blackjack")
        player_won = True
    elif player_score > 21:
        if ace in player_cards:
            check_ace(player_cards)
        else:
            computer_won = True

def check_ace(player_cards):
    global ace
    ace = 1
    player_score = 0

    for card in player_cards:
        player_score += card
    
    check_win(player_cards, computer_cards)         

def check_win(player_cards, computer_cards):
    global computer_won, player_won
    if computer_won == True:
        print(f"{player_cards} | {computer_cards} - Computer wins")
    elif player_won == True:
        print(f"{player_cards} | {computer_cards} - Player wins")
    else:
        draw_card = input("Enter 'd' to draw another card.\nEnter anything but 'd' to pass.")
        if draw_card == 'd':
            player_draw_card(player_cards)
        else:
            computer_draw_card(computer_cards)



def player_draw_card(player_cards):
    player_cards.append(random.choice(cards))
    print(player_cards)
    check_blackjack(player_cards, player_score, computer_cards, computer_score)
    check_win(player_cards, computer_cards)


def computer_draw_card(computer_cards):
    computer_cards.append(random.choice(cards))
    print(computer_cards)
    check_blackjack(player_cards, player_score, computer_cards, computer_score)
    check_win(player_cards, computer_cards)

# main loop
while computer_won == False:
    check_blackjack(player_cards, player_score, computer_cards, computer_score)
    check_win(player_cards, computer_cards)

