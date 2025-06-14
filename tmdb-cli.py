import argparse
import sys
import requests

parser = argparse.ArgumentParser()
valid_options = {"now_playing", "popular", "top_rated", "upcoming"}
parser.add_argument("--type", help="Choose a category: now_playing | popular | top_rated | upcoming", choices=valid_options, type=str, metavar="<category>")
args = parser.parse_args()

URL = f"https://api.themoviedb.org/3/movie/{args.type}?language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer YOUR_TMDB_API_KEY"
}

try:
    response = requests.get(URL, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: Failed to fetch data from TMDB API: {e}")
    sys.exit(1)
except ValueError:
    print("Error: Received invalid JSON response from TMDB API.")
    sys.exit(1)

if "results" not in data:
    print("Error: Unexpected response format from TMDB API.")
    sys.exit(1)

RESET = "\033[0m"
BOLD = "\033[1m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"

GENRE_MAP = {
    28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy",
    80: "Crime", 99: "Documentary", 18: "Drama", 10751: "Family",
    14: "Fantasy", 36: "History", 27: "Horror", 10402: "Music",
    9648: "Mystery", 10749: "Romance", 878: "Science Fiction",
    10770: "TV Movie", 53: "Thriller", 10752: "War", 37: "Western"
}

def display_movies():
    """
    Prints a formatted list of movies retrieved from the TMDB API.

    Each movie includes:
    - Title
    - Release date
    - User rating and vote count
    - Genres (mapped from genre IDs)
    - Synopsis/overview

    Uses ANSI escape codes for colored output in the terminal.
    """

    for movie in data["results"]:
        print(YELLOW + "════════════════════════════════════════" + RESET)
        print(BOLD + CYAN + f"🎥 {movie.get('original_title', 'Unknown')}" + RESET)
        print(BLUE + "📅 Release Date:" + RESET, movie.get("release_date", "Unknown"))
        print(MAGENTA + "⭐ Rating:" + RESET, f"{movie.get('vote_average', 'N/A')}/10 ({movie.get('vote_count', 'N/A')} votes)")

        genre_names = [GENRE_MAP.get(gid, "Unknown") for gid in movie.get("genre_ids", [])]
        print(CYAN + "🎭 Genres:" + RESET, ", ".join(genre_names) if genre_names else "N/A")

        print(BOLD + "📜 SYNOPSIS:" + RESET)
        print(movie.get("overview", "No description available."))
        print(YELLOW + "════════════════════════════════════════" + RESET)

category_headers = {
    "now_playing": "🎬 Now Playing in Theaters",
    "popular": "🔥 Trending & Popular Movies",
    "top_rated": "⭐ All-Time Top Rated Movies",
    "upcoming": "⏳ Upcoming Movies to Watch"
}

print()
print(BOLD + category_headers.get(args.type, "Movies") + RESET)
display_movies()
