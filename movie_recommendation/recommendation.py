import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
API_KEY = "4fe02a43e61a1f62472057d9fcc78e6d"

# Load Dataset
df = pd.read_csv("data/movies.csv")   # Change path if needed

movies_data = df

# Selected Features
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

# Fill Missing Values
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Combine Features
combined_features = (
    movies_data['genres'] + ' ' +
    movies_data['keywords'] + ' ' +
    movies_data['tagline'] + ' ' +
    movies_data['cast'] + ' ' +
    movies_data['director']
)

# Convert Text to Feature Vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Cosine Similarity
similarity = cosine_similarity(feature_vectors)

def fetch_movie_details(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return {
            "poster": None,
            "rating": "N/A",
            "release_date": "Unknown"
        }
    print(movie_id, response.status_code)

    if response.status_code != 200:
        print(response.text)
        return None

    data = response.json()

    poster = ""

    if data.get("poster_path"):
        poster = f"https://image.tmdb.org/t/p/w500{data['poster_path']}"

    return {
        "poster": poster,
        "rating": data.get("vote_average"),
        "release_date": data.get("release_date")
    }
    
def recommend_movies(movie_name):

    list_of_all_titles = movies_data['title'].tolist()

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if len(find_close_match) == 0:
        return []

    close_match = find_close_match[0]

    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    sorted_similar_movies = sorted(
        similarity_score,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    i = 1

    for movie in sorted_similar_movies:

        index = movie[0]

        movie_data = movies_data[movies_data.index == index]

        title = movie_data['title'].values[0]
        movie_id = movie_data['id'].values[0]

        details = fetch_movie_details(movie_id)

        if details:
            recommendations.append({
                "title": title,
                "poster": details["poster"],
                "rating": details["rating"],
                "release_date": details["release_date"]
            })

        if i >= 28:
            break

        i += 1
    print("Recommendations found:")
    return recommendations