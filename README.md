# Movie Ratings Analysis

A beginner-friendly data analysis project using Python, NumPy, and Pandas to explore movie ratings and extract basic insights from the MovieLens dataset.

## Overview

This project analyzes movie ratings to understand rating patterns, highly rated movies, movie genres, and rating trends across different years.

The project was created to practice fundamental data analysis concepts in Python, including:

- Loading CSV datasets
- Exploring structured data
- Cleaning and handling missing values
- Numerical calculations with NumPy
- Data manipulation with Pandas
- Filtering and sorting data
- Merging multiple datasets
- Grouping data by categories
- Calculating average ratings
- Extracting basic insights from a dataset

---

## Dataset

This project uses the **MovieLens** dataset provided by GroupLens.

Dataset:

[MovieLens Dataset](https://grouplens.org/datasets/movielens/)

The project uses the following files:

### `movies.csv`

Contains information about movies:

| Column | Description |
|---|---|
| `movieId` | Unique identifier for each movie |
| `title` | Movie title and release year |
| `genres` | One or more genres associated with the movie |

### `ratings.csv`

Contains user ratings:

| Column | Description |
|---|---|
| `userId` | Unique identifier for each user |
| `movieId` | Identifier of the rated movie |
| `rating` | User rating |
| `timestamp` | Time when the rating was submitted |

The two datasets are connected through the `movieId` column.

---

## Technologies Used

- **Python**
- **NumPy**
- **Pandas**
- **Git / GitHub**

### Python

Used for the overall program structure, variables, conditions, and output.

### NumPy

Used for numerical calculations such as:

- Mean
- Median
- Standard deviation
- Minimum
- Maximum

### Pandas

Used for:

- Reading CSV files
- Exploring datasets
- Filtering records
- Sorting data
- Handling missing values
- Merging datasets
- Grouping data
- Calculating statistics

---

## Project Structure

```text
Movie-Ratings-Analysis/
│
├── data/
│   ├── movies.csv
│   └── ratings.csv
│
├── movie_analysis.py
│
├── requirements.txt
│
└── README.md