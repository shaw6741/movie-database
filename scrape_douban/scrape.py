import re
import random
from bs4 import BeautifulSoup
from upload import *


class MovieList:
    def __init__(self, user_cookies, database_id, status, token):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
        self.cookies = user_cookies
        self.database_id = database_id
        self.status = status
        self.fail = []
        self.token = token

    def req(self, url, start_number):
        r1 = requests.request("GET", url=url, headers=self.headers, cookies=self.cookies)
        page_number = start_number / 15 + 1
        if r1.status_code == 200:
            print(f'{int(page_number)}page success，syncing')
            list_soup = BeautifulSoup(r1.text, 'lxml')
            movies_list = list_soup.find_all("div", class_="item")
            for movie in movies_list:
                movie_status = {"name": self.status} # my watched, want to watch, and watching list
                movie_title = movie.find("em").get_text()
                # let's get my rating for this movie
                try:
                    rating = movie.find("span", class_=re.compile("rating"))["class"]
                    if rating == ['rating1-t']:
                        movie_rate = "1"
                    elif rating == ['rating2-t']:
                        movie_rate = "2"
                    elif rating == ['rating3-t']:
                        movie_rate = "3"
                    elif rating == ['rating4-t']:
                        movie_rate = "4"
                    elif rating == ['rating5-t']:
                        movie_rate = "5"
                    else:
                        movie_rate = "No Rating"
                except TypeError:
                    movie_rate = "No Rating"

                # my comment for the film
                try:
                    movie_comment = movie.find("span", class_="comment").get_text()
                except AttributeError:
                    movie_comment = "No Comment"

                # when do i watch the film
                movie_date = movie.find("span", class_="date").get_text()

                # the douban link for the film
                movie_link = movie.find("a", href=True)["href"]

                # get director, genre, production country, IMDb link
                r2 = requests.request("GET", url=movie_link, headers=self.headers, cookies=self.cookies)
                if r2.status_code == 200:
                    print(f'《{movie_title}》page success, loading')
                    detail_soup = BeautifulSoup(r2.text, 'lxml')

                    # director
                    # multiple directors are splited to get the dictionary
                    try:
                        movie_director = []
                        directors = detail_soup.find_all("a", rel="v:directedBy")
                        if directors != []:
                            for director in directors:
                                director_dict = {}
                                director_dict["name"] = director.get_text()
                                movie_director.append(director_dict)
                        else:
                            movie_director = [{"name": "No Director Info"}]
                    except AttributeError:
                        movie_director = [{"name": "No Director Info"}]

                    # genre
                    try:
                        movie_genre = []
                        genres = detail_soup.find_all("span", property="v:genre")
                        for genre in genres:
                            genre_dict = {}
                            genre_dict["name"] = genre.get_text()
                            movie_genre.append(genre_dict)
                    except AttributeError:
                        movie_genre = [{"name": "No Genre Info"}]

                    # production
                    try:
                        movie_country = []
                        countries = detail_soup.find("span", class_="pl", text=re.compile("production_country")).next_sibling.lstrip().split(" / ")
                        for country in countries:
                            country_dict = {}
                            country_dict["name"] = country
                            movie_country.append(country_dict)
                    except AttributeError:
                        movie_country = [{"name": "No Production Info"}]

                    # IMDB link
                    try:
                        imdb_id = detail_soup.find("span", class_="pl", text=re.compile("IMDb")).next_sibling.lstrip()
                        imdb_link = f"https://www.imdb.com/title/{imdb_id}/"
                    except AttributeError:
                        imdb_link = "No IMDB link"

                    # poster
                    try:
                        poster_origin_url = detail_soup.find("img", rel="v:image")["src"]
                        poster_l_url = poster_origin_url.replace("s_ratio_poster", "l")
                        if poster_origin_url.count("webp") == 1:
                            poster_l_url = poster_l_url.replace("webp", "jpg")
                    except TypeError:
                        poster_l_url = "No poster"

                    # Release Year
                    try:
                        movie_year = {}
                        find_year = detail_soup.find("span", class_="year").get_text().replace("(", "").replace(")", "")
                        movie_year["name"] = find_year
                    except AttributeError:
                        movie_year = {"name": "No Release Year Info"}
                else:
                    imdb_link = "Failed, no imdb link"
                    poster_l_url = "Failed, no cover"
                    movie_director = [{"name": "Faild, no director info"}]
                    movie_country = [{"name": "Failed, no production info"}]
                    movie_genre = [{"name": "Failed, no genre info"}]
                    movie_year = {"name": "Failed, no release year info"}
                    self.fail.append(f"《{movie_title}》")

                create_page = NotionDatabase(token=self.token)
                failure = create_page.create_a_page(database_id=self.database_id,
                                                    movie_title=movie_title,
                                                    movie_rate=movie_rate,
                                                    movie_comment=movie_comment,
                                                    movie_date=movie_date,
                                                    movie_link=movie_link,
                                                    imdb_link=imdb_link,
                                                    poster_l_url=poster_l_url,
                                                    movie_director=movie_director,
                                                    movie_country=movie_country,
                                                    movie_genre=movie_genre,
                                                    movie_year=movie_year,
                                                    movie_status=movie_status)
                if failure != "":
                    self.fail.append(failure)

                
                time.sleep(random.randint(5, 10))

        else:
            print(f'{int(page_number)}page failed, moving to next page')
            self.fail.append(f"{int(page_number)} page's all movies")