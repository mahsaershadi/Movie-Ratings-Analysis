import numpy as np
import pandas as pd


# ==========================================
# 1. LOAD DATASETS
# ==========================================

movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")


# ==========================================
# 2. EXPLORE THE DATASETS
# ==========================================

print("===== MOVIES DATASET =====")
print(movies.head())

print("\n===== RATINGS DATASET =====")
print(ratings.head())


print("\n===== DATASET SHAPES =====")
print("Movies:", movies.shape)
print("Ratings:", ratings.shape)


print("\n===== MOVIE COLUMNS =====")
print(movies.columns)


print("\n===== RATING COLUMNS =====")
print(ratings.columns)


# ==========================================
# 3. CHECK DATASET INFORMATION
# ==========================================

print("\n===== MOVIES INFO =====")
movies.info()

print("\n===== RATINGS INFO =====")
ratings.info()


# ==========================================
# 4. CHECK MISSING VALUES
# ==========================================

print("\n===== MISSING VALUES =====")

print("Movies:")
print(movies.isnull().sum())

print("\nRatings:")
print(ratings.isnull().sum())


# ==========================================
# 5. BASIC NUMPY ANALYSIS
# ==========================================

rating_array = ratings["rating"].to_numpy()

mean_rating = np.mean(rating_array)
median_rating = np.median(rating_array)
std_rating = np.std(rating_array)
minimum_rating = np.min(rating_array)
maximum_rating = np.max(rating_array)

# ==========================================
# 6. FILTER RATINGS ABOVE 4
# ==========================================

high_ratings = ratings[ratings["rating"] > 4]

print("\n===== RATINGS ABOVE 4 =====")
print(high_ratings.head())

print("\n===== RATING STATISTICS =====")
print("Mean rating:", mean_rating)
print("Median rating:", median_rating)
print("Standard deviation:", std_rating)
print("Minimum rating:", minimum_rating)
print("Maximum rating:", maximum_rating)