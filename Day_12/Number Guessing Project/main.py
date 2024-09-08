from art import logo
import random


def check_num(num, num_rand):
    num = int(num)
    num_rand = int(num_rand)
    if num > num_rand:
        print("Too high")
    elif num < num_rand:
        print("Too low")


def check_win(num, num_rand):
    num = int(num)
    num_rand = int(num_rand)
    if num == num_rand:
        print("You Win")
        flag = False
    elif num != num_rand:
        flag = True
    return flag


print(logo)
rand_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty level 'easy' or 'hard'\n")

if level == "easy":
    attempts = 10
    flag = True
    while attempts != 0 and flag:
        print(f"You have {attempts} attempts")
        guess = input("Make a guess: ")
        check_num(guess, rand_number)
        flag = check_win(guess, rand_number)
        attempts -= 1
        if attempts == 0 and flag == False:
            print("Congratulation you did it on the last chance")
            flag = False
        elif attempts == 0:
            print("You Lose")

elif level == "hard":
    attempts = 5
    flag = True
    while attempts != 0 and flag:
        print(f"You have {attempts} attempts")
        guess = input("Make a guess: ")
        check_num(guess, rand_number)
        flag = check_win(guess, rand_number)
        attempts -= 1

        if attempts == 0 and flag == False:
            print("Congratulation you did it on the last chance")
            flag = False
        elif attempts == 0:
            print("You Lose")

else:
    print("You provide bad name of the level")
