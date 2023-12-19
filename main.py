import pandas as pd
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# nato_df = pandas.DataFrame()

#TODO 1. Create a dictionary in this format:
# nato_dict = { for(index, row) }

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = { row.letter:row.code for (index, row) in nato_df.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

