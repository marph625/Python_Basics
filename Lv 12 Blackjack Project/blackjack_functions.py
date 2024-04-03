from blackjack_project import *

def check_blackjack(player_cards, player_score, player_won, computer_cards, computer_score, computer_won):

    # check if computer or player has blackjack
    # this needs improvement

    for card in computer_cards:
        computer_score += card
    for card in player_cards:
        player_score += card

    if computer_score == 21:
        print("Computer has Blackjack")
        computer_won = True
    elif player_score == 21:
        print("Player has Blackjack")
        player_won = True
    elif player_score > 21:
        if ace in player_cards:
            ace = 1
            player_score -= 10
            print(player_cards)



def check_win(player_won, player_cards, computer_won, computer_cards):
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
    check_blackjack(player_cards, player_score, player_won, computer_cards, computer_score, computer_won)
    check_win(player_won, player_cards, computer_won, computer_cards)


def computer_draw_card(computer_cards):
    computer_cards.append(random.choice(cards))
    print(computer_cards)
    check_blackjack(player_cards, player_score, player_won, computer_cards, computer_score, computer_won)
    check_win(player_won, player_cards, computer_won, computer_cards)