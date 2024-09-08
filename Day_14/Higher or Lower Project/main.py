from art import logo, vs
from game_data import data
import random


def check_win(rand1, rand2, score):
    if rand1['follower_count'] < rand2['follower_count']:
        flag = False
        random_1 = rand1
        print(logo)
        print(f"Sorry, that is wrong. Your score: {score}")
        return flag, score, random_1
    else:
        score += 1
        flag = True
        random_1 = rand1
        print(logo)
        print(f"You are right! Your score: {score}")
        return flag, score, random_1


print(logo)
flag = True
score = 0
random_data1 = random.choice(data)
while flag:
    random_data2 = random.choice(data)
    print(f"Compare A: {random_data1['name']}, {random_data1['description']}, from {random_data1['country']}")
    print(vs)
    print(f"Compare B: {random_data2['name']}, {random_data2['description']}, from {random_data2['country']}")
    flag = False
    guess = input("Who has more follower? A or B")
    print("\n" * 20)
    if guess == "A" or guess == "a":
        flag, score, random_data1 = check_win(random_data1, random_data2, score)
    else:
        flag, score, random_data1 = check_win(random_data2, random_data1, score)
