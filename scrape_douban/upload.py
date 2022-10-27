import requests
import json
import time


class NotionDatabase:
    def __init__(self, token):
        self.database_url = "https://api.notion.com/v1/databases"
        self.page_url = "https://api.notion.com/v1/pages"
        self.headers = {'Authorization': f'Bearer {token}',
                        'Notion-Version': '2021-08-16',
                        "Content-Type": "application/json"}

    def create_a_database(self, page_id):
        create_database_data = {
            "parent": {"type": "page_id", "page_id": page_id},
            "title": [{"type": "text", "text": {"content": "MyMovieDatabase"}}],
            "icon": {"type": "emoji", "emoji": "🎬"},
            "properties": {
                "movie_title": {"title": {}},
                "my_rating": {"select": {"options": [
                    {"name": "1"},
                    {"name": "2"},
                    {"name": "3"},
                    {"name": "4"},
                    {"name": "5"},
                ]}},
                "my_comment": {"rich_text": {}},
                "watched_date": {"date": {}},
                "douban_url": {"url": {}},
                "director": {"multi_select": {}},
                "type": {"multi_select": {}},
                "production_country": {"multi_select": {}},
                "imdb_link": {"url": {}},
                "poster": {"files": {}},
                "release_year": {"select": {}},
                "status": {"select": {}}
            }
        }

        data = json.dumps(create_database_data)

        r = requests.request("POST", url=self.database_url, headers=self.headers, data=data)
        if r.status_code == 200:
            database_id = eval(r.text.replace(":null", ":'null'").replace(":false", ":'false'"))["id"]
            return database_id
        else:
            print("Failed to create database. Check if the page is connected to the integration. Then, restart the program.")
            input("Press ENTER to exit.")
            exit()

    def create_a_page(self,
                      database_id,
                      movie_title,
                      movie_rate,
                      movie_comment,
                      movie_date,
                      movie_link,
                      imdb_link,
                      poster_l_url,
                      movie_director,
                      movie_country,
                      movie_genre,
                      movie_year,
                      movie_status):
        create_page_data = {
            "parent": {"database_id": database_id},
            "properties": {
                "movie_title": {"title": [{"text": {"content": movie_title}}]},
                "my_rating": {"select": {"name": movie_rate}},
                "my_comment": {"rich_text": [{"text": {"content": movie_comment}}]},
                "watched_date": {"date": {"start": movie_date}},
                "douban_url": {"url": movie_link},
                "imdb_link": {"url": imdb_link},
                "poster": {"files": [{"name": poster_l_url, "external": {"url": poster_l_url}}]},
                "director": {"multi_select": movie_director},
                "production_country": {"multi_select": movie_country},
                "type": {"multi_select": movie_genre},
                "release_year": {"select": movie_year},
                "status": {"select": movie_status}
            }
        }

        data = json.dumps(create_page_data)
        r = requests.request("POST", url=self.page_url, headers=self.headers, data=data)
        if r.status_code == 200:
            print(f"《{movie_title}》uploaded")
            failure = ""
            return failure
        else:
            print(f"《{movie_title}》upload failed")
            failure = f"《{movie_title}》"
            return failure
