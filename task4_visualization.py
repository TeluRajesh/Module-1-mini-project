import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# 1. Setup
# -----------------------------
file_path = "data/trends_analysed.csv"

df = pd.read_csv(file_path)

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# 2. Chart 1: Top 10 Stories by Score
# -----------------------------
top10 = df.nlargest(10, "score")

# Shorten titles (max 50 chars)
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure(figsize=(10, 6))
plt.barh(top10["short_title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()

plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# -----------------------------
# 3. Chart 2: Stories per Category
# -----------------------------
category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()

# -----------------------------
# 4. Chart 3: Score vs Comments
# -----------------------------
popular = df[df["is_popular"] == True]
non_popular = df[df["is_popular"] == False]

plt.figure(figsize=(8, 6))
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(non_popular["score"], non_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# -----------------------------
# 5. Bonus: Dashboard
# -----------------------------
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Chart 1 (horizontal bar)
axs[0].barh(top10["short_title"], top10["score"])
axs[0].set_title("Top 10 Stories")
axs[0].invert_yaxis()

# Chart 2 (category count)
axs[1].bar(category_counts.index, category_counts.values)
axs[1].set_title("Stories per Category")

# Chart 3 (scatter)
axs[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axs[2].scatter(non_popular["score"], non_popular["num_comments"], label="Not Popular")
axs[2].set_title("Score vs Comments")
axs[2].legend()

fig.suptitle("TrendPulse Dashboard")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in 'outputs/' folder ✅")