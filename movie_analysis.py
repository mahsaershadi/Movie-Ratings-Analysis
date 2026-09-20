import numpy as np
import pandas as pd


#load the datasets
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")


#explore the datasets
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


#check the data types of each column in both datasets
print("\n===== MOVIES INFO =====")
movies.info()

print("\n===== RATINGS INFO =====")
ratings.info()


#check for missing values in both datasets
print("\n===== MISSING VALUES =====")

print("Movies:")
print(movies.isnull().sum())

print("\nRatings:")
print(ratings.isnull().sum())


#basic statistics for ratings
rating_array = ratings["rating"].to_numpy()

mean_rating = np.mean(rating_array)
median_rating = np.median(rating_array)
std_rating = np.std(rating_array)
minimum_rating = np.min(rating_array)
maximum_rating = np.max(rating_array)


#filter ratings above 4
high_ratings = ratings[ratings["rating"] > 4]

print("\n===== RATINGS ABOVE 4 =====")
print(high_ratings.head())

print("\n===== RATING STATISTICS =====")
print("Mean rating:", mean_rating)
print("Median rating:", median_rating)
print("Standard deviation:", std_rating)
print("Minimum rating:", minimum_rating)
print("Maximum rating:", maximum_rating)