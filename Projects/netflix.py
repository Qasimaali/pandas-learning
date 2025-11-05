import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('netflix_titles.csv')

# Optional: inspect
print(df.head())
#print(df.info())
#print(df.columns)
type_counts = df['type'].value_counts()
print("Movie vs TV Show counts:\n", type_counts)

# Visualise (optional)
type_counts.plot(kind='bar', title='Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# 3. Most common genres
# The column `listed_in` holds the genre(s) for each title
genres = df['listed_in'].str.split(',').explode().str.strip()
top_genres = genres.value_counts().head(10)
print("Top 10 genres:\n", top_genres)

# Visualise
top_genres.plot(kind='barh', title='Top 10 Genres')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()

# 4. Shows released after 2015
recent = df[df['release_year'] > 2015]
print("Titles released after 2015:\n", recent[['title','type','release_year']].head())

# Further analysis e.g., count by type
recent_counts = recent['type'].value_counts()
print("Recent counts by type:\n", recent_counts)

# 5. Group by country or director

# By country — count titles per country (for multi-country entries you may need to explode)
countries = df['country'].dropna().str.split(',').explode().str.strip()
country_counts = countries.value_counts().head(10)
print("Top 10 countries by number of titles:\n", country_counts)

# By director — note many missing/NaN values and multiple directors per title
directors = df['director'].dropna().str.split(',').explode().str.strip()
director_counts = directors.value_counts().head(10)
print("Top 10 directors by number of titles:\n", director_counts)