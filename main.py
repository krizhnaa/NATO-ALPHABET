import pandas as pd

#TODO 1. Create a dictionary in this format:

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = { row.letter:row.code for (index, row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word : ").upper()

List = [ nato_dict[letter] for letter in word]

print(List)