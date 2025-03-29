# TMDB CLI Tool

A simple command-line tool to fetch and display movie details from The Movie Database (TMDb) API.  
Supports fetching Now Playing, Popular, Top Rated, and Upcoming movies with a clean, formatted terminal output.  
Quickly browse movie ratings, release dates, genres, and overviews in the terminal.

---

## Features

- Fetch Now Playing, Popular, Top Rated, and Upcoming movies
- Displays movie details with ratings, genres, and overview
- Uses color formatting for better readability in the terminal

---

## Installation

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/Lethios/tmdb-cli-tool.git
   cd tmdb-cli-tool
   ```
2. **Ensure Python is installed (Python 3.x recommended).**
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Set up your API key in an environment variable:**
   ```bash
   export TMDB_API_KEY="your_api_key_here"   


## Usage

Run the program using Python:
```bash
python tmdb-cli.py --type now_playing
python tmdb-cli.py --type popular
python tmdb-cli.py --type top_rated
python tmdb-cli.py --type upcoming
```


## API Reference

This tool uses **The Movie Database (TMDB) API**. You can get an API key by signing up at [TMDB Developer](https://developer.themoviedb.org/docs).


## Author

**Lethios**
- Github: [@Lethios](https://github.com/Lethios)
- Twitter: [@LethiosDev](https://x.com/LethiosDev)


## License

Copyright © 2025 [Lethios](https://github.com/Lethios).  
This project is licensed under the [MIT License](LICENSE).
