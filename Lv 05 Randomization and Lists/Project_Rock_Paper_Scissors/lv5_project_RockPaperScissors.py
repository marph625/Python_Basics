import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Schreiben Sie Ihren Programmcode unter dieser Zeile 👇

player_win_counter = 0
computer_win_counter = 0

print("!!!Let's play a game of RPS!!!\nBest of Three.")

while player_win_counter < 2 and computer_win_counter < 2:

    moves_list = [rock, paper, scissors]
    player_input = int(input("Enter 1 for rock, 2 for paper or 3 for scissors\n"))
    rand_num = random.randint(0, 2)
    computer = moves_list[rand_num]
    player = moves_list[player_input-1]

    print("Computer:\n", computer)
    print("Player:\n", player)

    if computer == rock and player == rock or computer == paper and player == paper or computer == scissors and player == scissors:
        print("It's a tie!")
    elif computer == rock and player == scissors or computer == paper and player == rock or computer == scissors and player == paper:
        print("Computer wins!")
        computer_win_counter += 1
    else:
        print("Player wins!")
        player_win_counter += 1
    
    print(f"Current score:\nPlayer:{player_win_counter}\nComputer:{computer_win_counter}")