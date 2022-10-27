from scrape import *
from upload import *


def main():
    print("●●●●●●●●●●●●●●●●●●●●●●●●●●\n"
          "This program will sync my douban watching list to my notion database\n"
          "Prepare following data\n"
          "1. douban id\n"
          "2. douban user cookies\n"
          "3. notion integration token\n"
          "4. notion page link\n"
          "●●●●●●●●●●●●●●●●●●●●●●●●●●\n")
    user_id = input("----------------------------------------------------\n"
                    "Type douban id:")
    user_cookies = add_cookies()
    token = input("----------------------------------------------------\n"
                  "Type notion token:")

    choice = int(input("----------------------------------------------------\n"
                       "Backup watched list, press 1;\n"
                       "Backup watching list, press 2;\n"
                       "Backup waiting-to-watch list, press 3;\n"
                       "Exit program, press 4.\n"
                       "Enter: "))

    if choice == 1:
        database_id, start_number, end_number = first_or_not(token=token)

        watched_to_notion = MovieList(user_cookies=user_cookies, database_id=database_id, status="看过", token=token)

        while start_number <= end_number:
            watched_url = f"https://movie.douban.com/people/{user_id}/collect?start={start_number}&sort=time&rating=all&filter=all&mode=grid"
            watched_to_notion.req(url=watched_url, start_number=start_number)
            start_number += 15
        if len(watched_to_notion.fail) == 0:
            print(f'Sync completed')
        else:
            print(f"Sync completed, failed movie include{watched_to_notion.fail}")
    elif choice == 2:
        database_id, start_number, end_number = first_or_not(token=token)

        watched_to_notion = MovieList(user_cookies=user_cookies, database_id=database_id, status="正在看", token=token)

        while start_number <= end_number:
            watched_url = f"https://movie.douban.com/people/{user_id}/do?start={start_number}&sort=time&rating=all&filter=all&mode=grid"
            watched_to_notion.req(url=watched_url, start_number=start_number)
            start_number += 15
        if len(watched_to_notion.fail) == 0:
            print(f'Sync completed')
        else:
            print(f"Sync completed, failed movie include{watched_to_notion.fail}")
    elif choice == 3:
        database_id, start_number, end_number = first_or_not(token=token)

        watched_to_notion = MovieList(user_cookies=user_cookies, database_id=database_id, status="想看", token=token)

        while start_number <= end_number:
            watched_url = f"https://movie.douban.com/people/{user_id}/wish?start={start_number}&sort=time&rating=all&filter=all&mode=grid"
            watched_to_notion.req(url=watched_url, start_number=start_number)
            start_number += 15
        if len(watched_to_notion.fail) == 0:
            print(f'Sync completed')
        else:
            print(f"Sync completed, failed movie include{watched_to_notion.fail}")
    elif choice == 4:
        exit()
    else:
        print("----------------------------------------------------\n"
              "Input enter, please re-enter")
        main()


def first_or_not(token):
    choice = int(input("----------------------------------------------------\n"
                       "First time use the program with no database created, press 1;\n"
                       "Not first time and want to continue with the database used last time, press 2;\n"
                       "Exit, press 3.\n"
                       "Enter: "))
    if choice == 1:
        create_database = NotionDatabase(token=token)
        database_id = create_database.create_a_database(page_id=find_page_id())

        start_page_number = int(input("----------------------------------------------------\n"
                                      "Backup start page (enter page number):"))
        start_number = (start_page_number - 1) * 15
        end_page_number = int(input("----------------------------------------------------\n"
                                    "Backup end page (enter page number):"))
        end_number = (end_page_number - 1) * 15

        return database_id, start_number, end_number
    elif choice == 2:
        database_id = find_database_id()

        start_page_number = int(input("----------------------------------------------------\n"
                                      "Backup start page (enter page number):"))
        start_number = (start_page_number - 1) * 15
        end_page_number = int(input("----------------------------------------------------\n"
                                    "Backup end page (enter page number):"))
        end_number = (end_page_number - 1) * 15

        return database_id, start_number, end_number
    elif choice == 3:
        exit()
    else:
        print("----------------------------------------------------\n"
              "Input error, re-enter:")
        first_or_not(token=token)


def find_page_id():
    notion_page_url = input("----------------------------------------------------\n"
                            "Enter notion page link\n"
                            "1. need to connect the page to an integration\n"
                            "2. enter page link instead of notion database link\n"
                            "Enter link:")

    if notion_page_url[0:22] == "https://www.notion.so/":
        if notion_page_url.count("?v=") == 0:
            if notion_page_url.count("#") == 0:
                page_id = notion_page_url[len(notion_page_url) - 32:len(notion_page_url) - 24] + '-' \
                          + notion_page_url[len(notion_page_url) - 24:len(notion_page_url) - 20] + '-' \
                          + notion_page_url[len(notion_page_url) - 20:len(notion_page_url) - 16] + '-' \
                          + notion_page_url[len(notion_page_url) - 16:len(notion_page_url) - 12] + '-' \
                          + notion_page_url[len(notion_page_url) - 12:len(notion_page_url)]
                return page_id
            elif notion_page_url.count("#") != 0:
                last_hash = notion_page_url.index("#")
                page_id = notion_page_url[last_hash - 32:last_hash - 24] + "-" \
                          + notion_page_url[last_hash - 24:last_hash - 20] + "-" \
                          + notion_page_url[last_hash - 20:last_hash - 16] + "-" \
                          + notion_page_url[last_hash - 16:last_hash - 12] + "-" \
                          + notion_page_url[last_hash - 12:last_hash]
                return page_id
        elif notion_page_url.count("?v=") != 0:
            print("----------------------------------------------------\n"
                  "The link is database link, re-enter")
            try_to_find_page_id()
    else:
        print("----------------------------------------------------\n"
              "The link is not a notion link, re-enter")
        try_to_find_page_id()


def try_to_find_page_id():
    choice = int(input("----------------------------------------------------\n"
                       "To rediscover the Page ID, press 1, to exit, press 2."))

    if choice == 1:
        find_page_id()
    elif choice == 2:
        exit()
    else:
        print("----------------------------------------------------\n"
              "Input error, try again")
        try_to_find_page_id()


def find_database_id():
    notion_database_url = input("----------------------------------------------------\n"
                                "Enter the link to the existing Notion Database:")

    if notion_database_url[0:22] == "https://www.notion.so/":
        if notion_database_url.count("?v=") == 1:
            last_slash = notion_database_url.rfind("/")
            database_id = notion_database_url[last_slash + 1:last_slash + 33]
            return database_id
        elif notion_database_url.count("?v=") == 0:
            print("----------------------------------------------------\n"
                  "The link is not a Notion database link, try again")
            try_to_find_database_id()
    else:
        print("----------------------------------------------------\n"
              "The link may not be a Notion link, try again")
        try_to_find_database_id()


def try_to_find_database_id():
    choice = int(input("----------------------------------------------------\n"
                       "To rediscover Database ID, press 1, to exit, press 2."))

    if choice == 1:
        find_database_id()
    elif choice == 2:
        exit()
    else:
        print("----------------------------------------------------\n"
              "Input error, try again")
        try_to_find_database_id()


def add_cookies():
    cookies_str = input('----------------------------------------------------\n'
                        'Enter douban cookies:')
    if cookies_str[0:3] == "ll=":
        cookies_dict = {}
        cookies_list = cookies_str.replace('"', "").split('; ')
        for i in cookies_list:
            name, value = i.split('=', 1)
            cookies_dict[f'{name}'] = value
        return cookies_dict
    else:
        print("Wrong cookies, try again:")
        add_cookies()


if __name__ == "__main__":
    main()
