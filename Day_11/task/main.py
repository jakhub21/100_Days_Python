from art import logo
import random
cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]


def add_cards(card1, card2):
    return int(card1) + int(card2)


def check_win(score_play, score_comp):
    if score_play > 21:
        print("You lose")
    elif score_play < 21 and score_play > score_comp:
        print("You win")
    elif score_play < 21 and score_play == score_comp:
        print("Draw")
    elif score_play < 21 and score_comp > 21:
        print("You win")
    else:
        print("You lose")


def check_as(card1, card2):
    if card1 == 11:
        card1 = input("Do you want to have 1 or 11\n")
    if card2 == 11:
        card2 = input("Do you want to have 1 or 11\n")
    score_player = add_cards(card1, card2)
    print(f"Your cards: [{card1} : {card2}], current score: {score_player}")
    return card1, card2, score_player


flag = True
while flag:
    play = input("Do you want to play blackjack? yes or no\n")
    print("\n" * 20)
    comp_deck = []
    player_deck = []
    if play == "yes":
        print(logo)
        card1 = random.choice(cards)
        cards.remove(card1)
        player_deck.append(card1)
        card2 = random.choice(cards)
        cards.remove(card2)
        player_deck.append(card2)
        score_player = add_cards(card1, card2)


        com_card1 = random.choice(cards)
        cards.remove(com_card1)
        comp_deck.append(com_card1)
        com_card2 = random.choice(cards)
        cards.remove(com_card2)
        comp_deck.append(com_card2)
        score_com = add_cards(com_card1, com_card2)

        if com_card1 == 11 and com_card2 == 11:
            com_card2 = 1
            comp_deck[1] = com_card2
            score_com = add_cards(com_card1, com_card2)

        if score_com < 17:
            com_card3 = random.choice(cards)
            cards.remove(com_card3)
            comp_deck.append(com_card3)
            score_com = add_cards(score_com, com_card3)
            if score_com > 21 and com_card3 == 11:
                score_com -= 10

        print(f"Your cards: [{card1} : {card2}], current score: {score_player}")
        print(f"Computer first card is: {com_card1}")
        card1, card2, score_player = check_as(card1, card2)
        choice = input("Type 'y' to get another card, type 'n' to pass:\n")
        if choice == "y":
            card3 = random.choice(cards)
            cards.remove(card3)
            if card3 == 11:
                card3 = input("Do you want to have 1 or 11\n")
            score_player = add_cards(score_player, card3)
            print(f"Your cards: [{card1} : {card2} : {card3}], your score: {score_player}")
            print("Computer cards: ")
            print(*comp_deck, sep=":")
            print(f"computer score: {score_com}")
            check_win(score_player, score_com)
        else:
            print(f"Your cards: [{card1} : {card2}], your score: {score_player}")
            print("Computer cards: ")
            print(*comp_deck, sep=":")
            print(f"computer score: {score_com}")
            check_win(score_player, score_com)
    else:
        flag = False

