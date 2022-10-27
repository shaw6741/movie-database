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
  
The `main.exe` itself acts as a full ETL pipeline with data scraping, cleaning, and loading to Notion. 

I chose Notion as my primary database as Notion is easier for personal knowledge management.

The Notion database can be exported into csv file for future analysis.

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

## Combine douban & IMDb - ETL for Larger Database
This is to enlarge my database with film staff's info.

First, I created a database schema:
!['schema'](https://github.com/shaw6741/movie-database/blob/master/images/my%20schema.png)

### Extraction
1. [IMDB Dataset](https://www.imdb.com/interfaces/)
1. Python package: [Cinemagoer](https://imdbpy.readthedocs.io/en/latest/index.html)
2. A [Chinese API](https://github.com/iiiiiii1/douban-imdb-api) that can fetch IMDB rating, IMDB info, Rotten Tomatoes Rating

Cinemagoer and API are good tools to get updated information on new films. Each time I finished watching a film, I'll just use the API and Cinemagoer to add my data record.

### Transform (with Python)
1. `convert.py`: clean the IMDB dataset, delete some unwanted data, normalize it based on my schema by seperating original tables
2. After which, the desired set of tables are output as tab-separate-value (tsv) files.


### Load (with MySQL)
1. `create.sql`: create tables
2. `load.sql`: load the tsv file into tables
3. `constraints.sql`: add constraints
4. `indexing.sql`: add indexes


## My Watching Histories Dashboard (with Tableau)

!! This is for illustration only.

I used tableau to create a simple dashboard of monthly watching histories. There are four components in the dashboard: 

- What movies have I watched in the past month
- 5-star movies I've seen in the past month
- How much time I've spent watching movies in the past week & how many movies you've watched in total
- The percentage of time I spent on TV shows and movies.

!['My Dashboard'](https://github.com/shaw6741/movie-database/blob/master/images/tableau_dashboard.jpg)

Simple but useful but totally meet my needs:
- As long as time allows, I hope I can maintain a certain amount of film watching so that I can continue to learn from new films.
- By recording the five-star movies I've seen in the past period, I can re-watch them and write down my cinematography analysis when I'm free in the future.
- TV shows are also a good way to learn, especially comparing the writing and shooting styles of TV shows and movies, so it's also important to make sure I have good TV show input, which will make me to understand the content trends in the film and TV industry.

Also created some other sheets:
- watching history by country
- watching history by release year

!['by country'](https://github.com/shaw6741/movie-database/blob/master/images/tableau_sheet_history_by_country.jpg)

!['by release year'](https://github.com/shaw6741/movie-database/blob/master/images/tableau_sheet_history_by_releaseyear.jpg)

This tableau is for illustration only and does not contain the full dataset. 

However, even from these results, 

I'll say I need to watch more old films and films outside of East Asia and english-speaking countries!!



  
