# Simple Movie Recommendation System
# Content-based filtering using common genres

movies = {
    "Inception": ["Action", "Sci-Fi", "Thriller"],
    "Interstellar": ["Sci-Fi", "Drama", "Adventure"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Avengers: Endgame": ["Action", "Adventure", "Sci-Fi"],
    "Titanic": ["Romance", "Drama"],
    "The Notebook": ["Romance", "Drama"],
    "Jurassic Park": ["Adventure", "Sci-Fi", "Thriller"],
    "The Matrix": ["Action", "Sci-Fi", "Thriller"],
    "Toy Story": ["Animation", "Comedy", "Adventure"],
    "Finding Nemo": ["Animation", "Adventure", "Comedy"]
}

def recommend(movie):
    if movie not in movies:
        print("Movie not found.")
        return

    chosen = set(movies[movie])
    results = []

    for name, genres in movies.items():
        if name == movie:
            continue
        score = len(chosen & set(genres))
        results.append((score, name))

    results.sort(reverse=True)

    print("\nMovies similar to", movie + ":")
    for score, name in results[:5]:
        print(f"- {name} (similarity: {score})")

print("Available movies:")
for movie in movies:
    print("-", movie)

choice = input("\nEnter a movie you like: ").strip()
recommend(choice)
#hello