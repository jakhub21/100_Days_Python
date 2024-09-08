
import pandas as pd

#TODO 1. Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")
dict_alph = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
flag = True
while flag:
    word = input("Write the word: ").upper()
    try:
        output_list = [dict_alph[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in alphabet please")
    else:
        print(output_list)
        flag = False


