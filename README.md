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

!['notion database'](https://github.com/shaw6741/movie-database/blob/master/notion_preview.jpg)

## Combine douban & IMDb
This is to enlarge my database with film staff's info.

Data was extracted using both imdb Dataset [Cinemagoer](https://imdbpy.readthedocs.io/en/latest/index.html) and [this Chinese API](https://github.com/iiiiiii1/douban-imdb-api).

Python was used for extraction, data cleaning, and normalizing tables to prepare them for relational database.

After merging them based on imdbID, I created the following database with SQL.

!['schema'](https://github.com/shaw6741/movie-database/blob/master/my%20schema.png)

## My Watching Histories Dashboard (with Tableau)

!! This is for illustration only.





## Douban vs IMDB (with Python and Tableau)



  
