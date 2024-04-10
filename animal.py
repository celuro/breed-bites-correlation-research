# Research Question: What breed is more likely to have rabies?
# Variables: Breed (independent), Rabies (dependent)
# Hypothesis: There is a relationship between pit bulls having a higher chance of rabies compared to labrador retrievers due to a higher rate of animal abuse.
# Ensure breed is (PIT BULL, AMER. BULL DOG, GOLD RETRIEVER, LABRADOR RETRIV)
# Testable Prediction: If my hypothesis is correct, I expect animal abuse to have a higher correlation of rabies.
# Experient Model: Factorized design (2x2)

# Importing the pandas library to use its functions
import pandas as pd
df = pd.read_csv('Health_AnimalBites.csv')

# Handling Missing Values
# Delete rows that aren't dogs and dont have a breed
not_dog = df[df['SpeciesIDDesc'] != "DOG"].index
not_breed = df[df['BreedIDDesc'].isna()].index

# Deleting the rows based on variables
rows_to_drop = not_dog.union(not_breed)
df.drop(rows_to_drop, inplace=True)

# I want the data to be unique values
df.drop_duplicates(inplace=True)

# One-Hot Label Encoding due to categories not needing an order
df_encoded = pd.get_dummies(df, columns=['SpeciesIDDesc', 'BreedIDDesc', 'ResultsIDDesc'])

# Saving the cleaned and encoded data frame to a csv for future use
df_encoded.to_csv('fixed_data.csv', index=False)
