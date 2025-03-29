import argparse
import requests

parser = argparse.ArgumentParser()
valid_options = {"now_playing", "popular", "top_rated", "upcoming"}
parser.add_argument("--type", help="Specify the type of movie category (now_playing, popular, top_rated, upcoming)", choices=valid_options, type=str)
args = parser.parse_args()

url = f"https://api.themoviedb.org/3/movie/{args.type}?language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer YOUR_TMDB_API_KEY"
}
response = requests.get(url, headers=headers)
data = response.json()

RESET = "\033[0m"
BOLD = "\033[1m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"

GENRE_MAP = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Science Fiction",
    10770: "TV Movie",
    53: "Thriller",
    10752: "War",
    37: "Western"
}

def display_movies():
    for movie in data["results"]:        
        print(YELLOW + "════════════════════════════════════════" + RESET)

        print(BOLD + CYAN + f"🎬 {movie['original_title']}" + RESET)

        print(BLUE + "📅 Release Date:" + RESET, f"{movie['release_date']}")

        print(MAGENTA + "⭐ Rating:" + RESET, f"{movie['vote_average']}/10 ({movie['vote_count']} votes)")

        genre_names = [GENRE_MAP.get(gid, "Unknown") for gid in movie.get("genre_ids", [])]
        print(CYAN + "🎭 Genres:" + RESET, ", ".join(genre_names) if genre_names else "N/A")

        print(BOLD + "📜 OVERVIEW:" + RESET)
        print(movie['overview'])

        print(YELLOW + "════════════════════════════════════════" + RESET)

if args.type == "now_playing":
    
    print(BOLD + "🎬 Now Playing in Theaters" + RESET)    

    display_movies()

elif args.type == "popular":
    
    print(BOLD + "🔥 Trending & Popular Movies" + RESET)

    display_movies()

elif args.type == "top_rated":
    
    print(BOLD + "⭐ All-Time Top Rated Movies" + RESET)

    display_movies()

elif args.type == "upcoming":
    
    print(BOLD + "⏳ Upcoming Movies to Watch" + RESET)

    display_movies()
