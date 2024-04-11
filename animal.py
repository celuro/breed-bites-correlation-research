# Research Question: What breed is more likely to have bite the body?
# Variables: Breed (independent), BittenIDDesc (dependent)
# Hypothesis: There is a relationship between pit bulls having a higher chance of biting compared to labrador retrievers due to a higher rate of animal abuse.
# Ensure breed is (PIT BULL, AMER. BULL DOG) and (LABRADOR RETRIEVER, GOLDEN RETRIEVER)
# Testable Prediction: If my hypothesis is correct, I expect animal abuse to have a higher correlation of bites.

# Importing the pandas library to use its functions
import pandas as pd
df = pd.read_csv('Health_AnimalBites.csv')

#Handling Missing Values
#Delete rows that dont aren't dogs, dont have a breed and don't have a bitten id desc
not_dog = df[df['SpeciesIDDesc'] != "DOG"].index
not_breed = df[df['BreedIDDesc'].isna()].index
not_bitten = df[df['WhereBittenIDDesc'].isna()].index

rows_to_drop = not_dog.union(not_breed).union(not_bitten)
df.drop(rows_to_drop, inplace=True)

# Handle duplicate data
df.drop_duplicates(inplace=True)

#Label Encoding
df_encoded = pd.get_dummies(df, columns=['SpeciesIDDesc', 'BreedIDDesc', 'WhereBittenIDDesc'])
df_encoded.to_csv('new_data.csv', index=False)


