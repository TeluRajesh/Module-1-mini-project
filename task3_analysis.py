import pandas as pd
import numpy as np
import os

# -----------------------------
# 1. Load and Explore
# -----------------------------
file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)

print(f"Loaded data: {df.shape}")

print("\nFirst 5 rows:")
print(df.head())

# Average values
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score: {avg_score:,.0f}")
print(f"Average comments: {avg_comments:,.0f}")

# -----------------------------
# 2. NumPy Analysis
# -----------------------------
scores = df["score"].values

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)
max_score = np.max(scores)
min_score = np.min(scores)

print("\n--- NumPy Stats ---")
print(f"Mean score: {mean_score:,.0f}")
print(f"Median score: {median_score:,.0f}")
print(f"Std deviation: {std_score:,.0f}")
print(f"Max score: {max_score:,.0f}")
print(f"Min score: {min_score}")

# Category with most stories
top_category = df["category"].value_counts().idxmax()
top_count = df["category"].value_counts().max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")

# Most commented story
top_comment_row = df.loc[df["num_comments"].idxmax()]
print(f"\nMost commented story: \"{top_comment_row['title']}\" — {top_comment_row['num_comments']:,} comments")

# -----------------------------
# 3. Add New Columns
# -----------------------------

# Engagement column
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular column
avg_score_overall = df["score"].mean()
df["is_popular"] = df["score"] > avg_score_overall

# -----------------------------
# 4. Save Result
# -----------------------------
output_path = "data/trends_analysed.csv"

os.makedirs("data", exist_ok=True)

df.to_csv(output_path, index=False)

print(f"\nSaved to {output_path}")