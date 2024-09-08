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

input("Welcome to Rock, Paper, Scissors!\nPress Enter to start the game.")
player = input("Rock, Paper, Scissors, Shoot!")
ia = random.randint(0, 2)
if ia == 0:
    print(f"Computer chose:\n{rock}")
elif ia == 1:
    print(f"Computer chose:\n{paper}")
else:
    print(f"Computer chose:\n{scissors}")

if player == "Rock":
    if ia == 0:
        print("It's a draw!")
    elif ia == 1:
        print("You lose!")
    else:
        print("You win!")
elif player == "Paper":
    if ia == 0:
        print("You win!")
    elif ia == 1:
        print("It's a draw!")
    else:
        print("You lose!")
elif player == "Scissors":
    if ia == 0:
        print("You lose!")
    elif ia == 1:
        print("You win!")
    else:
        print("It's a draw!")
else:
    print("Invalid input. You lose!")