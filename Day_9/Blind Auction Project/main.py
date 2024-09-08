# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
import os

print(logo)

dictionary = {}
flag = True
while flag:
    name = input("Write your name:\n")
    price = input("How much you want to bit?\n")

    dictionary[name] = price

    bit = input("Another person to bit? yes or no\n")

    if bit == "yes":
        flag = True
        print("\n"*20)
    else:
        flag = False
        max = 0
        for i in dictionary:
            max_tmp = int(dictionary[i])
            if max_tmp < max:
                max = max
            else:
                max = max_tmp
                person = i
        print("\n"*20)
        print(f"The winner is {person}\n{person} bit {max}")




