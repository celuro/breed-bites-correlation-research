# Conducting exploratory analysis
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('new_data.csv')

# Inspect the data
print(df.head())
print(df.tail())
print(df.info())

# Summary Statistics
print(df.describe())

# I would like to visualize the data in a bar graph using counts

import seaborn as sns
import matplotlib.pyplot as plt

# Filters the data frame to only show records that have a bitten ID desc, need unknown cases as well for more info
bitten_cases = df[df['WhereBittenIDDesc_BODY'] == True]

unknown_cases = df[df['WhereBittenIDDesc_UNKNOWN'] == True]

# Count occurrences of each breed in bitten cases
bitten_counts = [bitten_cases['BreedIDDesc_PIT BULL'].sum(), bitten_cases['BreedIDDesc_AMER. BULL DOG'].sum(), bitten_cases['BreedIDDesc_LABRADOR RETRIV'].sum(), bitten_cases['BreedIDDesc_GOLD RETRIEVER'].sum()]
unknown_counts = [unknown_cases['BreedIDDesc_PIT BULL'].sum(), unknown_cases['BreedIDDesc_AMER. BULL DOG'].sum(), unknown_cases['BreedIDDesc_LABRADOR RETRIV'].sum(), unknown_cases['BreedIDDesc_GOLD RETRIEVER'].sum()]

# Listing the bite cases by breed
print("Bitten Cases By Breed")
print("PIT BULL: ", bitten_counts[0]) #821
print("AMERICAN BULL DOG: ", bitten_counts[1]) #12
print("LABRADOR RETRIEVER: ", bitten_counts[2]) #143
print("GOLDEN RETRIEVER: ", bitten_counts[3]) #38

print("Unknown Cases By Breed")
print("PIT BULL: ", unknown_counts[0]) #94
print("AMERICAN BULL DOG: ", unknown_counts[1]) #3
print("LABRADOR RETRIEVER: ", unknown_counts[2]) #37
print("GOLDEN RETRIEVER: ", unknown_counts[3]) #7

#Making the bar graph

breeds = ['Pit Bull', 'American Bull Dog', 'Labrador Retriever', 'Golden Retriever']
plt.figure(figsize=(10, 6))
sns.barplot(x=breeds, y=bitten_counts, palette='Set2', hue=unknown_counts)
plt.title('Bite Cases by Breed')
plt.xlabel('Breed')
plt.ylabel('Bite Count')
plt.xticks(rotation=0)
plt.show()
