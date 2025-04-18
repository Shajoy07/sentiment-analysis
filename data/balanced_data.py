import pandas as pd

# Step 1: Load the large dataset
df = pd.read_csv('Industrial_and_Scientific.csv')

# Step 2: Define rating groups for future sentiment mapping
positive_ratings = [4, 5]
neutral_ratings = [3]
negative_ratings = [1, 2]

# Step 3: Create subsets for each group
n_per_class = 5000

positive_df = df[df['rating'].isin(positive_ratings)].sample(n=n_per_class, random_state=15)
neutral_df  = df[df['rating'].isin(neutral_ratings)].sample(n=n_per_class, random_state=15)
negative_df = df[df['rating'].isin(negative_ratings)].sample(n=n_per_class, random_state=15)

# Step 4: Combine and shuffle
balanced_subset = pd.concat([positive_df, neutral_df, negative_df]).sample(frac=1, random_state=15).reset_index(drop=True)

# Step 5: Save to CSV
balanced_subset.to_csv('Industrial_and_Scientific_5000.csv', index=False)

print(" Balanced data saved as 'balanced_sentiment_subset.csv'")
