# movie-database

As a movie maniac, 
- I created my own mini ETL pipeline
- created movie & watching history dashboards with Tableau
- compared douban & imdb ratings

## Data Source:
- Douban: a chinese version of imdb 
- IMDB

## ETL Pipeline for douban database
- Scrape down my douban watched list with `main.exe`
  - Source code: `main.py`, `scrape.py`, `upload.py`
    - `scrape.py`: scrape down the information I needed douban
    - `upload.py`: upload the film info into my notion database
  - Requirement: python 3, pip install requests & beautifulsoups & lxml
  - 安装python3环境
  
The `main.exe` itself acts as a full ETL pipeline with data scraping, cleaning, and loading to Notion. 

I chose Notion as my primary database as Notion is easier for personal knowledge management.

The complete table includes the following features:
- 'movie_title'
- 'director'
- 'douban_url'
- 'imdb_url'
- 'my_comment': some short comments I wrote for a film
- 'release_year'
- 'status': categorical features including watched, currently watching, want to watch
- 'genre'
- 'watched_date': when I watched this film
- 'production country'

The Notion Database looks like:

!['notion database'](https://github.com/shaw6741/movie-database/blob/master/images/notion_preview.jpg)

## Combine douban & IMDb
This is to enlarge my database with film staff's info.

Data was extracted using both imdb Dataset [Cinemagoer](https://imdbpy.readthedocs.io/en/latest/index.html) and [this Chinese API](https://github.com/iiiiiii1/douban-imdb-api).

Python was used for extraction, data cleaning, and normalizing tables to prepare them for relational database.

After merging them based on imdbID, I created the following database with SQL.

!['schema'](https://github.com/shaw6741/movie-database/blob/master/images/my%20schema.png)

## My Watching Histories Dashboard (with Tableau)

!! This is for illustration only.

I used tableau to create a simple dashboard of monthly watching histories. There are four components in the dashboard: 

- What movies have I watched in the past month
- 5-star movies I've seen in the past month
- How much time I've spent watching movies in the past week & how many movies you've watched in total
- The percentage of time I spent on TV shows and movies.

['My Dashboard'](https://github.com/shaw6741/movie-database/blob/master/images/tableau_dashboard.jpg)

Simple but useful but totally meet my needs:
- As long as time allows, I hope I can maintain a certain amount of film watching so that I can continue to learn from new films.
- By recording the five-star movies I've seen in the past period, I can re-watch them and write down my cinematography analysis when I'm free in the future.
- TV shows are also a good way to learn, especially comparing the writing and shooting styles of TV shows and movies, so it's also important to make sure I have good TV show input, which will make me to understand the content trends in the film and TV industry.

Also created some other sheets:
- watching history by country
- watching history by release year

['by country']([https://github.com/shaw6741/movie-database/blob/master/images/tableau_dashboard.jpg](https://github.com/shaw6741/movie-database/blob/master/images/tableau_sheet_history_by_country.jpg))

['by release year']([https://github.com/shaw6741/movie-database/blob/master/images/tableau_dashboard.jpg](https://github.com/shaw6741/movie-database/blob/master/images/tableau_sheet_history_by_releaseyear.jpg))

This tableau is for illustration only and does not contain the full dataset. 

However, even from these results, 

I'll say I need to watch more old films and films outside of East Asia and english-speaking countries!!



  
