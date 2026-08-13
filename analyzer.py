import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("\n===== NETFLIX DATA ANALYZER =====")

# Basic information
print("\nTotal Titles:", len(df))

print("\nContent Type:")
print(df["type"].value_counts())

# Set Seaborn style
sns.set_theme(style="whitegrid")

# Create chart
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="type"
)

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.tight_layout()

# Save chart
plt.savefig("charts/movies_vs_tv_shows.png")

# Display chart
plt.show()
# ==========================================
# STEP 4: TOP 10 COUNTRIES
# ==========================================

# Remove rows where country is missing
country_data = df.dropna(subset=["country"]).copy()

# Split multiple countries and create separate rows
country_data["country"] = country_data["country"].str.split(", ")

country_data = country_data.explode("country")

# Count titles by country
top_countries = country_data["country"].value_counts().head(10)

print("\nTop 10 Countries:")
print(top_countries)

# Create Seaborn chart
plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.tight_layout()

# Save chart
plt.savefig("charts/top_10_countries.png")

# Display chart
plt.show()
# ==========================================
# STEP 5: TOP 10 NETFLIX GENRES
# ==========================================

# Remove rows where genre information is missing
genre_data = df.dropna(subset=["listed_in"]).copy()

# Split multiple genres
genre_data["listed_in"] = genre_data["listed_in"].str.split(", ")

# Create separate rows for each genre
genre_data = genre_data.explode("listed_in")

# Count genres
top_genres = genre_data["listed_in"].value_counts().head(10)

print("\nTop 10 Netflix Genres:")
print(top_genres)

# Create Seaborn chart
plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_genres.values,
    y=top_genres.index
)

plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")

plt.tight_layout()

# Save chart
plt.savefig("charts/top_10_genres.png")

# Display chart
plt.show()
# ==========================================
# STEP 6: NETFLIX CONTENT BY RELEASE YEAR
# ==========================================

# Count titles released in each year
year_data = df["release_year"].value_counts().sort_index()

print("\nContent Released by Year:")
print(year_data.tail(20))

# Create Seaborn line chart
plt.figure(figsize=(12, 6))

sns.lineplot(
    x=year_data.index,
    y=year_data.values,
    marker="o"
)

plt.title("Netflix Content Released by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig("charts/content_by_year.png")

# Display chart
plt.show()
# ==========================================
# STEP 7: NETFLIX RATINGS
# ==========================================

# Remove missing ratings
rating_data = df.dropna(subset=["rating"])

# Count ratings
rating_counts = rating_data["rating"].value_counts()

print("\nNetflix Ratings:")
print(rating_counts)

# Create Seaborn chart
plt.figure(figsize=(10, 6))

sns.countplot(
    data=rating_data,
    y="rating",
    order=rating_counts.index
)

plt.title("Netflix Content Ratings")
plt.xlabel("Number of Titles")
plt.ylabel("Rating")

plt.tight_layout()

# Save chart
plt.savefig("charts/netflix_ratings.png")

# Display chart
plt.show()
# ==========================================
# STEP 8: MOVIE DURATION ANALYSIS
# ==========================================

# Select only Movies
movies = df[df["type"] == "Movie"].copy()

# Remove missing duration values
movies = movies.dropna(subset=["duration"])

# Extract numeric duration
movies["duration_minutes"] = (
    movies["duration"]
    .str.replace(" min", "", regex=False)
    .astype(int)
)

# Display statistics
print("\nMovie Duration Statistics:")
print(movies["duration_minutes"].describe())

# Create Seaborn histogram
plt.figure(figsize=(10, 6))

sns.histplot(
    data=movies,
    x="duration_minutes",
    bins=30,
    kde=True
)

plt.title("Distribution of Netflix Movie Durations")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")

plt.tight_layout()

# Save chart
plt.savefig("charts/movie_duration.png")

# Display chart
plt.show()
# ==========================================
# STEP 9: TOP 10 DIRECTORS
# ==========================================

# Remove missing directors
director_data = df.dropna(subset=["director"]).copy()

# Split multiple directors
director_data["director"] = director_data["director"].str.split(", ")

# Create separate rows
director_data = director_data.explode("director")

# Count titles by director
top_directors = director_data["director"].value_counts().head(10)

print("\nTop 10 Directors:")
print(top_directors)

# Create Seaborn chart
plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_directors.values,
    y=top_directors.index
)

plt.title("Top 10 Directors on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Director")

plt.tight_layout()

# Save chart
plt.savefig("charts/top_10_directors.png")

# Display chart
plt.show()
# ==========================================
# STEP 10: MOVIES VS TV SHOWS BY YEAR
# ==========================================

# Count content by release year and type
year_type_data = (
    df.groupby(["release_year", "type"])
    .size()
    .reset_index(name="count")
)

print("\nMovies vs TV Shows by Year:")
print(year_type_data.tail(20))

# Create Seaborn line chart
plt.figure(figsize=(12, 6))

sns.lineplot(
    data=year_type_data,
    x="release_year",
    y="count",
    hue="type",
    marker="o"
)

plt.title("Movies vs TV Shows by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.legend(title="Content Type")

plt.tight_layout()

# Save chart
plt.savefig("charts/movies_vs_tv_shows_by_year.png")

# Display chart
plt.show()
# ==========================================
# STEP 11: NETFLIX ANALYSIS SUMMARY
# ==========================================

print("\n")
print("=" * 50)
print("        NETFLIX ANALYSIS SUMMARY")
print("=" * 50)

# Total titles
total_titles = len(df)

# Movies and TV Shows
total_movies = (df["type"] == "Movie").sum()
total_tv_shows = (df["type"] == "TV Show").sum()

# Release year
oldest_year = df["release_year"].min()
latest_year = df["release_year"].max()

# Most common rating
most_common_rating = df["rating"].mode()[0]

# Top country
top_country = (
    country_data["country"]
    .value_counts()
    .idxmax()
)

# Top genre
top_genre = (
    genre_data["listed_in"]
    .value_counts()
    .idxmax()
)

# Average movie duration
average_duration = movies["duration_minutes"].mean()

# Most active director
top_director = (
    director_data["director"]
    .value_counts()
    .idxmax()
)

# Display results
print(f"\nTotal Netflix Titles      : {total_titles}")
print(f"Total Movies              : {total_movies}")
print(f"Total TV Shows            : {total_tv_shows}")

print(f"\nOldest Release Year       : {oldest_year}")
print(f"Latest Release Year       : {latest_year}")

print(f"\nMost Common Rating        : {most_common_rating}")
print(f"Top Country               : {top_country}")
print(f"Top Genre                 : {top_genre}")

print(f"\nAverage Movie Duration    : {average_duration:.2f} minutes")
print(f"Most Active Director      : {top_director}")

print("\n" + "=" * 50)
print("       ANALYSIS COMPLETED")
print("=" * 50)